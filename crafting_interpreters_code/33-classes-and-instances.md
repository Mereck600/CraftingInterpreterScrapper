# Classes and Instances
_From: https://craftinginterpreters.com/classes-and-instances.html_

#### 1. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
} ObjClosure;
```

#### 2. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```


typedef struct {
  Obj obj;
  ObjString* name;
} ObjClass;
```

#### 3. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```


ObjClosure* newClosure(ObjFunction* function);
```

#### 4. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
typedef enum {
```

#### 5. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OBJ_CLASS,
```

#### 6. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OBJ_CLOSURE,
```

#### 7. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)

```

#### 8. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define IS_CLASS(value)        isObjType(value, OBJ_CLASS)
```

#### 9. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define IS_CLOSURE(value)      isObjType(value, OBJ_CLOSURE)
```

#### 10. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)

```

#### 11. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define AS_CLASS(value)        ((ObjClass*)AS_OBJ(value))
```

#### 12. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define AS_CLOSURE(value)      ((ObjClosure*)AS_OBJ(value))
```

#### 13. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
} ObjClass;

```

#### 14. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjClass* newClass(ObjString* name);
```

#### 15. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjClosure* newClosure(ObjFunction* function);
```

#### 16. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjClass* newClass(ObjString* name) {
  ObjClass* klass = ALLOCATE_OBJ(ObjClass, OBJ_CLASS);
  klass->name = name; 
  return klass;
}
```

#### 17. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  switch (object->type) {
```

#### 18. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_CLASS: {
      FREE(ObjClass, object);
      break;
    } 
```

#### 19. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_CLOSURE: {
```

#### 20. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  switch (object->type) {
```

#### 21. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_CLASS: {
      ObjClass* klass = (ObjClass*)object;
      markObject((Obj*)klass->name);
      break;
    }
```

#### 22. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_CLOSURE: {
```

#### 23. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  switch (OBJ_TYPE(value)) {
```

#### 24. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_CLASS:
      printf("%s", AS_CLASS(value)->name->chars);
      break;
```

#### 25. 27 . 1 Class Objects — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_CLOSURE:
```

#### 26. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
static void declaration() {
```

#### 27. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  if (match(TOKEN_CLASS)) {
    classDeclaration();
  } else if (match(TOKEN_FUN)) {
```

#### 28. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    funDeclaration();
```

#### 29. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
static void classDeclaration() {
  consume(TOKEN_IDENTIFIER, "Expect class name.");
  uint8_t nameConstant = identifierConstant(&parser.previous);
  declareVariable();

  emitBytes(OP_CLASS, nameConstant);
  defineVariable(nameConstant);

  consume(TOKEN_LEFT_BRACE, "Expect '{' before class body.");
  consume(TOKEN_RIGHT_BRACE, "Expect '}' after class body.");
}
```

#### 30. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
var Pie = class {}
```

#### 31. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OP_RETURN,
```

#### 32. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OP_CLASS,
```

#### 33. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
} OpCode;
```

#### 34. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OP_RETURN:
      return simpleInstruction("OP_RETURN", offset);
```

#### 35. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OP_CLASS:
      return constantInstruction("OP_CLASS", chunk, offset);
```

#### 36. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    default:
```

#### 37. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
        break;
      }
```

#### 38. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_CLASS:
        push(OBJ_VAL(newClass(READ_STRING())));
        break;
```

#### 39. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    }
```

#### 40. 27 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
class Brioche {}
print Brioche;
```

#### 41. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
} ObjClass;
```

#### 42. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```


typedef struct {
  Obj obj;
  ObjClass* klass;
  Table fields; 
} ObjInstance;
```

#### 43. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```


ObjClass* newClass(ObjString* name);
```

#### 44. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```c
#include "chunk.h"
```

#### 45. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```c
#include "table.h"
```

#### 46. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```c
#include "value.h"
```

#### 47. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OBJ_FUNCTION,
```

#### 48. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OBJ_INSTANCE,
```

#### 49. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OBJ_NATIVE,
```

#### 50. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

#### 51. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define IS_INSTANCE(value)     isObjType(value, OBJ_INSTANCE)
```

#### 52. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define IS_NATIVE(value)       isObjType(value, OBJ_NATIVE)
```

#### 53. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

#### 54. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define AS_INSTANCE(value)     ((ObjInstance*)AS_OBJ(value))
```

#### 55. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
#define AS_NATIVE(value) \
```

#### 56. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjFunction* newFunction();
```

#### 57. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjInstance* newInstance(ObjClass* klass);
```

#### 58. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjNative* newNative(NativeFn function);
```

#### 59. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
ObjInstance* newInstance(ObjClass* klass) {
  ObjInstance* instance = ALLOCATE_OBJ(ObjInstance, OBJ_INSTANCE);
  instance->klass = klass;
  initTable(&instance->fields);
  return instance;
}
```

#### 60. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      FREE(ObjFunction, object);
      break;
    }
```

#### 61. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_INSTANCE: {
      ObjInstance* instance = (ObjInstance*)object;
      freeTable(&instance->fields);
      FREE(ObjInstance, object);
      break;
    }
```

#### 62. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_NATIVE:
```

#### 63. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      markArray(&function->chunk.constants);
      break;
    }
```

#### 64. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_INSTANCE: {
      ObjInstance* instance = (ObjInstance*)object;
      markObject((Obj*)instance->klass);
      markTable(&instance->fields);
      break;
    }
```

#### 65. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_UPVALUE:
```

#### 66. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      break;
```

#### 67. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_INSTANCE:
      printf("%s instance",
             AS_INSTANCE(value)->klass->name->chars);
      break;
```

#### 68. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OBJ_NATIVE:
```

#### 69. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    switch (OBJ_TYPE(callee)) {
```

#### 70. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OBJ_CLASS: {
        ObjClass* klass = AS_CLASS(callee);
        vm.stackTop[-argCount - 1] = OBJ_VAL(newInstance(klass));
        return true;
      }
```

#### 71. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OBJ_CLOSURE:
```

#### 72. 27 . 3 Instances of Classes — [source](https://craftinginterpreters.com/classes-and-instances.html)
```java
class Brioche {}
print Brioche();
```

#### 73. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
eclair.filling = "pastry creme";
print eclair.filling;
```

#### 74. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  [TOKEN_COMMA]         = {NULL,     NULL,   PREC_NONE},
```

#### 75. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  [TOKEN_DOT]           = {NULL,     dot,    PREC_CALL},
```

#### 76. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  [TOKEN_MINUS]         = {unary,    binary, PREC_TERM},
```

#### 77. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
static void dot(bool canAssign) {
  consume(TOKEN_IDENTIFIER, "Expect property name after '.'.");
  uint8_t name = identifierConstant(&parser.previous);

  if (canAssign && match(TOKEN_EQUAL)) {
    expression();
    emitBytes(OP_SET_PROPERTY, name);
  } else {
    emitBytes(OP_GET_PROPERTY, name);
  }
}
```

#### 78. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
a + b.c = 3
```

#### 79. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
a + (b.c = 3)
```

#### 80. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OP_SET_UPVALUE,
```

#### 81. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OP_GET_PROPERTY,
  OP_SET_PROPERTY,
```

#### 82. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
  OP_EQUAL,
```

#### 83. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      return byteInstruction("OP_SET_UPVALUE", chunk, offset);
```

#### 84. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OP_GET_PROPERTY:
      return constantInstruction("OP_GET_PROPERTY", chunk, offset);
    case OP_SET_PROPERTY:
      return constantInstruction("OP_SET_PROPERTY", chunk, offset);
```

#### 85. 27 . 4 Get and Set Expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
    case OP_EQUAL:
```

#### 86. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      }
```

#### 87. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_GET_PROPERTY: {
        ObjInstance* instance = AS_INSTANCE(peek(0));
        ObjString* name = READ_STRING();

        Value value;
        if (tableGet(&instance->fields, name, &value)) {
          pop(); // Instance.
          push(value);
          break;
        }
      }
```

#### 88. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_EQUAL: {
```

#### 89. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
          push(value);
          break;
        }
```

#### 90. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```


        runtimeError("Undefined property '%s'.", name->chars);
        return INTERPRET_RUNTIME_ERROR;
```

#### 91. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      }
      case OP_EQUAL: {
```

#### 92. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
var obj = "not an instance";
print obj.field;
```

#### 93. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_GET_PROPERTY: {
```

#### 94. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
        if (!IS_INSTANCE(peek(0))) {
          runtimeError("Only instances have properties.");
          return INTERPRET_RUNTIME_ERROR;
        }

```

#### 95. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
        ObjInstance* instance = AS_INSTANCE(peek(0));
```

#### 96. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
        return INTERPRET_RUNTIME_ERROR;
      }
```

#### 97. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_SET_PROPERTY: {
        ObjInstance* instance = AS_INSTANCE(peek(1));
        tableSet(&instance->fields, READ_STRING(), peek(0));
        Value value = pop();
        pop();
        push(value);
        break;
      }
```

#### 98. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_EQUAL: {
```

#### 99. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```java
class Toast {}
var toast = Toast();
print toast.jam = "grape"; // Prints "grape".
```

#### 100. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
      case OP_SET_PROPERTY: {
```

#### 101. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
        if (!IS_INSTANCE(peek(1))) {
          runtimeError("Only instances have fields.");
          return INTERPRET_RUNTIME_ERROR;
        }

```

#### 102. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```
        ObjInstance* instance = AS_INSTANCE(peek(1));
```

#### 103. 27 . 4 . 1 Interpreting getter and setter expressions — [source](https://craftinginterpreters.com/classes-and-instances.html)
```java
class Pair {}

var pair = Pair();
pair.first = 1;
pair.second = 2;
print pair.first + pair.second; // 3.
```

