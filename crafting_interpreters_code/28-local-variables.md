# Local Variables
_From: https://craftinginterpreters.com/local-variables.html_

#### 1. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
} ParseRule;
```

#### 2. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


typedef struct {
  Local locals[UINT8_COUNT];
  int localCount;
  int scopeDepth;
} Compiler;
```

#### 3. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


Parser parser;
```

#### 4. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
#define DEBUG_TRACE_EXECUTION
```

#### 5. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


#define UINT8_COUNT (UINT8_MAX + 1)
```

#### 6. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


#endif
```

#### 7. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
} ParseRule;
```

#### 8. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


typedef struct {
  Token name;
  int depth;
} Local;
```

#### 9. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


typedef struct {
```

#### 10. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
Parser parser;
```

#### 11. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
Compiler* current = NULL;
```

#### 12. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
Chunk* compilingChunk;
```

#### 13. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static void initCompiler(Compiler* compiler) {
  compiler->localCount = 0;
  compiler->scopeDepth = 0;
  current = compiler;
}
```

#### 14. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  initScanner(source);
```

#### 15. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  Compiler compiler;
  initCompiler(&compiler);
```

#### 16. 22 . 1 Representing Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  compilingChunk = chunk;
```

#### 17. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
statement      â exprStmt
               | printStmt
               | block ;

block          â "{" declaration* "}" ;
```

#### 18. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
  if (match(TOKEN_PRINT)) {
    printStatement();
```

#### 19. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
  } else if (match(TOKEN_LEFT_BRACE)) {
    beginScope();
    block();
    endScope();
```

#### 20. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
  } else {
```

#### 21. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
static void block() {
  while (!check(TOKEN_RIGHT_BRACE) && !check(TOKEN_EOF)) {
    declaration();
  }

  consume(TOKEN_RIGHT_BRACE, "Expect '}' after block.");
}
```

#### 22. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
static void beginScope() {
  current->scopeDepth++;
}
```

#### 23. 22 . 2 Block Statements — [source](https://craftinginterpreters.com/local-variables.html)
```
static void endScope() {
  current->scopeDepth--;
}
```

#### 24. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  consume(TOKEN_IDENTIFIER, errorMessage);
```

#### 25. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


  declareVariable();
  if (current->scopeDepth > 0) return 0;

```

#### 26. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  return identifierConstant(&parser.previous);
```

#### 27. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static void defineVariable(uint8_t global) {
```

#### 28. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  if (current->scopeDepth > 0) {
    return;
  }

```

#### 29. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  emitBytes(OP_DEFINE_GLOBAL, global);
```

#### 30. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static void declareVariable() {
  if (current->scopeDepth == 0) return;

  Token* name = &parser.previous;
  addLocal(*name);
}
```

#### 31. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static void addLocal(Token name) {
  Local* local = &current->locals[current->localCount++];
  local->name = name;
  local->depth = current->scopeDepth;
}
```

#### 32. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static void addLocal(Token name) {
```

#### 33. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  if (current->localCount == UINT8_COUNT) {
    error("Too many local variables in function.");
    return;
  }

```

#### 34. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  Local* local = &current->locals[current->localCount++];
```

#### 35. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
{
  var a = "first";
  var a = "second";
}
```

#### 36. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
{
  var a = "outer";
  {
    var a = "inner";
  }
}
```

#### 37. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  Token* name = &parser.previous;
```

#### 38. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  for (int i = current->localCount - 1; i >= 0; i--) {
    Local* local = &current->locals[i];
    if (local->depth != -1 && local->depth < current->scopeDepth) {
      break; 
    }

    if (identifiersEqual(name, &local->name)) {
      error("Already a variable with this name in this scope.");
    }
  }

```

#### 39. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  addLocal(*name);
}
```

#### 40. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static bool identifiersEqual(Token* a, Token* b) {
  if (a->length != b->length) return false;
  return memcmp(a->start, b->start, a->length) == 0;
}
```

#### 41. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```c
#include <stdlib.h>
```

#### 42. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```c
#include <string.h>
```

#### 43. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```c


#include "common.h"
```

#### 44. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  current->scopeDepth--;
```

#### 45. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```


  while (current->localCount > 0 &&
         current->locals[current->localCount - 1].depth >
            current->scopeDepth) {
    emitByte(OP_POP);
    current->localCount--;
  }
```

#### 46. 22 . 3 Declaring Local Variables — [source](https://craftinginterpreters.com/local-variables.html)
```
}
```

#### 47. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
static void namedVariable(Token name, bool canAssign) {
```

#### 48. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
  uint8_t getOp, setOp;
  int arg = resolveLocal(current, &name);
  if (arg != -1) {
    getOp = OP_GET_LOCAL;
    setOp = OP_SET_LOCAL;
  } else {
    arg = identifierConstant(&name);
    getOp = OP_GET_GLOBAL;
    setOp = OP_SET_GLOBAL;
  }
```

#### 49. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```


  if (canAssign && match(TOKEN_EQUAL)) {
```

#### 50. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
  if (canAssign && match(TOKEN_EQUAL)) {
    expression();
```

#### 51. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
    emitBytes(setOp, (uint8_t)arg);
```

#### 52. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
  } else {
```

#### 53. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
    emitBytes(setOp, (uint8_t)arg);
  } else {
```

#### 54. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
    emitBytes(getOp, (uint8_t)arg);
```

#### 55. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
  }
```

#### 56. 22 . 4 Using Locals — [source](https://craftinginterpreters.com/local-variables.html)
```
static int resolveLocal(Compiler* compiler, Token* name) {
  for (int i = compiler->localCount - 1; i >= 0; i--) {
    Local* local = &compiler->locals[i];
    if (identifiersEqual(name, &local->name)) {
      return i;
    }
  }

  return -1;
}
```

#### 57. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  OP_POP,
```

#### 58. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  OP_GET_LOCAL,
```

#### 59. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  OP_GET_GLOBAL,
```

#### 60. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      case OP_POP: pop(); break;
```

#### 61. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      case OP_GET_LOCAL: {
        uint8_t slot = READ_BYTE();
        push(vm.stack[slot]); 
        break;
      }
```

#### 62. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      case OP_GET_GLOBAL: {
```

#### 63. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  OP_GET_LOCAL,
```

#### 64. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  OP_SET_LOCAL,
```

#### 65. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
  OP_GET_GLOBAL,
```

#### 66. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      }
```

#### 67. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      case OP_SET_LOCAL: {
        uint8_t slot = READ_BYTE();
        vm.stack[slot] = peek(0);
        break;
      }
```

#### 68. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      case OP_GET_GLOBAL: {
```

#### 69. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
      return simpleInstruction("OP_POP", offset);
```

#### 70. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
    case OP_GET_LOCAL:
      return byteInstruction("OP_GET_LOCAL", chunk, offset);
    case OP_SET_LOCAL:
      return byteInstruction("OP_SET_LOCAL", chunk, offset);
```

#### 71. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
    case OP_GET_GLOBAL:
```

#### 72. 22 . 4 . 1 Interpreting local variables — [source](https://craftinginterpreters.com/local-variables.html)
```
static int byteInstruction(const char* name, Chunk* chunk,
                           int offset) {
  uint8_t slot = chunk->code[offset + 1];
  printf("%-16s %4d\n", name, slot);
  return offset + 2; 
}
```

#### 73. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
{
  var a = "outer";
  {
    var a = a;
  }
}
```

#### 74. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
  local->name = name;
```

#### 75. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
  local->depth = -1;
```

#### 76. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
}
```

#### 77. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
  if (current->scopeDepth > 0) {
```

#### 78. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
    markInitialized();
```

#### 79. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
    return;
  }
```

#### 80. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
static void markInitialized() {
  current->locals[current->localCount - 1].depth =
      current->scopeDepth;
}
```

#### 81. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
    if (identifiersEqual(name, &local->name)) {
```

#### 82. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
      if (local->depth == -1) {
        error("Can't read local variable in its own initializer.");
      }
```

#### 83. 22 . 4 . 2 Another scope edge case — [source](https://craftinginterpreters.com/local-variables.html)
```
      return i;
```

#### 84. Challenges — [source](https://craftinginterpreters.com/local-variables.html)
```
var a = a;
```

