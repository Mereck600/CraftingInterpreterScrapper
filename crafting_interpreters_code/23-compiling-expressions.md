# Compiling Expressions
_From: https://craftinginterpreters.com/compiling-expressions.html_

#### 1. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
InterpretResult interpret(const char* source) {
```

#### 2. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  Chunk chunk;
  initChunk(&chunk);

  if (!compile(source, &chunk)) {
    freeChunk(&chunk);
    return INTERPRET_COMPILE_ERROR;
  }

  vm.chunk = &chunk;
  vm.ip = vm.chunk->code;

  InterpretResult result = run();

  freeChunk(&chunk);
  return result;
```

#### 3. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 4. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
#define clox_compiler_h

```

#### 5. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include "vm.h"

bool compile(const char* source, Chunk* chunk);
```

#### 6. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


#endif
```

#### 7. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include "scanner.h"

```

#### 8. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
bool compile(const char* source, Chunk* chunk) {
```

#### 9. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  initScanner(source);
```

#### 10. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  initScanner(source);
```

#### 11. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  advance();
  expression();
  consume(TOKEN_EOF, "Expect end of expression.");
```

#### 12. Compiling Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 13. 17 . 2 Parsing Tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include "scanner.h"
```

#### 14. 17 . 2 Parsing Tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


static void advance() {
  parser.previous = parser.current;

  for (;;) {
    parser.current = scanToken();
    if (parser.current.type != TOKEN_ERROR) break;

    errorAtCurrent(parser.current.start);
  }
}
```

#### 15. 17 . 2 Parsing Tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include "scanner.h"
```

#### 16. 17 . 2 Parsing Tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


typedef struct {
  Token current;
  Token previous;
} Parser;

Parser parser;
```

#### 17. 17 . 2 Parsing Tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


static void advance() {
```

#### 18. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void errorAtCurrent(const char* message) {
  errorAt(&parser.current, message);
}
```

#### 19. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void error(const char* message) {
  errorAt(&parser.previous, message);
}
```

#### 20. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void errorAt(Token* token, const char* message) {
  fprintf(stderr, "[line %d] Error", token->line);

  if (token->type == TOKEN_EOF) {
    fprintf(stderr, " at end");
  } else if (token->type == TOKEN_ERROR) {
    // Nothing.
  } else {
    fprintf(stderr, " at '%.*s'", token->length, token->start);
  }

  fprintf(stderr, ": %s\n", message);
  parser.hadError = true;
}
```

#### 21. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  Token previous;
```

#### 22. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  bool hadError;
```

#### 23. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
} Parser;
```

#### 24. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  consume(TOKEN_EOF, "Expect end of expression.");
```

#### 25. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  return !parser.hadError;
```

#### 26. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 27. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  bool hadError;
```

#### 28. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  bool panicMode;
```

#### 29. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
} Parser;
```

#### 30. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void errorAt(Token* token, const char* message) {
```

#### 31. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  parser.panicMode = true;
```

#### 32. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  fprintf(stderr, "[line %d] Error", token->line);
```

#### 33. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void errorAt(Token* token, const char* message) {
```

#### 34. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  if (parser.panicMode) return;
```

#### 35. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  parser.panicMode = true;
```

#### 36. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  initScanner(source);
```

#### 37. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


  parser.hadError = false;
  parser.panicMode = false;

```

#### 38. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  advance();
```

#### 39. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include <stdio.h>
```

#### 40. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include <stdlib.h>
```

#### 41. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c


#include "common.h"
```

#### 42. 17 . 2 . 1 Handling syntax errors — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void consume(TokenType type, const char* message) {
  if (parser.current.type == type) {
    advance();
    return;
  }

  errorAtCurrent(message);
}
```

#### 43. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void emitByte(uint8_t byte) {
  writeChunk(currentChunk(), byte, parser.previous.line);
}
```

#### 44. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
Parser parser;
```

#### 45. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
Chunk* compilingChunk;

static Chunk* currentChunk() {
  return compilingChunk;
}

```

#### 46. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void errorAt(Token* token, const char* message) {
```

#### 47. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
bool compile(const char* source, Chunk* chunk) {
  initScanner(source);
```

#### 48. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  compilingChunk = chunk;
```

#### 49. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


  parser.hadError = false;
```

#### 50. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  consume(TOKEN_EOF, "Expect end of expression.");
```

#### 51. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  endCompiler();
```

#### 52. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  return !parser.hadError;
```

#### 53. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void endCompiler() {
  emitReturn();
}
```

#### 54. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void emitReturn() {
  emitByte(OP_RETURN);
}
```

#### 55. 17 . 3 Emitting Bytecode — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void emitBytes(uint8_t byte1, uint8_t byte2) {
  emitByte(byte1);
  emitByte(byte2);
}
```

#### 56. 17 . 4 Parsing Prefix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void expression() {
  // What goes here?
}
```

#### 57. 17 . 4 . 1 Parsers for tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void number() {
  double value = strtod(parser.previous.start, NULL);
  emitConstant(value);
}
```

#### 58. 17 . 4 . 1 Parsers for tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void emitConstant(Value value) {
  emitBytes(OP_CONSTANT, makeConstant(value));
}
```

#### 59. 17 . 4 . 1 Parsers for tokens — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static uint8_t makeConstant(Value value) {
  int constant = addConstant(currentChunk(), value);
  if (constant > UINT8_MAX) {
    error("Too many constants in one chunk.");
    return 0;
  }

  return (uint8_t)constant;
}
```

#### 60. 17 . 4 . 2 Parentheses for grouping — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void grouping() {
  expression();
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after expression.");
}
```

#### 61. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void unary() {
  TokenType operatorType = parser.previous.type;

  // Compile the operand.
  expression();

  // Emit the operator instruction.
  switch (operatorType) {
    case TOKEN_MINUS: emitByte(OP_NEGATE); break;
    default: return; // Unreachable.
  }
}
```

#### 62. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
print -
  true;
```

#### 63. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
-a.b + c;
```

#### 64. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void parsePrecedence(Precedence precedence) {
  // What goes here?
}
```

#### 65. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
} Parser;
```

#### 66. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


typedef enum {
  PREC_NONE,
  PREC_ASSIGNMENT,  // =
  PREC_OR,          // or
  PREC_AND,         // and
  PREC_EQUALITY,    // == !=
  PREC_COMPARISON,  // < > <= >=
  PREC_TERM,        // + -
  PREC_FACTOR,      // * /
  PREC_UNARY,       // ! -
  PREC_CALL,        // . ()
  PREC_PRIMARY
} Precedence;
```

#### 67. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


Parser parser;
```

#### 68. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
-a.b + c
```

#### 69. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void expression() {
```

#### 70. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  parsePrecedence(PREC_ASSIGNMENT);
```

#### 71. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 72. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  // Compile the operand.
```

#### 73. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  parsePrecedence(PREC_UNARY);
```

#### 74. 17 . 4 . 3 Unary negation — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


  // Emit the operator instruction.
```

#### 75. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
1 + 2
```

#### 76. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void binary() {
  TokenType operatorType = parser.previous.type;
  ParseRule* rule = getRule(operatorType);
  parsePrecedence((Precedence)(rule->precedence + 1));

  switch (operatorType) {
    case TOKEN_PLUS:          emitByte(OP_ADD); break;
    case TOKEN_MINUS:         emitByte(OP_SUBTRACT); break;
    case TOKEN_STAR:          emitByte(OP_MULTIPLY); break;
    case TOKEN_SLASH:         emitByte(OP_DIVIDE); break;
    default: return; // Unreachable.
  }
}
```

#### 77. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
2 * 3 + 4
```

#### 78. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
1 + 2 + 3 + 4
```

#### 79. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
((1 + 2) + 3) + 4
```

#### 80. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
a = b = c = d
```

#### 81. 17 . 5 Parsing Infix Expressions — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
a = (b = (c = d))
```

#### 82. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
} Precedence;
```

#### 83. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


typedef struct {
  ParseFn prefix;
  ParseFn infix;
  Precedence precedence;
} ParseRule;
```

#### 84. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


Parser parser;
```

#### 85. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
} Precedence;
```

#### 86. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


typedef void (*ParseFn)();
```

#### 87. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


typedef struct {
```

#### 88. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
ParseRule rules[] = {
  [TOKEN_LEFT_PAREN]    = {grouping, NULL,   PREC_NONE},
  [TOKEN_RIGHT_PAREN]   = {NULL,     NULL,   PREC_NONE},
  [TOKEN_LEFT_BRACE]    = {NULL,     NULL,   PREC_NONE}, 
  [TOKEN_RIGHT_BRACE]   = {NULL,     NULL,   PREC_NONE},
  [TOKEN_COMMA]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_DOT]           = {NULL,     NULL,   PREC_NONE},
  [TOKEN_MINUS]         = {unary,    binary, PREC_TERM},
  [TOKEN_PLUS]          = {NULL,     binary, PREC_TERM},
  [TOKEN_SEMICOLON]     = {NULL,     NULL,   PREC_NONE},
  [TOKEN_SLASH]         = {NULL,     binary, PREC_FACTOR},
  [TOKEN_STAR]          = {NULL,     binary, PREC_FACTOR},
  [TOKEN_BANG]          = {NULL,     NULL,   PREC_NONE},
  [TOKEN_BANG_EQUAL]    = {NULL,     NULL,   PREC_NONE},
  [TOKEN_EQUAL]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_EQUAL_EQUAL]   = {NULL,     NULL,   PREC_NONE},
  [TOKEN_GREATER]       = {NULL,     NULL,   PREC_NONE},
  [TOKEN_GREATER_EQUAL] = {NULL,     NULL,   PREC_NONE},
  [TOKEN_LESS]          = {NULL,     NULL,   PREC_NONE},
  [TOKEN_LESS_EQUAL]    = {NULL,     NULL,   PREC_NONE},
  [TOKEN_IDENTIFIER]    = {NULL,     NULL,   PREC_NONE},
  [TOKEN_STRING]        = {NULL,     NULL,   PREC_NONE},
  [TOKEN_NUMBER]        = {number,   NULL,   PREC_NONE},
  [TOKEN_AND]           = {NULL,     NULL,   PREC_NONE},
  [TOKEN_CLASS]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_ELSE]          = {NULL,     NULL,   PREC_NONE},
  [TOKEN_FALSE]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_FOR]           = {NULL,     NULL,   PREC_NONE},
  [TOKEN_FUN]           = {NULL,     NULL,   PREC_NONE},
  [TOKEN_IF]            = {NULL,     NULL,   PREC_NONE},
  [TOKEN_NIL]           = {NULL,     NULL,   PREC_NONE},
  [TOKEN_OR]            = {NULL,     NULL,   PREC_NONE},
  [TOKEN_PRINT]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_RETURN]        = {NULL,     NULL,   PREC_NONE},
  [TOKEN_SUPER]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_THIS]          = {NULL,     NULL,   PREC_NONE},
  [TOKEN_TRUE]          = {NULL,     NULL,   PREC_NONE},
  [TOKEN_VAR]           = {NULL,     NULL,   PREC_NONE},
  [TOKEN_WHILE]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_ERROR]         = {NULL,     NULL,   PREC_NONE},
  [TOKEN_EOF]           = {NULL,     NULL,   PREC_NONE},
};
```

#### 89. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static ParseRule* getRule(TokenType type) {
  return &rules[type];
}
```

#### 90. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  emitReturn();
}
```

#### 91. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


static void expression();
static ParseRule* getRule(TokenType type);
static void parsePrecedence(Precedence precedence);

```

#### 92. 17 . 6 A Pratt Parser — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void binary() {
```

#### 93. 17 . 6 . 1 Parsing with precedence — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
static void parsePrecedence(Precedence precedence) {
```

#### 94. 17 . 6 . 1 Parsing with precedence — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  advance();
  ParseFn prefixRule = getRule(parser.previous.type)->prefix;
  if (prefixRule == NULL) {
    error("Expect expression.");
    return;
  }

  prefixRule();
```

#### 95. 17 . 6 . 1 Parsing with precedence — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 96. 17 . 6 . 1 Parsing with precedence — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  prefixRule();
```

#### 97. 17 . 6 . 1 Parsing with precedence — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


  while (precedence <= getRule(parser.current.type)->precedence) {
    advance();
    ParseFn infixRule = getRule(parser.previous.type)->infix;
    infixRule();
  }
```

#### 98. 17 . 6 . 1 Parsing with precedence — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 99. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include <stdint.h>

```

#### 100. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
#define DEBUG_PRINT_CODE
```

#### 101. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
#define DEBUG_TRACE_EXECUTION
```

#### 102. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
  emitReturn();
```

#### 103. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
#ifdef DEBUG_PRINT_CODE
  if (!parser.hadError) {
    disassembleChunk(currentChunk(), "code");
  }
#endif
```

#### 104. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
}
```

#### 105. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c
#include "scanner.h"
```

#### 106. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```c


#ifdef DEBUG_PRINT_CODE
#include "debug.h"
#endif
```

#### 107. 17 . 7 Dumping Chunks — [source](https://craftinginterpreters.com/compiling-expressions.html)
```


typedef struct {
```

#### 108. Challenges — [source](https://craftinginterpreters.com/compiling-expressions.html)
```
(-1 + 2) * 3 - -4
```

