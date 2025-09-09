# Mereck McGowan
## Program to scrape the Crafting Interpreters site and pull all of the code blocks
> All code blocks are generated in markdown files, and all code in those MD files belongs to the author of Crafting Interpreters.
> One markdown file per chapter

## To Use:
Set up VENV:
``` Python -m venv myenv ```
Then run:
``` pip install requests beautifulsoup4 lxml ``
Finally, to build the markdown files you can run:

```
python extract_crafting_interpreters_code.py \
      --outdir crafting_interpreters_code \
      --start https://craftinginterpreters.com/contents.html
 ```
Or just simply run the file. 

If you are getting errors on a mac you may need to change 
```
BeautifulSoup(r.text, "lxml")
```
to 
```
BeautifulSoup(r.text, "html.parser")
```
