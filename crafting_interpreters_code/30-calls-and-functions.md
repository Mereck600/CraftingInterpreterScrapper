# Calls and Functions
_From: https://craftinginterpreters.com/calls-and-functions.html_

#### 1. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  struct Obj* next;
};
```

#### 2. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


typedef struct {
  Obj obj;
  int arity;
  Chunk chunk;
  ObjString* name;
} ObjFunction;
```

#### 3. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


struct ObjString {
```

#### 4. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "common.h"
```

#### 5. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "chunk.h"
```

#### 6. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "value.h"
```

#### 7. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  uint32_t hash;
};

```

#### 8. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjFunction* newFunction();
```

#### 9. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjString* takeString(char* chars, int length);
```

#### 10. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjFunction* newFunction() {
  ObjFunction* function = ALLOCATE_OBJ(ObjFunction, OBJ_FUNCTION);
  function->arity = 0;
  function->name = NULL;
  initChunk(&function->chunk);
  return function;
}
```

#### 11. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
typedef enum {
```

#### 12. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OBJ_FUNCTION,
```

#### 13. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OBJ_STRING,
} ObjType;
```

#### 14. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  switch (object->type) {
```

#### 15. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_FUNCTION: {
      ObjFunction* function = (ObjFunction*)object;
      freeChunk(&function->chunk);
      FREE(ObjFunction, object);
      break;
    }
```

#### 16. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_STRING: {
```

#### 17. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  switch (OBJ_TYPE(value)) {
```

#### 18. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_FUNCTION:
      printFunction(AS_FUNCTION(value));
      break;
```

#### 19. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_STRING:
```

#### 20. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void printFunction(ObjFunction* function) {
  printf("<fn %s>", function->name->chars);
}
```

#### 21. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)

```

#### 22. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

#### 23. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

#### 24. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)

```

#### 25. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

#### 26. 24 . 1 Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define AS_STRING(value)       ((ObjString*)AS_OBJ(value))
```

#### 27. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
typedef struct {
```

#### 28. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  ObjFunction* function;
  FunctionType type;

```

#### 29. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  Local locals[UINT8_COUNT];
```

#### 30. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
typedef enum {
  TYPE_FUNCTION,
  TYPE_SCRIPT
} FunctionType;
```

#### 31. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
Compiler* current = NULL;
```

#### 32. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


static Chunk* currentChunk() {
  return &current->function->chunk;
}
```

#### 33. 24 . 2 Compiling to Function Objects — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


static void errorAt(Token* token, const char* message) {
```

#### 34. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  Compiler compiler;
```

#### 35. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  initCompiler(&compiler, TYPE_SCRIPT);
```

#### 36. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  parser.hadError = false;
```

#### 37. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void initCompiler(Compiler* compiler, FunctionType type) {
  compiler->function = NULL;
  compiler->type = type;
```

#### 38. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  compiler->localCount = 0;
```

#### 39. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  compiler->scopeDepth = 0;
```

#### 40. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  compiler->function = newFunction();
```

#### 41. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  current = compiler;
```

#### 42. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  current = compiler;
```

#### 43. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  Local* local = &current->locals[current->localCount++];
  local->depth = 0;
  local->name.start = "";
  local->name.length = 0;
```

#### 44. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
}
```

#### 45. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static ObjFunction* endCompiler() {
```

#### 46. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  emitReturn();
```

#### 47. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  emitReturn();
```

#### 48. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  ObjFunction* function = current->function;

```

#### 49. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#ifdef DEBUG_PRINT_CODE
```

#### 50. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#endif
```

#### 51. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  return function;
```

#### 52. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
}
```

#### 53. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#ifdef DEBUG_PRINT_CODE
  if (!parser.hadError) {
```

#### 54. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    disassembleChunk(currentChunk(), function->name != NULL
        ? function->name->chars : "<script>");
```

#### 55. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  }
#endif
```

#### 56. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void printFunction(ObjFunction* function) {
```

#### 57. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (function->name == NULL) {
    printf("<script>");
    return;
  }
```

#### 58. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  printf("<fn %s>", function->name->chars);
```

#### 59. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "vm.h"

```

#### 60. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjFunction* compile(const char* source);
```

#### 61. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


#endif
```

#### 62. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjFunction* compile(const char* source) {
```

#### 63. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  initScanner(source);
```

#### 64. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  while (!match(TOKEN_EOF)) {
    declaration();
  }

```

#### 65. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  ObjFunction* function = endCompiler();
  return parser.hadError ? NULL : function;
```

#### 66. 24 . 2 . 1 Creating functions at compile time — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
}
```

#### 67. 24 . 3 . 1 Allocating local variables — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun first() {
  var a = 1;
  second();
  var b = 2;
}

fun second() {
  var c = 3;
  var d = 4;
}

first();
```

#### 68. 24 . 3 . 1 Allocating local variables — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun first() {
  var a = 1;
  second();
  var b = 2;
  second();
}

fun second() {
  var c = 3;
  var d = 4;
}

first();
```

#### 69. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define STACK_MAX 256
```

#### 70. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


typedef struct {
  ObjFunction* function;
  uint8_t* ip;
  Value* slots;
} CallFrame;
```

#### 71. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


typedef struct {
```

#### 72. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
typedef struct {
```

#### 73. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  CallFrame frames[FRAMES_MAX];
  int frameCount;

```

#### 74. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  Value stack[STACK_MAX];
```

#### 75. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "value.h"

```

#### 76. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define FRAMES_MAX 64
#define STACK_MAX (FRAMES_MAX * UINT8_COUNT)
```

#### 77. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


typedef struct {
```

#### 78. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  vm.stackTop = vm.stack;
```

#### 79. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  vm.frameCount = 0;
```

#### 80. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
}
```

#### 81. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define clox_vm_h

```

#### 82. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "object.h"
```

#### 83. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include "table.h"
```

#### 84. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static InterpretResult run() {
```

#### 85. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  CallFrame* frame = &vm.frames[vm.frameCount - 1];

#define READ_BYTE() (*frame->ip++)

#define READ_SHORT() \
    (frame->ip += 2, \
    (uint16_t)((frame->ip[-2] << 8) | frame->ip[-1]))

#define READ_CONSTANT() \
    (frame->function->chunk.constants.values[READ_BYTE()])

```

#### 86. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define READ_STRING() AS_STRING(READ_CONSTANT())
```

#### 87. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_GET_LOCAL: {
        uint8_t slot = READ_BYTE();
```

#### 88. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        push(frame->slots[slot]);
```

#### 89. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        break;
```

#### 90. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_SET_LOCAL: {
        uint8_t slot = READ_BYTE();
```

#### 91. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        frame->slots[slot] = peek(0);
```

#### 92. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        break;
```

#### 93. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_JUMP: {
        uint16_t offset = READ_SHORT();
```

#### 94. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        frame->ip += offset;
```

#### 95. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        break;
```

#### 96. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_JUMP_IF_FALSE: {
        uint16_t offset = READ_SHORT();
```

#### 97. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        if (isFalsey(peek(0))) frame->ip += offset;
```

#### 98. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        break;
```

#### 99. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_LOOP: {
        uint16_t offset = READ_SHORT();
```

#### 100. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        frame->ip -= offset;
```

#### 101. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        break;
```

#### 102. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    printf("\n");
```

#### 103. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    disassembleInstruction(&frame->function->chunk,
        (int)(frame->ip - frame->function->chunk.code));
```

#### 104. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#endif
```

#### 105. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
InterpretResult interpret(const char* source) {
```

#### 106. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  ObjFunction* function = compile(source);
  if (function == NULL) return INTERPRET_COMPILE_ERROR;

  push(OBJ_VAL(function));
  CallFrame* frame = &vm.frames[vm.frameCount++];
  frame->function = function;
  frame->ip = function->chunk.code;
  frame->slots = vm.stack;
```

#### 107. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  InterpretResult result = run();
```

#### 108. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  frame->slots = vm.stack;

```

#### 109. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  return run();
```

#### 110. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
}
```

#### 111. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  fputs("\n", stderr);

```

#### 112. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  CallFrame* frame = &vm.frames[vm.frameCount - 1];
  size_t instruction = frame->ip - frame->function->chunk.code - 1;
  int line = frame->function->chunk.lines[instruction];
```

#### 113. 24 . 3 . 3 The call stack — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  fprintf(stderr, "[line %d] in script\n", line);
```

#### 114. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void declaration() {
```

#### 115. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (match(TOKEN_FUN)) {
    funDeclaration();
  } else if (match(TOKEN_VAR)) {
```

#### 116. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    varDeclaration();
```

#### 117. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void funDeclaration() {
  uint8_t global = parseVariable("Expect function name.");
  markInitialized();
  function(TYPE_FUNCTION);
  defineVariable(global);
}
```

#### 118. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void markInitialized() {
```

#### 119. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (current->scopeDepth == 0) return;
```

#### 120. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  current->locals[current->localCount - 1].depth =
```

#### 121. 24 . 4 Function Declarations — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void function(FunctionType type) {
  Compiler compiler;
  initCompiler(&compiler, type);
  beginScope(); 

  consume(TOKEN_LEFT_PAREN, "Expect '(' after function name.");
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after parameters.");
  consume(TOKEN_LEFT_BRACE, "Expect '{' before function body.");
  block();

  ObjFunction* function = endCompiler();
  emitBytes(OP_CONSTANT, makeConstant(OBJ_VAL(function)));
}
```

#### 122. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
} FunctionType;

```

#### 123. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
typedef struct Compiler {
  struct Compiler* enclosing;
```

#### 124. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  ObjFunction* function;
```

#### 125. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void initCompiler(Compiler* compiler, FunctionType type) {
```

#### 126. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  compiler->enclosing = current;
```

#### 127. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  compiler->function = NULL;
```

#### 128. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#endif

```

#### 129. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  current = current->enclosing;
```

#### 130. 24 . 4 . 1 A stack of compilers — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  return function;
```

#### 131. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after function name.");
```

#### 132. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (!check(TOKEN_RIGHT_PAREN)) {
    do {
      current->function->arity++;
      if (current->function->arity > 255) {
        errorAtCurrent("Can't have more than 255 parameters.");
      }
      uint8_t constant = parseVariable("Expect parameter name.");
      defineVariable(constant);
    } while (match(TOKEN_COMMA));
  }
```

#### 133. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after parameters.");
```

#### 134. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  current = compiler;
```

#### 135. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (type != TYPE_SCRIPT) {
    current->function->name = copyString(parser.previous.start,
                                         parser.previous.length);
  }
```

#### 136. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  Local* local = &current->locals[current->localCount++];
```

#### 137. 24 . 4 . 2 Function parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun areWeHavingItYet() {
  print "Yes we are!";
}

print areWeHavingItYet;
```

#### 138. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ParseRule rules[] = {
```

#### 139. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  [TOKEN_LEFT_PAREN]    = {grouping, call,   PREC_CALL},
```

#### 140. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  [TOKEN_RIGHT_PAREN]   = {NULL,     NULL,   PREC_NONE},
```

#### 141. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void call(bool canAssign) {
  uint8_t argCount = argumentList();
  emitBytes(OP_CALL, argCount);
}
```

#### 142. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static uint8_t argumentList() {
  uint8_t argCount = 0;
  if (!check(TOKEN_RIGHT_PAREN)) {
    do {
      expression();
      argCount++;
    } while (match(TOKEN_COMMA));
  }
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after arguments.");
  return argCount;
}
```

#### 143. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      expression();
```

#### 144. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      if (argCount == 255) {
        error("Can't have more than 255 arguments.");
      }
```

#### 145. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      argCount++;
```

#### 146. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OP_LOOP,
```

#### 147. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OP_CALL,
```

#### 148. 24 . 5 Function Calls — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OP_RETURN,
```

#### 149. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun sum(a, b, c) {
  return a + b + c;
}

print 4 + sum(5, 6, 7);
```

#### 150. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      }
```

#### 151. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_CALL: {
        int argCount = READ_BYTE();
        if (!callValue(peek(argCount), argCount)) {
          return INTERPRET_RUNTIME_ERROR;
        }
        break;
      }
```

#### 152. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_RETURN: {
```

#### 153. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
          return INTERPRET_RUNTIME_ERROR;
        }
```

#### 154. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        frame = &vm.frames[vm.frameCount - 1];
```

#### 155. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        break;
```

#### 156. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static bool callValue(Value callee, int argCount) {
  if (IS_OBJ(callee)) {
    switch (OBJ_TYPE(callee)) {
      case OBJ_FUNCTION: 
        return call(AS_FUNCTION(callee), argCount);
      default:
        break; // Non-callable object type.
    }
  }
  runtimeError("Can only call functions and classes.");
  return false;
}
```

#### 157. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
var notAFunction = 123;
notAFunction();
```

#### 158. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static bool call(ObjFunction* function, int argCount) {
  CallFrame* frame = &vm.frames[vm.frameCount++];
  frame->function = function;
  frame->ip = function->chunk.code;
  frame->slots = vm.stackTop - argCount - 1;
  return true;
}
```

#### 159. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      return jumpInstruction("OP_LOOP", -1, chunk, offset);
```

#### 160. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OP_CALL:
      return byteInstruction("OP_CALL", chunk, offset);
```

#### 161. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OP_RETURN:
```

#### 162. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  push(OBJ_VAL(function));
```

#### 163. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  call(function, 0);
```

#### 164. 24 . 5 . 1 Binding arguments to parameters — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  return run();
```

#### 165. 24 . 5 . 2 Runtime error checking — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static bool call(ObjFunction* function, int argCount) {
```

#### 166. 24 . 5 . 2 Runtime error checking — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (argCount != function->arity) {
    runtimeError("Expected %d arguments but got %d.",
        function->arity, argCount);
    return false;
  }

```

#### 167. 24 . 5 . 2 Runtime error checking — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  CallFrame* frame = &vm.frames[vm.frameCount++];
```

#### 168. 24 . 5 . 2 Runtime error checking — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  }

```

#### 169. 24 . 5 . 2 Runtime error checking — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (vm.frameCount == FRAMES_MAX) {
    runtimeError("Stack overflow.");
    return false;
  }

```

#### 170. 24 . 5 . 2 Runtime error checking — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  CallFrame* frame = &vm.frames[vm.frameCount++];
```

#### 171. 24 . 5 . 3 Printing stack traces — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  fputs("\n", stderr);

```

#### 172. 24 . 5 . 3 Printing stack traces — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  for (int i = vm.frameCount - 1; i >= 0; i--) {
    CallFrame* frame = &vm.frames[i];
    ObjFunction* function = frame->function;
    size_t instruction = frame->ip - function->chunk.code - 1;
    fprintf(stderr, "[line %d] in ", 
            function->chunk.lines[instruction]);
    if (function->name == NULL) {
      fprintf(stderr, "script\n");
    } else {
      fprintf(stderr, "%s()\n", function->name->chars);
    }
  }

```

#### 173. 24 . 5 . 3 Printing stack traces — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  resetStack();
}
```

#### 174. 24 . 5 . 3 Printing stack traces — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun a() { b(); }
fun b() { c(); }
fun c() {
  c("too", "many");
}

a();
```

#### 175. 24 . 5 . 3 Printing stack traces — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
Expected 0 arguments but got 2.
[line 4] in c()
[line 2] in b()
[line 1] in a()
[line 7] in script
```

#### 176. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OP_RETURN: {
```

#### 177. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
        Value result = pop();
        vm.frameCount--;
        if (vm.frameCount == 0) {
          pop();
          return INTERPRET_OK;
        }

        vm.stackTop = frame->slots;
        push(result);
        frame = &vm.frames[vm.frameCount - 1];
        break;
```

#### 178. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      }
```

#### 179. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun noReturn() {
  print "Do stuff";
  // No return here.
}

print noReturn(); // ???
```

#### 180. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void emitReturn() {
```

#### 181. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  emitByte(OP_NIL);
```

#### 182. 24 . 5 . 4 Returning from functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  emitByte(OP_RETURN);
}
```

#### 183. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    ifStatement();
```

#### 184. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  } else if (match(TOKEN_RETURN)) {
    returnStatement();
```

#### 185. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  } else if (match(TOKEN_WHILE)) {
```

#### 186. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void returnStatement() {
  if (match(TOKEN_SEMICOLON)) {
    emitReturn();
  } else {
    expression();
    consume(TOKEN_SEMICOLON, "Expect ';' after return value.");
    emitByte(OP_RETURN);
  }
}
```

#### 187. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
return "What?!";
```

#### 188. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void returnStatement() {
```

#### 189. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (current->type == TYPE_SCRIPT) {
    error("Can't return from top-level code.");
  }

```

#### 190. 24 . 6 Return Statements — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  if (match(TOKEN_SEMICOLON)) {
```

#### 191. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
} ObjFunction;
```

#### 192. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


typedef Value (*NativeFn)(int argCount, Value* args);

typedef struct {
  Obj obj;
  NativeFn function;
} ObjNative;
```

#### 193. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


struct ObjString {
```

#### 194. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjFunction* newFunction();
```

#### 195. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjNative* newNative(NativeFn function);
```

#### 196. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjString* takeString(char* chars, int length);
```

#### 197. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
ObjNative* newNative(NativeFn function) {
  ObjNative* native = ALLOCATE_OBJ(ObjNative, OBJ_NATIVE);
  native->function = function;
  return native;
}
```

#### 198. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
typedef enum {
  OBJ_FUNCTION,
```

#### 199. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OBJ_NATIVE,
```

#### 200. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  OBJ_STRING,
} ObjType;
```

#### 201. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    }
```

#### 202. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_NATIVE:
      FREE(ObjNative, object);
      break;
```

#### 203. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_STRING: {
```

#### 204. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      break;
```

#### 205. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_NATIVE:
      printf("<native fn>");
      break;
```

#### 206. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
    case OBJ_STRING:
```

#### 207. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

#### 208. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define IS_NATIVE(value)       isObjType(value, OBJ_NATIVE)
```

#### 209. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

#### 210. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

#### 211. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define AS_NATIVE(value) \
    (((ObjNative*)AS_OBJ(value))->function)
```

#### 212. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
#define AS_STRING(value)       ((ObjString*)AS_OBJ(value))
```

#### 213. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OBJ_FUNCTION: 
        return call(AS_FUNCTION(callee), argCount);
```

#### 214. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      case OBJ_NATIVE: {
        NativeFn native = AS_NATIVE(callee);
        Value result = native(argCount, vm.stackTop - argCount);
        vm.stackTop -= argCount + 1;
        push(result);
        return true;
      }
```

#### 215. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
      default:
```

#### 216. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static void defineNative(const char* name, NativeFn function) {
  push(OBJ_VAL(copyString(name, (int)strlen(name))));
  push(OBJ_VAL(newNative(function)));
  tableSet(&vm.globals, AS_STRING(vm.stack[0]), vm.stack[1]);
  pop();
  pop();
}
```

#### 217. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
static Value clockNative(int argCount, Value* args) {
  return NUMBER_VAL((double)clock() / CLOCKS_PER_SEC);
}
```

#### 218. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
  initTable(&vm.strings);
```

#### 219. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```


  defineNative("clock", clockNative);
```

#### 220. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
}
```

#### 221. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include <string.h>
```

#### 222. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c
#include <time.h>
```

#### 223. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```c


#include "common.h"
```

#### 224. 24 . 7 Native Functions — [source](https://craftinginterpreters.com/calls-and-functions.html)
```
fun fib(n) {
  if (n < 2) return n;
  return fib(n - 2) + fib(n - 1);
}

var start = clock();
print fib(35);
print clock() - start;
```

