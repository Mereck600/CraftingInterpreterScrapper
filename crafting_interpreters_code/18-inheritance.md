# Inheritance
_From: https://craftinginterpreters.com/inheritance.html_

#### 1. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
class Doughnut {
  // General doughnut stuff...
}

class BostonCream < Doughnut {
  // Boston Cream-specific stuff...
}
```

#### 2. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
classDecl      â "class" IDENTIFIER ( "<" IDENTIFIER )?
                 "{" function* "}" ;
```

#### 3. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
      "Block      : List<Stmt> statements",
```

#### 4. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
      "Class      : Token name, Expr.Variable superclass," +
                  " List<Stmt.Function> methods",
```

#### 5. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
      "Expression : Expr expression",
```

#### 6. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    Token name = consume(IDENTIFIER, "Expect class name.");
```

#### 7. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```


    Expr.Variable superclass = null;
    if (match(LESS)) {
      consume(IDENTIFIER, "Expect superclass name.");
      superclass = new Expr.Variable(previous());
    }

```

#### 8. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    consume(LEFT_BRACE, "Expect '{' before class body.");
```

#### 9. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    consume(RIGHT_BRACE, "Expect '}' after class body.");

```

#### 10. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    return new Stmt.Class(name, superclass, methods);
```

#### 11. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
  }
```

#### 12. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    define(stmt.name);
```

#### 13. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (stmt.superclass != null) {
      resolve(stmt.superclass);
    }
```

#### 14. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```


    beginScope();
```

#### 15. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
class Oops < Oops {}
```

#### 16. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    define(stmt.name);

```

#### 17. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    if (stmt.superclass != null &&
        stmt.name.lexeme.equals(stmt.superclass.name.lexeme)) {
      Lox.error(stmt.superclass.name,
          "A class can't inherit from itself.");
    }

```

#### 18. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    if (stmt.superclass != null) {
```

#### 19. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
  public Void visitClassStmt(Stmt.Class stmt) {
```

#### 20. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    Object superclass = null;
    if (stmt.superclass != null) {
      superclass = evaluate(stmt.superclass);
      if (!(superclass instanceof LoxClass)) {
        throw new RuntimeError(stmt.superclass.name,
            "Superclass must be a class.");
      }
    }

```

#### 21. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    environment.define(stmt.name.lexeme, null);
```

#### 22. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
var NotAClass = "I am totally not a class";

class Subclass < NotAClass {} // ?!
```

#### 23. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
      methods.put(method.name.lexeme, function);
    }

```

#### 24. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    LoxClass klass = new LoxClass(stmt.name.lexeme,
        (LoxClass)superclass, methods);

```

#### 25. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    environment.assign(stmt.name, klass);
```

#### 26. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
  LoxClass(String name, LoxClass superclass,
           Map<String, LoxFunction> methods) {
    this.superclass = superclass;
```

#### 27. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
    this.name = name;
```

#### 28. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
  final String name;
```

#### 29. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
  final LoxClass superclass;
```

#### 30. 13 . 1 Superclasses and Subclasses — [source](https://craftinginterpreters.com/inheritance.html)
```
  private final Map<String, LoxFunction> methods;
```

#### 31. 13 . 2 Inheriting Methods — [source](https://craftinginterpreters.com/inheritance.html)
```
      return methods.get(name);
    }

```

#### 32. 13 . 2 Inheriting Methods — [source](https://craftinginterpreters.com/inheritance.html)
```
    if (superclass != null) {
      return superclass.findMethod(name);
    }

```

#### 33. 13 . 2 Inheriting Methods — [source](https://craftinginterpreters.com/inheritance.html)
```
    return null;
```

#### 34. 13 . 2 Inheriting Methods — [source](https://craftinginterpreters.com/inheritance.html)
```java
class Doughnut {
  cook() {
    print "Fry until golden brown.";
  }
}

class BostonCream < Doughnut {}

BostonCream().cook();
```

#### 35. 13 . 3 Calling Superclass Methods — [source](https://craftinginterpreters.com/inheritance.html)
```java
class Doughnut {
  cook() {
    print "Fry until golden brown.";
  }
}

class BostonCream < Doughnut {
  cook() {
    super.cook();
    print "Pipe full of custard and coat with chocolate.";
  }
}

BostonCream().cook();
```

#### 36. 13 . 3 Calling Superclass Methods — [source](https://craftinginterpreters.com/inheritance.html)
```
Fry until golden brown.
Pipe full of custard and coat with chocolate.
```

#### 37. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
print super; // Syntax error.
```

#### 38. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
primary        â "true" | "false" | "nil" | "this"
               | NUMBER | STRING | IDENTIFIER | "(" expression ")"
               | "super" "." IDENTIFIER ;
```

#### 39. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
var method = super.cook;
method();
```

#### 40. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
      "Set      : Expr object, Token name, Expr value",
```

#### 41. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
      "Super    : Token keyword, Token method",
```

#### 42. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
      "This     : Token keyword",
```

#### 43. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```
      return new Expr.Literal(previous().literal);
    }
```

#### 44. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (match(SUPER)) {
      Token keyword = previous();
      consume(DOT, "Expect '.' after 'super'.");
      Token method = consume(IDENTIFIER,
          "Expect superclass method name.");
      return new Expr.Super(keyword, method);
    }
```

#### 45. 13 . 3 . 1 Syntax — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (match(THIS)) return new Expr.This(previous());
```

#### 46. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
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

#### 47. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
      resolve(stmt.superclass);
    }
```

#### 48. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (stmt.superclass != null) {
      beginScope();
      scopes.peek().put("super", true);
    }
```

#### 49. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    beginScope();
```

#### 50. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    endScope();

```

#### 51. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    if (stmt.superclass != null) endScope();

```

#### 52. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    currentClass = enclosingClass;
```

#### 53. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
  @Override
  public Void visitSuperExpr(Expr.Super expr) {
    resolveLocal(expr, expr.keyword);
    return null;
  }
```

#### 54. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
        throw new RuntimeError(stmt.superclass.name,
            "Superclass must be a class.");
      }
    }

    environment.define(stmt.name.lexeme, null);
```

#### 55. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (stmt.superclass != null) {
      environment = new Environment(environment);
      environment.define("super", superclass);
    }
```

#### 56. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    Map<String, LoxFunction> methods = new HashMap<>();
```

#### 57. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    LoxClass klass = new LoxClass(stmt.name.lexeme,
        (LoxClass)superclass, methods);
```

#### 58. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (superclass != null) {
      environment = environment.enclosing;
    }
```

#### 59. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    environment.assign(stmt.name, klass);
```

#### 60. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
  @Override
  public Object visitSuperExpr(Expr.Super expr) {
    int distance = locals.get(expr);
    LoxClass superclass = (LoxClass)environment.getAt(
        distance, "super");
  }
```

#### 61. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    LoxClass superclass = (LoxClass)environment.getAt(
        distance, "super");
```

#### 62. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    LoxInstance object = (LoxInstance)environment.getAt(
        distance - 1, "this");
```

#### 63. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
  }
```

#### 64. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    LoxInstance object = (LoxInstance)environment.getAt(
        distance - 1, "this");
```

#### 65. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    LoxFunction method = superclass.findMethod(expr.method.lexeme);
    return method.bind(object);
```

#### 66. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
  }
```

#### 67. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    LoxFunction method = superclass.findMethod(expr.method.lexeme);
```

#### 68. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```


    if (method == null) {
      throw new RuntimeError(expr.method,
          "Undefined property '" + expr.method.lexeme + "'.");
    }

```

#### 69. 13 . 3 . 2 Semantics — [source](https://craftinginterpreters.com/inheritance.html)
```
    return method.bind(object);
  }
```

#### 70. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```java
class Eclair {
  cook() {
    super.cook();
    print "Pipe full of crÃ¨me pÃ¢tissiÃ¨re.";
  }
}
```

#### 71. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
super.notEvenInAClass();
```

#### 72. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
    NONE,
```

#### 73. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
    CLASS,
```

#### 74. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
    SUBCLASS
```

#### 75. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
  }
```

#### 76. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
    if (stmt.superclass != null) {
```

#### 77. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
      currentClass = ClassType.SUBCLASS;
```

#### 78. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
      resolve(stmt.superclass);
```

#### 79. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
  public Void visitSuperExpr(Expr.Super expr) {
```

#### 80. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
    if (currentClass == ClassType.NONE) {
      Lox.error(expr.keyword,
          "Can't use 'super' outside of a class.");
    } else if (currentClass != ClassType.SUBCLASS) {
      Lox.error(expr.keyword,
          "Can't use 'super' in a class with no superclass.");
    }

```

#### 81. 13 . 3 . 3 Invalid uses of super — [source](https://craftinginterpreters.com/inheritance.html)
```
    resolveLocal(expr, expr.keyword);
```

#### 82. Challenges — [source](https://craftinginterpreters.com/inheritance.html)
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

#### 83. Challenges — [source](https://craftinginterpreters.com/inheritance.html)
```
Fry until golden brown.
Pipe full of custard and coat with chocolate.
Place in a nice box.
```

