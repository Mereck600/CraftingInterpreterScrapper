# Methods and Initializers
_From: https://craftinginterpreters.com/methods-and-initializers.html_

#### 1. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
typedef struct {
  Obj obj;
  ObjString* name;
```

#### 2. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  Table methods;
```

#### 3. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
} ObjClass;
```

#### 4. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  klass->name = name; 
```

#### 5. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  initTable(&klass->methods);
```

#### 6. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  return klass;
```

#### 7. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_CLASS: {
```

#### 8. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      ObjClass* klass = (ObjClass*)object;
      freeTable(&klass->methods);
```

#### 9. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      FREE(ObjClass, object);
```

#### 10. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      markObject((Obj*)klass->name);
```

#### 11. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      markTable(&klass->methods);
```

#### 12. 28 . 1 . 1 Representing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      break;
```

#### 13. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  consume(TOKEN_LEFT_BRACE, "Expect '{' before class body.");
```

#### 14. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  while (!check(TOKEN_RIGHT_BRACE) && !check(TOKEN_EOF)) {
    method();
  }
```

#### 15. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  consume(TOKEN_RIGHT_BRACE, "Expect '}' after class body.");
```

#### 16. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static void method() {
  consume(TOKEN_IDENTIFIER, "Expect method name.");
  uint8_t constant = identifierConstant(&parser.previous);
  emitBytes(OP_METHOD, constant);
}
```

#### 17. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  uint8_t constant = identifierConstant(&parser.previous);
```

#### 18. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


  FunctionType type = TYPE_FUNCTION;
  function(type);
```

#### 19. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  emitBytes(OP_METHOD, constant);
```

#### 20. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  consume(TOKEN_IDENTIFIER, "Expect class name.");
```

#### 21. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  Token className = parser.previous;
```

#### 22. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  uint8_t nameConstant = identifierConstant(&parser.previous);
```

#### 23. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  defineVariable(nameConstant);

```

#### 24. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  namedVariable(className, false);
```

#### 25. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  consume(TOKEN_LEFT_BRACE, "Expect '{' before class body.");
```

#### 26. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  consume(TOKEN_RIGHT_BRACE, "Expect '}' after class body.");
```

#### 27. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  emitByte(OP_POP);
```

#### 28. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
}
```

#### 29. 28 . 1 . 2 Compiling method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
class Brunch {
  bacon() {}
  eggs() {}
}
```

#### 30. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OP_CLASS,
```

#### 31. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OP_METHOD
```

#### 32. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
} OpCode;
```

#### 33. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OP_CLASS:
      return constantInstruction("OP_CLASS", chunk, offset);
```

#### 34. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OP_METHOD:
      return constantInstruction("OP_METHOD", chunk, offset);
```

#### 35. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    default:
```

#### 36. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        break;
```

#### 37. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      case OP_METHOD:
        defineMethod(READ_STRING());
        break;
```

#### 38. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    }
```

#### 39. 28 . 1 . 3 Executing method declarations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static void defineMethod(ObjString* name) {
  Value method = peek(0);
  ObjClass* klass = AS_CLASS(peek(1));
  tableSet(&klass->methods, name, method);
  pop();
}
```

#### 40. 28 . 2 Method References — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
instance.method(argument);
```

#### 41. 28 . 2 Method References — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
var closure = instance.method;
closure(argument);
```

#### 42. 28 . 2 Method References — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class Person {
  sayName() {
    print this.name;
  }
}

var jane = Person();
jane.name = "Jane";

var method = jane.sayName;
method(); // ?
```

#### 43. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
} ObjInstance;

```

#### 44. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
typedef struct {
  Obj obj;
  Value receiver;
  ObjClosure* method;
} ObjBoundMethod;

```

#### 45. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
ObjClass* newClass(ObjString* name);
```

#### 46. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
typedef enum {
```

#### 47. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OBJ_BOUND_METHOD,
```

#### 48. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OBJ_CLASS,
```

#### 49. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)

```

#### 50. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
#define IS_BOUND_METHOD(value) isObjType(value, OBJ_BOUND_METHOD)
```

#### 51. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
#define IS_CLASS(value)        isObjType(value, OBJ_CLASS)
```

#### 52. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)

```

#### 53. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
#define AS_BOUND_METHOD(value) ((ObjBoundMethod*)AS_OBJ(value))
```

#### 54. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
#define AS_CLASS(value)        ((ObjClass*)AS_OBJ(value))
```

#### 55. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
} ObjBoundMethod;

```

#### 56. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
ObjBoundMethod* newBoundMethod(Value receiver,
                               ObjClosure* method);
```

#### 57. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
ObjClass* newClass(ObjString* name);
```

#### 58. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
ObjBoundMethod* newBoundMethod(Value receiver,
                               ObjClosure* method) {
  ObjBoundMethod* bound = ALLOCATE_OBJ(ObjBoundMethod,
                                       OBJ_BOUND_METHOD);
  bound->receiver = receiver;
  bound->method = method;
  return bound;
}
```

#### 59. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  switch (object->type) {
```

#### 60. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_BOUND_METHOD:
      FREE(ObjBoundMethod, object);
      break;
```

#### 61. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_CLASS: {
```

#### 62. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  switch (object->type) {
```

#### 63. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_BOUND_METHOD: {
      ObjBoundMethod* bound = (ObjBoundMethod*)object;
      markValue(bound->receiver);
      markObject((Obj*)bound->method);
      break;
    }
```

#### 64. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_CLASS: {
```

#### 65. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  switch (OBJ_TYPE(value)) {
```

#### 66. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_BOUND_METHOD:
      printFunction(AS_BOUND_METHOD(value)->method->function);
      break;
```

#### 67. 28 . 2 . 1 Bound methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OBJ_CLASS:
```

#### 68. 28 . 2 . 2 Accessing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
          pop(); // Instance.
          push(value);
          break;
        }

```

#### 69. 28 . 2 . 2 Accessing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        if (!bindMethod(instance->klass, name)) {
          return INTERPRET_RUNTIME_ERROR;
        }
        break;
```

#### 70. 28 . 2 . 2 Accessing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      }
```

#### 71. 28 . 2 . 2 Accessing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static bool bindMethod(ObjClass* klass, ObjString* name) {
  Value method;
  if (!tableGet(&klass->methods, name, &method)) {
    runtimeError("Undefined property '%s'.", name->chars);
    return false;
  }

  ObjBoundMethod* bound = newBoundMethod(peek(0),
                                         AS_CLOSURE(method));
  pop();
  push(OBJ_VAL(bound));
  return true;
}
```

#### 72. 28 . 2 . 2 Accessing methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class Brunch {
  eggs() {}
}

var brunch = Brunch();
var eggs = brunch.eggs;
```

#### 73. 28 . 2 . 3 Calling methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    switch (OBJ_TYPE(callee)) {
```

#### 74. 28 . 2 . 3 Calling methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      case OBJ_BOUND_METHOD: {
        ObjBoundMethod* bound = AS_BOUND_METHOD(callee);
        return call(bound->method, argCount);
      }
```

#### 75. 28 . 2 . 3 Calling methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      case OBJ_CLASS: {
```

#### 76. 28 . 2 . 3 Calling methods — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class Scone {
  topping(first, second) {
    print "scone with " + first + " and " + second;
  }
}

var scone = Scone();
scone.topping("berries", "cream");
```

#### 77. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  [TOKEN_SUPER]         = {NULL,     NULL,   PREC_NONE},
```

#### 78. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  [TOKEN_THIS]          = {this_,    NULL,   PREC_NONE},
```

#### 79. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  [TOKEN_TRUE]          = {literal,  NULL,   PREC_NONE},
```

#### 80. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static void this_(bool canAssign) {
  variable(false);
} 
```

#### 81. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  local->isCaptured = false;
```

#### 82. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  if (type != TYPE_FUNCTION) {
    local->name.start = "this";
    local->name.length = 4;
  } else {
    local->name.start = "";
    local->name.length = 0;
  }
```

#### 83. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
}
```

#### 84. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class Nested {
  method() {
    fun function() {
      print this;
    }

    function();
  }
}

Nested().method();
```

#### 85. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  TYPE_FUNCTION,
```

#### 86. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  TYPE_METHOD,
```

#### 87. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  TYPE_SCRIPT
```

#### 88. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  uint8_t constant = identifierConstant(&parser.previous);

```

#### 89. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  FunctionType type = TYPE_METHOD;
```

#### 90. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  function(type);
```

#### 91. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      case OBJ_BOUND_METHOD: {
        ObjBoundMethod* bound = AS_BOUND_METHOD(callee);
```

#### 92. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        vm.stackTop[-argCount - 1] = bound->receiver;
```

#### 93. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        return call(bound->method, argCount);
      }
```

#### 94. 28 . 3 This — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
scone.topping("berries", "cream");
```

#### 95. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
print this; // At top level.

fun notMethod() {
  print this; // In a function.
}
```

#### 96. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
Compiler* current = NULL;
```

#### 97. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
ClassCompiler* currentClass = NULL;
```

#### 98. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


static Chunk* currentChunk() {
```

#### 99. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
} Compiler;
```

#### 100. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


typedef struct ClassCompiler {
  struct ClassCompiler* enclosing;
} ClassCompiler;
```

#### 101. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


Parser parser;
```

#### 102. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  defineVariable(nameConstant);

```

#### 103. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  ClassCompiler classCompiler;
  classCompiler.enclosing = currentClass;
  currentClass = &classCompiler;

```

#### 104. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  namedVariable(className, false);
```

#### 105. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  emitByte(OP_POP);
```

#### 106. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


  currentClass = currentClass->enclosing;
```

#### 107. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
}
```

#### 108. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static void this_(bool canAssign) {
```

#### 109. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  if (currentClass == NULL) {
    error("Can't use 'this' outside of a class.");
    return;
  }

```

#### 110. 28 . 3 . 1 Misusing this — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  variable(false);
```

#### 111. 28 . 4 Instance Initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
fun create(klass) {
  var obj = newInstance(klass);
  obj.init();
  return obj;
}
```

#### 112. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        vm.stackTop[-argCount - 1] = OBJ_VAL(newInstance(klass));
```

#### 113. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        Value initializer;
        if (tableGet(&klass->methods, vm.initString,
                     &initializer)) {
          return call(AS_CLOSURE(initializer), argCount);
        }
```

#### 114. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        return true;
```

#### 115. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class Brunch {
  init(food, drink) {}
}

Brunch("eggs", "coffee");
```

#### 116. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
          return call(AS_CLOSURE(initializer), argCount);
```

#### 117. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        } else if (argCount != 0) {
          runtimeError("Expected 0 arguments but got %d.",
                       argCount);
          return false;
```

#### 118. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
        }
```

#### 119. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  Table strings;
```

#### 120. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  ObjString* initString;
```

#### 121. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  ObjUpvalue* openUpvalues;
```

#### 122. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  initTable(&vm.strings);
```

#### 123. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


  vm.initString = copyString("init", 4);
```

#### 124. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


  defineNative("clock", clockNative);
```

#### 125. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  markCompilerRoots();
```

#### 126. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  markObject((Obj*)vm.initString);
```

#### 127. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
}
```

#### 128. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  initTable(&vm.strings);

```

#### 129. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  vm.initString = NULL;
```

#### 130. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  vm.initString = copyString("init", 4);

```

#### 131. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  freeTable(&vm.strings);
```

#### 132. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  vm.initString = NULL;
```

#### 133. 28 . 4 . 1 Invoking initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  freeObjects();
```

#### 134. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  FunctionType type = TYPE_METHOD;
```

#### 135. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  if (parser.previous.length == 4 &&
      memcmp(parser.previous.start, "init", 4) == 0) {
    type = TYPE_INITIALIZER;
  }

```

#### 136. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  function(type);
```

#### 137. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  TYPE_FUNCTION,
```

#### 138. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  TYPE_INITIALIZER,
```

#### 139. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  TYPE_METHOD,
```

#### 140. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static void emitReturn() {
```

#### 141. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  if (current->type == TYPE_INITIALIZER) {
    emitBytes(OP_GET_LOCAL, 0);
  } else {
    emitByte(OP_NIL);
  }

```

#### 142. 28 . 4 . 2 Initializer return values — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  emitByte(OP_RETURN);
```

#### 143. 28 . 4 . 3 Incorrect returns in initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  if (match(TOKEN_SEMICOLON)) {
    emitReturn();
  } else {
```

#### 144. 28 . 4 . 3 Incorrect returns in initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    if (current->type == TYPE_INITIALIZER) {
      error("Can't return a value from an initializer.");
    }

```

#### 145. 28 . 4 . 3 Incorrect returns in initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    expression();
```

#### 146. 28 . 4 . 3 Incorrect returns in initializers — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class CoffeeMaker {
  init(coffee) {
    this.coffee = coffee;
  }

  brew() {
    print "Enjoy your cup of " + this.coffee;

    // No reusing the grounds!
    this.coffee = nil;
  }
}

var maker = CoffeeMaker("coffee and chicory");
maker.brew();
```

#### 147. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  if (canAssign && match(TOKEN_EQUAL)) {
    expression();
    emitBytes(OP_SET_PROPERTY, name);
```

#### 148. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  } else if (match(TOKEN_LEFT_PAREN)) {
    uint8_t argCount = argumentList();
    emitBytes(OP_INVOKE, name);
    emitByte(argCount);
```

#### 149. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  } else {
```

#### 150. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OP_CALL,
```

#### 151. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OP_INVOKE,
```

#### 152. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  OP_CLOSURE,
```

#### 153. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OP_CALL:
      return byteInstruction("OP_CALL", chunk, offset);
```

#### 154. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OP_INVOKE:
      return invokeInstruction("OP_INVOKE", chunk, offset);
```

#### 155. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
    case OP_CLOSURE: {
```

#### 156. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static int invokeInstruction(const char* name, Chunk* chunk,
                                int offset) {
  uint8_t constant = chunk->code[offset + 1];
  uint8_t argCount = chunk->code[offset + 2];
  printf("%-16s (%d args) %4d '", name, argCount, constant);
  printValue(chunk->constants.values[constant]);
  printf("'\n");
  return offset + 3;
}
```

#### 157. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      }
```

#### 158. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      case OP_INVOKE: {
        ObjString* method = READ_STRING();
        int argCount = READ_BYTE();
        if (!invoke(method, argCount)) {
          return INTERPRET_RUNTIME_ERROR;
        }
        frame = &vm.frames[vm.frameCount - 1];
        break;
      }
```

#### 159. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
      case OP_CLOSURE: {
```

#### 160. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static bool invoke(ObjString* name, int argCount) {
  Value receiver = peek(argCount);
  ObjInstance* instance = AS_INSTANCE(receiver);
  return invokeFromClass(instance->klass, name, argCount);
}
```

#### 161. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  Value receiver = peek(argCount);
```

#### 162. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


  if (!IS_INSTANCE(receiver)) {
    runtimeError("Only instances have methods.");
    return false;
  }

```

#### 163. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  ObjInstance* instance = AS_INSTANCE(receiver);
```

#### 164. 28 . 5 Optimized Invocations — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
static bool invokeFromClass(ObjClass* klass, ObjString* name,
                            int argCount) {
  Value method;
  if (!tableGet(&klass->methods, name, &method)) {
    runtimeError("Undefined property '%s'.", name->chars);
    return false;
  }
  return call(AS_CLOSURE(method), argCount);
}
```

#### 165. 28 . 5 . 1 Invoking fields — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```java
class Oops {
  init() {
    fun f() {
      print "not a method";
    }

    this.field = f;
  }
}

var oops = Oops();
oops.field();
```

#### 166. 28 . 5 . 1 Invoking fields — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  ObjInstance* instance = AS_INSTANCE(receiver);
```

#### 167. 28 . 5 . 1 Invoking fields — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```


  Value value;
  if (tableGet(&instance->fields, name, &value)) {
    vm.stackTop[-argCount - 1] = value;
    return callValue(value, argCount);
  }

```

#### 168. 28 . 5 . 1 Invoking fields — [source](https://craftinginterpreters.com/methods-and-initializers.html)
```
  return invokeFromClass(instance->klass, name, argCount);
```

