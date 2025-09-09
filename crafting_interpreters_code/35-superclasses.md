# Superclasses
_From: https://craftinginterpreters.com/superclasses.html_

#### 1. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```java
class Doughnut {
  cook() {
    print "Dunk in the fryer.";
  }
}

class Cruller < Doughnut {
  finish() {
    print "Glaze with icing.";
  }
}
```

#### 2. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```
  currentClass = &classCompiler;

```

#### 3. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```
  if (match(TOKEN_LESS)) {
    consume(TOKEN_IDENTIFIER, "Expect superclass name.");
    variable(false);
    namedVariable(className, false);
    emitByte(OP_INHERIT);
  }

```

#### 4. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```
  namedVariable(className, false);
```

#### 5. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```
class Cruller < Doughnut {
```

#### 6. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```
    variable(false);
```

#### 7. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```


    if (identifiersEqual(&className, &parser.previous)) {
      error("A class can't inherit from itself.");
    }

```

#### 8. 29 . 1 Inheriting Methods — [source](https://craftinginterpreters.com/superclasses.html)
```
    namedVariable(className, false);
```

#### 9. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_CLASS,
```

#### 10. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_INHERIT,
```

#### 11. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_METHOD
```

#### 12. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
      return constantInstruction("OP_CLASS", chunk, offset);
```

#### 13. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
    case OP_INHERIT:
      return simpleInstruction("OP_INHERIT", offset);
```

#### 14. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
    case OP_METHOD:
```

#### 15. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
        break;
```

#### 16. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
      case OP_INHERIT: {
        Value superclass = peek(1);
        ObjClass* subclass = AS_CLASS(peek(0));
        tableAddAll(&AS_CLASS(superclass)->methods,
                    &subclass->methods);
        pop(); // Subclass.
        break;
      }
```

#### 17. 29 . 1 . 1 Executing inheritance — [source](https://craftinginterpreters.com/superclasses.html)
```
      case OP_METHOD:
```

#### 18. 29 . 1 . 2 Invalid superclasses — [source](https://craftinginterpreters.com/superclasses.html)
```
var NotClass = "So not a class";
class OhNo < NotClass {}
```

#### 19. 29 . 1 . 2 Invalid superclasses — [source](https://craftinginterpreters.com/superclasses.html)
```
        Value superclass = peek(1);
```

#### 20. 29 . 1 . 2 Invalid superclasses — [source](https://craftinginterpreters.com/superclasses.html)
```
        if (!IS_CLASS(superclass)) {
          runtimeError("Superclass must be a class.");
          return INTERPRET_RUNTIME_ERROR;
        }

```

#### 21. 29 . 1 . 2 Invalid superclasses — [source](https://craftinginterpreters.com/superclasses.html)
```
        ObjClass* subclass = AS_CLASS(peek(0));
```

#### 22. 29 . 2 Storing Superclasses — [source](https://craftinginterpreters.com/superclasses.html)
```java
class A {
  method() {
    print "A method";
  }
}

class B < A {
  method() {
    print "B method";
  }

  test() {
    super.method();
  }
}

class C < B {}

C().test();
```

#### 23. 29 . 2 Storing Superclasses — [source](https://craftinginterpreters.com/superclasses.html)
```java
class A {
  method() {
    print "A method";
  }
}

var Bs_super = A;
class B < A {
  method() {
    print "B method";
  }

  test() {
    runtimeSuperCall(Bs_super, "method");
  }
}

var Cs_super = B;
class C < B {}

C().test();
```

#### 24. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
    }

```

#### 25. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
    beginScope();
    addLocal(syntheticToken("super"));
    defineVariable(0);

```

#### 26. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
    namedVariable(className, false);
    emitByte(OP_INHERIT);
```

#### 27. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
static Token syntheticToken(const char* text) {
  Token token;
  token.start = text;
  token.length = (int)strlen(text);
  return token;
}
```

#### 28. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
  emitByte(OP_POP);
```

#### 29. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```


  if (classCompiler.hasSuperclass) {
    endScope();
  }
```

#### 30. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```


  currentClass = currentClass->enclosing;
```

#### 31. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
typedef struct ClassCompiler {
  struct ClassCompiler* enclosing;
```

#### 32. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
  bool hasSuperclass;
```

#### 33. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
} ClassCompiler;
```

#### 34. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
  ClassCompiler classCompiler;
```

#### 35. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
  classCompiler.hasSuperclass = false;
```

#### 36. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
  classCompiler.enclosing = currentClass;
```

#### 37. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
    emitByte(OP_INHERIT);
```

#### 38. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
    classCompiler.hasSuperclass = true;
```

#### 39. 29 . 2 . 1 A superclass local variable — [source](https://craftinginterpreters.com/superclasses.html)
```
  }
```

#### 40. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  [TOKEN_RETURN]        = {NULL,     NULL,   PREC_NONE},
```

#### 41. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  [TOKEN_SUPER]         = {super_,   NULL,   PREC_NONE},
```

#### 42. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  [TOKEN_THIS]          = {this_,    NULL,   PREC_NONE},
```

#### 43. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
static void super_(bool canAssign) {
  consume(TOKEN_DOT, "Expect '.' after 'super'.");
  consume(TOKEN_IDENTIFIER, "Expect superclass method name.");
  uint8_t name = identifierConstant(&parser.previous);
}
```

#### 44. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```java
class A {
  method() {
    print "A";
  }
}

class B < A {
  method() {
    var closure = super.method;
    closure(); // Prints "A".
  }
}
```

#### 45. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  uint8_t name = identifierConstant(&parser.previous);
```

#### 46. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```


  namedVariable(syntheticToken("this"), false);
  namedVariable(syntheticToken("super"), false);
  emitBytes(OP_GET_SUPER, name);
```

#### 47. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
}
```

#### 48. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```java
class Doughnut {
  cook() {
    print "Dunk in the fryer.";
    this.finish("sprinkles");
  }

  finish(ingredient) {
    print "Finish with " + ingredient;
  }
}

class Cruller < Doughnut {
  finish(ingredient) {
    // No sprinkles, always icing.
    super.finish("icing");
  }
}
```

#### 49. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
static void super_(bool canAssign) {
```

#### 50. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  if (currentClass == NULL) {
    error("Can't use 'super' outside of a class.");
  } else if (!currentClass->hasSuperclass) {
    error("Can't use 'super' in a class with no superclass.");
  }

```

#### 51. 29 . 3 Super Calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  consume(TOKEN_DOT, "Expect '.' after 'super'.");
```

#### 52. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_SET_PROPERTY,
```

#### 53. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_GET_SUPER,
```

#### 54. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_EQUAL,
```

#### 55. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
      return constantInstruction("OP_SET_PROPERTY", chunk, offset);
```

#### 56. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
    case OP_GET_SUPER:
      return constantInstruction("OP_GET_SUPER", chunk, offset);
```

#### 57. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
    case OP_EQUAL:
```

#### 58. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
      }
```

#### 59. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
      case OP_GET_SUPER: {
        ObjString* name = READ_STRING();
        ObjClass* superclass = AS_CLASS(pop());

        if (!bindMethod(superclass, name)) {
          return INTERPRET_RUNTIME_ERROR;
        }
        break;
      }
```

#### 60. 29 . 3 . 1 Executing super accesses — [source](https://craftinginterpreters.com/superclasses.html)
```
      case OP_EQUAL: {
```

#### 61. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  namedVariable(syntheticToken("this"), false);
```

#### 62. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  if (match(TOKEN_LEFT_PAREN)) {
    uint8_t argCount = argumentList();
    namedVariable(syntheticToken("super"), false);
    emitBytes(OP_SUPER_INVOKE, name);
    emitByte(argCount);
  } else {
    namedVariable(syntheticToken("super"), false);
    emitBytes(OP_GET_SUPER, name);
  }
```

#### 63. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
}
```

#### 64. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_INVOKE,
```

#### 65. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_SUPER_INVOKE,
```

#### 66. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
  OP_CLOSURE,
```

#### 67. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
      return invokeInstruction("OP_INVOKE", chunk, offset);
```

#### 68. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
    case OP_SUPER_INVOKE:
      return invokeInstruction("OP_SUPER_INVOKE", chunk, offset);
```

#### 69. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
    case OP_CLOSURE: {
```

#### 70. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
        break;
      }
```

#### 71. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
      case OP_SUPER_INVOKE: {
        ObjString* method = READ_STRING();
        int argCount = READ_BYTE();
        ObjClass* superclass = AS_CLASS(pop());
        if (!invokeFromClass(superclass, method, argCount)) {
          return INTERPRET_RUNTIME_ERROR;
        }
        frame = &vm.frames[vm.frameCount - 1];
        break;
      }
```

#### 72. 29 . 3 . 2 Faster super calls — [source](https://craftinginterpreters.com/superclasses.html)
```
      case OP_CLOSURE: {
```

#### 73. Challenges — [source](https://craftinginterpreters.com/superclasses.html)
```java
class Doughnut {
  cook() {
    print "Fry until golden brown.";
    inner();
    print "Place in a nice box.";
  }
}

class BostonCream < Doughnut {
  cook() {
    print "Pipe full of custard and coat with chocolate.";
  }
}

BostonCream().cook();
```

#### 74. Challenges — [source](https://craftinginterpreters.com/superclasses.html)
```
Fry until golden brown.
Pipe full of custard and coat with chocolate.
Place in a nice box.
```

