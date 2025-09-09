# Resolving and Binding
_From: https://craftinginterpreters.com/resolving-and-binding.html_

#### 1. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a = "outer";
{
  var a = "inner";
  print a;
}
```

#### 2. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a = "outer";
{
  print a;
  var a = "inner";
}
```

#### 3. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
{
  console.log(a);
  var a = "value";
}
```

#### 4. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
{
  var a; // Hoist.
  console.log(a);
  a = "value";
}
```

#### 5. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a = "outer";
{
  var a = "inner";
  print a;
}
```

#### 6. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a = "global";
{
  fun showA() {
    print a;
  }

  showA();
  var a = "block";
  showA();
}
```

#### 7. 11 . 1 Static Scope — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
global
block
```

#### 8. 11 . 1 . 1 Scopes and mutable environments — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
{
  var a;
  // 1.
  var b;
  // 2.
}
```

#### 9. 11 . 3 A Resolver Class — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```lox
package com.craftinginterpreters.lox;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

class Resolver implements Expr.Visitor<Void>, Stmt.Visitor<Void> {
  private final Interpreter interpreter;

  Resolver(Interpreter interpreter) {
    this.interpreter = interpreter;
  }
}
```

#### 10. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitBlockStmt(Stmt.Block stmt) {
    beginScope();
    resolve(stmt.statements);
    endScope();
    return null;
  }
```

#### 11. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  void resolve(List<Stmt> statements) {
    for (Stmt statement : statements) {
      resolve(statement);
    }
  }
```

#### 12. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void resolve(Stmt stmt) {
    stmt.accept(this);
  }
```

#### 13. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void resolve(Expr expr) {
    expr.accept(this);
  }
```

#### 14. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void beginScope() {
    scopes.push(new HashMap<String, Boolean>());
  }
```

#### 15. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private final Interpreter interpreter;
```

#### 16. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private final Stack<Map<String, Boolean>> scopes = new Stack<>();
```

#### 17. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


  Resolver(Interpreter interpreter) {
```

#### 18. 11 . 3 . 1 Resolving blocks — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void endScope() {
    scopes.pop();
  }
```

#### 19. 11 . 3 . 2 Resolving variable declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitVarStmt(Stmt.Var stmt) {
    declare(stmt.name);
    if (stmt.initializer != null) {
      resolve(stmt.initializer);
    }
    define(stmt.name);
    return null;
  }
```

#### 20. 11 . 3 . 2 Resolving variable declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a = "outer";
{
  var a = a;
}
```

#### 21. 11 . 3 . 2 Resolving variable declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var temp = a; // Run the initializer.
var a;        // Declare the variable.
a = temp;     // Initialize it.
```

#### 22. 11 . 3 . 2 Resolving variable declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a; // Define the variable.
a = a; // Run the initializer.
```

#### 23. 11 . 3 . 2 Resolving variable declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void declare(Token name) {
    if (scopes.isEmpty()) return;

    Map<String, Boolean> scope = scopes.peek();
    scope.put(name.lexeme, false);
  }
```

#### 24. 11 . 3 . 2 Resolving variable declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void define(Token name) {
    if (scopes.isEmpty()) return;
    scopes.peek().put(name.lexeme, true);
  }
```

#### 25. 11 . 3 . 3 Resolving variable expressions — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitVariableExpr(Expr.Variable expr) {
    if (!scopes.isEmpty() &&
        scopes.peek().get(expr.name.lexeme) == Boolean.FALSE) {
      Lox.error(expr.name,
          "Can't read local variable in its own initializer.");
    }

    resolveLocal(expr, expr.name);
    return null;
  }
```

#### 26. 11 . 3 . 3 Resolving variable expressions — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void resolveLocal(Expr expr, Token name) {
    for (int i = scopes.size() - 1; i >= 0; i--) {
      if (scopes.get(i).containsKey(name.lexeme)) {
        interpreter.resolve(expr, scopes.size() - 1 - i);
        return;
      }
    }
  }
```

#### 27. 11 . 3 . 4 Resolving assignment expressions — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitAssignExpr(Expr.Assign expr) {
    resolve(expr.value);
    resolveLocal(expr, expr.name);
    return null;
  }
```

#### 28. 11 . 3 . 5 Resolving function declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitFunctionStmt(Stmt.Function stmt) {
    declare(stmt.name);
    define(stmt.name);

    resolveFunction(stmt);
    return null;
  }
```

#### 29. 11 . 3 . 5 Resolving function declarations — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void resolveFunction(Stmt.Function function) {
    beginScope();
    for (Token param : function.params) {
      declare(param);
      define(param);
    }
    resolve(function.body);
    endScope();
  }
```

#### 30. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitExpressionStmt(Stmt.Expression stmt) {
    resolve(stmt.expression);
    return null;
  }
```

#### 31. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitIfStmt(Stmt.If stmt) {
    resolve(stmt.condition);
    resolve(stmt.thenBranch);
    if (stmt.elseBranch != null) resolve(stmt.elseBranch);
    return null;
  }
```

#### 32. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitPrintStmt(Stmt.Print stmt) {
    resolve(stmt.expression);
    return null;
  }
```

#### 33. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitReturnStmt(Stmt.Return stmt) {
    if (stmt.value != null) {
      resolve(stmt.value);
    }

    return null;
  }
```

#### 34. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitWhileStmt(Stmt.While stmt) {
    resolve(stmt.condition);
    resolve(stmt.body);
    return null;
  }
```

#### 35. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitBinaryExpr(Expr.Binary expr) {
    resolve(expr.left);
    resolve(expr.right);
    return null;
  }
```

#### 36. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitCallExpr(Expr.Call expr) {
    resolve(expr.callee);

    for (Expr argument : expr.arguments) {
      resolve(argument);
    }

    return null;
  }
```

#### 37. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitGroupingExpr(Expr.Grouping expr) {
    resolve(expr.expression);
    return null;
  }
```

#### 38. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitLiteralExpr(Expr.Literal expr) {
    return null;
  }
```

#### 39. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitLogicalExpr(Expr.Logical expr) {
    resolve(expr.left);
    resolve(expr.right);
    return null;
  }
```

#### 40. 11 . 3 . 6 Resolving the other syntax tree nodes — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  @Override
  public Void visitUnaryExpr(Expr.Unary expr) {
    resolve(expr.right);
    return null;
  }
```

#### 41. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  void resolve(Expr expr, int depth) {
    locals.put(expr, depth);
  }
```

#### 42. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private Environment environment = globals;
```

#### 43. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private final Map<Expr, Integer> locals = new HashMap<>();
```

#### 44. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


  Interpreter() {
```

#### 45. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
import java.util.ArrayList;
```

#### 46. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
import java.util.HashMap;
```

#### 47. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
import java.util.List;
```

#### 48. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
import java.util.List;
```

#### 49. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
import java.util.Map;
```

#### 50. 11 . 4 Interpreting Resolved Variables — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


class Interpreter implements Expr.Visitor<Object>,
```

#### 51. 11 . 4 . 1 Accessing a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  public Object visitVariableExpr(Expr.Variable expr) {
```

#### 52. 11 . 4 . 1 Accessing a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    return lookUpVariable(expr.name, expr);
```

#### 53. 11 . 4 . 1 Accessing a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  }
```

#### 54. 11 . 4 . 1 Accessing a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private Object lookUpVariable(Token name, Expr expr) {
    Integer distance = locals.get(expr);
    if (distance != null) {
      return environment.getAt(distance, name.lexeme);
    } else {
      return globals.get(name);
    }
  }
```

#### 55. 11 . 4 . 1 Accessing a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  Object getAt(int distance, String name) {
    return ancestor(distance).values.get(name);
  }
```

#### 56. 11 . 4 . 1 Accessing a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  Environment ancestor(int distance) {
    Environment environment = this;
    for (int i = 0; i < distance; i++) {
      environment = environment.enclosing; 
    }

    return environment;
  }
```

#### 57. 11 . 4 . 2 Assigning to a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  public Object visitAssignExpr(Expr.Assign expr) {
    Object value = evaluate(expr.value);
```

#### 58. 11 . 4 . 2 Assigning to a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


    Integer distance = locals.get(expr);
    if (distance != null) {
      environment.assignAt(distance, expr.name, value);
    } else {
      globals.assign(expr.name, value);
    }

```

#### 59. 11 . 4 . 2 Assigning to a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    return value;
```

#### 60. 11 . 4 . 2 Assigning to a resolved variable — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  void assignAt(int distance, Token name, Object value) {
    ancestor(distance).values.put(name.lexeme, value);
  }
```

#### 61. 11 . 4 . 3 Running the resolver — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    // Stop if there was a syntax error.
    if (hadError) return;

```

#### 62. 11 . 4 . 3 Running the resolver — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    Resolver resolver = new Resolver(interpreter);
    resolver.resolve(statements);

```

#### 63. 11 . 4 . 3 Running the resolver — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    interpreter.interpret(statements);
```

#### 64. 11 . 5 Resolution Errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
fun bad() {
  var a = "first";
  var a = "second";
}
```

#### 65. 11 . 5 Resolution Errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    Map<String, Boolean> scope = scopes.peek();
```

#### 66. 11 . 5 Resolution Errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    if (scope.containsKey(name.lexeme)) {
      Lox.error(name,
          "Already a variable with this name in this scope.");
    }

```

#### 67. 11 . 5 Resolution Errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    scope.put(name.lexeme, false);
```

#### 68. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
return "at top level";
```

#### 69. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private final Stack<Map<String, Boolean>> scopes = new Stack<>();
```

#### 70. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private FunctionType currentFunction = FunctionType.NONE;
```

#### 71. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


  Resolver(Interpreter interpreter) {
```

#### 72. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private enum FunctionType {
    NONE,
    FUNCTION
  }
```

#### 73. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    define(stmt.name);

```

#### 74. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    resolveFunction(stmt, FunctionType.FUNCTION);
```

#### 75. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    return null;
```

#### 76. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  private void resolveFunction(
      Stmt.Function function, FunctionType type) {
    FunctionType enclosingFunction = currentFunction;
    currentFunction = type;

```

#### 77. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    beginScope();
```

#### 78. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    endScope();
```

#### 79. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    currentFunction = enclosingFunction;
```

#### 80. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  }
```

#### 81. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
  public Void visitReturnStmt(Stmt.Return stmt) {
```

#### 82. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    if (currentFunction == FunctionType.NONE) {
      Lox.error(stmt.keyword, "Can't return from top-level code.");
    }

```

#### 83. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    if (stmt.value != null) {
```

#### 84. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
    resolver.resolve(statements);
```

#### 85. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


    // Stop if there was a resolution error.
    if (hadError) return;
```

#### 86. 11 . 5 . 1 Invalid return errors — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```


    interpreter.interpret(statements);
```

#### 87. Challenges — [source](https://craftinginterpreters.com/resolving-and-binding.html)
```
var a = "outer";
{
  var a = a;
}
```

