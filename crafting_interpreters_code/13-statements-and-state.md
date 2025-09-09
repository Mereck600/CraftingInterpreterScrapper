# Statements and State
_From: https://craftinginterpreters.com/statements-and-state.html_

#### 1. 8 . 1 Statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
program        â statement* EOF ;

statement      â exprStmt
               | printStmt ;

exprStmt       â expression ";" ;
printStmt      â "print" expression ";" ;
```

#### 2. 8 . 1 . 1 Statement syntax trees — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Unary    : Token operator, Expr right"
    ));
```

#### 3. 8 . 1 . 1 Statement syntax trees — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    defineAst(outputDir, "Stmt", Arrays.asList(
      "Expression : Expr expression",
      "Print      : Expr expression"
    ));
```

#### 4. 8 . 1 . 1 Statement syntax trees — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  }
```

#### 5. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  List<Stmt> parse() {
    List<Stmt> statements = new ArrayList<>();
    while (!isAtEnd()) {
      statements.add(statement());
    }

    return statements; 
  }
```

#### 6. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
package com.craftinginterpreters.lox;

```

#### 7. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
import java.util.ArrayList;
```

#### 8. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
import java.util.List;
```

#### 9. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Stmt statement() {
    if (match(PRINT)) return printStatement();

    return expressionStatement();
  }
```

#### 10. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Stmt printStatement() {
    Expr value = expression();
    consume(SEMICOLON, "Expect ';' after value.");
    return new Stmt.Print(value);
  }
```

#### 11. 8 . 1 . 2 Parsing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Stmt expressionStatement() {
    Expr expr = expression();
    consume(SEMICOLON, "Expect ';' after expression.");
    return new Stmt.Expression(expr);
  }
```

#### 12. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
class Interpreter implements Expr.Visitor<Object>,
                             Stmt.Visitor<Void> {
```

#### 13. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void interpret(Expr expression) { 
```

#### 14. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  @Override
  public Void visitExpressionStmt(Stmt.Expression stmt) {
    evaluate(stmt.expression);
    return null;
  }
```

#### 15. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  @Override
  public Void visitPrintStmt(Stmt.Print stmt) {
    Object value = evaluate(stmt.expression);
    System.out.println(stringify(value));
    return null;
  }
```

#### 16. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void interpret(List<Stmt> statements) {
    try {
      for (Stmt statement : statements) {
        execute(statement);
      }
    } catch (RuntimeError error) {
      Lox.runtimeError(error);
    }
  }
```

#### 17. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private void execute(Stmt stmt) {
    stmt.accept(this);
  }
```

#### 18. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
package com.craftinginterpreters.lox;
```

#### 19. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```


import java.util.List;
```

#### 20. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```


class Interpreter implements Expr.Visitor<Object>,
```

#### 21. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    Parser parser = new Parser(tokens);
```

#### 22. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    List<Stmt> statements = parser.parse();
```

#### 23. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    // Stop if there was a syntax error.
```

#### 24. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    if (hadError) return;

```

#### 25. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    interpreter.interpret(statements);
```

#### 26. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  }
```

#### 27. 8 . 1 . 3 Executing statements — [source](https://craftinginterpreters.com/statements-and-state.html)
```
print "one";
print true;
print 2 + 1;
```

#### 28. 8 . 2 Global Variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var beverage = "espresso";
```

#### 29. 8 . 2 Global Variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
print beverage; // "espresso".
```

#### 30. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
if (monday) print "Ugh, already?";
```

#### 31. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
if (monday) var beverage = "espresso";
```

#### 32. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
program        â declaration* EOF ;

declaration    â varDecl
               | statement ;

statement      â exprStmt
               | printStmt ;
```

#### 33. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
varDecl        â "var" IDENTIFIER ( "=" expression )? ";" ;
```

#### 34. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
primary        â "true" | "false" | "nil"
               | NUMBER | STRING
               | "(" expression ")"
               | IDENTIFIER ;
```

#### 35. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Expression : Expr expression",
```

#### 36. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Print      : Expr expression",
```

#### 37. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Var        : Token name, Expr initializer"
```

#### 38. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    ));
```

#### 39. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Literal  : Object value",
```

#### 40. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Unary    : Token operator, Expr right",
```

#### 41. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Variable : Token name"
```

#### 42. 8 . 2 . 1 Variable syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    ));
```

#### 43. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  List<Stmt> parse() {
    List<Stmt> statements = new ArrayList<>();
    while (!isAtEnd()) {
```

#### 44. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      statements.add(declaration());
```

#### 45. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    }

    return statements; 
  }
```

#### 46. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Stmt declaration() {
    try {
      if (match(VAR)) return varDeclaration();

      return statement();
    } catch (ParseError error) {
      synchronize();
      return null;
    }
  }
```

#### 47. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Stmt varDeclaration() {
    Token name = consume(IDENTIFIER, "Expect variable name.");

    Expr initializer = null;
    if (match(EQUAL)) {
      initializer = expression();
    }

    consume(SEMICOLON, "Expect ';' after variable declaration.");
    return new Stmt.Var(name, initializer);
  }
```

#### 48. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      return new Expr.Literal(previous().literal);
    }
```

#### 49. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    if (match(IDENTIFIER)) {
      return new Expr.Variable(previous());
    }
```

#### 50. 8 . 2 . 2 Parsing variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    if (match(LEFT_PAREN)) {
```

#### 51. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```java
package com.craftinginterpreters.lox;

import java.util.HashMap;
import java.util.Map;

class Environment {
  private final Map<String, Object> values = new HashMap<>();
}
```

#### 52. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void define(String name, Object value) {
    values.put(name, value);
  }
```

#### 53. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a = "before";
print a; // "before".
var a = "after";
print a; // "after".
```

#### 54. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```java
class Environment {
  private final Map<String, Object> values = new HashMap<>();
```

#### 55. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```


  Object get(Token name) {
    if (values.containsKey(name.lexeme)) {
      return values.get(name.lexeme);
    }

    throw new RuntimeError(name,
        "Undefined variable '" + name.lexeme + "'.");
  }

```

#### 56. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void define(String name, Object value) {
```

#### 57. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```
fun isOdd(n) {
  if (n == 0) return false;
  return isEven(n - 1);
}

fun isEven(n) {
  if (n == 0) return true;
  return isOdd(n - 1);
}
```

#### 58. 8 . 3 Environments — [source](https://craftinginterpreters.com/statements-and-state.html)
```
print a;
var a = "too late!";
```

#### 59. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
class Interpreter implements Expr.Visitor<Object>,
                             Stmt.Visitor<Void> {
```

#### 60. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Environment environment = new Environment();

```

#### 61. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void interpret(List<Stmt> statements) {
```

#### 62. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  @Override
  public Void visitVarStmt(Stmt.Var stmt) {
    Object value = null;
    if (stmt.initializer != null) {
      value = evaluate(stmt.initializer);
    }

    environment.define(stmt.name.lexeme, value);
    return null;
  }
```

#### 63. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a;
print a; // "nil".
```

#### 64. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  @Override
  public Object visitVariableExpr(Expr.Variable expr) {
    return environment.get(expr.name);
  }
```

#### 65. 8 . 3 . 1 Interpreting global variables — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a = 1;
var b = 2;
print a + b;
```

#### 66. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
expression     â assignment ;
assignment     â IDENTIFIER "=" assignment
               | equality ;
```

#### 67. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
instance.field = "value";
```

#### 68. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    defineAst(outputDir, "Expr", Arrays.asList(
```

#### 69. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Assign   : Token name, Expr value",
```

#### 70. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Binary   : Expr left, Token operator, Expr right",
```

#### 71. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Expr expression() {
```

#### 72. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    return assignment();
```

#### 73. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  }
```

#### 74. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a = "before";
a = "value";
```

#### 75. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
makeList().head.next = node;
```

#### 76. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private Expr assignment() {
    Expr expr = equality();

    if (match(EQUAL)) {
      Token equals = previous();
      Expr value = assignment();

      if (expr instanceof Expr.Variable) {
        Token name = ((Expr.Variable)expr).name;
        return new Expr.Assign(name, value);
      }

      error(equals, "Invalid assignment target."); 
    }

    return expr;
  }
```

#### 77. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
newPoint(x + 2, 0).y = 3;
```

#### 78. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
newPoint(x + 2, 0).y;
```

#### 79. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
a + b = c;
```

#### 80. 8 . 4 . 1 Assignment syntax — [source](https://craftinginterpreters.com/statements-and-state.html)
```
a = 3;   // OK.
(a) = 3; // Error.
```

#### 81. 8 . 4 . 2 Assignment semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  @Override
  public Object visitAssignExpr(Expr.Assign expr) {
    Object value = evaluate(expr.value);
    environment.assign(expr.name, value);
    return value;
  }
```

#### 82. 8 . 4 . 2 Assignment semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void assign(Token name, Object value) {
    if (values.containsKey(name.lexeme)) {
      values.put(name.lexeme, value);
      return;
    }

    throw new RuntimeError(name,
        "Undefined variable '" + name.lexeme + "'.");
  }
```

#### 83. 8 . 4 . 2 Assignment semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a = 1;
print a = 2; // "2".
```

#### 84. 8 . 5 Scope — [source](https://craftinginterpreters.com/statements-and-state.html)
```
{
  var a = "first";
  print a; // "first".
}

{
  var a = "second";
  print a; // "second".
}
```

#### 85. 8 . 5 Scope — [source](https://craftinginterpreters.com/statements-and-state.html)
```java
class Saxophone {
  play() {
    print "Careless Whisper";
  }
}

class GolfClub {
  play() {
    print "Fore!";
  }
}

fun playIt(thing) {
  thing.play();
}
```

#### 86. 8 . 5 Scope — [source](https://craftinginterpreters.com/statements-and-state.html)
```
{
  var a = "in block";
}
print a; // Error! No more "a".
```

#### 87. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
// How loud?
var volume = 11;

// Silence.
volume = 0;

// Calculate size of 3x4x5 cuboid.
{
  var volume = 3 * 4 * 5;
  print volume;
}
```

#### 88. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var global = "outside";
{
  var local = "inside";
  print global + local;
}
```

#### 89. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
class Environment {
```

#### 90. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  final Environment enclosing;
```

#### 91. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private final Map<String, Object> values = new HashMap<>();
```

#### 92. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  Environment() {
    enclosing = null;
  }

  Environment(Environment enclosing) {
    this.enclosing = enclosing;
  }
```

#### 93. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      return values.get(name.lexeme);
    }
```

#### 94. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    if (enclosing != null) return enclosing.get(name);
```

#### 95. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    throw new RuntimeError(name,
        "Undefined variable '" + name.lexeme + "'.");
```

#### 96. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      values.put(name.lexeme, value);
      return;
    }

```

#### 97. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    if (enclosing != null) {
      enclosing.assign(name, value);
      return;
    }

```

#### 98. 8 . 5 . 1 Nesting and shadowing — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    throw new RuntimeError(name,
```

#### 99. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
statement      â exprStmt
               | printStmt
               | block ;

block          â "{" declaration* "}" ;
```

#### 100. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    defineAst(outputDir, "Stmt", Arrays.asList(
```

#### 101. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Block      : List<Stmt> statements",
```

#### 102. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
      "Expression : Expr expression",
```

#### 103. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    if (match(PRINT)) return printStatement();
```

#### 104. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
    if (match(LEFT_BRACE)) return new Stmt.Block(block());
```

#### 105. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```


    return expressionStatement();
```

#### 106. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  private List<Stmt> block() {
    List<Stmt> statements = new ArrayList<>();

    while (!check(RIGHT_BRACE) && !isAtEnd()) {
      statements.add(declaration());
    }

    consume(RIGHT_BRACE, "Expect '}' after block.");
    return statements;
  }
```

#### 107. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  @Override
  public Void visitBlockStmt(Stmt.Block stmt) {
    executeBlock(stmt.statements, new Environment(environment));
    return null;
  }
```

#### 108. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
  void executeBlock(List<Stmt> statements,
                    Environment environment) {
    Environment previous = this.environment;
    try {
      this.environment = environment;

      for (Stmt statement : statements) {
        execute(statement);
      }
    } finally {
      this.environment = previous;
    }
  }
```

#### 109. 8 . 5 . 2 Block syntax and semantics — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a = "global a";
var b = "global b";
var c = "global c";
{
  var a = "outer a";
  var b = "outer b";
  {
    var a = "inner a";
    print a;
    print b;
    print c;
  }
  print a;
  print b;
  print c;
}
print a;
print b;
print c;
```

#### 110. Challenges — [source](https://craftinginterpreters.com/statements-and-state.html)
```
// No initializers.
var a;
var b;

a = "assigned";
print a; // OK, was assigned first.

print b; // Error!
```

#### 111. Challenges — [source](https://craftinginterpreters.com/statements-and-state.html)
```
var a = 1;
{
  var a = a + 2;
  print a;
}
```

