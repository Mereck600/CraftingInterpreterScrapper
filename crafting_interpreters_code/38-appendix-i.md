# Appendix I
_From: https://craftinginterpreters.com/appendix-i.html_

#### 1. A1 . 1 Syntax Grammar — [source](https://craftinginterpreters.com/appendix-i.html)
```
program        â declaration* EOF ;
```

#### 2. A1 . 1 . 1 Declarations — [source](https://craftinginterpreters.com/appendix-i.html)
```
declaration    â classDecl
               | funDecl
               | varDecl
               | statement ;

classDecl      â "class" IDENTIFIER ( "<" IDENTIFIER )?
                 "{" function* "}" ;
funDecl        â "fun" function ;
varDecl        â "var" IDENTIFIER ( "=" expression )? ";" ;
```

#### 3. A1 . 1 . 2 Statements — [source](https://craftinginterpreters.com/appendix-i.html)
```
statement      â exprStmt
               | forStmt
               | ifStmt
               | printStmt
               | returnStmt
               | whileStmt
               | block ;

exprStmt       â expression ";" ;
forStmt        â "for" "(" ( varDecl | exprStmt | ";" )
                           expression? ";"
                           expression? ")" statement ;
ifStmt         â "if" "(" expression ")" statement
                 ( "else" statement )? ;
printStmt      â "print" expression ";" ;
returnStmt     â "return" expression? ";" ;
whileStmt      â "while" "(" expression ")" statement ;
block          â "{" declaration* "}" ;
```

#### 4. A1 . 1 . 3 Expressions — [source](https://craftinginterpreters.com/appendix-i.html)
```
expression     â assignment ;

assignment     â ( call "." )? IDENTIFIER "=" assignment
               | logic_or ;

logic_or       â logic_and ( "or" logic_and )* ;
logic_and      â equality ( "and" equality )* ;
equality       â comparison ( ( "!=" | "==" ) comparison )* ;
comparison     â term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           â factor ( ( "-" | "+" ) factor )* ;
factor         â unary ( ( "/" | "*" ) unary )* ;

unary          â ( "!" | "-" ) unary | call ;
call           â primary ( "(" arguments? ")" | "." IDENTIFIER )* ;
primary        â "true" | "false" | "nil" | "this"
               | NUMBER | STRING | IDENTIFIER | "(" expression ")"
               | "super" "." IDENTIFIER ;
```

#### 5. A1 . 1 . 4 Utility rules — [source](https://craftinginterpreters.com/appendix-i.html)
```
function       â IDENTIFIER "(" parameters? ")" block ;
parameters     â IDENTIFIER ( "," IDENTIFIER )* ;
arguments      â expression ( "," expression )* ;
```

#### 6. A1 . 2 Lexical Grammar — [source](https://craftinginterpreters.com/appendix-i.html)
```
NUMBER         â DIGIT+ ( "." DIGIT+ )? ;
STRING         â "\"" <any char except "\"">* "\"" ;
IDENTIFIER     â ALPHA ( ALPHA | DIGIT )* ;
ALPHA          â "a" ... "z" | "A" ... "Z" | "_" ;
DIGIT          â "0" ... "9" ;
```

