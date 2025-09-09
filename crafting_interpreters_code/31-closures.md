# Closures
_From: https://craftinginterpreters.com/closures.html_

#### 1. Closures — [source](https://craftinginterpreters.com/closures.html)
```
var x = "global";
fun outer() {
  var x = "outer";
  fun inner() {
    print x;
  }
  inner();
}
outer();
```

#### 2. Closures — [source](https://craftinginterpreters.com/closures.html)
```
fun makeClosure() {
  var local = "local";
  fun closure() {
    print local;
  }
  return closure;
}

var closure = makeClosure();
closure();
```

#### 3. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
fun makeClosure(value) {
  fun closure() {
    print value;
  }
  return closure;
}

var doughnut = makeClosure("doughnut");
var bagel = makeClosure("bagel");
doughnut();
bagel();
```

#### 4. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
typedef struct {
  Obj obj;
  ObjFunction* function;
} ObjClosure;
```

#### 5. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
} ObjClosure;

```

#### 6. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
ObjClosure* newClosure(ObjFunction* function);
```

#### 7. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
ObjFunction* newFunction();
```

#### 8. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
ObjClosure* newClosure(ObjFunction* function) {
  ObjClosure* closure = ALLOCATE_OBJ(ObjClosure, OBJ_CLOSURE);
  closure->function = function;
  return closure;
}
```

#### 9. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
typedef enum {
```

#### 10. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
  OBJ_CLOSURE,
```

#### 11. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
  OBJ_FUNCTION,
```

#### 12. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
  switch (object->type) {
```

#### 13. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_CLOSURE: {
      FREE(ObjClosure, object);
      break;
    }
```

#### 14. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_FUNCTION: {
```

#### 15. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)

```

#### 16. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
#define IS_CLOSURE(value)      isObjType(value, OBJ_CLOSURE)
```

#### 17. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

#### 18. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)

```

#### 19. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
#define AS_CLOSURE(value)      ((ObjClosure*)AS_OBJ(value))
```

#### 20. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

#### 21. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
  switch (OBJ_TYPE(value)) {
```

#### 22. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_CLOSURE:
      printFunction(AS_CLOSURE(value)->function);
      break;
```

#### 23. 25 . 1 Closure Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_FUNCTION:
```

#### 24. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
  ObjFunction* function = endCompiler();
```

#### 25. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
  emitBytes(OP_CLOSURE, makeConstant(OBJ_VAL(function)));
```

#### 26. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
}
```

#### 27. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
  OP_CALL,
```

#### 28. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
  OP_CLOSURE,
```

#### 29. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
  OP_RETURN,
```

#### 30. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_CALL:
      return byteInstruction("OP_CALL", chunk, offset);
```

#### 31. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_CLOSURE: {
      offset++;
      uint8_t constant = chunk->code[offset++];
      printf("%-16s %4d ", "OP_CLOSURE", constant);
      printValue(chunk->constants.values[constant]);
      printf("\n");
      return offset;
    }
```

#### 32. 25 . 1 . 1 Compiling to closure objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_RETURN:
```

#### 33. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
      }
```

#### 34. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_CLOSURE: {
        ObjFunction* function = AS_FUNCTION(READ_CONSTANT());
        ObjClosure* closure = newClosure(function);
        push(OBJ_VAL(closure));
        break;
      }
```

#### 35. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_RETURN: {
```

#### 36. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    switch (OBJ_TYPE(callee)) {
```

#### 37. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
      case OBJ_CLOSURE:
        return call(AS_CLOSURE(callee), argCount);
```

#### 38. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
      case OBJ_NATIVE: {
```

#### 39. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
static bool call(ObjClosure* closure, int argCount) {
```

#### 40. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  if (argCount != function->arity) {
```

#### 41. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
static bool call(ObjClosure* closure, int argCount) {
```

#### 42. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  if (argCount != closure->function->arity) {
    runtimeError("Expected %d arguments but got %d.",
        closure->function->arity, argCount);
```

#### 43. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    return false;
```

#### 44. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  CallFrame* frame = &vm.frames[vm.frameCount++];
```

#### 45. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  frame->closure = closure;
  frame->ip = closure->function->chunk.code;
```

#### 46. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  frame->slots = vm.stackTop - argCount - 1;
```

#### 47. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
typedef struct {
```

#### 48. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  ObjClosure* closure;
```

#### 49. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  uint8_t* ip;
```

#### 50. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    (uint16_t)((frame->ip[-2] << 8) | frame->ip[-1]))

```

#### 51. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
#define READ_CONSTANT() \
    (frame->closure->function->chunk.constants.values[READ_BYTE()])
```

#### 52. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```


#define READ_STRING() AS_STRING(READ_CONSTANT())
```

#### 53. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    printf("\n");
```

#### 54. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    disassembleInstruction(&frame->closure->function->chunk,
        (int)(frame->ip - frame->closure->function->chunk.code));
```

#### 55. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
#endif
```

#### 56. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    CallFrame* frame = &vm.frames[i];
```

#### 57. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    ObjFunction* function = frame->closure->function;
```

#### 58. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
    size_t instruction = frame->ip - function->chunk.code - 1;
```

#### 59. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  push(OBJ_VAL(function));
```

#### 60. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```
  ObjClosure* closure = newClosure(function);
  pop();
  push(OBJ_VAL(closure));
  call(closure, 0);
```

#### 61. 25 . 1 . 2 Interpreting function declarations — [source](https://craftinginterpreters.com/closures.html)
```


  return run();
```

#### 62. 25 . 2 Upvalues — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = 1;    // (1)
  x = 2;        // (2)
  fun inner() { // (3)
    print x;
  }
  inner();
}
```

#### 63. 25 . 2 Upvalues — [source](https://craftinginterpreters.com/closures.html)
```
{
  var a = 3;
  fun f() {
    print a;
  }
}
```

#### 64. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  if (arg != -1) {
    getOp = OP_GET_LOCAL;
    setOp = OP_SET_LOCAL;
```

#### 65. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  } else if ((arg = resolveUpvalue(current, &name)) != -1) {
    getOp = OP_GET_UPVALUE;
    setOp = OP_SET_UPVALUE;
```

#### 66. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  } else {
```

#### 67. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  OP_SET_GLOBAL,
```

#### 68. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  OP_GET_UPVALUE,
  OP_SET_UPVALUE,
```

#### 69. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  OP_EQUAL,
```

#### 70. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
static int resolveUpvalue(Compiler* compiler, Token* name) {
  if (compiler->enclosing == NULL) return -1;

  int local = resolveLocal(compiler->enclosing, name);
  if (local != -1) {
    return addUpvalue(compiler, (uint8_t)local, true);
  }

  return -1;
}
```

#### 71. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = 1;
  fun inner() {
    print x; // (1)
  }
  inner();
}
```

#### 72. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
static int addUpvalue(Compiler* compiler, uint8_t index,
                      bool isLocal) {
  int upvalueCount = compiler->function->upvalueCount;
  compiler->upvalues[upvalueCount].isLocal = isLocal;
  compiler->upvalues[upvalueCount].index = index;
  return compiler->function->upvalueCount++;
}
```

#### 73. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int upvalueCount = compiler->function->upvalueCount;
```

#### 74. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```


  for (int i = 0; i < upvalueCount; i++) {
    Upvalue* upvalue = &compiler->upvalues[i];
    if (upvalue->index == index && upvalue->isLocal == isLocal) {
      return i;
    }
  }

```

#### 75. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  compiler->upvalues[upvalueCount].isLocal = isLocal;
```

#### 76. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int arity;
```

#### 77. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int upvalueCount;
```

#### 78. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  Chunk chunk;
```

#### 79. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  function->arity = 0;
```

#### 80. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  function->upvalueCount = 0;
```

#### 81. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  function->name = NULL;
```

#### 82. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int localCount;
```

#### 83. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  Upvalue upvalues[UINT8_COUNT];
```

#### 84. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int scopeDepth;
```

#### 85. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    if (upvalue->index == index && upvalue->isLocal == isLocal) {
      return i;
    }
  }

```

#### 86. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  if (upvalueCount == UINT8_COUNT) {
    error("Too many closure variables in function.");
    return 0;
  }

```

#### 87. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  compiler->upvalues[upvalueCount].isLocal = isLocal;
```

#### 88. 25 . 2 . 1 Compiling upvalues — [source](https://craftinginterpreters.com/closures.html)
```
typedef struct {
  uint8_t index;
  bool isLocal;
} Upvalue;
```

#### 89. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = 1;
  fun middle() {
    fun inner() {
      print x;
    }
  }
}
```

#### 90. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = "value";
  fun middle() {
    fun inner() {
      print x;
    }

    print "create inner closure";
    return inner;
  }

  print "return from outer";
  return middle;
}

var mid = outer();
var in = mid();
in();
```

#### 91. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
return from outer
create inner closure
value
```

#### 92. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  if (local != -1) {
    return addUpvalue(compiler, (uint8_t)local, true);
  }

```

#### 93. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int upvalue = resolveUpvalue(compiler->enclosing, name);
  if (upvalue != -1) {
    return addUpvalue(compiler, (uint8_t)upvalue, false);
  }

```

#### 94. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  return -1;
```

#### 95. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  emitBytes(OP_CLOSURE, makeConstant(OBJ_VAL(function)));
```

#### 96. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```


  for (int i = 0; i < function->upvalueCount; i++) {
    emitByte(compiler.upvalues[i].isLocal ? 1 : 0);
    emitByte(compiler.upvalues[i].index);
  }
```

#### 97. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
}
```

#### 98. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
      printf("\n");
```

#### 99. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```


      ObjFunction* function = AS_FUNCTION(
          chunk->constants.values[constant]);
      for (int j = 0; j < function->upvalueCount; j++) {
        int isLocal = chunk->code[offset++];
        int index = chunk->code[offset++];
        printf("%04d      |                     %s %d\n",
               offset - 2, isLocal ? "local" : "upvalue", index);
      }

```

#### 100. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
      return offset;
```

#### 101. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var a = 1;
  var b = 2;
  fun middle() {
    var c = 3;
    var d = 4;
    fun inner() {
      print a + c + b + d;
    }
  }
}
```

#### 102. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
0004    9 OP_CLOSURE          2 <fn inner>
0006      |                     upvalue 0
0008      |                     local 1
0010      |                     upvalue 1
0012      |                     local 2
```

#### 103. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_SET_GLOBAL:
      return constantInstruction("OP_SET_GLOBAL", chunk, offset);
```

#### 104. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_GET_UPVALUE:
      return byteInstruction("OP_GET_UPVALUE", chunk, offset);
    case OP_SET_UPVALUE:
      return byteInstruction("OP_SET_UPVALUE", chunk, offset);
```

#### 105. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_EQUAL:
```

#### 106. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```c
#include "debug.h"
```

#### 107. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```c
#include "object.h"
```

#### 108. 25 . 2 . 2 Flattening upvalues — [source](https://craftinginterpreters.com/closures.html)
```c
#include "value.h"
```

#### 109. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
typedef struct ObjUpvalue {
  Obj obj;
  Value* location;
} ObjUpvalue;
```

#### 110. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = "before";
  fun inner() {
    x = "assigned";
  }
  inner();
  print x;
}
outer();
```

#### 111. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
ObjString* copyString(const char* chars, int length);
```

#### 112. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
ObjUpvalue* newUpvalue(Value* slot);
```

#### 113. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
void printObject(Value value);
```

#### 114. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
ObjUpvalue* newUpvalue(Value* slot) {
  ObjUpvalue* upvalue = ALLOCATE_OBJ(ObjUpvalue, OBJ_UPVALUE);
  upvalue->location = slot;
  return upvalue;
}
```

#### 115. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
  OBJ_STRING,
```

#### 116. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
  OBJ_UPVALUE
```

#### 117. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
} ObjType;
```

#### 118. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
      FREE(ObjString, object);
      break;
    }
```

#### 119. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_UPVALUE:
      FREE(ObjUpvalue, object);
      break;
```

#### 120. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
  }
```

#### 121. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_STRING:
      printf("%s", AS_CSTRING(value));
      break;
```

#### 122. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_UPVALUE:
      printf("upvalue");
      break;
```

#### 123. 25 . 3 Upvalue Objects — [source](https://craftinginterpreters.com/closures.html)
```
  }
```

#### 124. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  ObjFunction* function;
```

#### 125. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue** upvalues;
  int upvalueCount;
```

#### 126. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
} ObjClosure;
```

#### 127. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
ObjClosure* newClosure(ObjFunction* function) {
```

#### 128. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue** upvalues = ALLOCATE(ObjUpvalue*,
                                   function->upvalueCount);
  for (int i = 0; i < function->upvalueCount; i++) {
    upvalues[i] = NULL;
  }

```

#### 129. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  ObjClosure* closure = ALLOCATE_OBJ(ObjClosure, OBJ_CLOSURE);
```

#### 130. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  closure->function = function;
```

#### 131. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  closure->upvalues = upvalues;
  closure->upvalueCount = function->upvalueCount;
```

#### 132. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
  return closure;
```

#### 133. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
    case OBJ_CLOSURE: {
```

#### 134. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      ObjClosure* closure = (ObjClosure*)object;
      FREE_ARRAY(ObjUpvalue*, closure->upvalues,
                 closure->upvalueCount);
```

#### 135. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      FREE(ObjClosure, object);
```

#### 136. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
        push(OBJ_VAL(closure));
```

#### 137. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
        for (int i = 0; i < closure->upvalueCount; i++) {
          uint8_t isLocal = READ_BYTE();
          uint8_t index = READ_BYTE();
          if (isLocal) {
            closure->upvalues[i] =
                captureUpvalue(frame->slots + index);
          } else {
            closure->upvalues[i] = frame->closure->upvalues[index];
          }
        }
```

#### 138. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
        break;
```

#### 139. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
static ObjUpvalue* captureUpvalue(Value* local) {
  ObjUpvalue* createdUpvalue = newUpvalue(local);
  return createdUpvalue;
}
```

#### 140. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      }
```

#### 141. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_GET_UPVALUE: {
        uint8_t slot = READ_BYTE();
        push(*frame->closure->upvalues[slot]->location);
        break;
      }
```

#### 142. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_EQUAL: {
```

#### 143. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      }
```

#### 144. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_SET_UPVALUE: {
        uint8_t slot = READ_BYTE();
        *frame->closure->upvalues[slot]->location = peek(0);
        break;
      }
```

#### 145. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_EQUAL: {
```

#### 146. 25 . 3 . 1 Upvalues in closures — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = "outside";
  fun inner() {
    print x;
  }
  inner();
}
outer();
```

#### 147. 25 . 4 Closed Upvalues — [source](https://craftinginterpreters.com/closures.html)
```
fun outer() {
  var x = "outside";
  fun inner() {
    print x;
  }

  return inner;
}

var closure = outer();
closure();
```

#### 148. 25 . 4 . 1 Values and variables — [source](https://craftinginterpreters.com/closures.html)
```
var globalSet;
var globalGet;

fun main() {
  var a = "initial";

  fun set() { a = "updated"; }
  fun get() { print a; }

  globalSet = set;
  globalGet = get;
}

main();
globalSet();
globalGet();
```

#### 149. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  int depth;
```

#### 150. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  bool isCaptured;
```

#### 151. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
} Local;
```

#### 152. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  local->depth = -1;
```

#### 153. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  local->isCaptured = false;
```

#### 154. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
}
```

#### 155. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  local->depth = 0;
```

#### 156. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  local->isCaptured = false;
```

#### 157. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  local->name.start = "";
```

#### 158. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  if (local != -1) {
```

#### 159. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    compiler->enclosing->locals[local].isCaptured = true;
```

#### 160. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    return addUpvalue(compiler, (uint8_t)local, true);
```

#### 161. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  while (current->localCount > 0 &&
         current->locals[current->localCount - 1].depth >
            current->scopeDepth) {
```

#### 162. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    if (current->locals[current->localCount - 1].isCaptured) {
      emitByte(OP_CLOSE_UPVALUE);
    } else {
      emitByte(OP_POP);
    }
```

#### 163. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    current->localCount--;
  }
```

#### 164. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  OP_CLOSURE,
```

#### 165. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  OP_CLOSE_UPVALUE,
```

#### 166. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  OP_RETURN,
```

#### 167. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    }
```

#### 168. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_CLOSE_UPVALUE:
      return simpleInstruction("OP_CLOSE_UPVALUE", offset);
```

#### 169. 25 . 4 . 2 Closing upvalues — [source](https://craftinginterpreters.com/closures.html)
```
    case OP_RETURN:
```

#### 170. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  Value* location;
```

#### 171. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  struct ObjUpvalue* next;
```

#### 172. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
} ObjUpvalue;
```

#### 173. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  upvalue->location = slot;
```

#### 174. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  upvalue->next = NULL;
```

#### 175. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  return upvalue;
```

#### 176. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  Table strings;
```

#### 177. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue* openUpvalues;
```

#### 178. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  Obj* objects;
```

#### 179. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  vm.frameCount = 0;
```

#### 180. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  vm.openUpvalues = NULL;
```

#### 181. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
}
```

#### 182. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
{
  var a = 1;
  fun f() {
    print a;
  }
  var b = 2;
  fun g() {
    print b;
  }
  var c = 3;
  fun h() {
    print c;
  }
}
```

#### 183. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
static ObjUpvalue* captureUpvalue(Value* local) {
```

#### 184. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue* prevUpvalue = NULL;
  ObjUpvalue* upvalue = vm.openUpvalues;
  while (upvalue != NULL && upvalue->location > local) {
    prevUpvalue = upvalue;
    upvalue = upvalue->next;
  }

  if (upvalue != NULL && upvalue->location == local) {
    return upvalue;
  }

```

#### 185. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue* createdUpvalue = newUpvalue(local);
```

#### 186. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue* createdUpvalue = newUpvalue(local);
```

#### 187. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  createdUpvalue->next = upvalue;

  if (prevUpvalue == NULL) {
    vm.openUpvalues = createdUpvalue;
  } else {
    prevUpvalue->next = createdUpvalue;
  }

```

#### 188. 25 . 4 . 3 Tracking open upvalues — [source](https://craftinginterpreters.com/closures.html)
```
  return createdUpvalue;
```

#### 189. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
      }
```

#### 190. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_CLOSE_UPVALUE:
        closeUpvalues(vm.stackTop - 1);
        pop();
        break;
```

#### 191. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
      case OP_RETURN: {
```

#### 192. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
static void closeUpvalues(Value* last) {
  while (vm.openUpvalues != NULL &&
         vm.openUpvalues->location >= last) {
    ObjUpvalue* upvalue = vm.openUpvalues;
    upvalue->closed = *upvalue->location;
    upvalue->location = &upvalue->closed;
    vm.openUpvalues = upvalue->next;
  }
}
```

#### 193. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
  Value* location;
```

#### 194. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
  Value closed;
```

#### 195. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
  struct ObjUpvalue* next;
```

#### 196. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
  ObjUpvalue* upvalue = ALLOCATE_OBJ(ObjUpvalue, OBJ_UPVALUE);
```

#### 197. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
  upvalue->closed = NIL_VAL;
```

#### 198. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
  upvalue->location = slot;
```

#### 199. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
        Value result = pop();
```

#### 200. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
        closeUpvalues(frame->slots);
```

#### 201. 25 . 4 . 4 Closing upvalues at runtime — [source](https://craftinginterpreters.com/closures.html)
```
        vm.frameCount--;
```

#### 202. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
var globalOne;
var globalTwo;

fun main() {
  {
    var a = "one";
    fun one() {
      print a;
    }
    globalOne = one;
  }

  {
    var a = "two";
    fun two() {
      print a;
    }
    globalTwo = two;
  }
}

main();
globalOne();
globalTwo();
```

#### 203. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
var globalOne;
var globalTwo;

fun main() {
  for (var a = 1; a <= 2; a = a + 1) {
    fun closure() {
      print a;
    }
    if (globalOne == nil) {
      globalOne = closure;
    } else {
      globalTwo = closure;
    }
  }
}

main();
globalOne();
globalTwo();
```

#### 204. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
var closures = [];
for (var i = 1; i <= 2; i++) {
  closures.push(function () { console.log(i); });
}

closures[0]();
closures[1]();
```

#### 205. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
var closures = [];
var i;
for (i = 1; i <= 2; i++) {
  closures.push(function () { console.log(i); });
}

closures[0]();
closures[1]();
```

#### 206. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
var closures = [];
for (let i = 1; i <= 2; i++) {
  closures.push(function () { console.log(i); });
}

closures[0]();
closures[1]();
```

#### 207. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
closures = []
for i in range(1, 3):
  closures.append(lambda: print(i))

closures[0]()
closures[1]()
```

#### 208. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
closures = []
for i in 1..2 do
  closures << lambda { puts i }
end

closures[0].call
closures[1].call
```

#### 209. Design Note: Closing Over the Loop Variable — [source](https://craftinginterpreters.com/closures.html)
```
closures = []
(1..2).each do |i|
  closures << lambda { puts i }
end

closures[0].call
closures[1].call
```

