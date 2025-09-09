# Global Variables
_From: https://craftinginterpreters.com/global-variables.html_

#### 1. Global Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
fun showVariable() {
  print global;
}

var global = "after";
showVariable();
```

#### 2. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
if (monday) var croissant = "yes"; // Error.
```

#### 3. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
statement      â exprStmt
               | forStmt
               | ifStmt
               | printStmt
               | returnStmt
               | whileStmt
               | block ;
```

#### 4. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
declaration    â classDecl
               | funDecl
               | varDecl
               | statement ;
```

#### 5. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
statement      â exprStmt
               | printStmt ;

declaration    â varDecl
               | statement ;
```

#### 6. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  advance();
```

#### 7. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```


  while (!match(TOKEN_EOF)) {
    declaration();
  }

```

#### 8. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  endCompiler();
```

#### 9. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static void declaration() {
  statement();
}
```

#### 10. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static void statement() {
  if (match(TOKEN_PRINT)) {
    printStatement();
  }
}
```

#### 11. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static void expression();
```

#### 12. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static void statement();
static void declaration();
```

#### 13. 21 . 1 Statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static ParseRule* getRule(TokenType type);
```

#### 14. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static bool match(TokenType type) {
  if (!check(type)) return false;
  advance();
  return true;
}
```

#### 15. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static bool check(TokenType type) {
  return parser.current.type == type;
}
```

#### 16. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static void printStatement() {
  expression();
  consume(TOKEN_SEMICOLON, "Expect ';' after value.");
  emitByte(OP_PRINT);
}
```

#### 17. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_NEGATE,
```

#### 18. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_PRINT,
```

#### 19. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_RETURN,
```

#### 20. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
        break;
```

#### 21. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_PRINT: {
        printValue(pop());
        printf("\n");
        break;
      }
```

#### 22. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_RETURN: {
```

#### 23. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_RETURN: {
```

#### 24. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
        // Exit interpreter.
```

#### 25. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
        return INTERPRET_OK;
```

#### 26. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      return simpleInstruction("OP_NEGATE", offset);
```

#### 27. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_PRINT:
      return simpleInstruction("OP_PRINT", offset);
```

#### 28. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_RETURN:
```

#### 29. 21 . 1 . 1 Print statements — [source](https://craftinginterpreters.com/global-variables.html)
```
print 1 + 2;
print 3 * 4;
```

#### 30. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
    printStatement();
```

#### 31. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  } else {
    expressionStatement();
```

#### 32. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  }
```

#### 33. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
static void expressionStatement() {
  expression();
  consume(TOKEN_SEMICOLON, "Expect ';' after expression.");
  emitByte(OP_POP);
}
```

#### 34. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
brunch = "quiche";
eat(brunch);
```

#### 35. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_FALSE,
```

#### 36. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_POP,
```

#### 37. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_EQUAL,
```

#### 38. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_FALSE: push(BOOL_VAL(false)); break;
```

#### 39. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_POP: pop(); break;
```

#### 40. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_EQUAL: {
```

#### 41. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
      return simpleInstruction("OP_FALSE", offset);
```

#### 42. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_POP:
      return simpleInstruction("OP_POP", offset);
```

#### 43. 21 . 1 . 2 Expression statements — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_EQUAL:
```

#### 44. 21 . 1 . 3 Error synchronization — [source](https://craftinginterpreters.com/global-variables.html)
```
  statement();
```

#### 45. 21 . 1 . 3 Error synchronization — [source](https://craftinginterpreters.com/global-variables.html)
```


  if (parser.panicMode) synchronize();
```

#### 46. 21 . 1 . 3 Error synchronization — [source](https://craftinginterpreters.com/global-variables.html)
```
}
```

#### 47. 21 . 1 . 3 Error synchronization — [source](https://craftinginterpreters.com/global-variables.html)
```
static void synchronize() {
  parser.panicMode = false;

  while (parser.current.type != TOKEN_EOF) {
    if (parser.previous.type == TOKEN_SEMICOLON) return;
    switch (parser.current.type) {
      case TOKEN_CLASS:
      case TOKEN_FUN:
      case TOKEN_VAR:
      case TOKEN_FOR:
      case TOKEN_IF:
      case TOKEN_WHILE:
      case TOKEN_PRINT:
      case TOKEN_RETURN:
        return;

      default:
        ; // Do nothing.
    }

    advance();
  }
}
```

#### 48. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static void declaration() {
```

#### 49. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  if (match(TOKEN_VAR)) {
    varDeclaration();
  } else {
    statement();
  }
```

#### 50. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```


  if (parser.panicMode) synchronize();
```

#### 51. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static void varDeclaration() {
  uint8_t global = parseVariable("Expect variable name.");

  if (match(TOKEN_EQUAL)) {
    expression();
  } else {
    emitByte(OP_NIL);
  }
  consume(TOKEN_SEMICOLON,
          "Expect ';' after variable declaration.");

  defineVariable(global);
}
```

#### 52. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
var a;
```

#### 53. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
var a = nil;
```

#### 54. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static void parsePrecedence(Precedence precedence);

```

#### 55. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static uint8_t parseVariable(const char* errorMessage) {
  consume(TOKEN_IDENTIFIER, errorMessage);
  return identifierConstant(&parser.previous);
}
```

#### 56. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static void parsePrecedence(Precedence precedence);

```

#### 57. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static uint8_t identifierConstant(Token* name) {
  return makeConstant(OBJ_VAL(copyString(name->start,
                                         name->length)));
}
```

#### 58. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
static void defineVariable(uint8_t global) {
  emitBytes(OP_DEFINE_GLOBAL, global);
}
```

#### 59. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_POP,
```

#### 60. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_DEFINE_GLOBAL,
```

#### 61. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_EQUAL,
```

#### 62. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_POP: pop(); break;
```

#### 63. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_DEFINE_GLOBAL: {
        ObjString* name = READ_STRING();
        tableSet(&vm.globals, name, peek(0));
        pop();
        break;
      }
```

#### 64. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_EQUAL: {
```

#### 65. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

#### 66. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
#define READ_STRING() AS_STRING(READ_CONSTANT())
```

#### 67. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
#define BINARY_OP(valueType, op) \
```

#### 68. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
#undef READ_CONSTANT
```

#### 69. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
#undef READ_STRING
```

#### 70. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
#undef BINARY_OP
```

#### 71. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  Value* stackTop;
```

#### 72. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  Table globals;
```

#### 73. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  Table strings;
```

#### 74. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  vm.objects = NULL;
```

#### 75. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```


  initTable(&vm.globals);
```

#### 76. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  initTable(&vm.strings);
```

#### 77. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
void freeVM() {
```

#### 78. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  freeTable(&vm.globals);
```

#### 79. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
  freeTable(&vm.strings);
```

#### 80. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
      return simpleInstruction("OP_POP", offset);
```

#### 81. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_DEFINE_GLOBAL:
      return constantInstruction("OP_DEFINE_GLOBAL", chunk,
                                 offset);
```

#### 82. 21 . 2 Variable Declarations — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_EQUAL:
```

#### 83. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
  [TOKEN_LESS_EQUAL]    = {NULL,     binary, PREC_COMPARISON},
```

#### 84. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
  [TOKEN_IDENTIFIER]    = {variable, NULL,   PREC_NONE},
```

#### 85. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
  [TOKEN_STRING]        = {string,   NULL,   PREC_NONE},
```

#### 86. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
static void variable() {
  namedVariable(parser.previous);
}
```

#### 87. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
static void namedVariable(Token name) {
  uint8_t arg = identifierConstant(&name);
  emitBytes(OP_GET_GLOBAL, arg);
}
```

#### 88. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_POP,
```

#### 89. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_GET_GLOBAL,
```

#### 90. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_DEFINE_GLOBAL,
```

#### 91. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_POP: pop(); break;
```

#### 92. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_GET_GLOBAL: {
        ObjString* name = READ_STRING();
        Value value;
        if (!tableGet(&vm.globals, name, &value)) {
          runtimeError("Undefined variable '%s'.", name->chars);
          return INTERPRET_RUNTIME_ERROR;
        }
        push(value);
        break;
      }
```

#### 93. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_DEFINE_GLOBAL: {
```

#### 94. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
      return simpleInstruction("OP_POP", offset);
```

#### 95. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_GET_GLOBAL:
      return constantInstruction("OP_GET_GLOBAL", chunk, offset);
```

#### 96. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_DEFINE_GLOBAL:
```

#### 97. 21 . 3 Reading Variables — [source](https://craftinginterpreters.com/global-variables.html)
```
var beverage = "cafe au lait";
var breakfast = "beignets with " + beverage;
print breakfast;
```

#### 98. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
menu.brunch(sunday).beverage = "mimosa";
```

#### 99. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  uint8_t arg = identifierConstant(&name);
```

#### 100. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```


  if (match(TOKEN_EQUAL)) {
    expression();
    emitBytes(OP_SET_GLOBAL, arg);
  } else {
    emitBytes(OP_GET_GLOBAL, arg);
  }
```

#### 101. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
}
```

#### 102. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_DEFINE_GLOBAL,
```

#### 103. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_SET_GLOBAL,
```

#### 104. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  OP_EQUAL,
```

#### 105. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
      }
```

#### 106. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_SET_GLOBAL: {
        ObjString* name = READ_STRING();
        if (tableSet(&vm.globals, name, peek(0))) {
          tableDelete(&vm.globals, name); 
          runtimeError("Undefined variable '%s'.", name->chars);
          return INTERPRET_RUNTIME_ERROR;
        }
        break;
      }
```

#### 107. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
      case OP_EQUAL: {
```

#### 108. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
      return constantInstruction("OP_DEFINE_GLOBAL", chunk,
                                 offset);
```

#### 109. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_SET_GLOBAL:
      return constantInstruction("OP_SET_GLOBAL", chunk, offset);
```

#### 110. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    case OP_EQUAL:
```

#### 111. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
a * b = c + d;
```

#### 112. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    error("Expect expression.");
    return;
  }

```

#### 113. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  bool canAssign = precedence <= PREC_ASSIGNMENT;
  prefixRule(canAssign);
```

#### 114. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```


  while (precedence <= getRule(parser.current.type)->precedence) {
```

#### 115. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void variable(bool canAssign) {
  namedVariable(parser.previous, canAssign);
}
```

#### 116. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void namedVariable(Token name, bool canAssign) {
```

#### 117. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  uint8_t arg = identifierConstant(&name);
```

#### 118. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  uint8_t arg = identifierConstant(&name);

```

#### 119. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  if (canAssign && match(TOKEN_EQUAL)) {
```

#### 120. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    expression();
```

#### 121. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    infixRule();
  }
```

#### 122. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```


  if (canAssign && match(TOKEN_EQUAL)) {
    error("Invalid assignment target.");
  }
```

#### 123. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
}
```

#### 124. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    ParseFn infixRule = getRule(parser.previous.type)->infix;
```

#### 125. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
    infixRule(canAssign);
```

#### 126. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  }
```

#### 127. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
} Precedence;

```

#### 128. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
typedef void (*ParseFn)(bool canAssign);
```

#### 129. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```


typedef struct {
```

#### 130. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void binary(bool canAssign) {
```

#### 131. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  TokenType operatorType = parser.previous.type;
```

#### 132. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void literal(bool canAssign) {
```

#### 133. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  switch (parser.previous.type) {
```

#### 134. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void grouping(bool canAssign) {
```

#### 135. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  expression();
```

#### 136. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void number(bool canAssign) {
```

#### 137. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  double value = strtod(parser.previous.start, NULL);
```

#### 138. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void string(bool canAssign) {
```

#### 139. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  emitConstant(OBJ_VAL(copyString(parser.previous.start + 1,
```

#### 140. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
static void unary(bool canAssign) {
```

#### 141. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
  TokenType operatorType = parser.previous.type;
```

#### 142. 21 . 4 Assignment — [source](https://craftinginterpreters.com/global-variables.html)
```
var breakfast = "beignets";
var beverage = "cafe au lait";
breakfast = "beignets with " + beverage;

print breakfast;
```

#### 143. Challenges — [source](https://craftinginterpreters.com/global-variables.html)
```
fun useVar() {
  print oops;
}

var ooops = "too many o's!";
```

