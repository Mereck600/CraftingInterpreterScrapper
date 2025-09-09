# Classes
_From: https://craftinginterpreters.com/classes.html_

#### 1. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
declaration    â classDecl
               | funDecl
               | varDecl
               | statement ;

classDecl      â "class" IDENTIFIER "{" function* "}" ;
```

#### 2. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
function       â IDENTIFIER "(" parameters? ")" block ;
parameters     â IDENTIFIER ( "," IDENTIFIER )* ;
```

#### 3. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```java
class Breakfast {
  cook() {
    print "Eggs a-fryin'!";
  }

  serve(who) {
    print "Enjoy your breakfast, " + who + ".";
  }
}
```

#### 4. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
      "Block      : List<Stmt> statements",
```

#### 5. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
      "Class      : Token name, List<Stmt.Function> methods",
```

#### 6. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
      "Expression : Expr expression",
```

#### 7. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
    try {
```

#### 8. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
      if (match(CLASS)) return classDeclaration();
```

#### 9. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
      if (match(FUN)) return function("function");
```

#### 10. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
  private Stmt classDeclaration() {
    Token name = consume(IDENTIFIER, "Expect class name.");
    consume(LEFT_BRACE, "Expect '{' before class body.");

    List<Stmt.Function> methods = new ArrayList<>();
    while (!check(RIGHT_BRACE) && !isAtEnd()) {
      methods.add(function("method"));
    }

    consume(RIGHT_BRACE, "Expect '}' after class body.");

    return new Stmt.Class(name, methods);
  }
```

#### 11. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Void visitClassStmt(Stmt.Class stmt) {
    declare(stmt.name);
    define(stmt.name);
    return null;
  }
```

#### 12. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```lox
  @Override
  public Void visitClassStmt(Stmt.Class stmt) {
    environment.define(stmt.name.lexeme, null);
    LoxClass klass = new LoxClass(stmt.name.lexeme);
    environment.assign(stmt.name, klass);
    return null;
  }
```

#### 13. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```java
package com.craftinginterpreters.lox;

import java.util.List;
import java.util.Map;

class LoxClass {
  final String name;

  LoxClass(String name) {
    this.name = name;
  }

  @Override
  public String toString() {
    return name;
  }
}
```

#### 14. 12 . 2 Class Declarations — [source](https://craftinginterpreters.com/classes.html)
```java
class DevonshireCream {
  serveOn() {
    return "Scones";
  }
}

print DevonshireCream; // Prints "DevonshireCream".
```

#### 15. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```java
class Bagel {}
Bagel();
```

#### 16. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```
import java.util.Map;

```

#### 17. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```lox
class LoxClass implements LoxCallable {
```

#### 18. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```
  final String name;
```

#### 19. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Object call(Interpreter interpreter,
                     List<Object> arguments) {
    LoxInstance instance = new LoxInstance(this);
    return instance;
  }

  @Override
  public int arity() {
    return 0;
  }
```

#### 20. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```java
package com.craftinginterpreters.lox;

import java.util.HashMap;
import java.util.Map;

class LoxInstance {
  private LoxClass klass;

  LoxInstance(LoxClass klass) {
    this.klass = klass;
  }

  @Override
  public String toString() {
    return klass.name + " instance";
  }
}
```

#### 21. 12 . 3 Creating Instances — [source](https://craftinginterpreters.com/classes.html)
```java
class Bagel {}
var bagel = Bagel();
print bagel; // Prints "Bagel instance".
```

#### 22. 12 . 4 Properties on Instances — [source](https://craftinginterpreters.com/classes.html)
```
someObject.someProperty
```

#### 23. 12 . 4 Properties on Instances — [source](https://craftinginterpreters.com/classes.html)
```
call           â primary ( "(" arguments? ")" | "." IDENTIFIER )* ;
```

#### 24. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
      "Call     : Expr callee, Token paren, List<Expr> arguments",
```

#### 25. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
      "Get      : Expr object, Token name",
```

#### 26. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
      "Grouping : Expr expression",
```

#### 27. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
    while (true) { 
      if (match(LEFT_PAREN)) {
        expr = finishCall(expr);
```

#### 28. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
      } else if (match(DOT)) {
        Token name = consume(IDENTIFIER,
            "Expect property name after '.'.");
        expr = new Expr.Get(expr, name);
```

#### 29. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
      } else {
        break;
      }
    }
```

#### 30. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Void visitGetExpr(Expr.Get expr) {
    resolve(expr.object);
    return null;
  }
```

#### 31. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Object visitGetExpr(Expr.Get expr) {
    Object object = evaluate(expr.object);
    if (object instanceof LoxInstance) {
      return ((LoxInstance) object).get(expr.name);
    }

    throw new RuntimeError(expr.name,
        "Only instances have properties.");
  }
```

#### 32. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
  private LoxClass klass;
```

#### 33. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
  private final Map<String, Object> fields = new HashMap<>();
```

#### 34. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```


  LoxInstance(LoxClass klass) {
```

#### 35. 12 . 4 . 1 Get expressions — [source](https://craftinginterpreters.com/classes.html)
```
  Object get(Token name) {
    if (fields.containsKey(name.lexeme)) {
      return fields.get(name.lexeme);
    }

    throw new RuntimeError(name, 
        "Undefined property '" + name.lexeme + "'.");
  }
```

#### 36. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
someObject.someProperty = value;
```

#### 37. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
assignment     â ( call "." )? IDENTIFIER "=" assignment
               | logic_or ;
```

#### 38. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
      "Logical  : Expr left, Token operator, Expr right",
```

#### 39. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
      "Set      : Expr object, Token name, Expr value",
```

#### 40. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
      "Unary    : Token operator, Expr right",
```

#### 41. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
        return new Expr.Assign(name, value);
```

#### 42. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
      } else if (expr instanceof Expr.Get) {
        Expr.Get get = (Expr.Get)expr;
        return new Expr.Set(get.object, get.name, value);
```

#### 43. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
      }
```

#### 44. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Void visitSetExpr(Expr.Set expr) {
    resolve(expr.value);
    resolve(expr.object);
    return null;
  }
```

#### 45. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Object visitSetExpr(Expr.Set expr) {
    Object object = evaluate(expr.object);

    if (!(object instanceof LoxInstance)) { 
      throw new RuntimeError(expr.name,
                             "Only instances have fields.");
    }

    Object value = evaluate(expr.value);
    ((LoxInstance)object).set(expr.name, value);
    return value;
  }
```

#### 46. 12 . 4 . 2 Set expressions — [source](https://craftinginterpreters.com/classes.html)
```
  void set(Token name, Object value) {
    fields.put(name.lexeme, value);
  }
```

#### 47. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
var m = object.method;
m(argument);
```

#### 48. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```java
class Box {}

fun notMethod(argument) {
  print "called function with " + argument;
}

var box = Box();
box.function = notMethod;
box.function("argument");
```

#### 49. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
breakfast(omelette.filledWith(cheese), sausage);
```

#### 50. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
var eggs = omelette.filledWith(cheese);
breakfast(eggs, sausage);
```

#### 51. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
fun callback(a, b, c) {
  object.method(a, b, c);
}

takeCallback(callback);
```

#### 52. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
takeCallback(object.method);
```

#### 53. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
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

#### 54. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```java
class Person {
  sayName() {
    print this.name;
  }
}

var jane = Person();
jane.name = "Jane";

var bill = Person();
bill.name = "Bill";

bill.sayName = jane.sayName;
bill.sayName(); // ?
```

#### 55. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    define(stmt.name);
```

#### 56. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```


    for (Stmt.Function method : stmt.methods) {
      FunctionType declaration = FunctionType.METHOD;
      resolveFunction(method, declaration); 
    }

```

#### 57. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    return null;
```

#### 58. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    NONE,
```

#### 59. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    FUNCTION,
```

#### 60. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    METHOD
```

#### 61. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
  }
```

#### 62. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    environment.define(stmt.name.lexeme, null);
```

#### 63. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```


    Map<String, LoxFunction> methods = new HashMap<>();
    for (Stmt.Function method : stmt.methods) {
      LoxFunction function = new LoxFunction(method, environment);
      methods.put(method.name.lexeme, function);
    }

    LoxClass klass = new LoxClass(stmt.name.lexeme, methods);
```

#### 64. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    environment.assign(stmt.name, klass);
```

#### 65. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
  final String name;
```

#### 66. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
  private final Map<String, LoxFunction> methods;

  LoxClass(String name, Map<String, LoxFunction> methods) {
    this.name = name;
    this.methods = methods;
  }
```

#### 67. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```


  @Override
  public String toString() {
```

#### 68. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
  Object get(Token name) {
    if (fields.containsKey(name.lexeme)) {
      return fields.get(name.lexeme);
    }

```

#### 69. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    LoxFunction method = klass.findMethod(name.lexeme);
    if (method != null) return method;

```

#### 70. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
    throw new RuntimeError(name, 
        "Undefined property '" + name.lexeme + "'.");
```

#### 71. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```
  LoxFunction findMethod(String name) {
    if (methods.containsKey(name)) {
      return methods.get(name);
    }

    return null;
  }
```

#### 72. 12 . 5 Methods on Classes — [source](https://craftinginterpreters.com/classes.html)
```java
class Bacon {
  eat() {
    print "Crunch crunch crunch!";
  }
}

Bacon().eat(); // Prints "Crunch crunch crunch!".
```

#### 73. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```java
class Egotist {
  speak() {
    print this;
  }
}

var method = Egotist().speak;
method();
```

#### 74. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```java
class Cake {
  taste() {
    var adjective = "delicious";
    print "The " + this.flavor + " cake is " + adjective + "!";
  }
}

var cake = Cake();
cake.flavor = "German chocolate";
cake.taste(); // Prints "The German chocolate cake is delicious!".
```

#### 75. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```java
class Thing {
  getCallback() {
    fun localFunction() {
      print this;
    }

    return localFunction;
  }
}

var callback = Thing().getCallback();
callback();
```

#### 76. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
      "Set      : Expr object, Token name, Expr value",
```

#### 77. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
      "This     : Token keyword",
```

#### 78. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
      "Unary    : Token operator, Expr right",
```

#### 79. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
      return new Expr.Literal(previous().literal);
    }
```

#### 80. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```


    if (match(THIS)) return new Expr.This(previous());
```

#### 81. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```


    if (match(IDENTIFIER)) {
```

#### 82. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Void visitThisExpr(Expr.This expr) {
    resolveLocal(expr, expr.keyword);
    return null;
  }

```

#### 83. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    define(stmt.name);

```

#### 84. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    beginScope();
    scopes.peek().put("this", true);

```

#### 85. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    for (Stmt.Function method : stmt.methods) {
```

#### 86. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    }

```

#### 87. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    endScope();

```

#### 88. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    return null;
```

#### 89. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    LoxFunction method = klass.findMethod(name.lexeme);
```

#### 90. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
    if (method != null) return method.bind(this);
```

#### 91. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```


    throw new RuntimeError(name, 
        "Undefined property '" + name.lexeme + "'.");
```

#### 92. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
  LoxFunction bind(LoxInstance instance) {
    Environment environment = new Environment(closure);
    environment.define("this", instance);
    return new LoxFunction(declaration, environment);
  }
```

#### 93. 12 . 6 This — [source](https://craftinginterpreters.com/classes.html)
```
  @Override
  public Object visitThisExpr(Expr.This expr) {
    return lookUpVariable(expr.keyword, expr);
  }
```

#### 94. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
print this;
```

#### 95. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
fun notAMethod() {
  print this;
}
```

#### 96. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
  }
```

#### 97. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```


  private enum ClassType {
    NONE,
    CLASS
  }

  private ClassType currentClass = ClassType.NONE;

```

#### 98. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
  void resolve(List<Stmt> statements) {
```

#### 99. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
  public Void visitClassStmt(Stmt.Class stmt) {
```

#### 100. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    ClassType enclosingClass = currentClass;
    currentClass = ClassType.CLASS;

```

#### 101. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    declare(stmt.name);
```

#### 102. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    endScope();

```

#### 103. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    currentClass = enclosingClass;
```

#### 104. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    return null;
```

#### 105. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
  public Void visitThisExpr(Expr.This expr) {
```

#### 106. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    if (currentClass == ClassType.NONE) {
      Lox.error(expr.keyword,
          "Can't use 'this' outside of a class.");
      return null;
    }

```

#### 107. 12 . 6 . 1 Invalid uses of this — [source](https://craftinginterpreters.com/classes.html)
```
    resolveLocal(expr, expr.keyword);
```

#### 108. 12 . 7 Constructors and Initializers — [source](https://craftinginterpreters.com/classes.html)
```
                     List<Object> arguments) {
    LoxInstance instance = new LoxInstance(this);
```

#### 109. 12 . 7 Constructors and Initializers — [source](https://craftinginterpreters.com/classes.html)
```
    LoxFunction initializer = findMethod("init");
    if (initializer != null) {
      initializer.bind(instance).call(interpreter, arguments);
    }

```

#### 110. 12 . 7 Constructors and Initializers — [source](https://craftinginterpreters.com/classes.html)
```
    return instance;
```

#### 111. 12 . 7 Constructors and Initializers — [source](https://craftinginterpreters.com/classes.html)
```
  public int arity() {
```

#### 112. 12 . 7 Constructors and Initializers — [source](https://craftinginterpreters.com/classes.html)
```
    LoxFunction initializer = findMethod("init");
    if (initializer == null) return 0;
    return initializer.arity();
```

#### 113. 12 . 7 Constructors and Initializers — [source](https://craftinginterpreters.com/classes.html)
```
  }
```

#### 114. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```java
class Foo {
  init() {
    print this;
  }
}

var foo = Foo();
print foo.init();
```

#### 115. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
      return returnValue.value;
    }
```

#### 116. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```


    if (isInitializer) return closure.getAt(0, "this");
```

#### 117. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    return null;
```

#### 118. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
  private final Environment closure;

```

#### 119. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
  private final boolean isInitializer;

  LoxFunction(Stmt.Function declaration, Environment closure,
              boolean isInitializer) {
    this.isInitializer = isInitializer;
```

#### 120. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    this.closure = closure;
    this.declaration = declaration;
```

#### 121. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
  public Void visitFunctionStmt(Stmt.Function stmt) {
```

#### 122. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    LoxFunction function = new LoxFunction(stmt, environment,
                                           false);
```

#### 123. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    environment.define(stmt.name.lexeme, function);
```

#### 124. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    for (Stmt.Function method : stmt.methods) {
```

#### 125. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
      LoxFunction function = new LoxFunction(method, environment,
          method.name.lexeme.equals("init"));
```

#### 126. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
      methods.put(method.name.lexeme, function);
```

#### 127. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    environment.define("this", instance);
```

#### 128. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
    return new LoxFunction(declaration, environment,
                           isInitializer);
```

#### 129. 12 . 7 . 1 Invoking init() directly — [source](https://craftinginterpreters.com/classes.html)
```
  }
```

#### 130. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```java
class Foo {
  init() {
    return "something else";
  }
}
```

#### 131. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
    FUNCTION,
```

#### 132. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
    INITIALIZER,
```

#### 133. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
    METHOD
```

#### 134. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      FunctionType declaration = FunctionType.METHOD;
```

#### 135. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      if (method.name.lexeme.equals("init")) {
        declaration = FunctionType.INITIALIZER;
      }

```

#### 136. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      resolveFunction(method, declaration); 
```

#### 137. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
    if (stmt.value != null) {
```

#### 138. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      if (currentFunction == FunctionType.INITIALIZER) {
        Lox.error(stmt.keyword,
            "Can't return a value from an initializer.");
      }

```

#### 139. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      resolve(stmt.value);
```

#### 140. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```java
class Foo {
  init() {
    return;
  }
}
```

#### 141. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
    } catch (Return returnValue) {
```

#### 142. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      if (isInitializer) return closure.getAt(0, "this");

```

#### 143. 12 . 7 . 2 Returning from init() — [source](https://craftinginterpreters.com/classes.html)
```
      return returnValue.value;
```

#### 144. Challenges — [source](https://craftinginterpreters.com/classes.html)
```java
class Math {
  class square(n) {
    return n * n;
  }
}

print Math.square(3); // Prints "9".
```

#### 145. Challenges — [source](https://craftinginterpreters.com/classes.html)
```java
class Circle {
  init(radius) {
    this.radius = radius;
  }

  area {
    return 3.141592653 * this.radius * this.radius;
  }
}

var circle = Circle(4);
print circle.area; // Prints roughly "50.2655".
```

#### 146. Design Note: Prototypes and Power — [source](https://craftinginterpreters.com/classes.html)
```
power = breadth Ã ease Ã· complexity
```

