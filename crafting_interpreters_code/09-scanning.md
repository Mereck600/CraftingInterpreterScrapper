# Scanning
_From: https://craftinginterpreters.com/scanning.html_

#### 1. 4 . 1 The Interpreter Framework — [source](https://craftinginterpreters.com/scanning.html)
```java
package com.craftinginterpreters.lox;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Lox {
  public static void main(String[] args) throws IOException {
    if (args.length > 1) {
      System.out.println("Usage: jlox [script]");
      System.exit(64); 
    } else if (args.length == 1) {
      runFile(args[0]);
    } else {
      runPrompt();
    }
  }
}
```

#### 2. 4 . 1 The Interpreter Framework — [source](https://craftinginterpreters.com/scanning.html)
```
  private static void runFile(String path) throws IOException {
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    run(new String(bytes, Charset.defaultCharset()));
  }
```

#### 3. 4 . 1 The Interpreter Framework — [source](https://craftinginterpreters.com/scanning.html)
```
(print (eval (read)))
```

#### 4. 4 . 1 The Interpreter Framework — [source](https://craftinginterpreters.com/scanning.html)
```
  private static void runPrompt() throws IOException {
    InputStreamReader input = new InputStreamReader(System.in);
    BufferedReader reader = new BufferedReader(input);

    for (;;) { 
      System.out.print("> ");
      String line = reader.readLine();
      if (line == null) break;
      run(line);
    }
  }
```

#### 5. 4 . 1 The Interpreter Framework — [source](https://craftinginterpreters.com/scanning.html)
```
  private static void run(String source) {
    Scanner scanner = new Scanner(source);
    List<Token> tokens = scanner.scanTokens();

    // For now, just print the tokens.
    for (Token token : tokens) {
      System.out.println(token);
    }
  }
```

#### 6. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
  static void error(int line, String message) {
    report(line, "", message);
  }

  private static void report(int line, String where,
                             String message) {
    System.err.println(
        "[line " + line + "] Error" + where + ": " + message);
    hadError = true;
  }
```

#### 7. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
Error: Unexpected "," somewhere in your code. Good luck finding it!
```

#### 8. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
Error: Unexpected "," in argument list.

    15 | function(first, second,);
                               ^-- Here.
```

#### 9. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
public class Lox {
```

#### 10. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
  static boolean hadError = false;
```

#### 11. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
    run(new String(bytes, Charset.defaultCharset()));
```

#### 12. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```


    // Indicate an error in the exit code.
    if (hadError) System.exit(65);
```

#### 13. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
  }
```

#### 14. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
      run(line);
```

#### 15. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
      hadError = false;
```

#### 16. 4 . 1 . 1 Error handling — [source](https://craftinginterpreters.com/scanning.html)
```
    }
```

#### 17. 4 . 2 Lexemes and Tokens — [source](https://craftinginterpreters.com/scanning.html)
```lox
var language = "lox";
```

#### 18. 4 . 2 . 1 Token type — [source](https://craftinginterpreters.com/scanning.html)
```lox
package com.craftinginterpreters.lox;

enum TokenType {
  // Single-character tokens.
  LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
  COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,

  // One or two character tokens.
  BANG, BANG_EQUAL,
  EQUAL, EQUAL_EQUAL,
  GREATER, GREATER_EQUAL,
  LESS, LESS_EQUAL,

  // Literals.
  IDENTIFIER, STRING, NUMBER,

  // Keywords.
  AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,
  PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,

  EOF
}
```

#### 19. 4 . 2 . 3 Location information — [source](https://craftinginterpreters.com/scanning.html)
```java
package com.craftinginterpreters.lox;

class Token {
  final TokenType type;
  final String lexeme;
  final Object literal;
  final int line; 

  Token(TokenType type, String lexeme, Object literal, int line) {
    this.type = type;
    this.lexeme = lexeme;
    this.literal = literal;
    this.line = line;
  }

  public String toString() {
    return type + " " + lexeme + " " + literal;
  }
}
```

#### 20. 4 . 3 Regular Languages and Expressions — [source](https://craftinginterpreters.com/scanning.html)
```
[a-zA-Z_][a-zA-Z_0-9]*
```

#### 21. 4 . 4 The Scanner Class — [source](https://craftinginterpreters.com/scanning.html)
```java
package com.craftinginterpreters.lox;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.craftinginterpreters.lox.TokenType.*; 

class Scanner {
  private final String source;
  private final List<Token> tokens = new ArrayList<>();

  Scanner(String source) {
    this.source = source;
  }
}
```

#### 22. 4 . 4 The Scanner Class — [source](https://craftinginterpreters.com/scanning.html)
```
  List<Token> scanTokens() {
    while (!isAtEnd()) {
      // We are at the beginning of the next lexeme.
      start = current;
      scanToken();
    }

    tokens.add(new Token(EOF, "", null, line));
    return tokens;
  }
```

#### 23. 4 . 4 The Scanner Class — [source](https://craftinginterpreters.com/scanning.html)
```
  private final List<Token> tokens = new ArrayList<>();
```

#### 24. 4 . 4 The Scanner Class — [source](https://craftinginterpreters.com/scanning.html)
```
  private int start = 0;
  private int current = 0;
  private int line = 1;
```

#### 25. 4 . 4 The Scanner Class — [source](https://craftinginterpreters.com/scanning.html)
```


  Scanner(String source) {
```

#### 26. 4 . 4 The Scanner Class — [source](https://craftinginterpreters.com/scanning.html)
```
  private boolean isAtEnd() {
    return current >= source.length();
  }
```

#### 27. 4 . 5 Recognizing Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
  private void scanToken() {
    char c = advance();
    switch (c) {
      case '(': addToken(LEFT_PAREN); break;
      case ')': addToken(RIGHT_PAREN); break;
      case '{': addToken(LEFT_BRACE); break;
      case '}': addToken(RIGHT_BRACE); break;
      case ',': addToken(COMMA); break;
      case '.': addToken(DOT); break;
      case '-': addToken(MINUS); break;
      case '+': addToken(PLUS); break;
      case ';': addToken(SEMICOLON); break;
      case '*': addToken(STAR); break; 
    }
  }
```

#### 28. 4 . 5 Recognizing Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
  private char advance() {
    return source.charAt(current++);
  }

  private void addToken(TokenType type) {
    addToken(type, null);
  }

  private void addToken(TokenType type, Object literal) {
    String text = source.substring(start, current);
    tokens.add(new Token(type, text, literal, line));
  }
```

#### 29. 4 . 5 . 1 Lexical errors — [source](https://craftinginterpreters.com/scanning.html)
```
      case '*': addToken(STAR); break; 
```

#### 30. 4 . 5 . 1 Lexical errors — [source](https://craftinginterpreters.com/scanning.html)
```


      default:
        Lox.error(line, "Unexpected character.");
        break;
```

#### 31. 4 . 5 . 1 Lexical errors — [source](https://craftinginterpreters.com/scanning.html)
```
    }
```

#### 32. 4 . 5 . 2 Operators — [source](https://craftinginterpreters.com/scanning.html)
```
      case '*': addToken(STAR); break; 
```

#### 33. 4 . 5 . 2 Operators — [source](https://craftinginterpreters.com/scanning.html)
```
      case '!':
        addToken(match('=') ? BANG_EQUAL : BANG);
        break;
      case '=':
        addToken(match('=') ? EQUAL_EQUAL : EQUAL);
        break;
      case '<':
        addToken(match('=') ? LESS_EQUAL : LESS);
        break;
      case '>':
        addToken(match('=') ? GREATER_EQUAL : GREATER);
        break;
```

#### 34. 4 . 5 . 2 Operators — [source](https://craftinginterpreters.com/scanning.html)
```


      default:
```

#### 35. 4 . 5 . 2 Operators — [source](https://craftinginterpreters.com/scanning.html)
```
  private boolean match(char expected) {
    if (isAtEnd()) return false;
    if (source.charAt(current) != expected) return false;

    current++;
    return true;
  }
```

#### 36. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
        break;
```

#### 37. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
      case '/':
        if (match('/')) {
          // A comment goes until the end of the line.
          while (peek() != '\n' && !isAtEnd()) advance();
        } else {
          addToken(SLASH);
        }
        break;
```

#### 38. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```


      default:
```

#### 39. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
  private char peek() {
    if (isAtEnd()) return '\0';
    return source.charAt(current);
  }
```

#### 40. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
        break;
```

#### 41. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```


      case ' ':
      case '\r':
      case '\t':
        // Ignore whitespace.
        break;

      case '\n':
        line++;
        break;
```

#### 42. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```


      default:
        Lox.error(line, "Unexpected character.");
```

#### 43. 4 . 6 Longer Lexemes — [source](https://craftinginterpreters.com/scanning.html)
```
// this is a comment
(( )){} // grouping stuff
!*+-/=<> <= == // operators
```

#### 44. 4 . 6 . 1 String literals — [source](https://craftinginterpreters.com/scanning.html)
```
        break;
```

#### 45. 4 . 6 . 1 String literals — [source](https://craftinginterpreters.com/scanning.html)
```


      case '"': string(); break;
```

#### 46. 4 . 6 . 1 String literals — [source](https://craftinginterpreters.com/scanning.html)
```


      default:
```

#### 47. 4 . 6 . 1 String literals — [source](https://craftinginterpreters.com/scanning.html)
```
  private void string() {
    while (peek() != '"' && !isAtEnd()) {
      if (peek() == '\n') line++;
      advance();
    }

    if (isAtEnd()) {
      Lox.error(line, "Unterminated string.");
      return;
    }

    // The closing ".
    advance();

    // Trim the surrounding quotes.
    String value = source.substring(start + 1, current - 1);
    addToken(STRING, value);
  }
```

#### 48. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
print -123.abs();
```

#### 49. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
var n = 123;
print -n.abs();
```

#### 50. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
1234
12.34
```

#### 51. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
.1234
1234.
```

#### 52. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
      default:
```

#### 53. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
        if (isDigit(c)) {
          number();
        } else {
          Lox.error(line, "Unexpected character.");
        }
```

#### 54. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
        break;
```

#### 55. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
  private boolean isDigit(char c) {
    return c >= '0' && c <= '9';
  } 
```

#### 56. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
  private void number() {
    while (isDigit(peek())) advance();

    // Look for a fractional part.
    if (peek() == '.' && isDigit(peekNext())) {
      // Consume the "."
      advance();

      while (isDigit(peek())) advance();
    }

    addToken(NUMBER,
        Double.parseDouble(source.substring(start, current)));
  }
```

#### 57. 4 . 6 . 2 Number literals — [source](https://craftinginterpreters.com/scanning.html)
```
  private char peekNext() {
    if (current + 1 >= source.length()) return '\0';
    return source.charAt(current + 1);
  } 
```

#### 58. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
case 'o':
  if (match('r')) {
    addToken(OR);
  }
  break;
```

#### 59. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
---a;
```

#### 60. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
- --a;
```

#### 61. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
-- -a;
```

#### 62. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
      default:
        if (isDigit(c)) {
          number();
```

#### 63. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
        } else if (isAlpha(c)) {
          identifier();
```

#### 64. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
        } else {
          Lox.error(line, "Unexpected character.");
        }
```

#### 65. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
  private void identifier() {
    while (isAlphaNumeric(peek())) advance();

    addToken(IDENTIFIER);
  }
```

#### 66. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
  private boolean isAlpha(char c) {
    return (c >= 'a' && c <= 'z') ||
           (c >= 'A' && c <= 'Z') ||
            c == '_';
  }

  private boolean isAlphaNumeric(char c) {
    return isAlpha(c) || isDigit(c);
  }
```

#### 67. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
  private static final Map<String, TokenType> keywords;

  static {
    keywords = new HashMap<>();
    keywords.put("and",    AND);
    keywords.put("class",  CLASS);
    keywords.put("else",   ELSE);
    keywords.put("false",  FALSE);
    keywords.put("for",    FOR);
    keywords.put("fun",    FUN);
    keywords.put("if",     IF);
    keywords.put("nil",    NIL);
    keywords.put("or",     OR);
    keywords.put("print",  PRINT);
    keywords.put("return", RETURN);
    keywords.put("super",  SUPER);
    keywords.put("this",   THIS);
    keywords.put("true",   TRUE);
    keywords.put("var",    VAR);
    keywords.put("while",  WHILE);
  }
```

#### 68. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
    while (isAlphaNumeric(peek())) advance();

```

#### 69. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
    String text = source.substring(start, current);
    TokenType type = keywords.get(text);
    if (type == null) type = IDENTIFIER;
    addToken(type);
```

#### 70. 4 . 7 Reserved Words and Identifiers — [source](https://craftinginterpreters.com/scanning.html)
```
  }
```

#### 71. Design Note: Implicit Semicolons — [source](https://craftinginterpreters.com/scanning.html)
```
if (condition) return
"value"
```

#### 72. Design Note: Implicit Semicolons — [source](https://craftinginterpreters.com/scanning.html)
```
func
(parenthesized)
```

#### 73. Design Note: Implicit Semicolons — [source](https://craftinginterpreters.com/scanning.html)
```
first
-second
```

#### 74. Design Note: Implicit Semicolons — [source](https://craftinginterpreters.com/scanning.html)
```
a = 1 b = 2
```

#### 75. Design Note: Implicit Semicolons — [source](https://craftinginterpreters.com/scanning.html)
```
console.log(function() {
  statement();
});
```

