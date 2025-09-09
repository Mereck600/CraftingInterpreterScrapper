#!/usr/bin/env python3
"""
Extract Crafting Interpreters code blocks and write one Markdown file per chapter.

Key features:
- Preserves original code formatting exactly 
- One Markdown file per chapter in an output directory, numbered + slugged.
- Compact per-snippet header line: "#### N. <Section> — [source](...)" on a single line.
- Adds language fences when possible for syntax highlighting.

Usage:
  python -m venv myvenv
  On windows run myvenv/Scripts/activate.bat  
  pip install requests beautifulsoup4 lxml
   # quick test:
   Just run this file or 
  python extract_crafting_interpreters_code.py \
      --outdir crafting_interpreters_code \
      --start https://craftinginterpreters.com/contents.html
 
  
"""

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup

DEFAULT_START = "https://craftinginterpreters.com/contents.html"
UA = "CodeScraper/1.2 (+https://github.com/; educational use)"

# ------------ Helpers ------------

def slugify(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[–—/:]+", "-", s)           # dashes, slashes, colons
    s = re.sub(r"[^\w\s.-]", "", s)          # drop stray punctuation
    s = re.sub(r"\s+", "-", s)               # spaces -> dashes
    s = re.sub(r"-{2,}", "-", s)             # collapse repeats
    return s.strip("-._")

def get_soup(url, session, retries=3, sleep=0.7):
    for i in range(retries):
        try:
            r = session.get(url, timeout=20)
            r.raise_for_status()
            return BeautifulSoup(r.text, "lxml")
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(sleep * (i + 1))

def extract_toc_links(start_url, session):
    soup = get_soup(start_url, session)
    links = []
    for a in soup.select("a[href]"):
        href = a.get("href", "")
        if not href.endswith(".html"):  # chapters are .html pages
            continue
        full = urljoin(start_url, href)
        base, _ = urldefrag(full)
        if base.endswith("contents.html"):
            continue
        if urlparse(base).netloc != urlparse(start_url).netloc:
            continue
        links.append(base)
    # de-dupe preserving order
    seen, ordered = set(), []
    for u in links:
        if u not in seen:
            seen.add(u)
            ordered.append(u)
    return ordered

def clean_text(s):
    return re.sub(r"\s+", " ", (s or "").strip())

def chapter_title(soup):
    h1 = soup.find("h1")
    return clean_text(h1.get_text(" ", strip=True)) if h1 else ""

def nearest_heading_id(el):
    ptr = el
    while ptr:
        ptr = ptr.find_previous(["h3", "h2", "h1"])
        if ptr:
            return (ptr.name, clean_text(ptr.get_text(" ", strip=True)), ptr.get("id"))
    return (None, None, None)

FILENAME_LANG_MAP = {
    ".java": "java", ".c": "c", ".h": "c",
    ".lox": "lox", ".py": "python", ".cpp": "cpp", ".hpp": "cpp",
    ".md": "markdown", ".sh": "bash",
}

def block_filename_hint(block):
    fig = block.find_parent("figure")
    caption, filehint = "", ""
    if fig:
        cap = fig.find("figcaption")
        if cap:
            caption = clean_text(cap.get_text(" ", strip=True))
            m = re.search(r"\b([A-Za-z0-9_\-./]+\.[A-Za-z0-9]+)\b", caption)
            if m:
                filehint = m.group(1)
    return caption, filehint

def guess_lang(block, figcaption_text="", filename_hint=""):
    classes = []
    for tag in (block, block.find("code")):
        if tag and tag.has_attr("class"):
            classes.extend(tag["class"])
    for cls in classes:
        m = re.match(r"(?:language|lang)-([A-Za-z0-9_+-]+)", cls)
        if m:
            return m.group(1).lower()
        if cls.lower() in ("java","c","cpp","python","bash","shell","sh","lox","javascript","json","cmake","makefile"):
            return cls.lower()
    for hint in (filename_hint, figcaption_text):
        if not hint:
            continue
        m = re.search(r"(\.[A-Za-z0-9]+)\b", hint)
        if m and m.group(1).lower() in FILENAME_LANG_MAP:
            return FILENAME_LANG_MAP[m.group(1).lower()]
        if "lox" in hint.lower():
            return "lox"
    text = ''.join((block.get_text('\n', strip=False) or "")).lower()
    if "#include" in text or "int main(" in text:
        return "c"
    if re.search(r"\bclass\s+\w+\s*{", text) and ";" in text and "(" in text and ")" in text:
        return "java"
    if "print(" in text and ";" not in text:
        return "python"
    if re.search(r"^\s*(var|fun|class)\s", text, re.M) and "lox" in text:
        return "lox"
    if re.search(r"^\s*\$", text, re.M):
        return "bash"
    return ""

# ------------ Core extraction ------------

def extract_blocks(chapter_url, session):
    soup = get_soup(chapter_url, session)
    chap_title = chapter_title(soup)

    # Candidates: <pre> (usually wrap code) and multi-line <code> not inside <pre>
    candidates = list(soup.select("pre"))
    for code in soup.select("code"):
        if not code.find_parent("pre") and "\n" in code.get_text():
            candidates.append(code)

    results = []
    for el in candidates:
        # Normalize: treat <code> inside <pre> as the block
        block = el.find("code") or el

        
        # join text nodes WITHOUT adding separators (prevents fake newlines from spans)
        # normalize Windows newlines; replace NBSP with regular space; trim only ONE trailing newline
        text = ''.join(block.strings).replace('\r\n', '\n').replace('\xa0', ' ')
        if text.endswith('\n'):
            text = text[:-1]

        # Skip only if truly empty. Allow short single-line <pre> blocks.
        is_pre = (el.name == "pre") or (el.find_parent("pre") is not None)
        if not text.strip():
            continue
        if not is_pre and ("\n" not in text) and len(text) < 40:
            # tiny inline <code> snippet, not a real code block
            continue

        # Section & anchor (nearest heading)
        _, sect_text, sect_id = nearest_heading_id(block)
        section = sect_text or chap_title

        # Language hint
        caption, filehint = block_filename_hint(block)
        lang = guess_lang(block, caption, filehint)

        # Anchored source URL if we have an id
        source = f"{chapter_url}#{sect_id}" if sect_id else chapter_url

        results.append({
            "chapter": chap_title,
            "section": section,
            "lang": lang,
            "source": source,
            "code": text,
        })
    return chap_title, results

# ------------ Writer ------------

def write_chapter_md(idx, title, url, snippets, outdir: Path):
    """
    Writes a compact Markdown file for a single chapter:
    - One compact header line per snippet (no separate 'Source:' line).
    - Minimal blank lines: header, code fence, code, fence, blank line.
    """
    outdir.mkdir(parents=True, exist_ok=True)
    fname = f"{idx:02d}-{slugify(title) or 'chapter'}.md"
    path = outdir / fname

    with path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"_From: {url}_\n\n")
        for i, snip in enumerate(snippets, 1):
            # Keep the link on the SAME line as the header
            f.write(f"#### {i}. {snip['section']} — [source]({snip['source']})\n")
            fence = "```" + (snip["lang"] or "")
            f.write(f"{fence}\n{snip['code']}\n```\n\n")
    return path

# ------------ Main ------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=DEFAULT_START, help="Contents page URL")
    ap.add_argument("--outdir", default="crafting_interpreters_code", help="Output directory (per-chapter .md files)")
    ap.add_argument("--max", type=int, default=None, help="Limit number of chapters (for testing)")
    ap.add_argument("--delay", type=float, default=0.6, help="Delay between requests (seconds)")
    args = ap.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    print(f"[+] Fetching ToC: {args.start}", file=sys.stderr)
    links = extract_toc_links(args.start, session)
    if not links:
        print("No chapter links found.", file=sys.stderr)
        sys.exit(2)
    if args.max:
        links = links[:args.max]

    outdir = Path(args.outdir)
    written = []

    for i, url in enumerate(links, 1):
        print(f"[{i}/{len(links)}] {url}", file=sys.stderr)
        try:
            chap_title, blocks = extract_blocks(url, session)
            if not chap_title:
                chap_title = f"Chapter {i}"
            p = write_chapter_md(i, chap_title, url, blocks, outdir)
            written.append(p)
        except Exception as e:
            print(f"  ! Failed {url}: {e}", file=sys.stderr)
        time.sleep(args.delay)

    print(f"[+] Wrote {len(written)} chapter files to {outdir.resolve()}", file=sys.stderr)

if __name__ == "__main__":
    main()
