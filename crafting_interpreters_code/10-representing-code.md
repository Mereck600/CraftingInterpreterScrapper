# Representing Code
_From: https://craftinginterpreters.com/representing-code.html_

#### 1. Representing Code — [source](https://craftinginterpreters.com/representing-code.html)
```
1 + 2 * 3 - 4
```

#### 2. 5 . 1 . 1 Rules for grammars — [source](https://craftinginterpreters.com/representing-code.html)
```
breakfast  â protein "with" breakfast "on the side" ;
breakfast  â protein ;
breakfast  â bread ;

protein    â crispiness "crispy" "bacon" ;
protein    â "sausage" ;
protein    â cooked "eggs" ;

crispiness â "really" ;
crispiness â "really" crispiness ;

cooked     â "scrambled" ;
cooked     â "poached" ;
cooked     â "fried" ;

bread      â "toast" ;
bread      â "biscuits" ;
bread      â "English muffin" ;
```

#### 3. 5 . 1 . 1 Rules for grammars — [source](https://craftinginterpreters.com/representing-code.html)
```
protein "with" breakfast "on the side"
```

#### 4. 5 . 1 . 1 Rules for grammars — [source](https://craftinginterpreters.com/representing-code.html)
```
protein â cooked "eggs" ;
```

#### 5. 5 . 1 . 1 Rules for grammars — [source](https://craftinginterpreters.com/representing-code.html)
```
"poached" "eggs" "with" breakfast "on the side"
```

#### 6. 5 . 1 . 2 Enhancing our notation — [source](https://craftinginterpreters.com/representing-code.html)
```
bread â "toast" | "biscuits" | "English muffin" ;
```

#### 7. 5 . 1 . 2 Enhancing our notation — [source](https://craftinginterpreters.com/representing-code.html)
```
protein â ( "scrambled" | "poached" | "fried" ) "eggs" ;
```

#### 8. 5 . 1 . 2 Enhancing our notation — [source](https://craftinginterpreters.com/representing-code.html)
```
crispiness â "really" "really"* ;
```

#### 9. 5 . 1 . 2 Enhancing our notation — [source](https://craftinginterpreters.com/representing-code.html)
```
crispiness â "really"+ ;
```

#### 10. 5 . 1 . 2 Enhancing our notation — [source](https://craftinginterpreters.com/representing-code.html)
```
breakfast â protein ( "with" breakfast "on the side" )? ;
```

#### 11. 5 . 1 . 2 Enhancing our notation — [source](https://craftinginterpreters.com/representing-code.html)
```
breakfast â protein ( "with" breakfast "on the side" )?
          | bread ;

protein   â "really"+ "crispy" "bacon"
          | "sausage"
          | ( "scrambled" | "poached" | "fried" ) "eggs" ;

bread     â "toast" | "biscuits" | "English muffin" ;
```

#### 12. 5 . 1 . 3 A Grammar for Lox expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
1 - (2 * 3) < 4 == false
```

#### 13. 5 . 1 . 3 A Grammar for Lox expressions — [source](https://craftinginterpreters.com/representing-code.html)
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

#### 14. 5 . 2 Implementing Syntax Trees — [source](https://craftinginterpreters.com/representing-code.html)
```java
package com.craftinginterpreters.lox;

abstract class Expr { 
  static class Binary extends Expr {
    Binary(Expr left, Token operator, Expr right) {
      this.left = left;
      this.operator = operator;
      this.right = right;
    }

    final Expr left;
    final Token operator;
    final Expr right;
  }

  // Other expressions...
}
```

#### 15. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```java
package com.craftinginterpreters.tool;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.List;

public class GenerateAst {
  public static void main(String[] args) throws IOException {
    if (args.length != 1) {
      System.err.println("Usage: generate_ast <output directory>");
      System.exit(64);
    }
    String outputDir = args[0];
  }
}
```

#### 16. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
    String outputDir = args[0];
```

#### 17. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
    defineAst(outputDir, "Expr", Arrays.asList(
      "Binary   : Expr left, Token operator, Expr right",
      "Grouping : Expr expression",
      "Literal  : Object value",
      "Unary    : Token operator, Expr right"
    ));
```

#### 18. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
  }
```

#### 19. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
  private static void defineAst(
      String outputDir, String baseName, List<String> types)
      throws IOException {
    String path = outputDir + "/" + baseName + ".java";
    PrintWriter writer = new PrintWriter(path, "UTF-8");

    writer.println("package com.craftinginterpreters.lox;");
    writer.println();
    writer.println("import java.util.List;");
    writer.println();
    writer.println("abstract class " + baseName + " {");

    writer.println("}");
    writer.close();
  }
```

#### 20. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
    writer.println("abstract class " + baseName + " {");

```

#### 21. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
    // The AST classes.
    for (String type : types) {
      String className = type.split(":")[0].trim();
      String fields = type.split(":")[1].trim(); 
      defineType(writer, baseName, className, fields);
    }
```

#### 22. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
    writer.println("}");
```

#### 23. 5 . 2 . 2 Metaprogramming the trees — [source](https://craftinginterpreters.com/representing-code.html)
```
  private static void defineType(
      PrintWriter writer, String baseName,
      String className, String fieldList) {
    writer.println("  static class " + className + " extends " +
        baseName + " {");

    // Constructor.
    writer.println("    " + className + "(" + fieldList + ") {");

    // Store parameters in fields.
    String[] fields = fieldList.split(", ");
    for (String field : fields) {
      String name = field.split(" ")[1];
      writer.println("      this." + name + " = " + name + ";");
    }

    writer.println("    }");

    // Fields.
    writer.println();
    for (String field : fields) {
      writer.println("    final " + field + ";");
    }

    writer.println("  }");
  }
```

#### 24. 5 . 3 Working with Trees — [source](https://craftinginterpreters.com/representing-code.html)
```
if (expr instanceof Expr.Binary) {
  // ...
} else if (expr instanceof Expr.Grouping) {
  // ...
} else // ...
```

#### 25. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  abstract class Pastry {
  }

  class Beignet extends Pastry {
  }

  class Cruller extends Pastry {
  }
```

#### 26. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  interface PastryVisitor {
    void visitBeignet(Beignet beignet); 
    void visitCruller(Cruller cruller);
  }
```

#### 27. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  abstract class Pastry {
```

#### 28. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
    abstract void accept(PastryVisitor visitor);
```

#### 29. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  }
```

#### 30. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  class Beignet extends Pastry {
```

#### 31. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
    @Override
    void accept(PastryVisitor visitor) {
      visitor.visitBeignet(this);
    }
```

#### 32. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  }
```

#### 33. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  class Cruller extends Pastry {
```

#### 34. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
    @Override
    void accept(PastryVisitor visitor) {
      visitor.visitCruller(this);
    }
```

#### 35. 5 . 3 . 2 The Visitor pattern — [source](https://craftinginterpreters.com/representing-code.html)
```
  }
```

#### 36. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
    writer.println("abstract class " + baseName + " {");

```

#### 37. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
    defineVisitor(writer, baseName, types);

```

#### 38. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
    // The AST classes.
```

#### 39. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
  private static void defineVisitor(
      PrintWriter writer, String baseName, List<String> types) {
    writer.println("  interface Visitor<R> {");

    for (String type : types) {
      String typeName = type.split(":")[0].trim();
      writer.println("    R visit" + typeName + baseName + "(" +
          typeName + " " + baseName.toLowerCase() + ");");
    }

    writer.println("  }");
  }
```

#### 40. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
      defineType(writer, baseName, className, fields);
    }
```

#### 41. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```


    // The base accept() method.
    writer.println();
    writer.println("  abstract <R> R accept(Visitor<R> visitor);");

```

#### 42. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
    writer.println("}");
```

#### 43. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```
    writer.println("    }");
```

#### 44. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```


    // Visitor pattern.
    writer.println();
    writer.println("    @Override");
    writer.println("    <R> R accept(Visitor<R> visitor) {");
    writer.println("      return visitor.visit" +
        className + baseName + "(this);");
    writer.println("    }");
```

#### 45. 5 . 3 . 3 Visitors for expressions — [source](https://craftinginterpreters.com/representing-code.html)
```


    // Fields.
```

#### 46. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
(* (- 123) (group 45.67))
```

#### 47. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```lox
package com.craftinginterpreters.lox;

class AstPrinter implements Expr.Visitor<String> {
  String print(Expr expr) {
    return expr.accept(this);
  }
}
```

#### 48. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
    return expr.accept(this);
  }
```

#### 49. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```


  @Override
  public String visitBinaryExpr(Expr.Binary expr) {
    return parenthesize(expr.operator.lexeme,
                        expr.left, expr.right);
  }

  @Override
  public String visitGroupingExpr(Expr.Grouping expr) {
    return parenthesize("group", expr.expression);
  }

  @Override
  public String visitLiteralExpr(Expr.Literal expr) {
    if (expr.value == null) return "nil";
    return expr.value.toString();
  }

  @Override
  public String visitUnaryExpr(Expr.Unary expr) {
    return parenthesize(expr.operator.lexeme, expr.right);
  }
```

#### 50. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
}
```

#### 51. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
  private String parenthesize(String name, Expr... exprs) {
    StringBuilder builder = new StringBuilder();

    builder.append("(").append(name);
    for (Expr expr : exprs) {
      builder.append(" ");
      builder.append(expr.accept(this));
    }
    builder.append(")");

    return builder.toString();
  }
```

#### 52. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
(+ 1 2)
```

#### 53. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
  public static void main(String[] args) {
    Expr expression = new Expr.Binary(
        new Expr.Unary(
            new Token(TokenType.MINUS, "-", null, 1),
            new Expr.Literal(123)),
        new Token(TokenType.STAR, "*", null, 1),
        new Expr.Grouping(
            new Expr.Literal(45.67)));

    System.out.println(new AstPrinter().print(expression));
  }
```

#### 54. 5 . 4 A (Not Very) Pretty Printer — [source](https://craftinginterpreters.com/representing-code.html)
```
(* (- 123) (group 45.67))
```

#### 55. Challenges — [source](https://craftinginterpreters.com/representing-code.html)
```
expr â expr ( "(" ( expr ( "," expr )* )? ")" | "." IDENTIFIER )+
     | IDENTIFIER
     | NUMBER
```

#### 56. Challenges — [source](https://craftinginterpreters.com/representing-code.html)
```
(1 + 2) * (4 - 3)
```

#### 57. Challenges — [source](https://craftinginterpreters.com/representing-code.html)
```
1 2 + 4 3 - *
```

