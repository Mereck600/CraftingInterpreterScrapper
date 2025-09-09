# Jumping Back and Forth
_From: https://craftinginterpreters.com/jumping-back-and-forth.html_

#### 1. Jumping Back and Forth — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
if (condition) print("condition was truthy");
```

#### 2. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  if (match(TOKEN_PRINT)) {
    printStatement();
```

#### 3. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  } else if (match(TOKEN_IF)) {
    ifStatement();
```

#### 4. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  } else if (match(TOKEN_LEFT_BRACE)) {
```

#### 5. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void ifStatement() {
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'if'.");
  expression();
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after condition."); 

  int thenJump = emitJump(OP_JUMP_IF_FALSE);
  statement();

  patchJump(thenJump);
}
```

#### 6. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
if condition) print("looks weird");
```

#### 7. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static int emitJump(uint8_t instruction) {
  emitByte(instruction);
  emitByte(0xff);
  emitByte(0xff);
  return currentChunk()->count - 2;
}
```

#### 8. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void patchJump(int offset) {
  // -2 to adjust for the bytecode for the jump offset itself.
  int jump = currentChunk()->count - offset - 2;

  if (jump > UINT16_MAX) {
    error("Too much code to jump over.");
  }

  currentChunk()->code[offset] = (jump >> 8) & 0xff;
  currentChunk()->code[offset + 1] = jump & 0xff;
}
```

#### 9. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_PRINT,
```

#### 10. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_JUMP_IF_FALSE,
```

#### 11. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_RETURN,
```

#### 12. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
        break;
      }
```

#### 13. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      case OP_JUMP_IF_FALSE: {
        uint16_t offset = READ_SHORT();
        if (isFalsey(peek(0))) vm.ip += offset;
        break;
      }
```

#### 14. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      case OP_RETURN: {
```

#### 15. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

#### 16. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
#define READ_SHORT() \
    (vm.ip += 2, (uint16_t)((vm.ip[-2] << 8) | vm.ip[-1]))
```

#### 17. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
#define READ_STRING() AS_STRING(READ_CONSTANT())
```

#### 18. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
#undef READ_BYTE
```

#### 19. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
#undef READ_SHORT
```

#### 20. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
#undef READ_CONSTANT
```

#### 21. 23 . 1 If Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
case OP_JUMP_IF_FALSE: {
  uint16_t offset = READ_SHORT();
  vm.ip += falsey() * offset;
  break;
}
```

#### 22. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  patchJump(thenJump);
```

#### 23. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```


  if (match(TOKEN_ELSE)) statement();
```

#### 24. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
}
```

#### 25. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  statement();

```

#### 26. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  int elseJump = emitJump(OP_JUMP);

```

#### 27. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  patchJump(thenJump);
```

#### 28. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  if (match(TOKEN_ELSE)) statement();
```

#### 29. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  patchJump(elseJump);
```

#### 30. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
}
```

#### 31. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_PRINT,
```

#### 32. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_JUMP,
```

#### 33. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_JUMP_IF_FALSE,
```

#### 34. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
        break;
      }
```

#### 35. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      case OP_JUMP: {
        uint16_t offset = READ_SHORT();
        vm.ip += offset;
        break;
      }
```

#### 36. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      case OP_JUMP_IF_FALSE: {
```

#### 37. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  int thenJump = emitJump(OP_JUMP_IF_FALSE);
```

#### 38. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  emitByte(OP_POP);
```

#### 39. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  statement();
```

#### 40. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  patchJump(thenJump);
```

#### 41. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  emitByte(OP_POP);
```

#### 42. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```


  if (match(TOKEN_ELSE)) statement();
```

#### 43. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      return simpleInstruction("OP_PRINT", offset);
```

#### 44. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
    case OP_JUMP:
      return jumpInstruction("OP_JUMP", 1, chunk, offset);
    case OP_JUMP_IF_FALSE:
      return jumpInstruction("OP_JUMP_IF_FALSE", 1, chunk, offset);
```

#### 45. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
    case OP_RETURN:
```

#### 46. 23 . 1 . 1 Else clauses — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static int jumpInstruction(const char* name, int sign,
                           Chunk* chunk, int offset) {
  uint16_t jump = (uint16_t)(chunk->code[offset + 1] << 8);
  jump |= chunk->code[offset + 2];
  printf("%-16s %4d -> %d\n", name, offset,
         offset + 3 + sign * jump);
  return offset + 3;
}
```

#### 47. 23 . 2 Logical Operators — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  [TOKEN_NUMBER]        = {number,   NULL,   PREC_NONE},
```

#### 48. 23 . 2 Logical Operators — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  [TOKEN_AND]           = {NULL,     and_,   PREC_AND},
```

#### 49. 23 . 2 Logical Operators — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  [TOKEN_CLASS]         = {NULL,     NULL,   PREC_NONE},
```

#### 50. 23 . 2 Logical Operators — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void and_(bool canAssign) {
  int endJump = emitJump(OP_JUMP_IF_FALSE);

  emitByte(OP_POP);
  parsePrecedence(PREC_AND);

  patchJump(endJump);
}
```

#### 51. 23 . 2 . 1 Logical or operator — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  [TOKEN_NIL]           = {literal,  NULL,   PREC_NONE},
```

#### 52. 23 . 2 . 1 Logical or operator — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  [TOKEN_OR]            = {NULL,     or_,    PREC_OR},
```

#### 53. 23 . 2 . 1 Logical or operator — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  [TOKEN_PRINT]         = {NULL,     NULL,   PREC_NONE},
```

#### 54. 23 . 2 . 1 Logical or operator — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void or_(bool canAssign) {
  int elseJump = emitJump(OP_JUMP_IF_FALSE);
  int endJump = emitJump(OP_JUMP);

  patchJump(elseJump);
  emitByte(OP_POP);

  parsePrecedence(PREC_OR);
  patchJump(endJump);
}
```

#### 55. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
    ifStatement();
```

#### 56. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  } else if (match(TOKEN_WHILE)) {
    whileStatement();
```

#### 57. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  } else if (match(TOKEN_LEFT_BRACE)) {
```

#### 58. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void whileStatement() {
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'while'.");
  expression();
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after condition.");

  int exitJump = emitJump(OP_JUMP_IF_FALSE);
  emitByte(OP_POP);
  statement();

  patchJump(exitJump);
  emitByte(OP_POP);
}
```

#### 59. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  statement();
```

#### 60. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  emitLoop(loopStart);
```

#### 61. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```


  patchJump(exitJump);
```

#### 62. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void whileStatement() {
```

#### 63. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  int loopStart = currentChunk()->count;
```

#### 64. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'while'.");
```

#### 65. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void emitLoop(int loopStart) {
  emitByte(OP_LOOP);

  int offset = currentChunk()->count - loopStart + 2;
  if (offset > UINT16_MAX) error("Loop body too large.");

  emitByte((offset >> 8) & 0xff);
  emitByte(offset & 0xff);
}
```

#### 66. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_JUMP_IF_FALSE,
```

#### 67. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_LOOP,
```

#### 68. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  OP_RETURN,
```

#### 69. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      }
```

#### 70. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      case OP_LOOP: {
        uint16_t offset = READ_SHORT();
        vm.ip -= offset;
        break;
      }
```

#### 71. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      case OP_RETURN: {
```

#### 72. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
      return jumpInstruction("OP_JUMP_IF_FALSE", 1, chunk, offset);
```

#### 73. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
    case OP_LOOP:
      return jumpInstruction("OP_LOOP", -1, chunk, offset);
```

#### 74. 23 . 3 While Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
    case OP_RETURN:
```

#### 75. 23 . 4 For Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
    printStatement();
```

#### 76. 23 . 4 For Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  } else if (match(TOKEN_FOR)) {
    forStatement();
```

#### 77. 23 . 4 For Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  } else if (match(TOKEN_IF)) {
```

#### 78. 23 . 4 For Statements — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void forStatement() {
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'for'.");
  consume(TOKEN_SEMICOLON, "Expect ';'.");

  int loopStart = currentChunk()->count;
  consume(TOKEN_SEMICOLON, "Expect ';'.");
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after for clauses.");

  statement();
  emitLoop(loopStart);
}
```

#### 79. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'for'.");
```

#### 80. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  if (match(TOKEN_SEMICOLON)) {
    // No initializer.
  } else if (match(TOKEN_VAR)) {
    varDeclaration();
  } else {
    expressionStatement();
  }
```

#### 81. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```


  int loopStart = currentChunk()->count;
```

#### 82. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
static void forStatement() {
```

#### 83. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  beginScope();
```

#### 84. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'for'.");
```

#### 85. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  emitLoop(loopStart);
```

#### 86. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  endScope();
```

#### 87. 23 . 4 . 1 Initializer clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
}
```

#### 88. 23 . 4 . 2 Condition clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  int loopStart = currentChunk()->count;
```

#### 89. 23 . 4 . 2 Condition clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  int exitJump = -1;
  if (!match(TOKEN_SEMICOLON)) {
    expression();
    consume(TOKEN_SEMICOLON, "Expect ';' after loop condition.");

    // Jump out of the loop if the condition is false.
    exitJump = emitJump(OP_JUMP_IF_FALSE);
    emitByte(OP_POP); // Condition.
  }

```

#### 90. 23 . 4 . 2 Condition clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after for clauses.");
```

#### 91. 23 . 4 . 2 Condition clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  emitLoop(loopStart);
```

#### 92. 23 . 4 . 2 Condition clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```


  if (exitJump != -1) {
    patchJump(exitJump);
    emitByte(OP_POP); // Condition.
  }

```

#### 93. 23 . 4 . 2 Condition clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  endScope();
}
```

#### 94. 23 . 4 . 3 Increment clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  }

```

#### 95. 23 . 4 . 3 Increment clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
  if (!match(TOKEN_RIGHT_PAREN)) {
    int bodyJump = emitJump(OP_JUMP);
    int incrementStart = currentChunk()->count;
    expression();
    emitByte(OP_POP);
    consume(TOKEN_RIGHT_PAREN, "Expect ')' after for clauses.");

    emitLoop(loopStart);
    loopStart = incrementStart;
    patchJump(bodyJump);
  }
```

#### 96. 23 . 4 . 3 Increment clause — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```


  statement();
```

#### 97. Challenges — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
switchStmt     â "switch" "(" expression ")"
                 "{" switchCase* defaultCase? "}" ;
switchCase     â "case" expression ":" statement* ;
defaultCase    â "default" ":" statement* ;
```

#### 98. Challenges — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
continueStmt   â "continue" ";" ;
```

#### 99. Design Note: Considering Goto Harmful — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
// See if the matrix contains a zero.
bool found = false;
for (int x = 0; x < xSize; x++) {
  for (int y = 0; y < ySize; y++) {
    for (int z = 0; z < zSize; z++) {
      if (matrix[x][y][z] == 0) {
        printf("found");
        found = true;
        break;
      }
    }
    if (found) break;
  }
  if (found) break;
}
```

#### 100. Design Note: Considering Goto Harmful — [source](https://craftinginterpreters.com/jumping-back-and-forth.html)
```
for (int x = 0; x < xSize; x++) {
  for (int y = 0; y < ySize; y++) {
    for (int z = 0; z < zSize; z++) {
      if (matrix[x][y][z] == 0) {
        printf("found");
        goto done;
      }
    }
  }
}
done:
```

