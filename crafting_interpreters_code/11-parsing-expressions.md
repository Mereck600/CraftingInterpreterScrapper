# Parsing Expressions
_From: https://craftinginterpreters.com/parsing-expressions.html_

#### 1. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
expression     â literal
               | unary
               | binary
               | grouping ;

literal        â NUMBER | STRING | "true" | "false" | "nil" ;
grouping       â "(" expression ")" ;
unary          â ( "-" | "!" ) expression ;
binary         â expression operator expression ;
operator       â "==" | "!=" | "<" | "<=" | ">" | ">="
               | "+"  | "-"  | "*" | "/" ;
```

#### 2. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
5 - 3 - 1
```

#### 3. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
(5 - 3) - 1
```

#### 4. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
a = b = c
```

#### 5. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
a = (b = c)
```

#### 6. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
expression     â ...
equality       â ...
comparison     â ...
term           â ...
factor         â ...
unary          â ...
primary        â ...
```

#### 7. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
expression     â equality
```

#### 8. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
primary        â NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" ;
```

#### 9. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
unary          â ( "!" | "-" ) unary ;
```

#### 10. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
unary          â ( "!" | "-" ) unary
               | primary ;
```

#### 11. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
factor         â factor ( "/" | "*" ) unary
               | unary ;
```

#### 12. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
print 0.1 * (0.2 * 0.3);
print (0.1 * 0.2) * 0.3;
```

#### 13. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
factor         â unary ( ( "/" | "*" ) unary )* ;
```

#### 14. 6 . 1 Ambiguity and the Parsing Game — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
expression     â equality ;
equality       â comparison ( ( "!=" | "==" ) comparison )* ;
comparison     â term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           â factor ( ( "-" | "+" ) factor )* ;
factor         â unary ( ( "/" | "*" ) unary )* ;
unary          â ( "!" | "-" ) unary
               | primary ;
primary        â NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" ;
```

#### 15. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```java
package com.craftinginterpreters.lox;

import java.util.List;

import static com.craftinginterpreters.lox.TokenType.*;

class Parser {
  private final List<Token> tokens;
  private int current = 0;

  Parser(List<Token> tokens) {
    this.tokens = tokens;
  }
}
```

#### 16. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr expression() {
    return equality();
  }
```

#### 17. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
equality       â comparison ( ( "!=" | "==" ) comparison )* ;
```

#### 18. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr equality() {
    Expr expr = comparison();

    while (match(BANG_EQUAL, EQUAL_EQUAL)) {
      Token operator = previous();
      Expr right = comparison();
      expr = new Expr.Binary(expr, operator, right);
    }

    return expr;
  }
```

#### 19. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private boolean match(TokenType... types) {
    for (TokenType type : types) {
      if (check(type)) {
        advance();
        return true;
      }
    }

    return false;
  }
```

#### 20. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private boolean check(TokenType type) {
    if (isAtEnd()) return false;
    return peek().type == type;
  }
```

#### 21. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Token advance() {
    if (!isAtEnd()) current++;
    return previous();
  }
```

#### 22. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private boolean isAtEnd() {
    return peek().type == EOF;
  }

  private Token peek() {
    return tokens.get(current);
  }

  private Token previous() {
    return tokens.get(current - 1);
  }
```

#### 23. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
comparison     â term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
```

#### 24. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr comparison() {
    Expr expr = term();

    while (match(GREATER, GREATER_EQUAL, LESS, LESS_EQUAL)) {
      Token operator = previous();
      Expr right = term();
      expr = new Expr.Binary(expr, operator, right);
    }

    return expr;
  }
```

#### 25. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr term() {
    Expr expr = factor();

    while (match(MINUS, PLUS)) {
      Token operator = previous();
      Expr right = factor();
      expr = new Expr.Binary(expr, operator, right);
    }

    return expr;
  }
```

#### 26. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr factor() {
    Expr expr = unary();

    while (match(SLASH, STAR)) {
      Token operator = previous();
      Expr right = unary();
      expr = new Expr.Binary(expr, operator, right);
    }

    return expr;
  }
```

#### 27. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
unary          â ( "!" | "-" ) unary
               | primary ;
```

#### 28. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr unary() {
    if (match(BANG, MINUS)) {
      Token operator = previous();
      Expr right = unary();
      return new Expr.Unary(operator, right);
    }

    return primary();
  }
```

#### 29. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
primary        â NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" ;
```

#### 30. 6 . 2 . 1 The parser class — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Expr primary() {
    if (match(FALSE)) return new Expr.Literal(false);
    if (match(TRUE)) return new Expr.Literal(true);
    if (match(NIL)) return new Expr.Literal(null);

    if (match(NUMBER, STRING)) {
      return new Expr.Literal(previous().literal);
    }

    if (match(LEFT_PAREN)) {
      Expr expr = expression();
      consume(RIGHT_PAREN, "Expect ')' after expression.");
      return new Expr.Grouping(expr);
    }
  }
```

#### 31. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private Token consume(TokenType type, String message) {
    if (check(type)) return advance();

    throw error(peek(), message);
  }
```

#### 32. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private ParseError error(Token token, String message) {
    Lox.error(token, message);
    return new ParseError();
  }
```

#### 33. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  static void error(Token token, String message) {
    if (token.type == TokenType.EOF) {
      report(token.line, " at end", message);
    } else {
      report(token.line, " at '" + token.lexeme + "'", message);
    }
  }
```

#### 34. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
class Parser {
```

#### 35. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private static class ParseError extends RuntimeException {}

```

#### 36. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private final List<Token> tokens;
```

#### 37. 6 . 3 . 2 Entering panic mode — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
unary â ( "!" | "-" | "+" ) unary
      | primary ;
```

#### 38. 6 . 3 . 3 Synchronizing a recursive descent parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  private void synchronize() {
    advance();

    while (!isAtEnd()) {
      if (previous().type == SEMICOLON) return;

      switch (peek().type) {
        case CLASS:
        case FUN:
        case VAR:
        case FOR:
        case IF:
        case WHILE:
        case PRINT:
        case RETURN:
          return;
      }

      advance();
    }
  }
```

#### 39. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
    if (match(LEFT_PAREN)) {
      Expr expr = expression();
      consume(RIGHT_PAREN, "Expect ')' after expression.");
      return new Expr.Grouping(expr);
    }
```

#### 40. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```


    throw error(peek(), "Expect expression.");
```

#### 41. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  }
```

#### 42. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  Expr parse() {
    try {
      return expression();
    } catch (ParseError error) {
      return null;
    }
  }
```

#### 43. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
    List<Token> tokens = scanner.scanTokens();
```

#### 44. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
    Parser parser = new Parser(tokens);
    Expr expression = parser.parse();

    // Stop if there was a syntax error.
    if (hadError) return;

    System.out.println(new AstPrinter().print(expression));
```

#### 45. 6 . 4 Wiring up the Parser — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
  }
```

#### 46. Design Note: Logic Versus History — [source](https://craftinginterpreters.com/parsing-expressions.html)
```
if (flags & FLAG_MASK == SOME_FLAG) { ... } // Wrong.
if ((flags & FLAG_MASK) == SOME_FLAG) { ... } // Right.
```

