# Functions
_From: https://craftinginterpreters.com/functions.html_

#### 1. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
average(1, 2);
```

#### 2. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
getCallback()();
```

#### 3. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
unary          â ( "!" | "-" ) unary | call ;
call           â primary ( "(" arguments? ")" )* ;
```

#### 4. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
arguments      â expression ( "," expression )* ;
```

#### 5. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
      "Binary   : Expr left, Token operator, Expr right",
```

#### 6. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
      "Call     : Expr callee, Token paren, List<Expr> arguments",
```

#### 7. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
      "Grouping : Expr expression",
```

#### 8. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
      return new Expr.Unary(operator, right);
    }

```

#### 9. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
    return call();
```

#### 10. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
  }
```

#### 11. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
  private Expr call() {
    Expr expr = primary();

    while (true) { 
      if (match(LEFT_PAREN)) {
        expr = finishCall(expr);
      } else {
        break;
      }
    }

    return expr;
  }
```

#### 12. 10 . 1 Function Calls — [source](https://craftinginterpreters.com/functions.html)
```
  private Expr finishCall(Expr callee) {
    List<Expr> arguments = new ArrayList<>();
    if (!check(RIGHT_PAREN)) {
      do {
        arguments.add(expression());
      } while (match(COMMA));
    }

    Token paren = consume(RIGHT_PAREN,
                          "Expect ')' after arguments.");

    return new Expr.Call(callee, paren, arguments);
  }
```

#### 13. 10 . 1 . 1 Maximum argument counts — [source](https://craftinginterpreters.com/functions.html)
```
      do {
```

#### 14. 10 . 1 . 1 Maximum argument counts — [source](https://craftinginterpreters.com/functions.html)
```
        if (arguments.size() >= 255) {
          error(peek(), "Can't have more than 255 arguments.");
        }
```

#### 15. 10 . 1 . 1 Maximum argument counts — [source](https://craftinginterpreters.com/functions.html)
```
        arguments.add(expression());
```

#### 16. 10 . 1 . 2 Interpreting function calls — [source](https://craftinginterpreters.com/functions.html)
```
import java.util.ArrayList;
```

#### 17. 10 . 1 . 2 Interpreting function calls — [source](https://craftinginterpreters.com/functions.html)
```
import java.util.List;
```

#### 18. 10 . 1 . 2 Interpreting function calls — [source](https://craftinginterpreters.com/functions.html)
```
  @Override
  public Object visitCallExpr(Expr.Call expr) {
    Object callee = evaluate(expr.callee);

    List<Object> arguments = new ArrayList<>();
    for (Expr argument : expr.arguments) { 
      arguments.add(evaluate(argument));
    }

    LoxCallable function = (LoxCallable)callee;
    return function.call(this, arguments);
  }
```

#### 19. 10 . 1 . 2 Interpreting function calls — [source](https://craftinginterpreters.com/functions.html)
```
package com.craftinginterpreters.lox;

import java.util.List;

interface LoxCallable {
  Object call(Interpreter interpreter, List<Object> arguments);
}
```

#### 20. 10 . 1 . 3 Call type errors — [source](https://craftinginterpreters.com/functions.html)
```
"totally not a function"();
```

#### 21. 10 . 1 . 3 Call type errors — [source](https://craftinginterpreters.com/functions.html)
```
    }

```

#### 22. 10 . 1 . 3 Call type errors — [source](https://craftinginterpreters.com/functions.html)
```
    if (!(callee instanceof LoxCallable)) {
      throw new RuntimeError(expr.paren,
          "Can only call functions and classes.");
    }

```

#### 23. 10 . 1 . 3 Call type errors — [source](https://craftinginterpreters.com/functions.html)
```
    LoxCallable function = (LoxCallable)callee;
```

#### 24. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
fun add(a, b, c) {
  print a + b + c;
}
```

#### 25. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
add(1, 2, 3, 4); // Too many.
add(1, 2);       // Too few.
```

#### 26. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
    LoxCallable function = (LoxCallable)callee;
```

#### 27. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
    if (arguments.size() != function.arity()) {
      throw new RuntimeError(expr.paren, "Expected " +
          function.arity() + " arguments but got " +
          arguments.size() + ".");
    }

```

#### 28. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
    return function.call(this, arguments);
```

#### 29. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
interface LoxCallable {
```

#### 30. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
  int arity();
```

#### 31. 10 . 1 . 4 Checking arity — [source](https://craftinginterpreters.com/functions.html)
```
  Object call(Interpreter interpreter, List<Object> arguments);
```

#### 32. 10 . 2 . 1 Telling time — [source](https://craftinginterpreters.com/functions.html)
```
class Interpreter implements Expr.Visitor<Object>,
                             Stmt.Visitor<Void> {
```

#### 33. 10 . 2 . 1 Telling time — [source](https://craftinginterpreters.com/functions.html)
```
  final Environment globals = new Environment();
  private Environment environment = globals;
```

#### 34. 10 . 2 . 1 Telling time — [source](https://craftinginterpreters.com/functions.html)
```


  void interpret(List<Stmt> statements) {
```

#### 35. 10 . 2 . 1 Telling time — [source](https://craftinginterpreters.com/functions.html)
```
  private Environment environment = globals;

```

#### 36. 10 . 2 . 1 Telling time — [source](https://craftinginterpreters.com/functions.html)
```
  Interpreter() {
    globals.define("clock", new LoxCallable() {
      @Override
      public int arity() { return 0; }

      @Override
      public Object call(Interpreter interpreter,
                         List<Object> arguments) {
        return (double)System.currentTimeMillis() / 1000.0;
      }

      @Override
      public String toString() { return "<native fn>"; }
    });
  }

```

#### 37. 10 . 2 . 1 Telling time — [source](https://craftinginterpreters.com/functions.html)
```
  void interpret(List<Stmt> statements) {
```

#### 38. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
var add = fun (a, b) {
  print a + b;
};
```

#### 39. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
declaration    â funDecl
               | varDecl
               | statement ;
```

#### 40. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
funDecl        â "fun" function ;
function       â IDENTIFIER "(" parameters? ")" block ;
```

#### 41. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
parameters     â IDENTIFIER ( "," IDENTIFIER )* ;
```

#### 42. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
      "Expression : Expr expression",
```

#### 43. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
      "Function   : Token name, List<Token> params," +
                  " List<Stmt> body",
```

#### 44. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
      "If         : Expr condition, Stmt thenBranch," +
```

#### 45. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
    try {
```

#### 46. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
      if (match(FUN)) return function("function");
```

#### 47. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
      if (match(VAR)) return varDeclaration();
```

#### 48. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
  private Stmt.Function function(String kind) {
    Token name = consume(IDENTIFIER, "Expect " + kind + " name.");
  }
```

#### 49. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
    Token name = consume(IDENTIFIER, "Expect " + kind + " name.");
```

#### 50. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
    consume(LEFT_PAREN, "Expect '(' after " + kind + " name.");
    List<Token> parameters = new ArrayList<>();
    if (!check(RIGHT_PAREN)) {
      do {
        if (parameters.size() >= 255) {
          error(peek(), "Can't have more than 255 parameters.");
        }

        parameters.add(
            consume(IDENTIFIER, "Expect parameter name."));
      } while (match(COMMA));
    }
    consume(RIGHT_PAREN, "Expect ')' after parameters.");
```

#### 51. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
  }
```

#### 52. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
    consume(RIGHT_PAREN, "Expect ')' after parameters.");
```

#### 53. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```


    consume(LEFT_BRACE, "Expect '{' before " + kind + " body.");
    List<Stmt> body = block();
    return new Stmt.Function(name, parameters, body);
```

#### 54. 10 . 3 Function Declarations — [source](https://craftinginterpreters.com/functions.html)
```
  }
```

#### 55. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```lox
package com.craftinginterpreters.lox;

import java.util.List;

class LoxFunction implements LoxCallable {
  private final Stmt.Function declaration;
  LoxFunction(Stmt.Function declaration) {
    this.declaration = declaration;
  }
}
```

#### 56. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```
  @Override
  public Object call(Interpreter interpreter,
                     List<Object> arguments) {
    Environment environment = new Environment(interpreter.globals);
    for (int i = 0; i < declaration.params.size(); i++) {
      environment.define(declaration.params.get(i).lexeme,
          arguments.get(i));
    }

    interpreter.executeBlock(declaration.body, environment);
    return null;
  }
```

#### 57. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```
fun count(n) {
  if (n > 1) count(n - 1);
  print n;
}

count(3);
```

#### 58. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```
fun add(a, b, c) {
  print a + b + c;
}

add(1, 2, 3);
```

#### 59. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```
  @Override
  public int arity() {
    return declaration.params.size();
  }
```

#### 60. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```
  @Override
  public String toString() {
    return "<fn " + declaration.name.lexeme + ">";
  }
```

#### 61. 10 . 4 Function Objects — [source](https://craftinginterpreters.com/functions.html)
```
fun add(a, b) {
  print a + b;
}

print add; // "<fn add>".
```

#### 62. 10 . 4 . 1 Interpreting function declarations — [source](https://craftinginterpreters.com/functions.html)
```
  @Override
  public Void visitFunctionStmt(Stmt.Function stmt) {
    LoxFunction function = new LoxFunction(stmt);
    environment.define(stmt.name.lexeme, function);
    return null;
  }
```

#### 63. 10 . 4 . 1 Interpreting function declarations — [source](https://craftinginterpreters.com/functions.html)
```
fun sayHi(first, last) {
  print "Hi, " + first + " " + last + "!";
}

sayHi("Dear", "Reader");
```

#### 64. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
statement      â exprStmt
               | forStmt
               | ifStmt
               | printStmt
               | returnStmt
               | whileStmt
               | block ;

returnStmt     â "return" expression? ";" ;
```

#### 65. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
fun procedure() {
  print "don't return anything";
}

var result = procedure();
print result; // ?
```

#### 66. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
return nil;
```

#### 67. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
      "Print      : Expr expression",
```

#### 68. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
      "Return     : Token keyword, Expr value",
```

#### 69. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
      "Var        : Token name, Expr initializer",
```

#### 70. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
    if (match(PRINT)) return printStatement();
```

#### 71. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
    if (match(RETURN)) return returnStatement();
```

#### 72. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
    if (match(WHILE)) return whileStatement();
```

#### 73. 10 . 5 Return Statements — [source](https://craftinginterpreters.com/functions.html)
```
  private Stmt returnStatement() {
    Token keyword = previous();
    Expr value = null;
    if (!check(SEMICOLON)) {
      value = expression();
    }

    consume(SEMICOLON, "Expect ';' after return value.");
    return new Stmt.Return(keyword, value);
  }
```

#### 74. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
fun count(n) {
  while (n < 100) {
    if (n == 3) return n; // <--
    print n;
    n = n + 1;
  }
}

count(1);
```

#### 75. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
Interpreter.visitReturnStmt()
Interpreter.visitIfStmt()
Interpreter.executeBlock()
Interpreter.visitBlockStmt()
Interpreter.visitWhileStmt()
Interpreter.executeBlock()
LoxFunction.call()
Interpreter.visitCallExpr()
```

#### 76. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
  @Override
  public Void visitReturnStmt(Stmt.Return stmt) {
    Object value = null;
    if (stmt.value != null) value = evaluate(stmt.value);

    throw new Return(value);
  }
```

#### 77. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```lox
package com.craftinginterpreters.lox;

class Return extends RuntimeException {
  final Object value;

  Return(Object value) {
    super(null, null, false, false);
    this.value = value;
  }
}
```

#### 78. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
          arguments.get(i));
    }

```

#### 79. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
    try {
      interpreter.executeBlock(declaration.body, environment);
    } catch (Return returnValue) {
      return returnValue.value;
    }
```

#### 80. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
    return null;
```

#### 81. 10 . 5 . 1 Returning from calls — [source](https://craftinginterpreters.com/functions.html)
```
fun fib(n) {
  if (n <= 1) return n;
  return fib(n - 2) + fib(n - 1);
}

for (var i = 0; i < 20; i = i + 1) {
  print fib(i);
}
```

#### 82. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
fun makeCounter() {
  var i = 0;
  fun count() {
    i = i + 1;
    print i;
  }

  return count;
}

var counter = makeCounter();
counter(); // "1".
counter(); // "2".
```

#### 83. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
  private final Stmt.Function declaration;
```

#### 84. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
  private final Environment closure;

```

#### 85. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
  LoxFunction(Stmt.Function declaration) {
```

#### 86. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
  LoxFunction(Stmt.Function declaration, Environment closure) {
    this.closure = closure;
```

#### 87. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
    this.declaration = declaration;
```

#### 88. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
  public Void visitFunctionStmt(Stmt.Function stmt) {
```

#### 89. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
    LoxFunction function = new LoxFunction(stmt, environment);
```

#### 90. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
    environment.define(stmt.name.lexeme, function);
```

#### 91. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
                     List<Object> arguments) {
```

#### 92. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
    Environment environment = new Environment(closure);
```

#### 93. 10 . 6 Local Functions and Closures — [source](https://craftinginterpreters.com/functions.html)
```
    for (int i = 0; i < declaration.params.size(); i++) {
```

#### 94. Challenges — [source](https://craftinginterpreters.com/functions.html)
```
fun thrice(fn) {
  for (var i = 1; i <= 3; i = i + 1) {
    fn(i);
  }
}

thrice(fun (a) {
  print a;
});
// "1".
// "2".
// "3".
```

#### 95. Challenges — [source](https://craftinginterpreters.com/functions.html)
```
fun () {};
```

#### 96. Challenges — [source](https://craftinginterpreters.com/functions.html)
```
fun scope(a) {
  var a = "local";
}
```

