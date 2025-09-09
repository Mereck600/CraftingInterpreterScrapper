# Scanning on Demand
_From: https://craftinginterpreters.com/scanning-on-demand.html_

#### 1. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
int main(int argc, const char* argv[]) {
  initVM();

```

#### 2. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (argc == 1) {
    repl();
  } else if (argc == 2) {
    runFile(argv[1]);
  } else {
    fprintf(stderr, "Usage: clox [path]\n");
    exit(64);
  }

  freeVM();
```

#### 3. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  return 0;
}
```

#### 4. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

```

#### 5. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include "common.h"
```

#### 6. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include "vm.h"
```

#### 7. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


static void repl() {
  char line[1024];
  for (;;) {
    printf("> ");

    if (!fgets(line, sizeof(line), stdin)) {
      printf("\n");
      break;
    }

    interpret(line);
  }
}
```

#### 8. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static void runFile(const char* path) {
  char* source = readFile(path);
  InterpretResult result = interpret(source);
  free(source); 

  if (result == INTERPRET_COMPILE_ERROR) exit(65);
  if (result == INTERPRET_RUNTIME_ERROR) exit(70);
}
```

#### 9. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static char* readFile(const char* path) {
  FILE* file = fopen(path, "rb");

  fseek(file, 0L, SEEK_END);
  size_t fileSize = ftell(file);
  rewind(file);

  char* buffer = (char*)malloc(fileSize + 1);
  size_t bytesRead = fread(buffer, sizeof(char), fileSize, file);
  buffer[bytesRead] = '\0';

  fclose(file);
  return buffer;
}
```

#### 10. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  FILE* file = fopen(path, "rb");
```

#### 11. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (file == NULL) {
    fprintf(stderr, "Could not open file \"%s\".\n", path);
    exit(74);
  }
```

#### 12. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


  fseek(file, 0L, SEEK_END);
```

#### 13. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  char* buffer = (char*)malloc(fileSize + 1);
```

#### 14. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (buffer == NULL) {
    fprintf(stderr, "Not enough memory to read \"%s\".\n", path);
    exit(74);
  }

```

#### 15. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  size_t bytesRead = fread(buffer, sizeof(char), fileSize, file);
```

#### 16. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  size_t bytesRead = fread(buffer, sizeof(char), fileSize, file);
```

#### 17. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (bytesRead < fileSize) {
    fprintf(stderr, "Could not read file \"%s\".\n", path);
    exit(74);
  }

```

#### 18. 16 . 1 Spinning Up the Interpreter — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  buffer[bytesRead] = '\0';
```

#### 19. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
void freeVM();
```

#### 20. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
InterpretResult interpret(const char* source);
```

#### 21. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
void push(Value value);
```

#### 22. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
InterpretResult interpret(const char* source) {
  compile(source);
  return INTERPRET_OK;
```

#### 23. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
}
```

#### 24. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include "common.h"
```

#### 25. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include "compiler.h"
```

#### 26. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include "debug.h"
```

#### 27. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
#ifndef clox_compiler_h
#define clox_compiler_h

void compile(const char* source);

#endif
```

#### 28. 16 . 1 . 1 Opening the compilation pipeline — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include <stdio.h>

#include "common.h"
#include "compiler.h"
#include "scanner.h"

void compile(const char* source) {
  initScanner(source);
}
```

#### 29. 16 . 1 . 2 The scanner scans — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
#ifndef clox_scanner_h
#define clox_scanner_h

void initScanner(const char* source);

#endif
```

#### 30. 16 . 1 . 2 The scanner scans — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```c
#include <stdio.h>
#include <string.h>

#include "common.h"
#include "scanner.h"

typedef struct {
  const char* start;
  const char* current;
  int line;
} Scanner;

Scanner scanner;
```

#### 31. 16 . 1 . 2 The scanner scans — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
void initScanner(const char* source) {
  scanner.start = source;
  scanner.current = source;
  scanner.line = 1;
}
```

#### 32. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  initScanner(source);
```

#### 33. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  int line = -1;
  for (;;) {
    Token token = scanToken();
    if (token.line != line) {
      printf("%4d ", token.line);
      line = token.line;
    } else {
      printf("   | ");
    }
    printf("%2d '%.*s'\n", token.type, token.length, token.start); 

    if (token.type == TOKEN_EOF) break;
  }
```

#### 34. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
}
```

#### 35. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
print 1 + 2;
```

#### 36. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
   1 31 'print'
   | 21 '1'
   |  7 '+'
   | 21 '2'
   |  8 ';'
   2 39 ''
```

#### 37. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
void initScanner(const char* source);
```

#### 38. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
Token scanToken();
```

#### 39. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


#endif
```

#### 40. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
#define clox_scanner_h
```

#### 41. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


typedef struct {
  TokenType type;
  const char* start;
  int length;
  int line;
} Token;
```

#### 42. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


void initScanner(const char* source);
```

#### 43. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
#ifndef clox_scanner_h
#define clox_scanner_h
```

#### 44. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


typedef enum {
  // Single-character tokens.
  TOKEN_LEFT_PAREN, TOKEN_RIGHT_PAREN,
  TOKEN_LEFT_BRACE, TOKEN_RIGHT_BRACE,
  TOKEN_COMMA, TOKEN_DOT, TOKEN_MINUS, TOKEN_PLUS,
  TOKEN_SEMICOLON, TOKEN_SLASH, TOKEN_STAR,
  // One or two character tokens.
  TOKEN_BANG, TOKEN_BANG_EQUAL,
  TOKEN_EQUAL, TOKEN_EQUAL_EQUAL,
  TOKEN_GREATER, TOKEN_GREATER_EQUAL,
  TOKEN_LESS, TOKEN_LESS_EQUAL,
  // Literals.
  TOKEN_IDENTIFIER, TOKEN_STRING, TOKEN_NUMBER,
  // Keywords.
  TOKEN_AND, TOKEN_CLASS, TOKEN_ELSE, TOKEN_FALSE,
  TOKEN_FOR, TOKEN_FUN, TOKEN_IF, TOKEN_NIL, TOKEN_OR,
  TOKEN_PRINT, TOKEN_RETURN, TOKEN_SUPER, TOKEN_THIS,
  TOKEN_TRUE, TOKEN_VAR, TOKEN_WHILE,

  TOKEN_ERROR, TOKEN_EOF
} TokenType;
```

#### 45. 16 . 2 A Token at a Time — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


typedef struct {
```

#### 46. 16 . 2 . 1 Scanning tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
Token scanToken() {
  scanner.start = scanner.current;

  if (isAtEnd()) return makeToken(TOKEN_EOF);

  return errorToken("Unexpected character.");
}
```

#### 47. 16 . 2 . 1 Scanning tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static bool isAtEnd() {
  return *scanner.current == '\0';
}
```

#### 48. 16 . 2 . 1 Scanning tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static Token makeToken(TokenType type) {
  Token token;
  token.type = type;
  token.start = scanner.start;
  token.length = (int)(scanner.current - scanner.start);
  token.line = scanner.line;
  return token;
}
```

#### 49. 16 . 2 . 1 Scanning tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static Token errorToken(const char* message) {
  Token token;
  token.type = TOKEN_ERROR;
  token.start = message;
  token.length = (int)strlen(message);
  token.line = scanner.line;
  return token;
}
```

#### 50. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (isAtEnd()) return makeToken(TOKEN_EOF);
```

#### 51. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


  char c = advance();

  switch (c) {
    case '(': return makeToken(TOKEN_LEFT_PAREN);
    case ')': return makeToken(TOKEN_RIGHT_PAREN);
    case '{': return makeToken(TOKEN_LEFT_BRACE);
    case '}': return makeToken(TOKEN_RIGHT_BRACE);
    case ';': return makeToken(TOKEN_SEMICOLON);
    case ',': return makeToken(TOKEN_COMMA);
    case '.': return makeToken(TOKEN_DOT);
    case '-': return makeToken(TOKEN_MINUS);
    case '+': return makeToken(TOKEN_PLUS);
    case '/': return makeToken(TOKEN_SLASH);
    case '*': return makeToken(TOKEN_STAR);
  }
```

#### 52. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


  return errorToken("Unexpected character.");
```

#### 53. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static char advance() {
  scanner.current++;
  return scanner.current[-1];
}
```

#### 54. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case '*': return makeToken(TOKEN_STAR);
```

#### 55. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case '!':
      return makeToken(
          match('=') ? TOKEN_BANG_EQUAL : TOKEN_BANG);
    case '=':
      return makeToken(
          match('=') ? TOKEN_EQUAL_EQUAL : TOKEN_EQUAL);
    case '<':
      return makeToken(
          match('=') ? TOKEN_LESS_EQUAL : TOKEN_LESS);
    case '>':
      return makeToken(
          match('=') ? TOKEN_GREATER_EQUAL : TOKEN_GREATER);
```

#### 56. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  }
```

#### 57. 16 . 3 A Lexical Grammar for Lox — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static bool match(char expected) {
  if (isAtEnd()) return false;
  if (*scanner.current != expected) return false;
  scanner.current++;
  return true;
}
```

#### 58. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
Token scanToken() {
```

#### 59. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  skipWhitespace();
```

#### 60. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  scanner.start = scanner.current;
```

#### 61. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static void skipWhitespace() {
  for (;;) {
    char c = peek();
    switch (c) {
      case ' ':
      case '\r':
      case '\t':
        advance();
        break;
      default:
        return;
    }
  }
}
```

#### 62. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static char peek() {
  return *scanner.current;
}
```

#### 63. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
        break;
```

#### 64. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
      case '\n':
        scanner.line++;
        advance();
        break;
```

#### 65. 16 . 3 . 1 Whitespace — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
      default:
        return;
```

#### 66. 16 . 3 . 2 Comments — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
        break;
```

#### 67. 16 . 3 . 2 Comments — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
      case '/':
        if (peekNext() == '/') {
          // A comment goes until the end of the line.
          while (peek() != '\n' && !isAtEnd()) advance();
        } else {
          return;
        }
        break;
```

#### 68. 16 . 3 . 2 Comments — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
      default:
        return;
```

#### 69. 16 . 3 . 2 Comments — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static char peekNext() {
  if (isAtEnd()) return '\0';
  return scanner.current[1];
}
```

#### 70. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
          match('=') ? TOKEN_GREATER_EQUAL : TOKEN_GREATER);
```

#### 71. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case '"': return string();
```

#### 72. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  }
```

#### 73. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static Token string() {
  while (peek() != '"' && !isAtEnd()) {
    if (peek() == '\n') scanner.line++;
    advance();
  }

  if (isAtEnd()) return errorToken("Unterminated string.");

  // The closing quote.
  advance();
  return makeToken(TOKEN_STRING);
}
```

#### 74. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  char c = advance();
```

#### 75. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (isDigit(c)) return number();
```

#### 76. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```


  switch (c) {
```

#### 77. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static bool isDigit(char c) {
  return c >= '0' && c <= '9';
}
```

#### 78. 16 . 3 . 3 Literal tokens — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static Token number() {
  while (isDigit(peek())) advance();

  // Look for a fractional part.
  if (peek() == '.' && isDigit(peekNext())) {
    // Consume the ".".
    advance();

    while (isDigit(peek())) advance();
  }

  return makeToken(TOKEN_NUMBER);
}
```

#### 79. 16 . 4 Identifiers and Keywords — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  char c = advance();
```

#### 80. 16 . 4 Identifiers and Keywords — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (isAlpha(c)) return identifier();
```

#### 81. 16 . 4 Identifiers and Keywords — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  if (isDigit(c)) return number();
```

#### 82. 16 . 4 Identifiers and Keywords — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static bool isAlpha(char c) {
  return (c >= 'a' && c <= 'z') ||
         (c >= 'A' && c <= 'Z') ||
          c == '_';
}
```

#### 83. 16 . 4 Identifiers and Keywords — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static Token identifier() {
  while (isAlpha(peek()) || isDigit(peek())) advance();
  return makeToken(identifierType());
}
```

#### 84. 16 . 4 Identifiers and Keywords — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static TokenType identifierType() {
  return TOKEN_IDENTIFIER;
}
```

#### 85. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static TokenType identifierType() {
```

#### 86. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  switch (scanner.start[0]) {
    case 'a': return checkKeyword(1, 2, "nd", TOKEN_AND);
    case 'c': return checkKeyword(1, 4, "lass", TOKEN_CLASS);
    case 'e': return checkKeyword(1, 3, "lse", TOKEN_ELSE);
    case 'i': return checkKeyword(1, 1, "f", TOKEN_IF);
    case 'n': return checkKeyword(1, 2, "il", TOKEN_NIL);
    case 'o': return checkKeyword(1, 1, "r", TOKEN_OR);
    case 'p': return checkKeyword(1, 4, "rint", TOKEN_PRINT);
    case 'r': return checkKeyword(1, 5, "eturn", TOKEN_RETURN);
    case 's': return checkKeyword(1, 4, "uper", TOKEN_SUPER);
    case 'v': return checkKeyword(1, 2, "ar", TOKEN_VAR);
    case 'w': return checkKeyword(1, 4, "hile", TOKEN_WHILE);
  }

```

#### 87. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
  return TOKEN_IDENTIFIER;
```

#### 88. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
static TokenType checkKeyword(int start, int length,
    const char* rest, TokenType type) {
  if (scanner.current - scanner.start == start + length &&
      memcmp(scanner.start + start, rest, length) == 0) {
    return type;
  }

  return TOKEN_IDENTIFIER;
}
```

#### 89. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case 'e': return checkKeyword(1, 3, "lse", TOKEN_ELSE);
```

#### 90. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case 'f':
      if (scanner.current - scanner.start > 1) {
        switch (scanner.start[1]) {
          case 'a': return checkKeyword(2, 3, "lse", TOKEN_FALSE);
          case 'o': return checkKeyword(2, 1, "r", TOKEN_FOR);
          case 'u': return checkKeyword(2, 1, "n", TOKEN_FUN);
        }
      }
      break;
```

#### 91. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case 'i': return checkKeyword(1, 1, "f", TOKEN_IF);
```

#### 92. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case 's': return checkKeyword(1, 4, "uper", TOKEN_SUPER);
```

#### 93. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case 't':
      if (scanner.current - scanner.start > 1) {
        switch (scanner.start[1]) {
          case 'h': return checkKeyword(2, 2, "is", TOKEN_THIS);
          case 'r': return checkKeyword(2, 2, "ue", TOKEN_TRUE);
        }
      }
      break;
```

#### 94. 16 . 4 . 1 Tries and state machines — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
    case 'v': return checkKeyword(1, 2, "ar", TOKEN_VAR);
```

#### 95. Challenges — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
var drink = "Tea";
var steep = 4;
var cool = 2;
print "${drink} will be ready in ${steep + cool} minutes.";
```

#### 96. Challenges — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
Tea will be ready in 6 minutes.
```

#### 97. Challenges — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
"Nested ${"interpolation?! Are you ${"mad?!"}"}"
```

#### 98. Challenges — [source](https://craftinginterpreters.com/scanning-on-demand.html)
```
vector<vector<string>> nestedVectors;
```

