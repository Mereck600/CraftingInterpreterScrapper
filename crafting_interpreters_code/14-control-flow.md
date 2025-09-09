# Control Flow
_From: https://craftinginterpreters.com/control-flow.html_

#### 1. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
statement      â exprStmt
               | ifStmt
               | printStmt
               | block ;

ifStmt         â "if" "(" expression ")" statement
               ( "else" statement )? ;
```

#### 2. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Expression : Expr expression",
```

#### 3. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
      "If         : Expr condition, Stmt thenBranch," +
                  " Stmt elseBranch",
```

#### 4. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Print      : Expr expression",
```

#### 5. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Stmt statement() {
```

#### 6. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(IF)) return ifStatement();
```

#### 7. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(PRINT)) return printStatement();
```

#### 8. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Stmt ifStatement() {
    consume(LEFT_PAREN, "Expect '(' after 'if'.");
    Expr condition = expression();
    consume(RIGHT_PAREN, "Expect ')' after if condition."); 

    Stmt thenBranch = statement();
    Stmt elseBranch = null;
    if (match(ELSE)) {
      elseBranch = statement();
    }

    return new Stmt.If(condition, thenBranch, elseBranch);
  }
```

#### 9. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
if (first) if (second) whenTrue(); else whenFalse();
```

#### 10. 9 . 2 Conditional Execution — [source](https://craftinginterpreters.com/control-flow.html)
```
  @Override
  public Void visitIfStmt(Stmt.If stmt) {
    if (isTruthy(evaluate(stmt.condition))) {
      execute(stmt.thenBranch);
    } else if (stmt.elseBranch != null) {
      execute(stmt.elseBranch);
    }
    return null;
  }
```

#### 11. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
false and sideEffect();
```

#### 12. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
expression     â assignment ;
assignment     â IDENTIFIER "=" assignment
               | logic_or ;
logic_or       â logic_and ( "or" logic_and )* ;
logic_and      â equality ( "and" equality )* ;
```

#### 13. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Literal  : Object value",
```

#### 14. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Logical  : Expr left, Token operator, Expr right",
```

#### 15. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Unary    : Token operator, Expr right",
```

#### 16. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Expr assignment() {
```

#### 17. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
    Expr expr = or();
```

#### 18. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```


    if (match(EQUAL)) {
```

#### 19. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Expr or() {
    Expr expr = and();

    while (match(OR)) {
      Token operator = previous();
      Expr right = and();
      expr = new Expr.Logical(expr, operator, right);
    }

    return expr;
  }
```

#### 20. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Expr and() {
    Expr expr = equality();

    while (match(AND)) {
      Token operator = previous();
      Expr right = equality();
      expr = new Expr.Logical(expr, operator, right);
    }

    return expr;
  }
```

#### 21. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
  @Override
  public Object visitLogicalExpr(Expr.Logical expr) {
    Object left = evaluate(expr.left);

    if (expr.operator.type == TokenType.OR) {
      if (isTruthy(left)) return left;
    } else {
      if (!isTruthy(left)) return left;
    }

    return evaluate(expr.right);
  }
```

#### 22. 9 . 3 Logical Operators — [source](https://craftinginterpreters.com/control-flow.html)
```
print "hi" or 2; // "hi".
print nil or "yes"; // "yes".
```

#### 23. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
statement      â exprStmt
               | ifStmt
               | printStmt
               | whileStmt
               | block ;

whileStmt      â "while" "(" expression ")" statement ;
```

#### 24. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Print      : Expr expression",
```

#### 25. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
      "Var        : Token name, Expr initializer",
```

#### 26. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
      "While      : Expr condition, Stmt body"
```

#### 27. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
    ));
```

#### 28. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(PRINT)) return printStatement();
```

#### 29. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(WHILE)) return whileStatement();
```

#### 30. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(LEFT_BRACE)) return new Stmt.Block(block());
```

#### 31. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Stmt whileStatement() {
    consume(LEFT_PAREN, "Expect '(' after 'while'.");
    Expr condition = expression();
    consume(RIGHT_PAREN, "Expect ')' after condition.");
    Stmt body = statement();

    return new Stmt.While(condition, body);
  }
```

#### 32. 9 . 4 While Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
  @Override
  public Void visitWhileStmt(Stmt.While stmt) {
    while (isTruthy(evaluate(stmt.condition))) {
      execute(stmt.body);
    }
    return null;
  }
```

#### 33. 9 . 5 For Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
for (var i = 0; i < 10; i = i + 1) print i;
```

#### 34. 9 . 5 For Loops — [source](https://craftinginterpreters.com/control-flow.html)
```
statement      â exprStmt
               | forStmt
               | ifStmt
               | printStmt
               | whileStmt
               | block ;

forStmt        â "for" "(" ( varDecl | exprStmt | ";" )
                 expression? ";"
                 expression? ")" statement ;
```

#### 35. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
{
  var i = 0;
  while (i < 10) {
    print i;
    i = i + 1;
  }
}
```

#### 36. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
import java.util.ArrayList;
```

#### 37. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
import java.util.Arrays;
```

#### 38. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
import java.util.List;
```

#### 39. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Stmt statement() {
```

#### 40. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(FOR)) return forStatement();
```

#### 41. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (match(IF)) return ifStatement();
```

#### 42. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
  private Stmt forStatement() {
    consume(LEFT_PAREN, "Expect '(' after 'for'.");

    // More here...
  }
```

#### 43. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    consume(LEFT_PAREN, "Expect '(' after 'for'.");

```

#### 44. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    Stmt initializer;
    if (match(SEMICOLON)) {
      initializer = null;
    } else if (match(VAR)) {
      initializer = varDeclaration();
    } else {
      initializer = expressionStatement();
    }
```

#### 45. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
  }
```

#### 46. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
      initializer = expressionStatement();
    }
```

#### 47. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```


    Expr condition = null;
    if (!check(SEMICOLON)) {
      condition = expression();
    }
    consume(SEMICOLON, "Expect ';' after loop condition.");
```

#### 48. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
  }
```

#### 49. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    consume(SEMICOLON, "Expect ';' after loop condition.");
```

#### 50. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```


    Expr increment = null;
    if (!check(RIGHT_PAREN)) {
      increment = expression();
    }
    consume(RIGHT_PAREN, "Expect ')' after for clauses.");
```

#### 51. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
  }
```

#### 52. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    consume(RIGHT_PAREN, "Expect ')' after for clauses.");
```

#### 53. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    Stmt body = statement();

    return body;
```

#### 54. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
  }
```

#### 55. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    Stmt body = statement();

```

#### 56. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (increment != null) {
      body = new Stmt.Block(
          Arrays.asList(
              body,
              new Stmt.Expression(increment)));
    }

```

#### 57. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    return body;
```

#### 58. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    }

```

#### 59. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (condition == null) condition = new Expr.Literal(true);
    body = new Stmt.While(condition, body);

```

#### 60. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    return body;
```

#### 61. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    body = new Stmt.While(condition, body);

```

#### 62. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    if (initializer != null) {
      body = new Stmt.Block(Arrays.asList(initializer, body));
    }

```

#### 63. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
    return body;
```

#### 64. 9 . 5 . 1 Desugaring — [source](https://craftinginterpreters.com/control-flow.html)
```
var a = 0;
var temp;

for (var b = 1; a < 10000; b = temp + b) {
  print a;
  temp = a;
  a = b;
}
```

