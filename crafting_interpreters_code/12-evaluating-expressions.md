# Evaluating Expressions
_From: https://craftinginterpreters.com/evaluating-expressions.html_

#### 1. 7 . 2 Evaluating Expressions — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```lox
package com.craftinginterpreters.lox;

class Interpreter implements Expr.Visitor<Object> {
}
```

#### 2. 7 . 2 . 1 Evaluating literals — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  @Override
  public Object visitLiteralExpr(Expr.Literal expr) {
    return expr.value;
  }
```

#### 3. 7 . 2 . 2 Evaluating parentheses — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  @Override
  public Object visitGroupingExpr(Expr.Grouping expr) {
    return evaluate(expr.expression);
  }
```

#### 4. 7 . 2 . 2 Evaluating parentheses — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private Object evaluate(Expr expr) {
    return expr.accept(this);
  }
```

#### 5. 7 . 2 . 3 Evaluating unary expressions — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  @Override
  public Object visitUnaryExpr(Expr.Unary expr) {
    Object right = evaluate(expr.right);

    switch (expr.operator.type) {
      case MINUS:
        return -(double)right;
    }

    // Unreachable.
    return null;
  }
```

#### 6. 7 . 2 . 3 Evaluating unary expressions — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    switch (expr.operator.type) {
```

#### 7. 7 . 2 . 3 Evaluating unary expressions — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case BANG:
        return !isTruthy(right);
```

#### 8. 7 . 2 . 3 Evaluating unary expressions — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case MINUS:
```

#### 9. 7 . 2 . 4 Truthiness and falsiness — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private boolean isTruthy(Object object) {
    if (object == null) return false;
    if (object instanceof Boolean) return (boolean)object;
    return true;
  }
```

#### 10. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  @Override
  public Object visitBinaryExpr(Expr.Binary expr) {
    Object left = evaluate(expr.left);
    Object right = evaluate(expr.right); 

    switch (expr.operator.type) {
      case MINUS:
        return (double)left - (double)right;
      case SLASH:
        return (double)left / (double)right;
      case STAR:
        return (double)left * (double)right;
    }

    // Unreachable.
    return null;
  }
```

#### 11. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    switch (expr.operator.type) {
      case MINUS:
        return (double)left - (double)right;
```

#### 12. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case PLUS:
        if (left instanceof Double && right instanceof Double) {
          return (double)left + (double)right;
        } 

        if (left instanceof String && right instanceof String) {
          return (String)left + (String)right;
        }

        break;
```

#### 13. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case SLASH:
```

#### 14. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    switch (expr.operator.type) {
```

#### 15. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case GREATER:
        return (double)left > (double)right;
      case GREATER_EQUAL:
        return (double)left >= (double)right;
      case LESS:
        return (double)left < (double)right;
      case LESS_EQUAL:
        return (double)left <= (double)right;
```

#### 16. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case MINUS:
```

#### 17. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case BANG_EQUAL: return !isEqual(left, right);
      case EQUAL_EQUAL: return isEqual(left, right);
```

#### 18. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private boolean isEqual(Object a, Object b) {
    if (a == null && b == null) return true;
    if (a == null) return false;

    return a.equals(b);
  }
```

#### 19. 7 . 2 . 5 Evaluating binary operators — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
(0 / 0) == (0 / 0)
```

#### 20. 7 . 3 Runtime Errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
2 * (3 / -"muffin")
```

#### 21. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case MINUS:
```

#### 22. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperand(expr.operator, right);
```

#### 23. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return -(double)right;
```

#### 24. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private void checkNumberOperand(Token operator, Object operand) {
    if (operand instanceof Double) return;
    throw new RuntimeError(operator, "Operand must be a number.");
  }
```

#### 25. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```lox
package com.craftinginterpreters.lox;

class RuntimeError extends RuntimeException {
  final Token token;

  RuntimeError(Token token, String message) {
    super(message);
    this.token = token;
  }
}
```

#### 26. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case GREATER:
```

#### 27. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 28. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left > (double)right;
```

#### 29. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case GREATER_EQUAL:
```

#### 30. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 31. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left >= (double)right;
```

#### 32. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case LESS:
```

#### 33. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 34. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left < (double)right;
```

#### 35. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case LESS_EQUAL:
```

#### 36. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 37. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left <= (double)right;
```

#### 38. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case MINUS:
```

#### 39. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 40. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left - (double)right;
```

#### 41. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case SLASH:
```

#### 42. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 43. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left / (double)right;
```

#### 44. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case STAR:
```

#### 45. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        checkNumberOperands(expr.operator, left, right);
```

#### 46. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        return (double)left * (double)right;
```

#### 47. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private void checkNumberOperands(Token operator,
                                   Object left, Object right) {
    if (left instanceof Double && right instanceof Double) return;
    
    throw new RuntimeError(operator, "Operands must be numbers.");
  }
```

#### 48. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
say("left") - say("right");
```

#### 49. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
          return (String)left + (String)right;
        }

```

#### 50. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
        throw new RuntimeError(expr.operator,
            "Operands must be two numbers or two strings.");
```

#### 51. 7 . 3 . 1 Detecting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
      case SLASH:
```

#### 52. 7 . 4 Hooking Up the Interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  void interpret(Expr expression) { 
    try {
      Object value = evaluate(expression);
      System.out.println(stringify(value));
    } catch (RuntimeError error) {
      Lox.runtimeError(error);
    }
  }
```

#### 53. 7 . 4 Hooking Up the Interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private String stringify(Object object) {
    if (object == null) return "nil";

    if (object instanceof Double) {
      String text = object.toString();
      if (text.endsWith(".0")) {
        text = text.substring(0, text.length() - 2);
      }
      return text;
    }

    return object.toString();
  }
```

#### 54. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  static void runtimeError(RuntimeError error) {
    System.err.println(error.getMessage() +
        "\n[line " + error.token.line + "]");
    hadRuntimeError = true;
  }
```

#### 55. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  static boolean hadError = false;
```

#### 56. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  static boolean hadRuntimeError = false;

```

#### 57. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  public static void main(String[] args) throws IOException {
```

#### 58. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    run(new String(bytes, Charset.defaultCharset()));

    // Indicate an error in the exit code.
    if (hadError) System.exit(65);
```

#### 59. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    if (hadRuntimeError) System.exit(70);
```

#### 60. 7 . 4 . 1 Reporting runtime errors — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  }
```

#### 61. 7 . 4 . 2 Running the interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
public class Lox {
```

#### 62. 7 . 4 . 2 Running the interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  private static final Interpreter interpreter = new Interpreter();
```

#### 63. 7 . 4 . 2 Running the interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  static boolean hadError = false;
```

#### 64. 7 . 4 . 2 Running the interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    // Stop if there was a syntax error.
    if (hadError) return;

```

#### 65. 7 . 4 . 2 Running the interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
    interpreter.interpret(expression);
```

#### 66. 7 . 4 . 2 Running the interpreter — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
  }
```

#### 67. Design Note: Static and Dynamic Typing — [source](https://craftinginterpreters.com/evaluating-expressions.html)
```
Object[] stuff = new Integer[1];
stuff[0] = "not an int!";
```

