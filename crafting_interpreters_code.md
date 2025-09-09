# Old code ignore this 
# Crafting Interpreters — Collected Code Blocks

> Collected automatically from the online book. Each snippet is annotated with Chapter, Section, and Source URL.

_Total snippets: 2121_

---

### 1. Introduction — 1 . 2 . 2 Snippets

**Source:** https://craftinginterpreters.com/introduction.html

```

      default:
```

---

### 2. Introduction — 1 . 2 . 2 Snippets

**Source:** https://craftinginterpreters.com/introduction.html

```

        
if
 (
isDigit
(
c
)) {
          
number
();
        } 
else
 {
          
Lox
.
error
(
line
, 
"Unexpected character."
);
        }
```

---

### 3. Introduction — 1 . 2 . 2 Snippets

**Source:** https://craftinginterpreters.com/introduction.html

```

        break;
```

---

### 4. A Map of the Territory — 2 . 1 . 5 Optimization

**Source:** https://craftinginterpreters.com/a-map-of-the-territory.html

```
pennyArea
 = 
3.14159
 * (
0.75
 / 
2
) * (
0.75
 / 
2
);
```

---

### 5. A Map of the Territory — 2 . 1 . 5 Optimization

**Source:** https://craftinginterpreters.com/a-map-of-the-territory.html

```
pennyArea
 = 
0.4417860938
;
```

---

### 6. The Lox Language — 3 . 1 Hello, Lox

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
// Your first Lox program!


print
 
"Hello, world!"
;
```

---

### 7. The Lox Language — 3 . 3 Data Types

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
true
;  
// Not false.


false
; 
// Not *not* false.
```

---

### 8. The Lox Language — 3 . 3 Data Types

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
1234
;  
// An integer.


12.34
; 
// A decimal number.
```

---

### 9. The Lox Language — 3 . 3 Data Types

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
"I am a string"
;

""
;    
// The empty string.


"123"
; 
// This is a string, not a number.
```

---

### 10. The Lox Language — 3 . 4 . 1 Arithmetic

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
add
 + 
me
;

subtract
 - 
me
;

multiply
 * 
me
;

divide
 / 
me
;
```

---

### 11. The Lox Language — 3 . 4 . 1 Arithmetic

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
condition
 ? 
thenArm
 : 
elseArm
;
```

---

### 12. The Lox Language — 3 . 4 . 1 Arithmetic

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
-
negateMe
;
```

---

### 13. The Lox Language — 3 . 4 . 2 Comparison and equality

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
less
 < 
than
;

lessThan
 <= 
orEqual
;

greater
 > 
than
;

greaterThan
 >= 
orEqual
;
```

---

### 14. The Lox Language — 3 . 4 . 2 Comparison and equality

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
1
 == 
2
;         
// false.


"cat"
 != 
"dog"
; 
// true.
```

---

### 15. The Lox Language — 3 . 4 . 2 Comparison and equality

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
314
 == 
"pi"
; 
// false.
```

---

### 16. The Lox Language — 3 . 4 . 2 Comparison and equality

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
123
 == 
"123"
; 
// false.
```

---

### 17. The Lox Language — 3 . 4 . 3 Logical operators

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
!
true
;  
// false.

!
false
; 
// true.
```

---

### 18. The Lox Language — 3 . 4 . 3 Logical operators

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
true
 
and
 
false
; 
// false.


true
 
and
 
true
;  
// true.
```

---

### 19. The Lox Language — 3 . 4 . 3 Logical operators

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
false
 
or
 
false
; 
// false.


true
 
or
 
false
;  
// true.
```

---

### 20. The Lox Language — 3 . 4 . 4 Precedence and grouping

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
var
 
average
 = (
min
 + 
max
) / 
2
;
```

---

### 21. The Lox Language — 3 . 5 Statements

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
print
 
"Hello, world!"
;
```

---

### 22. The Lox Language — 3 . 5 Statements

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
"some expression"
;
```

---

### 23. The Lox Language — 3 . 5 Statements

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
{
  
print
 
"One statement."
;
  
print
 
"Two statements."
;
}
```

---

### 24. The Lox Language — 3 . 6 Variables

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
var
 
imAVariable
 = 
"here is my value"
;

var
 
iAmNil
;
```

---

### 25. The Lox Language — 3 . 6 Variables

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
var
 
breakfast
 = 
"bagels"
;

print
 
breakfast
; 
// "bagels".


breakfast
 = 
"beignets"
;

print
 
breakfast
; 
// "beignets".
```

---

### 26. The Lox Language — 3 . 7 Control Flow

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
if
 (
condition
) {
  
print
 
"yes"
;
} 
else
 {
  
print
 
"no"
;
}
```

---

### 27. The Lox Language — 3 . 7 Control Flow

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
var
 
a
 = 
1
;

while
 (
a
 < 
10
) {
  
print
 
a
;
  
a
 = 
a
 + 
1
;
}
```

---

### 28. The Lox Language — 3 . 7 Control Flow

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
for
 (
var
 
a
 = 
1
; 
a
 < 
10
; 
a
 = 
a
 + 
1
) {
  
print
 
a
;
}
```

---

### 29. The Lox Language — 3 . 8 Functions

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
makeBreakfast
(
bacon
, 
eggs
, 
toast
);
```

---

### 30. The Lox Language — 3 . 8 Functions

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
makeBreakfast
();
```

---

### 31. The Lox Language — 3 . 8 Functions

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
fun
 
printSum
(
a
, 
b
) {
  
print
 
a
 + 
b
;
}
```

---

### 32. The Lox Language — 3 . 8 Functions

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
fun
 
returnSum
(
a
, 
b
) {
  
return
 
a
 + 
b
;
}
```

---

### 33. The Lox Language — 3 . 8 . 1 Closures

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
fun
 
addPair
(
a
, 
b
) {
  
return
 
a
 + 
b
;
}


fun
 
identity
(
a
) {
  
return
 
a
;
}


print
 
identity
(
addPair
)(
1
, 
2
); 
// Prints "3".
```

---

### 34. The Lox Language — 3 . 8 . 1 Closures

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
fun
 
outerFunction
() {
  
fun
 
localFunction
() {
    
print
 
"I'm local!"
;
  }

  
localFunction
();
}
```

---

### 35. The Lox Language — 3 . 8 . 1 Closures

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
fun
 
returnFunction
() {
  
var
 
outside
 = 
"outside"
;

  
fun
 
inner
() {
    
print
 
outside
;
  }

  
return
 
inner
;
}


var
 
fn
 = 
returnFunction
();

fn
();
```

---

### 36. The Lox Language — 3 . 9 . 4 Classes in Lox

**Source:** https://craftinginterpreters.com/the-lox-language.html

```java
class
 
Breakfast
 {
  
cook
() {
    
print
 
"Eggs a-fryin'!"
;
  }

  
serve
(
who
) {
    
print
 
"Enjoy your breakfast, "
 + 
who
 + 
"."
;
  }
}
```

---

### 37. The Lox Language — 3 . 9 . 4 Classes in Lox

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
// Store it in variables.


var
 
someVariable
 = 
Breakfast
;


// Pass it to functions.


someFunction
(
Breakfast
);
```

---

### 38. The Lox Language — 3 . 9 . 4 Classes in Lox

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
var
 
breakfast
 = 
Breakfast
();

print
 
breakfast
; 
// "Breakfast instance".
```

---

### 39. The Lox Language — 3 . 9 . 5 Instantiation and initialization

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
breakfast
.
meat
 = 
"sausage"
;

breakfast
.
bread
 = 
"sourdough"
;
```

---

### 40. The Lox Language — 3 . 9 . 5 Instantiation and initialization

**Source:** https://craftinginterpreters.com/the-lox-language.html

```java
class
 
Breakfast
 {
  
serve
(
who
) {
    
print
 
"Enjoy your "
 + 
this
.
meat
 + 
" and "
 +
        
this
.
bread
 + 
", "
 + 
who
 + 
"."
;
  }

  
// ...

}
```

---

### 41. The Lox Language — 3 . 9 . 5 Instantiation and initialization

**Source:** https://craftinginterpreters.com/the-lox-language.html

```java
class
 
Breakfast
 {
  
init
(
meat
, 
bread
) {
    
this
.
meat
 = 
meat
;
    
this
.
bread
 = 
bread
;
  }

  
// ...

}


var
 
baconAndToast
 = 
Breakfast
(
"bacon"
, 
"toast"
);

baconAndToast
.
serve
(
"Dear Reader"
);

// "Enjoy your bacon and toast, Dear Reader."
```

---

### 42. The Lox Language — 3 . 9 . 6 Inheritance

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
class
 
Brunch
 < 
Breakfast
 {
  
drink
() {
    
print
 
"How about a Bloody Mary?"
;
  }
}
```

---

### 43. The Lox Language — 3 . 9 . 6 Inheritance

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
var
 
benedict
 = 
Brunch
(
"ham"
, 
"English muffin"
);

benedict
.
serve
(
"Noble Reader"
);
```

---

### 44. The Lox Language — 3 . 9 . 6 Inheritance

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
class
 
Brunch
 < 
Breakfast
 {
  
init
(
meat
, 
bread
, 
drink
) {
    
super
.
init
(
meat
, 
bread
);
    
this
.
drink
 = 
drink
;
  }
}
```

---

### 45. The Lox Language — Design Note: Expressions and Statements

**Source:** https://craftinginterpreters.com/the-lox-language.html

```
puts
 
1
 + 
if
 
true
 
then
 
2
 
else
 
3
 
end
 + 
4
```

---

### 46. Scanning — 4 . 1 The Interpreter Framework

**Source:** https://craftinginterpreters.com/scanning.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.io.BufferedReader
;

import
 
java.io.IOException
;

import
 
java.io.InputStreamReader
;

import
 
java.nio.charset.Charset
;

import
 
java.nio.file.Files
;

import
 
java.nio.file.Paths
;

import
 
java.util.List
;


public
 
class
 
Lox
 {
  
public
 
static
 
void
 
main
(
String
[] 
args
) 
throws
 
IOException
 {
    
if
 (
args
.
length
 > 
1
) {
      
System
.
out
.
println
(
"Usage: jlox [script]"
);
      
System
.
exit
(
64
);
 

    } 
else
 
if
 (
args
.
length
 == 
1
) {
      
runFile
(
args
[
0
]);
    } 
else
 {
      
runPrompt
();
    }
  }
}
```

---

### 47. Scanning — 4 . 1 The Interpreter Framework

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
static
 
void
 
runFile
(
String
 
path
) 
throws
 
IOException
 {
    
byte
[] 
bytes
 = 
Files
.
readAllBytes
(
Paths
.
get
(
path
));
    
run
(
new
 
String
(
bytes
, 
Charset
.
defaultCharset
()));
  }
```

---

### 48. Scanning — 4 . 1 The Interpreter Framework

**Source:** https://craftinginterpreters.com/scanning.html

```
(
print
 (
eval
 (
read
)))
```

---

### 49. Scanning — 4 . 1 The Interpreter Framework

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
static
 
void
 
runPrompt
() 
throws
 
IOException
 {
    
InputStreamReader
 
input
 = 
new
 
InputStreamReader
(
System
.
in
);
    
BufferedReader
 
reader
 = 
new
 
BufferedReader
(
input
);

    
for
 (;;) {
 

      
System
.
out
.
print
(
"> "
);
      
String
 
line
 = 
reader
.
readLine
();
      
if
 (
line
 == 
null
) 
break
;
      
run
(
line
);
    }
  }
```

---

### 50. Scanning — 4 . 1 The Interpreter Framework

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
static
 
void
 
run
(
String
 
source
) {
    
Scanner
 
scanner
 = 
new
 
Scanner
(
source
);
    
List
<
Token
> 
tokens
 = 
scanner
.
scanTokens
();

    
// For now, just print the tokens.

    
for
 (
Token
 
token
 : 
tokens
) {
      
System
.
out
.
println
(
token
);
    }
  }
```

---

### 51. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```
  
static
 
void
 
error
(
int
 
line
, 
String
 
message
) {
    
report
(
line
, 
""
, 
message
);
  }

  
private
 
static
 
void
 
report
(
int
 
line
, 
String
 
where
,
                             
String
 
message
) {
    
System
.
err
.
println
(
        
"[line "
 + 
line
 + 
"] Error"
 + 
where
 + 
": "
 + 
message
);
    
hadError
 = 
true
;
  }
```

---

### 52. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```
Error: Unexpected "," somewhere in your code. Good luck finding it!
```

---

### 53. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```
Error: Unexpected "," in argument list.

    15 | function(first, second,);
                               ^-- Here.
```

---

### 54. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```
  
static
 
boolean
 
hadError
 = 
false
;
```

---

### 55. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```
    run(new String(bytes, Charset.defaultCharset()));
```

---

### 56. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```


    
// Indicate an error in the exit code.

    
if
 (
hadError
) 
System
.
exit
(
65
);
```

---

### 57. Scanning — 4 . 1 . 1 Error handling

**Source:** https://craftinginterpreters.com/scanning.html

```
      
hadError
 = 
false
;
```

---

### 58. Scanning — 4 . 2 Lexemes and Tokens

**Source:** https://craftinginterpreters.com/scanning.html

```lox
var
 
language
 = 
"lox"
;
```

---

### 59. Scanning — 4 . 2 . 1 Token type

**Source:** https://craftinginterpreters.com/scanning.html

```
package
 
com.craftinginterpreters.lox
;


enum
 
TokenType
 {
  
// Single-character tokens.

  
LEFT_PAREN
, 
RIGHT_PAREN
, 
LEFT_BRACE
, 
RIGHT_BRACE
,
  
COMMA
, 
DOT
, 
MINUS
, 
PLUS
, 
SEMICOLON
, 
SLASH
, 
STAR
,

  
// One or two character tokens.

  
BANG
, 
BANG_EQUAL
,
  
EQUAL
, 
EQUAL_EQUAL
,
  
GREATER
, 
GREATER_EQUAL
,
  
LESS
, 
LESS_EQUAL
,

  
// Literals.

  
IDENTIFIER
, 
STRING
, 
NUMBER
,

  
// Keywords.

  
AND
, 
CLASS
, 
ELSE
, 
FALSE
, 
FUN
, 
FOR
, 
IF
, 
NIL
, 
OR
,
  
PRINT
, 
RETURN
, 
SUPER
, 
THIS
, 
TRUE
, 
VAR
, 
WHILE
,

  
EOF

}
```

---

### 60. Scanning — 4 . 2 . 3 Location information

**Source:** https://craftinginterpreters.com/scanning.html

```java
package
 
com.craftinginterpreters.lox
;


class
 
Token
 {
  
final
 
TokenType
 
type
;
  
final
 
String
 
lexeme
;
  
final
 
Object
 
literal
;
  
final
 
int
 
line
;
 


  
Token
(
TokenType
 
type
, 
String
 
lexeme
, 
Object
 
literal
, 
int
 
line
) {
    
this
.
type
 = 
type
;
    
this
.
lexeme
 = 
lexeme
;
    
this
.
literal
 = 
literal
;
    
this
.
line
 = 
line
;
  }

  
public
 
String
 
toString
() {
    
return
 
type
 + 
" "
 + 
lexeme
 + 
" "
 + 
literal
;
  }
}
```

---

### 61. Scanning — 4 . 4 The Scanner Class

**Source:** https://craftinginterpreters.com/scanning.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.ArrayList
;

import
 
java.util.HashMap
;

import
 
java.util.List
;

import
 
java.util.Map
;


import static
 
com.craftinginterpreters.lox.TokenType.*
;
 



class
 
Scanner
 {
  
private
 
final
 
String
 
source
;
  
private
 
final
 
List
<
Token
> 
tokens
 = 
new
 
ArrayList
<>();

  
Scanner
(
String
 
source
) {
    
this
.
source
 = 
source
;
  }
}
```

---

### 62. Scanning — 4 . 4 The Scanner Class

**Source:** https://craftinginterpreters.com/scanning.html

```
  
List
<
Token
> 
scanTokens
() {
    
while
 (!
isAtEnd
()) {
      
// We are at the beginning of the next lexeme.

      
start
 = 
current
;
      
scanToken
();
    }

    
tokens
.
add
(
new
 
Token
(
EOF
, 
""
, 
null
, 
line
));
    
return
 
tokens
;
  }
```

---

### 63. Scanning — 4 . 4 The Scanner Class

**Source:** https://craftinginterpreters.com/scanning.html

```
  private final List<Token> tokens = new ArrayList<>();
```

---

### 64. Scanning — 4 . 4 The Scanner Class

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
int
 
start
 = 
0
;
  
private
 
int
 
current
 = 
0
;
  
private
 
int
 
line
 = 
1
;
```

---

### 65. Scanning — 4 . 4 The Scanner Class

**Source:** https://craftinginterpreters.com/scanning.html

```


  Scanner(String source) {
```

---

### 66. Scanning — 4 . 4 The Scanner Class

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
boolean
 
isAtEnd
() {
    
return
 
current
 >= 
source
.
length
();
  }
```

---

### 67. Scanning — 4 . 5 Recognizing Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
void
 
scanToken
() {
    
char
 
c
 = 
advance
();
    
switch
 (
c
) {
      
case
 
'('
: 
addToken
(
LEFT_PAREN
); 
break
;
      
case
 
')'
: 
addToken
(
RIGHT_PAREN
); 
break
;
      
case
 
'{'
: 
addToken
(
LEFT_BRACE
); 
break
;
      
case
 
'}'
: 
addToken
(
RIGHT_BRACE
); 
break
;
      
case
 
','
: 
addToken
(
COMMA
); 
break
;
      
case
 
'.'
: 
addToken
(
DOT
); 
break
;
      
case
 
'-'
: 
addToken
(
MINUS
); 
break
;
      
case
 
'+'
: 
addToken
(
PLUS
); 
break
;
      
case
 
';'
: 
addToken
(
SEMICOLON
); 
break
;
      
case
 
'*'
: 
addToken
(
STAR
); 
break
;
 

    }
  }
```

---

### 68. Scanning — 4 . 5 Recognizing Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
char
 
advance
() {
    
return
 
source
.
charAt
(
current
++);
  }

  
private
 
void
 
addToken
(
TokenType
 
type
) {
    
addToken
(
type
, 
null
);
  }

  
private
 
void
 
addToken
(
TokenType
 
type
, 
Object
 
literal
) {
    
String
 
text
 = 
source
.
substring
(
start
, 
current
);
    
tokens
.
add
(
new
 
Token
(
type
, 
text
, 
literal
, 
line
));
  }
```

---

### 69. Scanning — 4 . 5 . 1 Lexical errors

**Source:** https://craftinginterpreters.com/scanning.html

```


      
default
:
        
Lox
.
error
(
line
, 
"Unexpected character."
);
        
break
;
```

---

### 70. Scanning — 4 . 5 . 2 Operators

**Source:** https://craftinginterpreters.com/scanning.html

```
      
case
 
'!'
:
        
addToken
(
match
(
'='
) ? 
BANG_EQUAL
 : 
BANG
);
        
break
;
      
case
 
'='
:
        
addToken
(
match
(
'='
) ? 
EQUAL_EQUAL
 : 
EQUAL
);
        
break
;
      
case
 
'<'
:
        
addToken
(
match
(
'='
) ? 
LESS_EQUAL
 : 
LESS
);
        
break
;
      
case
 
'>'
:
        
addToken
(
match
(
'='
) ? 
GREATER_EQUAL
 : 
GREATER
);
        
break
;
```

---

### 71. Scanning — 4 . 5 . 2 Operators

**Source:** https://craftinginterpreters.com/scanning.html

```


      default:
```

---

### 72. Scanning — 4 . 5 . 2 Operators

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
boolean
 
match
(
char
 
expected
) {
    
if
 (
isAtEnd
()) 
return
 
false
;
    
if
 (
source
.
charAt
(
current
) != 
expected
) 
return
 
false
;

    
current
++;
    
return
 
true
;
  }
```

---

### 73. Scanning — 4 . 6 Longer Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```
      
case
 
'/'
:
        
if
 (
match
(
'/'
)) {
          
// A comment goes until the end of the line.

          
while
 (
peek
() != 
'\n'
 && !
isAtEnd
()) 
advance
();
        } 
else
 {
          
addToken
(
SLASH
);
        }
        
break
;
```

---

### 74. Scanning — 4 . 6 Longer Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```


      default:
```

---

### 75. Scanning — 4 . 6 Longer Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
char
 
peek
() {
    
if
 (
isAtEnd
()) 
return
 
'\0'
;
    
return
 
source
.
charAt
(
current
);
  }
```

---

### 76. Scanning — 4 . 6 Longer Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```


      
case
 
' '
:
      
case
 
'\r'
:
      
case
 
'\t'
:
        
// Ignore whitespace.

        
break
;

      
case
 
'\n'
:
        
line
++;
        
break
;
```

---

### 77. Scanning — 4 . 6 Longer Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```


      default:
        Lox.error(line, "Unexpected character.");
```

---

### 78. Scanning — 4 . 6 Longer Lexemes

**Source:** https://craftinginterpreters.com/scanning.html

```
// this is a comment

(( )){} 
// grouping stuff

!*+-/=<> <= == 
// operators
```

---

### 79. Scanning — 4 . 6 . 1 String literals

**Source:** https://craftinginterpreters.com/scanning.html

```


      
case
 
'"'
: 
string
(); 
break
;
```

---

### 80. Scanning — 4 . 6 . 1 String literals

**Source:** https://craftinginterpreters.com/scanning.html

```


      default:
```

---

### 81. Scanning — 4 . 6 . 1 String literals

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
void
 
string
() {
    
while
 (
peek
() != 
'"'
 && !
isAtEnd
()) {
      
if
 (
peek
() == 
'\n'
) 
line
++;
      
advance
();
    }

    
if
 (
isAtEnd
()) {
      
Lox
.
error
(
line
, 
"Unterminated string."
);
      
return
;
    }

    
// The closing ".

    
advance
();

    
// Trim the surrounding quotes.

    
String
 
value
 = 
source
.
substring
(
start
 + 
1
, 
current
 - 
1
);
    
addToken
(
STRING
, 
value
);
  }
```

---

### 82. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
print
 -
123
.
abs
();
```

---

### 83. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
var
 
n
 = 
123
;

print
 -
n
.
abs
();
```

---

### 84. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
1234


12.34
```

---

### 85. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
.
1234


1234
.
```

---

### 86. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
        
if
 (
isDigit
(
c
)) {
          
number
();
        } 
else
 {
          
Lox
.
error
(
line
, 
"Unexpected character."
);
        }
```

---

### 87. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
boolean
 
isDigit
(
char
 
c
) {
    
return
 
c
 >= 
'0'
 && 
c
 <= 
'9'
;
  }
```

---

### 88. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
void
 
number
() {
    
while
 (
isDigit
(
peek
())) 
advance
();

    
// Look for a fractional part.

    
if
 (
peek
() == 
'.'
 && 
isDigit
(
peekNext
())) {
      
// Consume the "."

      
advance
();

      
while
 (
isDigit
(
peek
())) 
advance
();
    }

    
addToken
(
NUMBER
,
        
Double
.
parseDouble
(
source
.
substring
(
start
, 
current
)));
  }
```

---

### 89. Scanning — 4 . 6 . 2 Number literals

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
char
 
peekNext
() {
    
if
 (
current
 + 
1
 >= 
source
.
length
()) 
return
 
'\0'
;
    
return
 
source
.
charAt
(
current
 + 
1
);
  }
```

---

### 90. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
case
 
'o'
:
  
if
 (
match
(
'r'
)) {
    
addToken
(
OR
);
  }
  
break
;
```

---

### 91. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
---
a
;
```

---

### 92. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
- --
a
;
```

---

### 93. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
-- -
a
;
```

---

### 94. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
      default:
        if (isDigit(c)) {
          number();
```

---

### 95. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
        } 
else
 
if
 (
isAlpha
(
c
)) {
          
identifier
();
```

---

### 96. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
        } else {
          Lox.error(line, "Unexpected character.");
        }
```

---

### 97. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
void
 
identifier
() {
    
while
 (
isAlphaNumeric
(
peek
())) 
advance
();

    
addToken
(
IDENTIFIER
);
  }
```

---

### 98. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
boolean
 
isAlpha
(
char
 
c
) {
    
return
 (
c
 >= 
'a'
 && 
c
 <= 
'z'
) ||
           (
c
 >= 
'A'
 && 
c
 <= 
'Z'
) ||
            
c
 == 
'_'
;
  }

  
private
 
boolean
 
isAlphaNumeric
(
char
 
c
) {
    
return
 
isAlpha
(
c
) || 
isDigit
(
c
);
  }
```

---

### 99. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
  
private
 
static
 
final
 
Map
<
String
, 
TokenType
> 
keywords
;

  
static
 {
    
keywords
 = 
new
 
HashMap
<>();
    
keywords
.
put
(
"and"
,    
AND
);
    
keywords
.
put
(
"class"
,  
CLASS
);
    
keywords
.
put
(
"else"
,   
ELSE
);
    
keywords
.
put
(
"false"
,  
FALSE
);
    
keywords
.
put
(
"for"
,    
FOR
);
    
keywords
.
put
(
"fun"
,    
FUN
);
    
keywords
.
put
(
"if"
,     
IF
);
    
keywords
.
put
(
"nil"
,    
NIL
);
    
keywords
.
put
(
"or"
,     
OR
);
    
keywords
.
put
(
"print"
,  
PRINT
);
    
keywords
.
put
(
"return"
, 
RETURN
);
    
keywords
.
put
(
"super"
,  
SUPER
);
    
keywords
.
put
(
"this"
,   
THIS
);
    
keywords
.
put
(
"true"
,   
TRUE
);
    
keywords
.
put
(
"var"
,    
VAR
);
    
keywords
.
put
(
"while"
,  
WHILE
);
  }
```

---

### 100. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
    while (isAlphaNumeric(peek())) advance();
```

---

### 101. Scanning — 4 . 7 Reserved Words and Identifiers

**Source:** https://craftinginterpreters.com/scanning.html

```
    
String
 
text
 = 
source
.
substring
(
start
, 
current
);
    
TokenType
 
type
 = 
keywords
.
get
(
text
);
    
if
 (
type
 == 
null
) 
type
 = 
IDENTIFIER
;
    
addToken
(
type
);
```

---

### 102. Scanning — Design Note: Implicit Semicolons

**Source:** https://craftinginterpreters.com/scanning.html

```
if
 (
condition
) 
return


"value"
```

---

### 103. Scanning — Design Note: Implicit Semicolons

**Source:** https://craftinginterpreters.com/scanning.html

```
func

(
parenthesized
)
```

---

### 104. Scanning — Design Note: Implicit Semicolons

**Source:** https://craftinginterpreters.com/scanning.html

```
first

-
second
```

---

### 105. Scanning — Design Note: Implicit Semicolons

**Source:** https://craftinginterpreters.com/scanning.html

```
a
 = 
1
 
b
 = 
2
```

---

### 106. Scanning — Design Note: Implicit Semicolons

**Source:** https://craftinginterpreters.com/scanning.html

```
console
.
log
(
function
() {
  
statement
();
});
```

---

### 107. Representing Code — Representing Code

**Source:** https://craftinginterpreters.com/representing-code.html

```
1
 + 
2
 * 
3
 - 
4
```

---

### 108. Representing Code — 5 . 1 . 1 Rules for grammars

**Source:** https://craftinginterpreters.com/representing-code.html

```
breakfast
  â 
protein
 
"with"
 
breakfast
 
"on the side"
 ;

breakfast
  â 
protein
 ;

breakfast
  â 
bread
 ;


protein
    â 
crispiness
 
"crispy"
 
"bacon"
 ;

protein
    â 
"sausage"
 ;

protein
    â 
cooked
 
"eggs"
 ;


crispiness
 â 
"really"
 ;

crispiness
 â 
"really"
 
crispiness
 ;


cooked
     â 
"scrambled"
 ;

cooked
     â 
"poached"
 ;

cooked
     â 
"fried"
 ;


bread
      â 
"toast"
 ;

bread
      â 
"biscuits"
 ;

bread
      â 
"English muffin"
 ;
```

---

### 109. Representing Code — 5 . 1 . 1 Rules for grammars

**Source:** https://craftinginterpreters.com/representing-code.html

```
protein
 â 
cooked
 
"eggs"
 ;
```

---

### 110. Representing Code — 5 . 1 . 1 Rules for grammars

**Source:** https://craftinginterpreters.com/representing-code.html

```
"poached" "eggs" "with" breakfast "on the side"
```

---

### 111. Representing Code — 5 . 1 . 2 Enhancing our notation

**Source:** https://craftinginterpreters.com/representing-code.html

```
bread
 â 
"toast"
 | 
"biscuits"
 | 
"English muffin"
 ;
```

---

### 112. Representing Code — 5 . 1 . 2 Enhancing our notation

**Source:** https://craftinginterpreters.com/representing-code.html

```
protein
 â ( 
"scrambled"
 | 
"poached"
 | 
"fried"
 ) 
"eggs"
 ;
```

---

### 113. Representing Code — 5 . 1 . 2 Enhancing our notation

**Source:** https://craftinginterpreters.com/representing-code.html

```
crispiness
 â 
"really"
 
"really"
* ;
```

---

### 114. Representing Code — 5 . 1 . 2 Enhancing our notation

**Source:** https://craftinginterpreters.com/representing-code.html

```
crispiness
 â 
"really"
+ ;
```

---

### 115. Representing Code — 5 . 1 . 2 Enhancing our notation

**Source:** https://craftinginterpreters.com/representing-code.html

```
breakfast
 â 
protein
 ( 
"with"
 
breakfast
 
"on the side"
 )? ;
```

---

### 116. Representing Code — 5 . 1 . 2 Enhancing our notation

**Source:** https://craftinginterpreters.com/representing-code.html

```
breakfast
 â 
protein
 ( 
"with"
 
breakfast
 
"on the side"
 )?
          | 
bread
 ;


protein
   â 
"really"
+ 
"crispy"
 
"bacon"

          | 
"sausage"

          | ( 
"scrambled"
 | 
"poached"
 | 
"fried"
 ) 
"eggs"
 ;


bread
     â 
"toast"
 | 
"biscuits"
 | 
"English muffin"
 ;
```

---

### 117. Representing Code — 5 . 1 . 3 A Grammar for Lox expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```
1
 - (
2
 * 
3
) < 
4
 == 
false
```

---

### 118. Representing Code — 5 . 1 . 3 A Grammar for Lox expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```
expression
     â 
literal

               | 
unary

               | 
binary

               | 
grouping
 ;


literal
        â 
NUMBER
 | 
STRING
 | 
"true"
 | 
"false"
 | 
"nil"
 ;

grouping
       â 
"("
 
expression
 
")"
 ;

unary
          â ( 
"-"
 | 
"!"
 ) 
expression
 ;

binary
         â 
expression
 
operator
 
expression
 ;

operator
       â 
"=="
 | 
"!="
 | 
"<"
 | 
"<="
 | 
">"
 | 
">="

               | 
"+"
  | 
"-"
  | 
"*"
 | 
"/"
 ;
```

---

### 119. Representing Code — 5 . 2 Implementing Syntax Trees

**Source:** https://craftinginterpreters.com/representing-code.html

```java
package
 
com.craftinginterpreters.lox
;


abstract
 
class
 
Expr
 {
 

  
static
 
class
 
Binary
 
extends
 
Expr
 {
    
Binary
(
Expr
 
left
, 
Token
 
operator
, 
Expr
 
right
) {
      
this
.
left
 = 
left
;
      
this
.
operator
 = 
operator
;
      
this
.
right
 = 
right
;
    }

    
final
 
Expr
 
left
;
    
final
 
Token
 
operator
;
    
final
 
Expr
 
right
;
  }

  
// Other expressions...

}
```

---

### 120. Representing Code — 5 . 2 . 2 Metaprogramming the trees

**Source:** https://craftinginterpreters.com/representing-code.html

```java
package
 
com.craftinginterpreters.tool
;


import
 
java.io.IOException
;

import
 
java.io.PrintWriter
;

import
 
java.util.Arrays
;

import
 
java.util.List
;


public
 
class
 
GenerateAst
 {
  
public
 
static
 
void
 
main
(
String
[] 
args
) 
throws
 
IOException
 {
    
if
 (
args
.
length
 != 
1
) {
      
System
.
err
.
println
(
"Usage: generate_ast <output directory>"
);
      
System
.
exit
(
64
);
    }
    
String
 
outputDir
 = 
args
[
0
];
  }
}
```

---

### 121. Representing Code — 5 . 2 . 2 Metaprogramming the trees

**Source:** https://craftinginterpreters.com/representing-code.html

```
    
defineAst
(
outputDir
, 
"Expr"
, 
Arrays
.
asList
(
      
"Binary   : Expr left, Token operator, Expr right"
,
      
"Grouping : Expr expression"
,
      
"Literal  : Object value"
,
      
"Unary    : Token operator, Expr right"

    ));
```

---

### 122. Representing Code — 5 . 2 . 2 Metaprogramming the trees

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
private
 
static
 
void
 
defineAst
(
      
String
 
outputDir
, 
String
 
baseName
, 
List
<
String
> 
types
)
      
throws
 
IOException
 {
    
String
 
path
 = 
outputDir
 + 
"/"
 + 
baseName
 + 
".java"
;
    
PrintWriter
 
writer
 = 
new
 
PrintWriter
(
path
, 
"UTF-8"
);

    
writer
.
println
(
"package com.craftinginterpreters.lox;"
);
    
writer
.
println
();
    
writer
.
println
(
"import java.util.List;"
);
    
writer
.
println
();
    
writer
.
println
(
"abstract class "
 + 
baseName
 + 
" {"
);

    
writer
.
println
(
"}"
);
    
writer
.
close
();
  }
```

---

### 123. Representing Code — 5 . 2 . 2 Metaprogramming the trees

**Source:** https://craftinginterpreters.com/representing-code.html

```
    writer.println("abstract class " + baseName + " {");
```

---

### 124. Representing Code — 5 . 2 . 2 Metaprogramming the trees

**Source:** https://craftinginterpreters.com/representing-code.html

```
    
// The AST classes.

    
for
 (
String
 
type
 : 
types
) {
      
String
 
className
 = 
type
.
split
(
":"
)[
0
].
trim
();
      
String
 
fields
 = 
type
.
split
(
":"
)[
1
].
trim
();
 

      
defineType
(
writer
, 
baseName
, 
className
, 
fields
);
    }
```

---

### 125. Representing Code — 5 . 2 . 2 Metaprogramming the trees

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
private
 
static
 
void
 
defineType
(
      
PrintWriter
 
writer
, 
String
 
baseName
,
      
String
 
className
, 
String
 
fieldList
) {
    
writer
.
println
(
"  static class "
 + 
className
 + 
" extends "
 +
        
baseName
 + 
" {"
);

    
// Constructor.

    
writer
.
println
(
"    "
 + 
className
 + 
"("
 + 
fieldList
 + 
") {"
);

    
// Store parameters in fields.

    
String
[] 
fields
 = 
fieldList
.
split
(
", "
);
    
for
 (
String
 
field
 : 
fields
) {
      
String
 
name
 = 
field
.
split
(
" "
)[
1
];
      
writer
.
println
(
"      this."
 + 
name
 + 
" = "
 + 
name
 + 
";"
);
    }

    
writer
.
println
(
"    }"
);

    
// Fields.

    
writer
.
println
();
    
for
 (
String
 
field
 : 
fields
) {
      
writer
.
println
(
"    final "
 + 
field
 + 
";"
);
    }

    
writer
.
println
(
"  }"
);
  }
```

---

### 126. Representing Code — 5 . 3 Working with Trees

**Source:** https://craftinginterpreters.com/representing-code.html

```
if
 (
expr
 
instanceof
 
Expr
.
Binary
) {
  
// ...

} 
else
 
if
 (
expr
 
instanceof
 
Expr
.
Grouping
) {
  
// ...

} 
else
 
// ...
```

---

### 127. Representing Code — 5 . 3 . 2 The Visitor pattern

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
abstract
 
class
 
Pastry
 {
  }

  
class
 
Beignet
 
extends
 
Pastry
 {
  }

  
class
 
Cruller
 
extends
 
Pastry
 {
  }
```

---

### 128. Representing Code — 5 . 3 . 2 The Visitor pattern

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
interface
 
PastryVisitor
 {
    
void
 
visitBeignet
(
Beignet
 
beignet
);
 

    
void
 
visitCruller
(
Cruller
 
cruller
);
  }
```

---

### 129. Representing Code — 5 . 3 . 2 The Visitor pattern

**Source:** https://craftinginterpreters.com/representing-code.html

```
    
abstract
 
void
 
accept
(
PastryVisitor
 
visitor
);
```

---

### 130. Representing Code — 5 . 3 . 2 The Visitor pattern

**Source:** https://craftinginterpreters.com/representing-code.html

```
    
@Override

    
void
 
accept
(
PastryVisitor
 
visitor
) {
      
visitor
.
visitBeignet
(
this
);
    }
```

---

### 131. Representing Code — 5 . 3 . 2 The Visitor pattern

**Source:** https://craftinginterpreters.com/representing-code.html

```
    
@Override

    
void
 
accept
(
PastryVisitor
 
visitor
) {
      
visitor
.
visitCruller
(
this
);
    }
```

---

### 132. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```
    writer.println("abstract class " + baseName + " {");
```

---

### 133. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```
    
defineVisitor
(
writer
, 
baseName
, 
types
);
```

---

### 134. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
private
 
static
 
void
 
defineVisitor
(
      
PrintWriter
 
writer
, 
String
 
baseName
, 
List
<
String
> 
types
) {
    
writer
.
println
(
"  interface Visitor<R> {"
);

    
for
 (
String
 
type
 : 
types
) {
      
String
 
typeName
 = 
type
.
split
(
":"
)[
0
].
trim
();
      
writer
.
println
(
"    R visit"
 + 
typeName
 + 
baseName
 + 
"("
 +
          
typeName
 + 
" "
 + 
baseName
.
toLowerCase
() + 
");"
);
    }

    
writer
.
println
(
"  }"
);
  }
```

---

### 135. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```
      defineType(writer, baseName, className, fields);
    }
```

---

### 136. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```


    
// The base accept() method.

    
writer
.
println
();
    
writer
.
println
(
"  abstract <R> R accept(Visitor<R> visitor);"
);
```

---

### 137. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```


    
// Visitor pattern.

    
writer
.
println
();
    
writer
.
println
(
"    @Override"
);
    
writer
.
println
(
"    <R> R accept(Visitor<R> visitor) {"
);
    
writer
.
println
(
"      return visitor.visit"
 +
        
className
 + 
baseName
 + 
"(this);"
);
    
writer
.
println
(
"    }"
);
```

---

### 138. Representing Code — 5 . 3 . 3 Visitors for expressions

**Source:** https://craftinginterpreters.com/representing-code.html

```


    // Fields.
```

---

### 139. Representing Code — 5 . 4 A (Not Very) Pretty Printer

**Source:** https://craftinginterpreters.com/representing-code.html

```lox
package
 
com.craftinginterpreters.lox
;


class
 
AstPrinter
 
implements
 
Expr
.
Visitor
<
String
> {
  
String
 
print
(
Expr
 
expr
) {
    
return
 
expr
.
accept
(
this
);
  }
}
```

---

### 140. Representing Code — 5 . 4 A (Not Very) Pretty Printer

**Source:** https://craftinginterpreters.com/representing-code.html

```
    return expr.accept(this);
  }
```

---

### 141. Representing Code — 5 . 4 A (Not Very) Pretty Printer

**Source:** https://craftinginterpreters.com/representing-code.html

```


  
@Override

  
public
 
String
 
visitBinaryExpr
(
Expr
.
Binary
 
expr
) {
    
return
 
parenthesize
(
expr
.
operator
.
lexeme
,
                        
expr
.
left
, 
expr
.
right
);
  }

  
@Override

  
public
 
String
 
visitGroupingExpr
(
Expr
.
Grouping
 
expr
) {
    
return
 
parenthesize
(
"group"
, 
expr
.
expression
);
  }

  
@Override

  
public
 
String
 
visitLiteralExpr
(
Expr
.
Literal
 
expr
) {
    
if
 (
expr
.
value
 == 
null
) 
return
 
"nil"
;
    
return
 
expr
.
value
.
toString
();
  }

  
@Override

  
public
 
String
 
visitUnaryExpr
(
Expr
.
Unary
 
expr
) {
    
return
 
parenthesize
(
expr
.
operator
.
lexeme
, 
expr
.
right
);
  }
```

---

### 142. Representing Code — 5 . 4 A (Not Very) Pretty Printer

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
private
 
String
 
parenthesize
(
String
 
name
, 
Expr
... 
exprs
) {
    
StringBuilder
 
builder
 = 
new
 
StringBuilder
();

    
builder
.
append
(
"("
).
append
(
name
);
    
for
 (
Expr
 
expr
 : 
exprs
) {
      
builder
.
append
(
" "
);
      
builder
.
append
(
expr
.
accept
(
this
));
    }
    
builder
.
append
(
")"
);

    
return
 
builder
.
toString
();
  }
```

---

### 143. Representing Code — 5 . 4 A (Not Very) Pretty Printer

**Source:** https://craftinginterpreters.com/representing-code.html

```
  
public
 
static
 
void
 
main
(
String
[] 
args
) {
    
Expr
 
expression
 = 
new
 
Expr
.
Binary
(
        
new
 
Expr
.
Unary
(
            
new
 
Token
(
TokenType
.
MINUS
, 
"-"
, 
null
, 
1
),
            
new
 
Expr
.
Literal
(
123
)),
        
new
 
Token
(
TokenType
.
STAR
, 
"*"
, 
null
, 
1
),
        
new
 
Expr
.
Grouping
(
            
new
 
Expr
.
Literal
(
45.67
)));

    
System
.
out
.
println
(
new
 
AstPrinter
().
print
(
expression
));
  }
```

---

### 144. Representing Code — Challenges

**Source:** https://craftinginterpreters.com/representing-code.html

```
expr
 â 
expr
 ( 
"("
 ( 
expr
 ( 
","
 
expr
 )* )? 
")"
 | 
"."
 
IDENTIFIER
 )+
     | 
IDENTIFIER

     | 
NUMBER
```

---

### 145. Representing Code — Challenges

**Source:** https://craftinginterpreters.com/representing-code.html

```
(
1
 + 
2
) * (
4
 - 
3
)
```

---

### 146. Representing Code — Challenges

**Source:** https://craftinginterpreters.com/representing-code.html

```
1
 
2
 + 
4
 
3
 - *
```

---

### 147. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
expression
     â 
literal

               | 
unary

               | 
binary

               | 
grouping
 ;


literal
        â 
NUMBER
 | 
STRING
 | 
"true"
 | 
"false"
 | 
"nil"
 ;

grouping
       â 
"("
 
expression
 
")"
 ;

unary
          â ( 
"-"
 | 
"!"
 ) 
expression
 ;

binary
         â 
expression
 
operator
 
expression
 ;

operator
       â 
"=="
 | 
"!="
 | 
"<"
 | 
"<="
 | 
">"
 | 
">="

               | 
"+"
  | 
"-"
  | 
"*"
 | 
"/"
 ;
```

---

### 148. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
5
 - 
3
 - 
1
```

---

### 149. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
(
5
 - 
3
) - 
1
```

---

### 150. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
a
 = 
b
 = 
c
```

---

### 151. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
a
 = (
b
 = 
c
)
```

---

### 152. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
expression
     â ...

equality
       â ...

comparison
     â ...

term
           â ...

factor
         â ...

unary
          â ...

primary
        â ...
```

---

### 153. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
expression
     â 
equality
```

---

### 154. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
primary
        â 
NUMBER
 | 
STRING
 | 
"true"
 | 
"false"
 | 
"nil"

               | 
"("
 
expression
 
")"
 ;
```

---

### 155. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
unary
          â ( 
"!"
 | 
"-"
 ) 
unary
 ;
```

---

### 156. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
unary
          â ( 
"!"
 | 
"-"
 ) 
unary

               | 
primary
 ;
```

---

### 157. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
factor
         â 
factor
 ( 
"/"
 | 
"*"
 ) 
unary

               | 
unary
 ;
```

---

### 158. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
print
 
0.1
 * (
0.2
 * 
0.3
);

print
 (
0.1
 * 
0.2
) * 
0.3
;
```

---

### 159. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
factor
         â 
unary
 ( ( 
"/"
 | 
"*"
 ) 
unary
 )* ;
```

---

### 160. Parsing Expressions — 6 . 1 Ambiguity and the Parsing Game

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
expression
     â 
equality
 ;

equality
       â 
comparison
 ( ( 
"!="
 | 
"=="
 ) 
comparison
 )* ;

comparison
     â 
term
 ( ( 
">"
 | 
">="
 | 
"<"
 | 
"<="
 ) 
term
 )* ;

term
           â 
factor
 ( ( 
"-"
 | 
"+"
 ) 
factor
 )* ;

factor
         â 
unary
 ( ( 
"/"
 | 
"*"
 ) 
unary
 )* ;

unary
          â ( 
"!"
 | 
"-"
 ) 
unary

               | 
primary
 ;

primary
        â 
NUMBER
 | 
STRING
 | 
"true"
 | 
"false"
 | 
"nil"

               | 
"("
 
expression
 
")"
 ;
```

---

### 161. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.List
;


import static
 
com.craftinginterpreters.lox.TokenType.*
;


class
 
Parser
 {
  
private
 
final
 
List
<
Token
> 
tokens
;
  
private
 
int
 
current
 = 
0
;

  
Parser
(
List
<
Token
> 
tokens
) {
    
this
.
tokens
 = 
tokens
;
  }
}
```

---

### 162. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
expression
() {
    
return
 
equality
();
  }
```

---

### 163. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
equality
       â 
comparison
 ( ( 
"!="
 | 
"=="
 ) 
comparison
 )* ;
```

---

### 164. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
equality
() {
    
Expr
 
expr
 = 
comparison
();

    
while
 (
match
(
BANG_EQUAL
, 
EQUAL_EQUAL
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
comparison
();
      
expr
 = 
new
 
Expr
.
Binary
(
expr
, 
operator
, 
right
);
    }

    
return
 
expr
;
  }
```

---

### 165. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
boolean
 
match
(
TokenType
... 
types
) {
    
for
 (
TokenType
 
type
 : 
types
) {
      
if
 (
check
(
type
)) {
        
advance
();
        
return
 
true
;
      }
    }

    
return
 
false
;
  }
```

---

### 166. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
boolean
 
check
(
TokenType
 
type
) {
    
if
 (
isAtEnd
()) 
return
 
false
;
    
return
 
peek
().
type
 == 
type
;
  }
```

---

### 167. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Token
 
advance
() {
    
if
 (!
isAtEnd
()) 
current
++;
    
return
 
previous
();
  }
```

---

### 168. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
boolean
 
isAtEnd
() {
    
return
 
peek
().
type
 == 
EOF
;
  }

  
private
 
Token
 
peek
() {
    
return
 
tokens
.
get
(
current
);
  }

  
private
 
Token
 
previous
() {
    
return
 
tokens
.
get
(
current
 - 
1
);
  }
```

---

### 169. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
comparison
     â 
term
 ( ( 
">"
 | 
">="
 | 
"<"
 | 
"<="
 ) 
term
 )* ;
```

---

### 170. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
comparison
() {
    
Expr
 
expr
 = 
term
();

    
while
 (
match
(
GREATER
, 
GREATER_EQUAL
, 
LESS
, 
LESS_EQUAL
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
term
();
      
expr
 = 
new
 
Expr
.
Binary
(
expr
, 
operator
, 
right
);
    }

    
return
 
expr
;
  }
```

---

### 171. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
term
() {
    
Expr
 
expr
 = 
factor
();

    
while
 (
match
(
MINUS
, 
PLUS
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
factor
();
      
expr
 = 
new
 
Expr
.
Binary
(
expr
, 
operator
, 
right
);
    }

    
return
 
expr
;
  }
```

---

### 172. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
factor
() {
    
Expr
 
expr
 = 
unary
();

    
while
 (
match
(
SLASH
, 
STAR
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
unary
();
      
expr
 = 
new
 
Expr
.
Binary
(
expr
, 
operator
, 
right
);
    }

    
return
 
expr
;
  }
```

---

### 173. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
unary
          â ( 
"!"
 | 
"-"
 ) 
unary

               | 
primary
 ;
```

---

### 174. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
unary
() {
    
if
 (
match
(
BANG
, 
MINUS
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
unary
();
      
return
 
new
 
Expr
.
Unary
(
operator
, 
right
);
    }

    
return
 
primary
();
  }
```

---

### 175. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
primary
        â 
NUMBER
 | 
STRING
 | 
"true"
 | 
"false"
 | 
"nil"

               | 
"("
 
expression
 
")"
 ;
```

---

### 176. Parsing Expressions — 6 . 2 . 1 The parser class

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Expr
 
primary
() {
    
if
 (
match
(
FALSE
)) 
return
 
new
 
Expr
.
Literal
(
false
);
    
if
 (
match
(
TRUE
)) 
return
 
new
 
Expr
.
Literal
(
true
);
    
if
 (
match
(
NIL
)) 
return
 
new
 
Expr
.
Literal
(
null
);

    
if
 (
match
(
NUMBER
, 
STRING
)) {
      
return
 
new
 
Expr
.
Literal
(
previous
().
literal
);
    }

    
if
 (
match
(
LEFT_PAREN
)) {
      
Expr
 
expr
 = 
expression
();
      
consume
(
RIGHT_PAREN
, 
"Expect ')' after expression."
);
      
return
 
new
 
Expr
.
Grouping
(
expr
);
    }
  }
```

---

### 177. Parsing Expressions — 6 . 3 . 2 Entering panic mode

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
Token
 
consume
(
TokenType
 
type
, 
String
 
message
) {
    
if
 (
check
(
type
)) 
return
 
advance
();

    
throw
 
error
(
peek
(), 
message
);
  }
```

---

### 178. Parsing Expressions — 6 . 3 . 2 Entering panic mode

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
ParseError
 
error
(
Token
 
token
, 
String
 
message
) {
    
Lox
.
error
(
token
, 
message
);
    
return
 
new
 
ParseError
();
  }
```

---

### 179. Parsing Expressions — 6 . 3 . 2 Entering panic mode

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
static
 
void
 
error
(
Token
 
token
, 
String
 
message
) {
    
if
 (
token
.
type
 == 
TokenType
.
EOF
) {
      
report
(
token
.
line
, 
" at end"
, 
message
);
    } 
else
 {
      
report
(
token
.
line
, 
" at '"
 + 
token
.
lexeme
 + 
"'"
, 
message
);
    }
  }
```

---

### 180. Parsing Expressions — 6 . 3 . 2 Entering panic mode

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
static
 
class
 
ParseError
 
extends
 
RuntimeException
 {}
```

---

### 181. Parsing Expressions — 6 . 3 . 2 Entering panic mode

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
unary
 â ( 
"!"
 | 
"-"
 | 
"+"
 ) 
unary

      | 
primary
 ;
```

---

### 182. Parsing Expressions — 6 . 3 . 3 Synchronizing a recursive descent parser

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
private
 
void
 
synchronize
() {
    
advance
();

    
while
 (!
isAtEnd
()) {
      
if
 (
previous
().
type
 == 
SEMICOLON
) 
return
;

      
switch
 (
peek
().
type
) {
        
case
 
CLASS
:
        
case
 
FUN
:
        
case
 
VAR
:
        
case
 
FOR
:
        
case
 
IF
:
        
case
 
WHILE
:
        
case
 
PRINT
:
        
case
 
RETURN
:
          
return
;
      }

      
advance
();
    }
  }
```

---

### 183. Parsing Expressions — 6 . 4 Wiring up the Parser

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
    if (match(LEFT_PAREN)) {
      Expr expr = expression();
      consume(RIGHT_PAREN, "Expect ')' after expression.");
      return new Expr.Grouping(expr);
    }
```

---

### 184. Parsing Expressions — 6 . 4 Wiring up the Parser

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```


    
throw
 
error
(
peek
(), 
"Expect expression."
);
```

---

### 185. Parsing Expressions — 6 . 4 Wiring up the Parser

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
  
Expr
 
parse
() {
    
try
 {
      
return
 
expression
();
    } 
catch
 (
ParseError
 
error
) {
      
return
 
null
;
    }
  }
```

---

### 186. Parsing Expressions — 6 . 4 Wiring up the Parser

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
    List<Token> tokens = scanner.scanTokens();
```

---

### 187. Parsing Expressions — 6 . 4 Wiring up the Parser

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
    
Parser
 
parser
 = 
new
 
Parser
(
tokens
);
    
Expr
 
expression
 = 
parser
.
parse
();

    
// Stop if there was a syntax error.

    
if
 (
hadError
) 
return
;

    
System
.
out
.
println
(
new
 
AstPrinter
().
print
(
expression
));
```

---

### 188. Parsing Expressions — Design Note: Logic Versus History

**Source:** https://craftinginterpreters.com/parsing-expressions.html

```
if
 (
flags
 & 
FLAG_MASK
 == 
SOME_FLAG
) { ... } 
// Wrong.


if
 ((
flags
 & 
FLAG_MASK
) == 
SOME_FLAG
) { ... } 
// Right.
```

---

### 189. Evaluating Expressions — 7 . 2 Evaluating Expressions

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```lox
package
 
com.craftinginterpreters.lox
;


class
 
Interpreter
 
implements
 
Expr
.
Visitor
<
Object
> {
}
```

---

### 190. Evaluating Expressions — 7 . 2 . 1 Evaluating literals

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
@Override

  
public
 
Object
 
visitLiteralExpr
(
Expr
.
Literal
 
expr
) {
    
return
 
expr
.
value
;
  }
```

---

### 191. Evaluating Expressions — 7 . 2 . 2 Evaluating parentheses

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
@Override

  
public
 
Object
 
visitGroupingExpr
(
Expr
.
Grouping
 
expr
) {
    
return
 
evaluate
(
expr
.
expression
);
  }
```

---

### 192. Evaluating Expressions — 7 . 2 . 2 Evaluating parentheses

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
Object
 
evaluate
(
Expr
 
expr
) {
    
return
 
expr
.
accept
(
this
);
  }
```

---

### 193. Evaluating Expressions — 7 . 2 . 3 Evaluating unary expressions

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
@Override

  
public
 
Object
 
visitUnaryExpr
(
Expr
.
Unary
 
expr
) {
    
Object
 
right
 = 
evaluate
(
expr
.
right
);

    
switch
 (
expr
.
operator
.
type
) {
      
case
 
MINUS
:
        
return
 -(
double
)
right
;
    }

    
// Unreachable.

    
return
 
null
;
  }
```

---

### 194. Evaluating Expressions — 7 . 2 . 3 Evaluating unary expressions

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
      
case
 
BANG
:
        
return
 !
isTruthy
(
right
);
```

---

### 195. Evaluating Expressions — 7 . 2 . 4 Truthiness and falsiness

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
boolean
 
isTruthy
(
Object
 
object
) {
    
if
 (
object
 == 
null
) 
return
 
false
;
    
if
 (
object
 
instanceof
 
Boolean
) 
return
 (
boolean
)
object
;
    
return
 
true
;
  }
```

---

### 196. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
@Override

  
public
 
Object
 
visitBinaryExpr
(
Expr
.
Binary
 
expr
) {
    
Object
 
left
 = 
evaluate
(
expr
.
left
);
    
Object
 
right
 = 
evaluate
(
expr
.
right
);
 


    
switch
 (
expr
.
operator
.
type
) {
      
case
 
MINUS
:
        
return
 (
double
)
left
 - (
double
)
right
;
      
case
 
SLASH
:
        
return
 (
double
)
left
 / (
double
)
right
;
      
case
 
STAR
:
        
return
 (
double
)
left
 * (
double
)
right
;
    }

    
// Unreachable.

    
return
 
null
;
  }
```

---

### 197. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
    switch (expr.operator.type) {
      case MINUS:
        return (double)left - (double)right;
```

---

### 198. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
      
case
 
PLUS
:
        
if
 (
left
 
instanceof
 
Double
 && 
right
 
instanceof
 
Double
) {
          
return
 (
double
)
left
 + (
double
)
right
;
        }
 


        
if
 (
left
 
instanceof
 
String
 && 
right
 
instanceof
 
String
) {
          
return
 (
String
)
left
 + (
String
)
right
;
        }

        
break
;
```

---

### 199. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
      
case
 
GREATER
:
        
return
 (
double
)
left
 > (
double
)
right
;
      
case
 
GREATER_EQUAL
:
        
return
 (
double
)
left
 >= (
double
)
right
;
      
case
 
LESS
:
        
return
 (
double
)
left
 < (
double
)
right
;
      
case
 
LESS_EQUAL
:
        
return
 (
double
)
left
 <= (
double
)
right
;
```

---

### 200. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
      
case
 
BANG_EQUAL
: 
return
 !
isEqual
(
left
, 
right
);
      
case
 
EQUAL_EQUAL
: 
return
 
isEqual
(
left
, 
right
);
```

---

### 201. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
boolean
 
isEqual
(
Object
 
a
, 
Object
 
b
) {
    
if
 (
a
 == 
null
 && 
b
 == 
null
) 
return
 
true
;
    
if
 (
a
 == 
null
) 
return
 
false
;

    
return
 
a
.
equals
(
b
);
  }
```

---

### 202. Evaluating Expressions — 7 . 2 . 5 Evaluating binary operators

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
(
0
 / 
0
) == (
0
 / 
0
)
```

---

### 203. Evaluating Expressions — 7 . 3 Runtime Errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
2
 * (
3
 / -
"muffin"
)
```

---

### 204. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperand
(
expr
.
operator
, 
right
);
```

---

### 205. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
void
 
checkNumberOperand
(
Token
 
operator
, 
Object
 
operand
) {
    
if
 (
operand
 
instanceof
 
Double
) 
return
;
    
throw
 
new
 
RuntimeError
(
operator
, 
"Operand must be a number."
);
  }
```

---

### 206. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```lox
package
 
com.craftinginterpreters.lox
;


class
 
RuntimeError
 
extends
 
RuntimeException
 {
  
final
 
Token
 
token
;

  
RuntimeError
(
Token
 
token
, 
String
 
message
) {
    
super
(
message
);
    
this
.
token
 = 
token
;
  }
}
```

---

### 207. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 208. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left > (double)right;
```

---

### 209. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 210. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left >= (double)right;
```

---

### 211. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 212. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left < (double)right;
```

---

### 213. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 214. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left <= (double)right;
```

---

### 215. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 216. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left - (double)right;
```

---

### 217. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 218. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left / (double)right;
```

---

### 219. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
checkNumberOperands
(
expr
.
operator
, 
left
, 
right
);
```

---

### 220. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        return (double)left * (double)right;
```

---

### 221. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
void
 
checkNumberOperands
(
Token
 
operator
,
                                   
Object
 
left
, 
Object
 
right
) {
    
if
 (
left
 
instanceof
 
Double
 && 
right
 
instanceof
 
Double
) 
return
;
   
 

    
throw
 
new
 
RuntimeError
(
operator
, 
"Operands must be numbers."
);
  }
```

---

### 222. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
say
(
"left"
) - 
say
(
"right"
);
```

---

### 223. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
          return (String)left + (String)right;
        }
```

---

### 224. Evaluating Expressions — 7 . 3 . 1 Detecting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
        
throw
 
new
 
RuntimeError
(
expr
.
operator
,
            
"Operands must be two numbers or two strings."
);
```

---

### 225. Evaluating Expressions — 7 . 4 Hooking Up the Interpreter

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
void
 
interpret
(
Expr
 
expression
) {
 

    
try
 {
      
Object
 
value
 = 
evaluate
(
expression
);
      
System
.
out
.
println
(
stringify
(
value
));
    } 
catch
 (
RuntimeError
 
error
) {
      
Lox
.
runtimeError
(
error
);
    }
  }
```

---

### 226. Evaluating Expressions — 7 . 4 Hooking Up the Interpreter

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
String
 
stringify
(
Object
 
object
) {
    
if
 (
object
 == 
null
) 
return
 
"nil"
;

    
if
 (
object
 
instanceof
 
Double
) {
      
String
 
text
 = 
object
.
toString
();
      
if
 (
text
.
endsWith
(
".0"
)) {
        
text
 = 
text
.
substring
(
0
, 
text
.
length
() - 
2
);
      }
      
return
 
text
;
    }

    
return
 
object
.
toString
();
  }
```

---

### 227. Evaluating Expressions — 7 . 4 . 1 Reporting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
static
 
void
 
runtimeError
(
RuntimeError
 
error
) {
    
System
.
err
.
println
(
error
.
getMessage
() +
        
"
\n
[line "
 + 
error
.
token
.
line
 + 
"]"
);
    
hadRuntimeError
 = 
true
;
  }
```

---

### 228. Evaluating Expressions — 7 . 4 . 1 Reporting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
static
 
boolean
 
hadRuntimeError
 = 
false
;
```

---

### 229. Evaluating Expressions — 7 . 4 . 1 Reporting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  public static void main(String[] args) throws IOException {
```

---

### 230. Evaluating Expressions — 7 . 4 . 1 Reporting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
    run(new String(bytes, Charset.defaultCharset()));

    // Indicate an error in the exit code.
    if (hadError) System.exit(65);
```

---

### 231. Evaluating Expressions — 7 . 4 . 1 Reporting runtime errors

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
    
if
 (
hadRuntimeError
) 
System
.
exit
(
70
);
```

---

### 232. Evaluating Expressions — 7 . 4 . 2 Running the interpreter

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
  
private
 
static
 
final
 
Interpreter
 
interpreter
 = 
new
 
Interpreter
();
```

---

### 233. Evaluating Expressions — 7 . 4 . 2 Running the interpreter

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
    // Stop if there was a syntax error.
    if (hadError) return;
```

---

### 234. Evaluating Expressions — 7 . 4 . 2 Running the interpreter

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
    
interpreter
.
interpret
(
expression
);
```

---

### 235. Evaluating Expressions — Design Note: Static and Dynamic Typing

**Source:** https://craftinginterpreters.com/evaluating-expressions.html

```
Object
[] 
stuff
 = 
new
 
Integer
[
1
];

stuff
[
0
] = 
"not an int!"
;
```

---

### 236. Statements and State — 8 . 1 Statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
program
        â 
statement
* 
EOF
 ;


statement
      â 
exprStmt

               | 
printStmt
 ;


exprStmt
       â 
expression
 
";"
 ;

printStmt
      â 
"print"
 
expression
 
";"
 ;
```

---

### 237. Statements and State — 8 . 1 . 1 Statement syntax trees

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      "Unary    : Token operator, Expr right"
    ));
```

---

### 238. Statements and State — 8 . 1 . 1 Statement syntax trees

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    
defineAst
(
outputDir
, 
"Stmt"
, 
Arrays
.
asList
(
      
"Expression : Expr expression"
,
      
"Print      : Expr expression"

    ));
```

---

### 239. Statements and State — 8 . 1 . 2 Parsing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
List
<
Stmt
> 
parse
() {
    
List
<
Stmt
> 
statements
 = 
new
 
ArrayList
<>();
    
while
 (!
isAtEnd
()) {
      
statements
.
add
(
statement
());
    }

    
return
 
statements
;
 

  }
```

---

### 240. Statements and State — 8 . 1 . 2 Parsing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
import
 
java.util.ArrayList
;
```

---

### 241. Statements and State — 8 . 1 . 2 Parsing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Stmt
 
statement
() {
    
if
 (
match
(
PRINT
)) 
return
 
printStatement
();

    
return
 
expressionStatement
();
  }
```

---

### 242. Statements and State — 8 . 1 . 2 Parsing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Stmt
 
printStatement
() {
    
Expr
 
value
 = 
expression
();
    
consume
(
SEMICOLON
, 
"Expect ';' after value."
);
    
return
 
new
 
Stmt
.
Print
(
value
);
  }
```

---

### 243. Statements and State — 8 . 1 . 2 Parsing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Stmt
 
expressionStatement
() {
    
Expr
 
expr
 = 
expression
();
    
consume
(
SEMICOLON
, 
"Expect ';' after expression."
);
    
return
 
new
 
Stmt
.
Expression
(
expr
);
  }
```

---

### 244. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
class
 
Interpreter
 
implements
 
Expr
.
Visitor
<
Object
>,
                             
Stmt
.
Visitor
<
Void
> {
```

---

### 245. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
@Override

  
public
 
Void
 
visitExpressionStmt
(
Stmt
.
Expression
 
stmt
) {
    
evaluate
(
stmt
.
expression
);
    
return
 
null
;
  }
```

---

### 246. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
@Override

  
public
 
Void
 
visitPrintStmt
(
Stmt
.
Print
 
stmt
) {
    
Object
 
value
 = 
evaluate
(
stmt
.
expression
);
    
System
.
out
.
println
(
stringify
(
value
));
    
return
 
null
;
  }
```

---

### 247. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
void
 
interpret
(
List
<
Stmt
> 
statements
) {
    
try
 {
      
for
 (
Stmt
 
statement
 : 
statements
) {
        
execute
(
statement
);
      }
    } 
catch
 (
RuntimeError
 
error
) {
      
Lox
.
runtimeError
(
error
);
    }
  }
```

---

### 248. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
void
 
execute
(
Stmt
 
stmt
) {
    
stmt
.
accept
(
this
);
  }
```

---

### 249. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```



import
 
java.util.List
;
```

---

### 250. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


class Interpreter implements Expr.Visitor<Object>,
```

---

### 251. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    
List
<
Stmt
> 
statements
 = 
parser
.
parse
();
```

---

### 252. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    // Stop if there was a syntax error.
```

---

### 253. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    
interpreter
.
interpret
(
statements
);
```

---

### 254. Statements and State — 8 . 1 . 3 Executing statements

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
print
 
"one"
;

print
 
true
;

print
 
2
 + 
1
;
```

---

### 255. Statements and State — 8 . 2 Global Variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
beverage
 = 
"espresso"
;
```

---

### 256. Statements and State — 8 . 2 Global Variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
print
 
beverage
; 
// "espresso".
```

---

### 257. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
if
 (
monday
) 
print
 
"Ugh, already?"
;
```

---

### 258. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
if
 (
monday
) 
var
 
beverage
 = 
"espresso"
;
```

---

### 259. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
program
        â 
declaration
* 
EOF
 ;


declaration
    â 
varDecl

               | 
statement
 ;


statement
      â 
exprStmt

               | 
printStmt
 ;
```

---

### 260. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
varDecl
        â 
"var"
 
IDENTIFIER
 ( 
"="
 
expression
 )? 
";"
 ;
```

---

### 261. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
primary
        â 
"true"
 | 
"false"
 | 
"nil"

               | 
NUMBER
 | 
STRING

               | 
"("
 
expression
 
")"

               | 
IDENTIFIER
 ;
```

---

### 262. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
"Print      : Expr expression"
,
```

---

### 263. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
"Var        : Token name, Expr initializer"
```

---

### 264. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
"Unary    : Token operator, Expr right"
,
```

---

### 265. Statements and State — 8 . 2 . 1 Variable syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
"Variable : Token name"
```

---

### 266. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  List<Stmt> parse() {
    List<Stmt> statements = new ArrayList<>();
    while (!isAtEnd()) {
```

---

### 267. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
statements
.
add
(
declaration
());
```

---

### 268. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    }

    return statements;
 

  }
```

---

### 269. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Stmt
 
declaration
() {
    
try
 {
      
if
 (
match
(
VAR
)) 
return
 
varDeclaration
();

      
return
 
statement
();
    } 
catch
 (
ParseError
 
error
) {
      
synchronize
();
      
return
 
null
;
    }
  }
```

---

### 270. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Stmt
 
varDeclaration
() {
    
Token
 
name
 = 
consume
(
IDENTIFIER
, 
"Expect variable name."
);

    
Expr
 
initializer
 = 
null
;
    
if
 (
match
(
EQUAL
)) {
      
initializer
 = 
expression
();
    }

    
consume
(
SEMICOLON
, 
"Expect ';' after variable declaration."
);
    
return
 
new
 
Stmt
.
Var
(
name
, 
initializer
);
  }
```

---

### 271. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      return new Expr.Literal(previous().literal);
    }
```

---

### 272. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    
if
 (
match
(
IDENTIFIER
)) {
      
return
 
new
 
Expr
.
Variable
(
previous
());
    }
```

---

### 273. Statements and State — 8 . 2 . 2 Parsing variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    if (match(LEFT_PAREN)) {
```

---

### 274. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.HashMap
;

import
 
java.util.Map
;


class
 
Environment
 {
  
private
 
final
 
Map
<
String
, 
Object
> 
values
 = 
new
 
HashMap
<>();
}
```

---

### 275. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
void
 
define
(
String
 
name
, 
Object
 
value
) {
    
values
.
put
(
name
, 
value
);
  }
```

---

### 276. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
 = 
"before"
;

print
 
a
; 
// "before".


var
 
a
 = 
"after"
;

print
 
a
; 
// "after".
```

---

### 277. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```java
class Environment {
  private final Map<String, Object> values = new HashMap<>();
```

---

### 278. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


  
Object
 
get
(
Token
 
name
) {
    
if
 (
values
.
containsKey
(
name
.
lexeme
)) {
      
return
 
values
.
get
(
name
.
lexeme
);
    }

    
throw
 
new
 
RuntimeError
(
name
,
        
"Undefined variable '"
 + 
name
.
lexeme
 + 
"'."
);
  }
```

---

### 279. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  void define(String name, Object value) {
```

---

### 280. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
fun
 
isOdd
(
n
) {
  
if
 (
n
 == 
0
) 
return
 
false
;
  
return
 
isEven
(
n
 - 
1
);
}


fun
 
isEven
(
n
) {
  
if
 (
n
 == 
0
) 
return
 
true
;
  
return
 
isOdd
(
n
 - 
1
);
}
```

---

### 281. Statements and State — 8 . 3 Environments

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
print
 
a
;

var
 
a
 = 
"too late!"
;
```

---

### 282. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
class Interpreter implements Expr.Visitor<Object>,
                             Stmt.Visitor<Void> {
```

---

### 283. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Environment
 
environment
 = 
new
 
Environment
();
```

---

### 284. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  void interpret(List<Stmt> statements) {
```

---

### 285. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
@Override

  
public
 
Void
 
visitVarStmt
(
Stmt
.
Var
 
stmt
) {
    
Object
 
value
 = 
null
;
    
if
 (
stmt
.
initializer
 != 
null
) {
      
value
 = 
evaluate
(
stmt
.
initializer
);
    }

    
environment
.
define
(
stmt
.
name
.
lexeme
, 
value
);
    
return
 
null
;
  }
```

---

### 286. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
;

print
 
a
; 
// "nil".
```

---

### 287. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
@Override

  
public
 
Object
 
visitVariableExpr
(
Expr
.
Variable
 
expr
) {
    
return
 
environment
.
get
(
expr
.
name
);
  }
```

---

### 288. Statements and State — 8 . 3 . 1 Interpreting global variables

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
 = 
1
;

var
 
b
 = 
2
;

print
 
a
 + 
b
;
```

---

### 289. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
expression
     â 
assignment
 ;

assignment
     â 
IDENTIFIER
 
"="
 
assignment

               | 
equality
 ;
```

---

### 290. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
instance
.
field
 = 
"value"
;
```

---

### 291. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    defineAst(outputDir, "Expr", Arrays.asList(
```

---

### 292. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
"Assign   : Token name, Expr value"
,
```

---

### 293. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      "Binary   : Expr left, Token operator, Expr right",
```

---

### 294. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    
return
 
assignment
();
```

---

### 295. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
 = 
"before"
;

a
 = 
"value"
;
```

---

### 296. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
makeList
().
head
.
next
 = 
node
;
```

---

### 297. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
Expr
 
assignment
() {
    
Expr
 
expr
 = 
equality
();

    
if
 (
match
(
EQUAL
)) {
      
Token
 
equals
 = 
previous
();
      
Expr
 
value
 = 
assignment
();

      
if
 (
expr
 
instanceof
 
Expr
.
Variable
) {
        
Token
 
name
 = ((
Expr
.
Variable
)
expr
).
name
;
        
return
 
new
 
Expr
.
Assign
(
name
, 
value
);
      }

      
error
(
equals
, 
"Invalid assignment target."
);
 

    }

    
return
 
expr
;
  }
```

---

### 298. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
newPoint
(
x
 + 
2
, 
0
).
y
 = 
3
;
```

---

### 299. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
newPoint
(
x
 + 
2
, 
0
).
y
;
```

---

### 300. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
a
 + 
b
 = 
c
;
```

---

### 301. Statements and State — 8 . 4 . 1 Assignment syntax

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
a
 = 
3
;   
// OK.

(
a
) = 
3
; 
// Error.
```

---

### 302. Statements and State — 8 . 4 . 2 Assignment semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
@Override

  
public
 
Object
 
visitAssignExpr
(
Expr
.
Assign
 
expr
) {
    
Object
 
value
 = 
evaluate
(
expr
.
value
);
    
environment
.
assign
(
expr
.
name
, 
value
);
    
return
 
value
;
  }
```

---

### 303. Statements and State — 8 . 4 . 2 Assignment semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
void
 
assign
(
Token
 
name
, 
Object
 
value
) {
    
if
 (
values
.
containsKey
(
name
.
lexeme
)) {
      
values
.
put
(
name
.
lexeme
, 
value
);
      
return
;
    }

    
throw
 
new
 
RuntimeError
(
name
,
        
"Undefined variable '"
 + 
name
.
lexeme
 + 
"'."
);
  }
```

---

### 304. Statements and State — 8 . 4 . 2 Assignment semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
 = 
1
;

print
 
a
 = 
2
; 
// "2".
```

---

### 305. Statements and State — 8 . 5 Scope

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
{
  
var
 
a
 = 
"first"
;
  
print
 
a
; 
// "first".

}

{
  
var
 
a
 = 
"second"
;
  
print
 
a
; 
// "second".

}
```

---

### 306. Statements and State — 8 . 5 Scope

**Source:** https://craftinginterpreters.com/statements-and-state.html

```java
class
 
Saxophone
 {
  
play
() {
    
print
 
"Careless Whisper"
;
  }
}


class
 
GolfClub
 {
  
play
() {
    
print
 
"Fore!"
;
  }
}


fun
 
playIt
(
thing
) {
  
thing
.
play
();
}
```

---

### 307. Statements and State — 8 . 5 Scope

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
{
  
var
 
a
 = 
"in block"
;
}

print
 
a
; 
// Error! No more "a".
```

---

### 308. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
// How loud?


var
 
volume
 = 
11
;


// Silence.


volume
 = 
0
;


// Calculate size of 3x4x5 cuboid.

{
  
var
 
volume
 = 
3
 * 
4
 * 
5
;
  
print
 
volume
;
}
```

---

### 309. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
global
 = 
"outside"
;
{
  
var
 
local
 = 
"inside"
;
  
print
 
global
 + 
local
;
}
```

---

### 310. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
final
 
Environment
 
enclosing
;
```

---

### 311. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  private final Map<String, Object> values = new HashMap<>();
```

---

### 312. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
Environment
() {
    
enclosing
 = 
null
;
  }

  
Environment
(
Environment
 
enclosing
) {
    
this
.
enclosing
 = 
enclosing
;
  }
```

---

### 313. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      return values.get(name.lexeme);
    }
```

---

### 314. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    
if
 (
enclosing
 != 
null
) 
return
 
enclosing
.
get
(
name
);
```

---

### 315. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    throw new RuntimeError(name,
        "Undefined variable '" + name.lexeme + "'.");
```

---

### 316. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      values.put(name.lexeme, value);
      return;
    }
```

---

### 317. Statements and State — 8 . 5 . 1 Nesting and shadowing

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    
if
 (
enclosing
 != 
null
) {
      
enclosing
.
assign
(
name
, 
value
);
      
return
;
    }
```

---

### 318. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
statement
      â 
exprStmt

               | 
printStmt

               | 
block
 ;


block
          â 
"{"
 
declaration
* 
"}"
 ;
```

---

### 319. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    defineAst(outputDir, "Stmt", Arrays.asList(
```

---

### 320. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
      
"Block      : List<Stmt> statements"
,
```

---

### 321. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    if (match(PRINT)) return printStatement();
```

---

### 322. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
    
if
 (
match
(
LEFT_BRACE
)) 
return
 
new
 
Stmt
.
Block
(
block
());
```

---

### 323. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```


    return expressionStatement();
```

---

### 324. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
private
 
List
<
Stmt
> 
block
() {
    
List
<
Stmt
> 
statements
 = 
new
 
ArrayList
<>();

    
while
 (!
check
(
RIGHT_BRACE
) && !
isAtEnd
()) {
      
statements
.
add
(
declaration
());
    }

    
consume
(
RIGHT_BRACE
, 
"Expect '}' after block."
);
    
return
 
statements
;
  }
```

---

### 325. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
@Override

  
public
 
Void
 
visitBlockStmt
(
Stmt
.
Block
 
stmt
) {
    
executeBlock
(
stmt
.
statements
, 
new
 
Environment
(
environment
));
    
return
 
null
;
  }
```

---

### 326. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
  
void
 
executeBlock
(
List
<
Stmt
> 
statements
,
                    
Environment
 
environment
) {
    
Environment
 
previous
 = 
this
.
environment
;
    
try
 {
      
this
.
environment
 = 
environment
;

      
for
 (
Stmt
 
statement
 : 
statements
) {
        
execute
(
statement
);
      }
    } 
finally
 {
      
this
.
environment
 = 
previous
;
    }
  }
```

---

### 327. Statements and State — 8 . 5 . 2 Block syntax and semantics

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
 = 
"global a"
;

var
 
b
 = 
"global b"
;

var
 
c
 = 
"global c"
;
{
  
var
 
a
 = 
"outer a"
;
  
var
 
b
 = 
"outer b"
;
  {
    
var
 
a
 = 
"inner a"
;
    
print
 
a
;
    
print
 
b
;
    
print
 
c
;
  }
  
print
 
a
;
  
print
 
b
;
  
print
 
c
;
}

print
 
a
;

print
 
b
;

print
 
c
;
```

---

### 328. Statements and State — Challenges

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
// No initializers.


var
 
a
;

var
 
b
;


a
 = 
"assigned"
;

print
 
a
; 
// OK, was assigned first.



print
 
b
; 
// Error!
```

---

### 329. Statements and State — Challenges

**Source:** https://craftinginterpreters.com/statements-and-state.html

```
var
 
a
 = 
1
;
{
  
var
 
a
 = 
a
 + 
2
;
  
print
 
a
;
}
```

---

### 330. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
statement
      â 
exprStmt

               | 
ifStmt

               | 
printStmt

               | 
block
 ;


ifStmt
         â 
"if"
 
"("
 
expression
 
")"
 
statement

               ( 
"else"
 
statement
 )? ;
```

---

### 331. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
      
"If         : Expr condition, Stmt thenBranch,"
 +
                  
" Stmt elseBranch"
,
```

---

### 332. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
if
 (
match
(
IF
)) 
return
 
ifStatement
();
```

---

### 333. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
    if (match(PRINT)) return printStatement();
```

---

### 334. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
private
 
Stmt
 
ifStatement
() {
    
consume
(
LEFT_PAREN
, 
"Expect '(' after 'if'."
);
    
Expr
 
condition
 = 
expression
();
    
consume
(
RIGHT_PAREN
, 
"Expect ')' after if condition."
);
 


    
Stmt
 
thenBranch
 = 
statement
();
    
Stmt
 
elseBranch
 = 
null
;
    
if
 (
match
(
ELSE
)) {
      
elseBranch
 = 
statement
();
    }

    
return
 
new
 
Stmt
.
If
(
condition
, 
thenBranch
, 
elseBranch
);
  }
```

---

### 335. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
if
 (
first
) 
if
 (
second
) 
whenTrue
(); 
else
 
whenFalse
();
```

---

### 336. Control Flow — 9 . 2 Conditional Execution

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
@Override

  
public
 
Void
 
visitIfStmt
(
Stmt
.
If
 
stmt
) {
    
if
 (
isTruthy
(
evaluate
(
stmt
.
condition
))) {
      
execute
(
stmt
.
thenBranch
);
    } 
else
 
if
 (
stmt
.
elseBranch
 != 
null
) {
      
execute
(
stmt
.
elseBranch
);
    }
    
return
 
null
;
  }
```

---

### 337. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
false
 
and
 
sideEffect
();
```

---

### 338. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
expression
     â 
assignment
 ;

assignment
     â 
IDENTIFIER
 
"="
 
assignment

               | 
logic_or
 ;

logic_or
       â 
logic_and
 ( 
"or"
 
logic_and
 )* ;

logic_and
      â 
equality
 ( 
"and"
 
equality
 )* ;
```

---

### 339. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
      
"Logical  : Expr left, Token operator, Expr right"
,
```

---

### 340. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
      "Unary    : Token operator, Expr right",
```

---

### 341. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
Expr
 
expr
 = 
or
();
```

---

### 342. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```


    if (match(EQUAL)) {
```

---

### 343. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
private
 
Expr
 
or
() {
    
Expr
 
expr
 = 
and
();

    
while
 (
match
(
OR
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
and
();
      
expr
 = 
new
 
Expr
.
Logical
(
expr
, 
operator
, 
right
);
    }

    
return
 
expr
;
  }
```

---

### 344. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
private
 
Expr
 
and
() {
    
Expr
 
expr
 = 
equality
();

    
while
 (
match
(
AND
)) {
      
Token
 
operator
 = 
previous
();
      
Expr
 
right
 = 
equality
();
      
expr
 = 
new
 
Expr
.
Logical
(
expr
, 
operator
, 
right
);
    }

    
return
 
expr
;
  }
```

---

### 345. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
@Override

  
public
 
Object
 
visitLogicalExpr
(
Expr
.
Logical
 
expr
) {
    
Object
 
left
 = 
evaluate
(
expr
.
left
);

    
if
 (
expr
.
operator
.
type
 == 
TokenType
.
OR
) {
      
if
 (
isTruthy
(
left
)) 
return
 
left
;
    } 
else
 {
      
if
 (!
isTruthy
(
left
)) 
return
 
left
;
    }

    
return
 
evaluate
(
expr
.
right
);
  }
```

---

### 346. Control Flow — 9 . 3 Logical Operators

**Source:** https://craftinginterpreters.com/control-flow.html

```
print
 
"hi"
 
or
 
2
; 
// "hi".


print
 
nil
 
or
 
"yes"
; 
// "yes".
```

---

### 347. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
statement
      â 
exprStmt

               | 
ifStmt

               | 
printStmt

               | 
whileStmt

               | 
block
 ;


whileStmt
      â 
"while"
 
"("
 
expression
 
")"
 
statement
 ;
```

---

### 348. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
      
"Var        : Token name, Expr initializer"
,
```

---

### 349. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
      
"While      : Expr condition, Stmt body"
```

---

### 350. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
    if (match(PRINT)) return printStatement();
```

---

### 351. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
if
 (
match
(
WHILE
)) 
return
 
whileStatement
();
```

---

### 352. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
    if (match(LEFT_BRACE)) return new Stmt.Block(block());
```

---

### 353. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
private
 
Stmt
 
whileStatement
() {
    
consume
(
LEFT_PAREN
, 
"Expect '(' after 'while'."
);
    
Expr
 
condition
 = 
expression
();
    
consume
(
RIGHT_PAREN
, 
"Expect ')' after condition."
);
    
Stmt
 
body
 = 
statement
();

    
return
 
new
 
Stmt
.
While
(
condition
, 
body
);
  }
```

---

### 354. Control Flow — 9 . 4 While Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
@Override

  
public
 
Void
 
visitWhileStmt
(
Stmt
.
While
 
stmt
) {
    
while
 (
isTruthy
(
evaluate
(
stmt
.
condition
))) {
      
execute
(
stmt
.
body
);
    }
    
return
 
null
;
  }
```

---

### 355. Control Flow — 9 . 5 For Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
for
 (
var
 
i
 = 
0
; 
i
 < 
10
; 
i
 = 
i
 + 
1
) 
print
 
i
;
```

---

### 356. Control Flow — 9 . 5 For Loops

**Source:** https://craftinginterpreters.com/control-flow.html

```
statement
      â 
exprStmt

               | 
forStmt

               | 
ifStmt

               | 
printStmt

               | 
whileStmt

               | 
block
 ;


forStmt
        â 
"for"
 
"("
 ( 
varDecl
 | 
exprStmt
 | 
";"
 )
                 
expression
? 
";"

                 
expression
? 
")"
 
statement
 ;
```

---

### 357. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
{
  
var
 
i
 = 
0
;
  
while
 (
i
 < 
10
) {
    
print
 
i
;
    
i
 = 
i
 + 
1
;
  }
}
```

---

### 358. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
import
 
java.util.Arrays
;
```

---

### 359. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
if
 (
match
(
FOR
)) 
return
 
forStatement
();
```

---

### 360. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    if (match(IF)) return ifStatement();
```

---

### 361. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
  
private
 
Stmt
 
forStatement
() {
    
consume
(
LEFT_PAREN
, 
"Expect '(' after 'for'."
);

    
// More here...

  }
```

---

### 362. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    consume(LEFT_PAREN, "Expect '(' after 'for'.");
```

---

### 363. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
Stmt
 
initializer
;
    
if
 (
match
(
SEMICOLON
)) {
      
initializer
 = 
null
;
    } 
else
 
if
 (
match
(
VAR
)) {
      
initializer
 = 
varDeclaration
();
    } 
else
 {
      
initializer
 = 
expressionStatement
();
    }
```

---

### 364. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
      initializer = expressionStatement();
    }
```

---

### 365. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```


    
Expr
 
condition
 = 
null
;
    
if
 (!
check
(
SEMICOLON
)) {
      
condition
 = 
expression
();
    }
    
consume
(
SEMICOLON
, 
"Expect ';' after loop condition."
);
```

---

### 366. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    consume(SEMICOLON, "Expect ';' after loop condition.");
```

---

### 367. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```


    
Expr
 
increment
 = 
null
;
    
if
 (!
check
(
RIGHT_PAREN
)) {
      
increment
 = 
expression
();
    }
    
consume
(
RIGHT_PAREN
, 
"Expect ')' after for clauses."
);
```

---

### 368. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    consume(RIGHT_PAREN, "Expect ')' after for clauses.");
```

---

### 369. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
Stmt
 
body
 = 
statement
();

    
return
 
body
;
```

---

### 370. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
if
 (
increment
 != 
null
) {
      
body
 = 
new
 
Stmt
.
Block
(
          
Arrays
.
asList
(
              
body
,
              
new
 
Stmt
.
Expression
(
increment
)));
    }
```

---

### 371. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
if
 (
condition
 == 
null
) 
condition
 = 
new
 
Expr
.
Literal
(
true
);
    
body
 = 
new
 
Stmt
.
While
(
condition
, 
body
);
```

---

### 372. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    body = new Stmt.While(condition, body);
```

---

### 373. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
    
if
 (
initializer
 != 
null
) {
      
body
 = 
new
 
Stmt
.
Block
(
Arrays
.
asList
(
initializer
, 
body
));
    }
```

---

### 374. Control Flow — 9 . 5 . 1 Desugaring

**Source:** https://craftinginterpreters.com/control-flow.html

```
var
 
a
 = 
0
;

var
 
temp
;


for
 (
var
 
b
 = 
1
; 
a
 < 
10000
; 
b
 = 
temp
 + 
b
) {
  
print
 
a
;
  
temp
 = 
a
;
  
a
 = 
b
;
}
```

---

### 375. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
average
(
1
, 
2
);
```

---

### 376. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
getCallback
()();
```

---

### 377. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
unary
          â ( 
"!"
 | 
"-"
 ) 
unary
 | 
call
 ;

call
           â 
primary
 ( 
"("
 
arguments
? 
")"
 )* ;
```

---

### 378. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
arguments
      â 
expression
 ( 
","
 
expression
 )* ;
```

---

### 379. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
      "Binary   : Expr left, Token operator, Expr right",
```

---

### 380. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
      
"Call     : Expr callee, Token paren, List<Expr> arguments"
,
```

---

### 381. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
      return new Expr.Unary(operator, right);
    }
```

---

### 382. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
    
return
 
call
();
```

---

### 383. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
  
private
 
Expr
 
call
() {
    
Expr
 
expr
 = 
primary
();

    
while
 (
true
) {
 

      
if
 (
match
(
LEFT_PAREN
)) {
        
expr
 = 
finishCall
(
expr
);
      } 
else
 {
        
break
;
      }
    }

    
return
 
expr
;
  }
```

---

### 384. Functions — 10 . 1 Function Calls

**Source:** https://craftinginterpreters.com/functions.html

```
  
private
 
Expr
 
finishCall
(
Expr
 
callee
) {
    
List
<
Expr
> 
arguments
 = 
new
 
ArrayList
<>();
    
if
 (!
check
(
RIGHT_PAREN
)) {
      
do
 {
        
arguments
.
add
(
expression
());
      } 
while
 (
match
(
COMMA
));
    }

    
Token
 
paren
 = 
consume
(
RIGHT_PAREN
,
                          
"Expect ')' after arguments."
);

    
return
 
new
 
Expr
.
Call
(
callee
, 
paren
, 
arguments
);
  }
```

---

### 385. Functions — 10 . 1 . 1 Maximum argument counts

**Source:** https://craftinginterpreters.com/functions.html

```
        
if
 (
arguments
.
size
() >= 
255
) {
          
error
(
peek
(), 
"Can't have more than 255 arguments."
);
        }
```

---

### 386. Functions — 10 . 1 . 2 Interpreting function calls

**Source:** https://craftinginterpreters.com/functions.html

```
import
 
java.util.ArrayList
;
```

---

### 387. Functions — 10 . 1 . 2 Interpreting function calls

**Source:** https://craftinginterpreters.com/functions.html

```
  
@Override

  
public
 
Object
 
visitCallExpr
(
Expr
.
Call
 
expr
) {
    
Object
 
callee
 = 
evaluate
(
expr
.
callee
);

    
List
<
Object
> 
arguments
 = 
new
 
ArrayList
<>();
    
for
 (
Expr
 
argument
 : 
expr
.
arguments
) {
 

      
arguments
.
add
(
evaluate
(
argument
));
    }

    
LoxCallable
 
function
 = (
LoxCallable
)
callee
;
    
return
 
function
.
call
(
this
, 
arguments
);
  }
```

---

### 388. Functions — 10 . 1 . 2 Interpreting function calls

**Source:** https://craftinginterpreters.com/functions.html

```
package
 
com.craftinginterpreters.lox
;


import
 
java.util.List
;


interface
 
LoxCallable
 {
  
Object
 
call
(
Interpreter
 
interpreter
, 
List
<
Object
> 
arguments
);
}
```

---

### 389. Functions — 10 . 1 . 3 Call type errors

**Source:** https://craftinginterpreters.com/functions.html

```
"totally not a function"
();
```

---

### 390. Functions — 10 . 1 . 3 Call type errors

**Source:** https://craftinginterpreters.com/functions.html

```
    
if
 (!(
callee
 
instanceof
 
LoxCallable
)) {
      
throw
 
new
 
RuntimeError
(
expr
.
paren
,
          
"Can only call functions and classes."
);
    }
```

---

### 391. Functions — 10 . 1 . 3 Call type errors

**Source:** https://craftinginterpreters.com/functions.html

```
    LoxCallable function = (LoxCallable)callee;
```

---

### 392. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
add
(
a
, 
b
, 
c
) {
  
print
 
a
 + 
b
 + 
c
;
}
```

---

### 393. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
add
(
1
, 
2
, 
3
, 
4
); 
// Too many.


add
(
1
, 
2
);       
// Too few.
```

---

### 394. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
    LoxCallable function = (LoxCallable)callee;
```

---

### 395. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
    
if
 (
arguments
.
size
() != 
function
.
arity
()) {
      
throw
 
new
 
RuntimeError
(
expr
.
paren
, 
"Expected "
 +
          
function
.
arity
() + 
" arguments but got "
 +
          
arguments
.
size
() + 
"."
);
    }
```

---

### 396. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
    return function.call(this, arguments);
```

---

### 397. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
  
int
 
arity
();
```

---

### 398. Functions — 10 . 1 . 4 Checking arity

**Source:** https://craftinginterpreters.com/functions.html

```
  Object call(Interpreter interpreter, List<Object> arguments);
```

---

### 399. Functions — 10 . 2 . 1 Telling time

**Source:** https://craftinginterpreters.com/functions.html

```
class Interpreter implements Expr.Visitor<Object>,
                             Stmt.Visitor<Void> {
```

---

### 400. Functions — 10 . 2 . 1 Telling time

**Source:** https://craftinginterpreters.com/functions.html

```
  
final
 
Environment
 
globals
 = 
new
 
Environment
();
  
private
 
Environment
 
environment
 = 
globals
;
```

---

### 401. Functions — 10 . 2 . 1 Telling time

**Source:** https://craftinginterpreters.com/functions.html

```


  void interpret(List<Stmt> statements) {
```

---

### 402. Functions — 10 . 2 . 1 Telling time

**Source:** https://craftinginterpreters.com/functions.html

```
  private Environment environment = globals;
```

---

### 403. Functions — 10 . 2 . 1 Telling time

**Source:** https://craftinginterpreters.com/functions.html

```
  
Interpreter
() {
    
globals
.
define
(
"clock"
, 
new
 
LoxCallable
() {
      
@Override

      
public
 
int
 
arity
() { 
return
 
0
; }

      
@Override

      
public
 
Object
 
call
(
Interpreter
 
interpreter
,
                         
List
<
Object
> 
arguments
) {
        
return
 (
double
)
System
.
currentTimeMillis
() / 
1000.0
;
      }

      
@Override

      
public
 
String
 
toString
() { 
return
 
"<native fn>"
; }
    });
  }
```

---

### 404. Functions — 10 . 2 . 1 Telling time

**Source:** https://craftinginterpreters.com/functions.html

```
  void interpret(List<Stmt> statements) {
```

---

### 405. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
var
 
add
 = 
fun
 (
a
, 
b
) {
  
print
 
a
 + 
b
;
};
```

---

### 406. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
declaration
    â 
funDecl

               | 
varDecl

               | 
statement
 ;
```

---

### 407. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
funDecl
        â 
"fun"
 
function
 ;

function
       â 
IDENTIFIER
 
"("
 
parameters
? 
")"
 
block
 ;
```

---

### 408. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
parameters
     â 
IDENTIFIER
 ( 
","
 
IDENTIFIER
 )* ;
```

---

### 409. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
      
"Function   : Token name, List<Token> params,"
 +
                  
" List<Stmt> body"
,
```

---

### 410. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
      "If         : Expr condition, Stmt thenBranch," +
```

---

### 411. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
      
if
 (
match
(
FUN
)) 
return
 
function
(
"function"
);
```

---

### 412. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
      if (match(VAR)) return varDeclaration();
```

---

### 413. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
  
private
 
Stmt
.
Function
 
function
(
String
 
kind
) {
    
Token
 
name
 = 
consume
(
IDENTIFIER
, 
"Expect "
 + 
kind
 + 
" name."
);
  }
```

---

### 414. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
    Token name = consume(IDENTIFIER, "Expect " + kind + " name.");
```

---

### 415. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
    
consume
(
LEFT_PAREN
, 
"Expect '(' after "
 + 
kind
 + 
" name."
);
    
List
<
Token
> 
parameters
 = 
new
 
ArrayList
<>();
    
if
 (!
check
(
RIGHT_PAREN
)) {
      
do
 {
        
if
 (
parameters
.
size
() >= 
255
) {
          
error
(
peek
(), 
"Can't have more than 255 parameters."
);
        }

        
parameters
.
add
(
            
consume
(
IDENTIFIER
, 
"Expect parameter name."
));
      } 
while
 (
match
(
COMMA
));
    }
    
consume
(
RIGHT_PAREN
, 
"Expect ')' after parameters."
);
```

---

### 416. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```
    consume(RIGHT_PAREN, "Expect ')' after parameters.");
```

---

### 417. Functions — 10 . 3 Function Declarations

**Source:** https://craftinginterpreters.com/functions.html

```


    
consume
(
LEFT_BRACE
, 
"Expect '{' before "
 + 
kind
 + 
" body."
);
    
List
<
Stmt
> 
body
 = 
block
();
    
return
 
new
 
Stmt
.
Function
(
name
, 
parameters
, 
body
);
```

---

### 418. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```lox
package
 
com.craftinginterpreters.lox
;


import
 
java.util.List
;


class
 
LoxFunction
 
implements
 
LoxCallable
 {
  
private
 
final
 
Stmt
.
Function
 
declaration
;
  
LoxFunction
(
Stmt
.
Function
 
declaration
) {
    
this
.
declaration
 = 
declaration
;
  }
}
```

---

### 419. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```
  
@Override

  
public
 
Object
 
call
(
Interpreter
 
interpreter
,
                     
List
<
Object
> 
arguments
) {
    
Environment
 
environment
 = 
new
 
Environment
(
interpreter
.
globals
);
    
for
 (
int
 
i
 = 
0
; 
i
 < 
declaration
.
params
.
size
(); 
i
++) {
      
environment
.
define
(
declaration
.
params
.
get
(
i
).
lexeme
,
          
arguments
.
get
(
i
));
    }

    
interpreter
.
executeBlock
(
declaration
.
body
, 
environment
);
    
return
 
null
;
  }
```

---

### 420. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
count
(
n
) {
  
if
 (
n
 > 
1
) 
count
(
n
 - 
1
);
  
print
 
n
;
}


count
(
3
);
```

---

### 421. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
add
(
a
, 
b
, 
c
) {
  
print
 
a
 + 
b
 + 
c
;
}


add
(
1
, 
2
, 
3
);
```

---

### 422. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```
  
@Override

  
public
 
int
 
arity
() {
    
return
 
declaration
.
params
.
size
();
  }
```

---

### 423. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```
  
@Override

  
public
 
String
 
toString
() {
    
return
 
"<fn "
 + 
declaration
.
name
.
lexeme
 + 
">"
;
  }
```

---

### 424. Functions — 10 . 4 Function Objects

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
add
(
a
, 
b
) {
  
print
 
a
 + 
b
;
}


print
 
add
; 
// "<fn add>".
```

---

### 425. Functions — 10 . 4 . 1 Interpreting function declarations

**Source:** https://craftinginterpreters.com/functions.html

```
  
@Override

  
public
 
Void
 
visitFunctionStmt
(
Stmt
.
Function
 
stmt
) {
    
LoxFunction
 
function
 = 
new
 
LoxFunction
(
stmt
);
    
environment
.
define
(
stmt
.
name
.
lexeme
, 
function
);
    
return
 
null
;
  }
```

---

### 426. Functions — 10 . 4 . 1 Interpreting function declarations

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
sayHi
(
first
, 
last
) {
  
print
 
"Hi, "
 + 
first
 + 
" "
 + 
last
 + 
"!"
;
}


sayHi
(
"Dear"
, 
"Reader"
);
```

---

### 427. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
statement
      â 
exprStmt

               | 
forStmt

               | 
ifStmt

               | 
printStmt

               | 
returnStmt

               | 
whileStmt

               | 
block
 ;


returnStmt
     â 
"return"
 
expression
? 
";"
 ;
```

---

### 428. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
procedure
() {
  
print
 
"don't return anything"
;
}


var
 
result
 = 
procedure
();

print
 
result
; 
// ?
```

---

### 429. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
return
 
nil
;
```

---

### 430. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
      
"Return     : Token keyword, Expr value"
,
```

---

### 431. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
      "Var        : Token name, Expr initializer",
```

---

### 432. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
    if (match(PRINT)) return printStatement();
```

---

### 433. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
    
if
 (
match
(
RETURN
)) 
return
 
returnStatement
();
```

---

### 434. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
    if (match(WHILE)) return whileStatement();
```

---

### 435. Functions — 10 . 5 Return Statements

**Source:** https://craftinginterpreters.com/functions.html

```
  
private
 
Stmt
 
returnStatement
() {
    
Token
 
keyword
 = 
previous
();
    
Expr
 
value
 = 
null
;
    
if
 (!
check
(
SEMICOLON
)) {
      
value
 = 
expression
();
    }

    
consume
(
SEMICOLON
, 
"Expect ';' after return value."
);
    
return
 
new
 
Stmt
.
Return
(
keyword
, 
value
);
  }
```

---

### 436. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
count
(
n
) {
  
while
 (
n
 < 
100
) {
    
if
 (
n
 == 
3
) 
return
 
n
; 
// <--

    
print
 
n
;
    
n
 = 
n
 + 
1
;
  }
}


count
(
1
);
```

---

### 437. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

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

---

### 438. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

```
  
@Override

  
public
 
Void
 
visitReturnStmt
(
Stmt
.
Return
 
stmt
) {
    
Object
 
value
 = 
null
;
    
if
 (
stmt
.
value
 != 
null
) 
value
 = 
evaluate
(
stmt
.
value
);

    
throw
 
new
 
Return
(
value
);
  }
```

---

### 439. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

```lox
package
 
com.craftinginterpreters.lox
;


class
 
Return
 
extends
 
RuntimeException
 {
  
final
 
Object
 
value
;

  
Return
(
Object
 
value
) {
    
super
(
null
, 
null
, 
false
, 
false
);
    
this
.
value
 = 
value
;
  }
}
```

---

### 440. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

```
          arguments.get(i));
    }
```

---

### 441. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

```
    
try
 {
      
interpreter
.
executeBlock
(
declaration
.
body
, 
environment
);
    } 
catch
 (
Return
 
returnValue
) {
      
return
 
returnValue
.
value
;
    }
```

---

### 442. Functions — 10 . 5 . 1 Returning from calls

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
fib
(
n
) {
  
if
 (
n
 <= 
1
) 
return
 
n
;
  
return
 
fib
(
n
 - 
2
) + 
fib
(
n
 - 
1
);
}


for
 (
var
 
i
 = 
0
; 
i
 < 
20
; 
i
 = 
i
 + 
1
) {
  
print
 
fib
(
i
);
}
```

---

### 443. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
makeCounter
() {
  
var
 
i
 = 
0
;
  
fun
 
count
() {
    
i
 = 
i
 + 
1
;
    
print
 
i
;
  }

  
return
 
count
;
}


var
 
counter
 = 
makeCounter
();

counter
(); 
// "1".


counter
(); 
// "2".
```

---

### 444. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
  private final Stmt.Function declaration;
```

---

### 445. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
  
private
 
final
 
Environment
 
closure
;
```

---

### 446. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
  LoxFunction(Stmt.Function declaration) {
```

---

### 447. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
  
LoxFunction
(
Stmt
.
Function
 
declaration
, 
Environment
 
closure
) {
    
this
.
closure
 = 
closure
;
```

---

### 448. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
  public Void visitFunctionStmt(Stmt.Function stmt) {
```

---

### 449. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
    
LoxFunction
 
function
 = 
new
 
LoxFunction
(
stmt
, 
environment
);
```

---

### 450. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
    environment.define(stmt.name.lexeme, function);
```

---

### 451. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
                     List<Object> arguments) {
```

---

### 452. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
    
Environment
 
environment
 = 
new
 
Environment
(
closure
);
```

---

### 453. Functions — 10 . 6 Local Functions and Closures

**Source:** https://craftinginterpreters.com/functions.html

```
    for (int i = 0; i < declaration.params.size(); i++) {
```

---

### 454. Functions — Challenges

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
thrice
(
fn
) {
  
for
 (
var
 
i
 = 
1
; 
i
 <= 
3
; 
i
 = 
i
 + 
1
) {
    
fn
(
i
);
  }
}


thrice
(
fun
 (
a
) {
  
print
 
a
;
});

// "1".


// "2".


// "3".
```

---

### 455. Functions — Challenges

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 () {};
```

---

### 456. Functions — Challenges

**Source:** https://craftinginterpreters.com/functions.html

```
fun
 
scope
(
a
) {
  
var
 
a
 = 
"local"
;
}
```

---

### 457. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
 = 
"outer"
;
{
  
var
 
a
 = 
"inner"
;
  
print
 
a
;
}
```

---

### 458. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
 = 
"outer"
;
{
  
print
 
a
;
  
var
 
a
 = 
"inner"
;
}
```

---

### 459. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
{
  
console
.
log
(
a
);
  
var
 
a
 = 
"value"
;
}
```

---

### 460. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
{
  
var
 
a
; 
// Hoist.

  
console
.
log
(
a
);
  
a
 = 
"value"
;
}
```

---

### 461. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
 = 
"outer"
;
{
  
var
 
a
 = 
"inner"
;
  
print
 
a
;
}
```

---

### 462. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
 = 
"global"
;
{
  
fun
 
showA
() {
    
print
 
a
;
  }

  
showA
();
  
var
 
a
 = 
"block"
;
  
showA
();
}
```

---

### 463. Resolving and Binding — 11 . 1 Static Scope

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
global
block
```

---

### 464. Resolving and Binding — 11 . 1 . 1 Scopes and mutable environments

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
{
  
var
 
a
;
  
// 1.

  
var
 
b
;
  
// 2.

}
```

---

### 465. Resolving and Binding — 11 . 3 A Resolver Class

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```lox
package
 
com.craftinginterpreters.lox
;


import
 
java.util.HashMap
;

import
 
java.util.List
;

import
 
java.util.Map
;

import
 
java.util.Stack
;


class
 
Resolver
 
implements
 
Expr
.
Visitor
<
Void
>, 
Stmt
.
Visitor
<
Void
> {
  
private
 
final
 
Interpreter
 
interpreter
;

  
Resolver
(
Interpreter
 
interpreter
) {
    
this
.
interpreter
 = 
interpreter
;
  }
}
```

---

### 466. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitBlockStmt
(
Stmt
.
Block
 
stmt
) {
    
beginScope
();
    
resolve
(
stmt
.
statements
);
    
endScope
();
    
return
 
null
;
  }
```

---

### 467. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
void
 
resolve
(
List
<
Stmt
> 
statements
) {
    
for
 (
Stmt
 
statement
 : 
statements
) {
      
resolve
(
statement
);
    }
  }
```

---

### 468. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
resolve
(
Stmt
 
stmt
) {
    
stmt
.
accept
(
this
);
  }
```

---

### 469. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
resolve
(
Expr
 
expr
) {
    
expr
.
accept
(
this
);
  }
```

---

### 470. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
beginScope
() {
    
scopes
.
push
(
new
 
HashMap
<
String
, 
Boolean
>());
  }
```

---

### 471. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  private final Interpreter interpreter;
```

---

### 472. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
final
 
Stack
<
Map
<
String
, 
Boolean
>> 
scopes
 = 
new
 
Stack
<>();
```

---

### 473. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


  Resolver(Interpreter interpreter) {
```

---

### 474. Resolving and Binding — 11 . 3 . 1 Resolving blocks

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
endScope
() {
    
scopes
.
pop
();
  }
```

---

### 475. Resolving and Binding — 11 . 3 . 2 Resolving variable declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitVarStmt
(
Stmt
.
Var
 
stmt
) {
    
declare
(
stmt
.
name
);
    
if
 (
stmt
.
initializer
 != 
null
) {
      
resolve
(
stmt
.
initializer
);
    }
    
define
(
stmt
.
name
);
    
return
 
null
;
  }
```

---

### 476. Resolving and Binding — 11 . 3 . 2 Resolving variable declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
 = 
"outer"
;
{
  
var
 
a
 = 
a
;
}
```

---

### 477. Resolving and Binding — 11 . 3 . 2 Resolving variable declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
temp
 = 
a
; 
// Run the initializer.


var
 
a
;        
// Declare the variable.


a
 = 
temp
;     
// Initialize it.
```

---

### 478. Resolving and Binding — 11 . 3 . 2 Resolving variable declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
; 
// Define the variable.


a
 = 
a
; 
// Run the initializer.
```

---

### 479. Resolving and Binding — 11 . 3 . 2 Resolving variable declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
declare
(
Token
 
name
) {
    
if
 (
scopes
.
isEmpty
()) 
return
;

    
Map
<
String
, 
Boolean
> 
scope
 = 
scopes
.
peek
();
    
scope
.
put
(
name
.
lexeme
, 
false
);
  }
```

---

### 480. Resolving and Binding — 11 . 3 . 2 Resolving variable declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
define
(
Token
 
name
) {
    
if
 (
scopes
.
isEmpty
()) 
return
;
    
scopes
.
peek
().
put
(
name
.
lexeme
, 
true
);
  }
```

---

### 481. Resolving and Binding — 11 . 3 . 3 Resolving variable expressions

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitVariableExpr
(
Expr
.
Variable
 
expr
) {
    
if
 (!
scopes
.
isEmpty
() &&
        
scopes
.
peek
().
get
(
expr
.
name
.
lexeme
) == 
Boolean
.
FALSE
) {
      
Lox
.
error
(
expr
.
name
,
          
"Can't read local variable in its own initializer."
);
    }

    
resolveLocal
(
expr
, 
expr
.
name
);
    
return
 
null
;
  }
```

---

### 482. Resolving and Binding — 11 . 3 . 3 Resolving variable expressions

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
resolveLocal
(
Expr
 
expr
, 
Token
 
name
) {
    
for
 (
int
 
i
 = 
scopes
.
size
() - 
1
; 
i
 >= 
0
; 
i
--) {
      
if
 (
scopes
.
get
(
i
).
containsKey
(
name
.
lexeme
)) {
        
interpreter
.
resolve
(
expr
, 
scopes
.
size
() - 
1
 - 
i
);
        
return
;
      }
    }
  }
```

---

### 483. Resolving and Binding — 11 . 3 . 4 Resolving assignment expressions

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitAssignExpr
(
Expr
.
Assign
 
expr
) {
    
resolve
(
expr
.
value
);
    
resolveLocal
(
expr
, 
expr
.
name
);
    
return
 
null
;
  }
```

---

### 484. Resolving and Binding — 11 . 3 . 5 Resolving function declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitFunctionStmt
(
Stmt
.
Function
 
stmt
) {
    
declare
(
stmt
.
name
);
    
define
(
stmt
.
name
);

    
resolveFunction
(
stmt
);
    
return
 
null
;
  }
```

---

### 485. Resolving and Binding — 11 . 3 . 5 Resolving function declarations

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
resolveFunction
(
Stmt
.
Function
 
function
) {
    
beginScope
();
    
for
 (
Token
 
param
 : 
function
.
params
) {
      
declare
(
param
);
      
define
(
param
);
    }
    
resolve
(
function
.
body
);
    
endScope
();
  }
```

---

### 486. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitExpressionStmt
(
Stmt
.
Expression
 
stmt
) {
    
resolve
(
stmt
.
expression
);
    
return
 
null
;
  }
```

---

### 487. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitIfStmt
(
Stmt
.
If
 
stmt
) {
    
resolve
(
stmt
.
condition
);
    
resolve
(
stmt
.
thenBranch
);
    
if
 (
stmt
.
elseBranch
 != 
null
) 
resolve
(
stmt
.
elseBranch
);
    
return
 
null
;
  }
```

---

### 488. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitPrintStmt
(
Stmt
.
Print
 
stmt
) {
    
resolve
(
stmt
.
expression
);
    
return
 
null
;
  }
```

---

### 489. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitReturnStmt
(
Stmt
.
Return
 
stmt
) {
    
if
 (
stmt
.
value
 != 
null
) {
      
resolve
(
stmt
.
value
);
    }

    
return
 
null
;
  }
```

---

### 490. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitWhileStmt
(
Stmt
.
While
 
stmt
) {
    
resolve
(
stmt
.
condition
);
    
resolve
(
stmt
.
body
);
    
return
 
null
;
  }
```

---

### 491. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitBinaryExpr
(
Expr
.
Binary
 
expr
) {
    
resolve
(
expr
.
left
);
    
resolve
(
expr
.
right
);
    
return
 
null
;
  }
```

---

### 492. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitCallExpr
(
Expr
.
Call
 
expr
) {
    
resolve
(
expr
.
callee
);

    
for
 (
Expr
 
argument
 : 
expr
.
arguments
) {
      
resolve
(
argument
);
    }

    
return
 
null
;
  }
```

---

### 493. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitGroupingExpr
(
Expr
.
Grouping
 
expr
) {
    
resolve
(
expr
.
expression
);
    
return
 
null
;
  }
```

---

### 494. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitLiteralExpr
(
Expr
.
Literal
 
expr
) {
    
return
 
null
;
  }
```

---

### 495. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitLogicalExpr
(
Expr
.
Logical
 
expr
) {
    
resolve
(
expr
.
left
);
    
resolve
(
expr
.
right
);
    
return
 
null
;
  }
```

---

### 496. Resolving and Binding — 11 . 3 . 6 Resolving the other syntax tree nodes

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
@Override

  
public
 
Void
 
visitUnaryExpr
(
Expr
.
Unary
 
expr
) {
    
resolve
(
expr
.
right
);
    
return
 
null
;
  }
```

---

### 497. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
void
 
resolve
(
Expr
 
expr
, 
int
 
depth
) {
    
locals
.
put
(
expr
, 
depth
);
  }
```

---

### 498. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  private Environment environment = globals;
```

---

### 499. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
final
 
Map
<
Expr
, 
Integer
> 
locals
 = 
new
 
HashMap
<>();
```

---

### 500. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


  Interpreter() {
```

---

### 501. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
import
 
java.util.HashMap
;
```

---

### 502. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
import
 
java.util.Map
;
```

---

### 503. Resolving and Binding — 11 . 4 Interpreting Resolved Variables

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


class Interpreter implements Expr.Visitor<Object>,
```

---

### 504. Resolving and Binding — 11 . 4 . 1 Accessing a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  public Object visitVariableExpr(Expr.Variable expr) {
```

---

### 505. Resolving and Binding — 11 . 4 . 1 Accessing a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    
return
 
lookUpVariable
(
expr
.
name
, 
expr
);
```

---

### 506. Resolving and Binding — 11 . 4 . 1 Accessing a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
Object
 
lookUpVariable
(
Token
 
name
, 
Expr
 
expr
) {
    
Integer
 
distance
 = 
locals
.
get
(
expr
);
    
if
 (
distance
 != 
null
) {
      
return
 
environment
.
getAt
(
distance
, 
name
.
lexeme
);
    } 
else
 {
      
return
 
globals
.
get
(
name
);
    }
  }
```

---

### 507. Resolving and Binding — 11 . 4 . 1 Accessing a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
Object
 
getAt
(
int
 
distance
, 
String
 
name
) {
    
return
 
ancestor
(
distance
).
values
.
get
(
name
);
  }
```

---

### 508. Resolving and Binding — 11 . 4 . 1 Accessing a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
Environment
 
ancestor
(
int
 
distance
) {
    
Environment
 
environment
 = 
this
;
    
for
 (
int
 
i
 = 
0
; 
i
 < 
distance
; 
i
++) {
      
environment
 = 
environment
.
enclosing
;
 

    }

    
return
 
environment
;
  }
```

---

### 509. Resolving and Binding — 11 . 4 . 2 Assigning to a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  public Object visitAssignExpr(Expr.Assign expr) {
    Object value = evaluate(expr.value);
```

---

### 510. Resolving and Binding — 11 . 4 . 2 Assigning to a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


    
Integer
 
distance
 = 
locals
.
get
(
expr
);
    
if
 (
distance
 != 
null
) {
      
environment
.
assignAt
(
distance
, 
expr
.
name
, 
value
);
    } 
else
 {
      
globals
.
assign
(
expr
.
name
, 
value
);
    }
```

---

### 511. Resolving and Binding — 11 . 4 . 2 Assigning to a resolved variable

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
void
 
assignAt
(
int
 
distance
, 
Token
 
name
, 
Object
 
value
) {
    
ancestor
(
distance
).
values
.
put
(
name
.
lexeme
, 
value
);
  }
```

---

### 512. Resolving and Binding — 11 . 4 . 3 Running the resolver

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    // Stop if there was a syntax error.
    if (hadError) return;
```

---

### 513. Resolving and Binding — 11 . 4 . 3 Running the resolver

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    
Resolver
 
resolver
 = 
new
 
Resolver
(
interpreter
);
    
resolver
.
resolve
(
statements
);
```

---

### 514. Resolving and Binding — 11 . 5 Resolution Errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
fun
 
bad
() {
  
var
 
a
 = 
"first"
;
  
var
 
a
 = 
"second"
;
}
```

---

### 515. Resolving and Binding — 11 . 5 Resolution Errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    Map<String, Boolean> scope = scopes.peek();
```

---

### 516. Resolving and Binding — 11 . 5 Resolution Errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    
if
 (
scope
.
containsKey
(
name
.
lexeme
)) {
      
Lox
.
error
(
name
,
          
"Already a variable with this name in this scope."
);
    }
```

---

### 517. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
return
 
"at top level"
;
```

---

### 518. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  private final Stack<Map<String, Boolean>> scopes = new Stack<>();
```

---

### 519. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
FunctionType
 
currentFunction
 = 
FunctionType
.
NONE
;
```

---

### 520. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


  Resolver(Interpreter interpreter) {
```

---

### 521. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
enum
 
FunctionType
 {
    
NONE
,
    
FUNCTION

  }
```

---

### 522. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    
resolveFunction
(
stmt
, 
FunctionType
.
FUNCTION
);
```

---

### 523. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  
private
 
void
 
resolveFunction
(
      
Stmt
.
Function
 
function
, 
FunctionType
 
type
) {
    
FunctionType
 
enclosingFunction
 = 
currentFunction
;
    
currentFunction
 = 
type
;
```

---

### 524. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    
currentFunction
 = 
enclosingFunction
;
```

---

### 525. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
  public Void visitReturnStmt(Stmt.Return stmt) {
```

---

### 526. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
    
if
 (
currentFunction
 == 
FunctionType
.
NONE
) {
      
Lox
.
error
(
stmt
.
keyword
, 
"Can't return from top-level code."
);
    }
```

---

### 527. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


    
// Stop if there was a resolution error.

    
if
 (
hadError
) 
return
;
```

---

### 528. Resolving and Binding — 11 . 5 . 1 Invalid return errors

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```


    interpreter.interpret(statements);
```

---

### 529. Resolving and Binding — Challenges

**Source:** https://craftinginterpreters.com/resolving-and-binding.html

```
var
 
a
 = 
"outer"
;
{
  
var
 
a
 = 
a
;
}
```

---

### 530. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
declaration
    â 
classDecl

               | 
funDecl

               | 
varDecl

               | 
statement
 ;


classDecl
      â 
"class"
 
IDENTIFIER
 
"{"
 
function
* 
"}"
 ;
```

---

### 531. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
function
       â 
IDENTIFIER
 
"("
 
parameters
? 
")"
 
block
 ;

parameters
     â 
IDENTIFIER
 ( 
","
 
IDENTIFIER
 )* ;
```

---

### 532. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Breakfast
 {
  
cook
() {
    
print
 
"Eggs a-fryin'!"
;
  }

  
serve
(
who
) {
    
print
 
"Enjoy your breakfast, "
 + 
who
 + 
"."
;
  }
}
```

---

### 533. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
      "Block      : List<Stmt> statements",
```

---

### 534. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
      
"Class      : Token name, List<Stmt.Function> methods"
,
```

---

### 535. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
      
if
 (
match
(
CLASS
)) 
return
 
classDeclaration
();
```

---

### 536. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
      if (match(FUN)) return function("function");
```

---

### 537. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
  
private
 
Stmt
 
classDeclaration
() {
    
Token
 
name
 = 
consume
(
IDENTIFIER
, 
"Expect class name."
);
    
consume
(
LEFT_BRACE
, 
"Expect '{' before class body."
);

    
List
<
Stmt
.
Function
> 
methods
 = 
new
 
ArrayList
<>();
    
while
 (!
check
(
RIGHT_BRACE
) && !
isAtEnd
()) {
      
methods
.
add
(
function
(
"method"
));
    }

    
consume
(
RIGHT_BRACE
, 
"Expect '}' after class body."
);

    
return
 
new
 
Stmt
.
Class
(
name
, 
methods
);
  }
```

---

### 538. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Void
 
visitClassStmt
(
Stmt
.
Class
 
stmt
) {
    
declare
(
stmt
.
name
);
    
define
(
stmt
.
name
);
    
return
 
null
;
  }
```

---

### 539. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Void
 
visitClassStmt
(
Stmt
.
Class
 
stmt
) {
    
environment
.
define
(
stmt
.
name
.
lexeme
, 
null
);
    
LoxClass
 
klass
 = 
new
 
LoxClass
(
stmt
.
name
.
lexeme
);
    
environment
.
assign
(
stmt
.
name
, 
klass
);
    
return
 
null
;
  }
```

---

### 540. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.List
;

import
 
java.util.Map
;


class
 
LoxClass
 {
  
final
 
String
 
name
;

  
LoxClass
(
String
 
name
) {
    
this
.
name
 = 
name
;
  }

  
@Override

  
public
 
String
 
toString
() {
    
return
 
name
;
  }
}
```

---

### 541. Classes — 12 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
DevonshireCream
 {
  
serveOn
() {
    
return
 
"Scones"
;
  }
}


print
 
DevonshireCream
; 
// Prints "DevonshireCream".
```

---

### 542. Classes — 12 . 3 Creating Instances

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Bagel
 {}

Bagel
();
```

---

### 543. Classes — 12 . 3 Creating Instances

**Source:** https://craftinginterpreters.com/classes.html

```lox
class
 
LoxClass
 
implements
 
LoxCallable
 {
```

---

### 544. Classes — 12 . 3 Creating Instances

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Object
 
call
(
Interpreter
 
interpreter
,
                     
List
<
Object
> 
arguments
) {
    
LoxInstance
 
instance
 = 
new
 
LoxInstance
(
this
);
    
return
 
instance
;
  }

  
@Override

  
public
 
int
 
arity
() {
    
return
 
0
;
  }
```

---

### 545. Classes — 12 . 3 Creating Instances

**Source:** https://craftinginterpreters.com/classes.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.HashMap
;

import
 
java.util.Map
;


class
 
LoxInstance
 {
  
private
 
LoxClass
 
klass
;

  
LoxInstance
(
LoxClass
 
klass
) {
    
this
.
klass
 = 
klass
;
  }

  
@Override

  
public
 
String
 
toString
() {
    
return
 
klass
.
name
 + 
" instance"
;
  }
}
```

---

### 546. Classes — 12 . 3 Creating Instances

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Bagel
 {}

var
 
bagel
 = 
Bagel
();

print
 
bagel
; 
// Prints "Bagel instance".
```

---

### 547. Classes — 12 . 4 Properties on Instances

**Source:** https://craftinginterpreters.com/classes.html

```
someObject
.
someProperty
```

---

### 548. Classes — 12 . 4 Properties on Instances

**Source:** https://craftinginterpreters.com/classes.html

```
call
           â 
primary
 ( 
"("
 
arguments
? 
")"
 | 
"."
 
IDENTIFIER
 )* ;
```

---

### 549. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      "Call     : Expr callee, Token paren, List<Expr> arguments",
```

---

### 550. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      
"Get      : Expr object, Token name"
,
```

---

### 551. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
    while (true) {
 

      if (match(LEFT_PAREN)) {
        expr = finishCall(expr);
```

---

### 552. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      } 
else
 
if
 (
match
(
DOT
)) {
        
Token
 
name
 = 
consume
(
IDENTIFIER
,
            
"Expect property name after '.'."
);
        
expr
 = 
new
 
Expr
.
Get
(
expr
, 
name
);
```

---

### 553. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      } else {
        break;
      }
    }
```

---

### 554. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Void
 
visitGetExpr
(
Expr
.
Get
 
expr
) {
    
resolve
(
expr
.
object
);
    
return
 
null
;
  }
```

---

### 555. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Object
 
visitGetExpr
(
Expr
.
Get
 
expr
) {
    
Object
 
object
 = 
evaluate
(
expr
.
object
);
    
if
 (
object
 
instanceof
 
LoxInstance
) {
      
return
 ((
LoxInstance
) 
object
).
get
(
expr
.
name
);
    }

    
throw
 
new
 
RuntimeError
(
expr
.
name
,
        
"Only instances have properties."
);
  }
```

---

### 556. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
private
 
final
 
Map
<
String
, 
Object
> 
fields
 = 
new
 
HashMap
<>();
```

---

### 557. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```


  LoxInstance(LoxClass klass) {
```

---

### 558. Classes — 12 . 4 . 1 Get expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
Object
 
get
(
Token
 
name
) {
    
if
 (
fields
.
containsKey
(
name
.
lexeme
)) {
      
return
 
fields
.
get
(
name
.
lexeme
);
    }

    
throw
 
new
 
RuntimeError
(
name
,
 

        
"Undefined property '"
 + 
name
.
lexeme
 + 
"'."
);
  }
```

---

### 559. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
someObject
.
someProperty
 = 
value
;
```

---

### 560. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
assignment
     â ( 
call
 
"."
 )? 
IDENTIFIER
 
"="
 
assignment

               | 
logic_or
 ;
```

---

### 561. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      "Logical  : Expr left, Token operator, Expr right",
```

---

### 562. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      
"Set      : Expr object, Token name, Expr value"
,
```

---

### 563. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      "Unary    : Token operator, Expr right",
```

---

### 564. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
        return new Expr.Assign(name, value);
```

---

### 565. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
      } 
else
 
if
 (
expr
 
instanceof
 
Expr
.
Get
) {
        
Expr
.
Get
 
get
 = (
Expr
.
Get
)
expr
;
        
return
 
new
 
Expr
.
Set
(
get
.
object
, 
get
.
name
, 
value
);
```

---

### 566. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Void
 
visitSetExpr
(
Expr
.
Set
 
expr
) {
    
resolve
(
expr
.
value
);
    
resolve
(
expr
.
object
);
    
return
 
null
;
  }
```

---

### 567. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Object
 
visitSetExpr
(
Expr
.
Set
 
expr
) {
    
Object
 
object
 = 
evaluate
(
expr
.
object
);

    
if
 (!(
object
 
instanceof
 
LoxInstance
)) {
 

      
throw
 
new
 
RuntimeError
(
expr
.
name
,
                             
"Only instances have fields."
);
    }

    
Object
 
value
 = 
evaluate
(
expr
.
value
);
    ((
LoxInstance
)
object
).
set
(
expr
.
name
, 
value
);
    
return
 
value
;
  }
```

---

### 568. Classes — 12 . 4 . 2 Set expressions

**Source:** https://craftinginterpreters.com/classes.html

```
  
void
 
set
(
Token
 
name
, 
Object
 
value
) {
    
fields
.
put
(
name
.
lexeme
, 
value
);
  }
```

---

### 569. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
var
 
m
 = 
object
.
method
;

m
(
argument
);
```

---

### 570. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Box
 {}


fun
 
notMethod
(
argument
) {
  
print
 
"called function with "
 + 
argument
;
}


var
 
box
 = 
Box
();

box
.
function
 = 
notMethod
;

box
.
function
(
"argument"
);
```

---

### 571. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
breakfast
(
omelette
.
filledWith
(
cheese
), 
sausage
);
```

---

### 572. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
var
 
eggs
 = 
omelette
.
filledWith
(
cheese
);

breakfast
(
eggs
, 
sausage
);
```

---

### 573. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
fun
 
callback
(
a
, 
b
, 
c
) {
  
object
.
method
(
a
, 
b
, 
c
);
}


takeCallback
(
callback
);
```

---

### 574. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
takeCallback
(
object
.
method
);
```

---

### 575. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Person
 {
  
sayName
() {
    
print
 
this
.
name
;
  }
}


var
 
jane
 = 
Person
();

jane
.
name
 = 
"Jane"
;


var
 
method
 = 
jane
.
sayName
;

method
(); 
// ?
```

---

### 576. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Person
 {
  
sayName
() {
    
print
 
this
.
name
;
  }
}


var
 
jane
 = 
Person
();

jane
.
name
 = 
"Jane"
;


var
 
bill
 = 
Person
();

bill
.
name
 = 
"Bill"
;


bill
.
sayName
 = 
jane
.
sayName
;

bill
.
sayName
(); 
// ?
```

---

### 577. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```


    
for
 (
Stmt
.
Function
 
method
 : 
stmt
.
methods
) {
      
FunctionType
 
declaration
 = 
FunctionType
.
METHOD
;
      
resolveFunction
(
method
, 
declaration
);
 

    }
```

---

### 578. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
    
FUNCTION
,
```

---

### 579. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
    
METHOD
```

---

### 580. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
    environment.define(stmt.name.lexeme, null);
```

---

### 581. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```


    
Map
<
String
, 
LoxFunction
> 
methods
 = 
new
 
HashMap
<>();
    
for
 (
Stmt
.
Function
 
method
 : 
stmt
.
methods
) {
      
LoxFunction
 
function
 = 
new
 
LoxFunction
(
method
, 
environment
);
      
methods
.
put
(
method
.
name
.
lexeme
, 
function
);
    }

    
LoxClass
 
klass
 = 
new
 
LoxClass
(
stmt
.
name
.
lexeme
, 
methods
);
```

---

### 582. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
    environment.assign(stmt.name, klass);
```

---

### 583. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
  
private
 
final
 
Map
<
String
, 
LoxFunction
> 
methods
;

  
LoxClass
(
String
 
name
, 
Map
<
String
, 
LoxFunction
> 
methods
) {
    
this
.
name
 = 
name
;
    
this
.
methods
 = 
methods
;
  }
```

---

### 584. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```


  @Override
  public String toString() {
```

---

### 585. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
  Object get(Token name) {
    if (fields.containsKey(name.lexeme)) {
      return fields.get(name.lexeme);
    }
```

---

### 586. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
    
LoxFunction
 
method
 = 
klass
.
findMethod
(
name
.
lexeme
);
    
if
 (
method
 != 
null
) 
return
 
method
;
```

---

### 587. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
    throw new RuntimeError(name,
 

        "Undefined property '" + name.lexeme + "'.");
```

---

### 588. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```
  
LoxFunction
 
findMethod
(
String
 
name
) {
    
if
 (
methods
.
containsKey
(
name
)) {
      
return
 
methods
.
get
(
name
);
    }

    
return
 
null
;
  }
```

---

### 589. Classes — 12 . 5 Methods on Classes

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Bacon
 {
  
eat
() {
    
print
 
"Crunch crunch crunch!"
;
  }
}


Bacon
().
eat
(); 
// Prints "Crunch crunch crunch!".
```

---

### 590. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Egotist
 {
  
speak
() {
    
print
 
this
;
  }
}


var
 
method
 = 
Egotist
().
speak
;

method
();
```

---

### 591. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Cake
 {
  
taste
() {
    
var
 
adjective
 = 
"delicious"
;
    
print
 
"The "
 + 
this
.
flavor
 + 
" cake is "
 + 
adjective
 + 
"!"
;
  }
}


var
 
cake
 = 
Cake
();

cake
.
flavor
 = 
"German chocolate"
;

cake
.
taste
(); 
// Prints "The German chocolate cake is delicious!".
```

---

### 592. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Thing
 {
  
getCallback
() {
    
fun
 
localFunction
() {
      
print
 
this
;
    }

    
return
 
localFunction
;
  }
}


var
 
callback
 = 
Thing
().
getCallback
();

callback
();
```

---

### 593. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
      "Set      : Expr object, Token name, Expr value",
```

---

### 594. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
      
"This     : Token keyword"
,
```

---

### 595. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
      "Unary    : Token operator, Expr right",
```

---

### 596. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
      return new Expr.Literal(previous().literal);
    }
```

---

### 597. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```


    
if
 (
match
(
THIS
)) 
return
 
new
 
Expr
.
This
(
previous
());
```

---

### 598. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```


    if (match(IDENTIFIER)) {
```

---

### 599. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Void
 
visitThisExpr
(
Expr
.
This
 
expr
) {
    
resolveLocal
(
expr
, 
expr
.
keyword
);
    
return
 
null
;
  }
```

---

### 600. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
    
beginScope
();
    
scopes
.
peek
().
put
(
"this"
, 
true
);
```

---

### 601. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
    for (Stmt.Function method : stmt.methods) {
```

---

### 602. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
    
endScope
();
```

---

### 603. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
    LoxFunction method = klass.findMethod(name.lexeme);
```

---

### 604. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
    
if
 (
method
 != 
null
) 
return
 
method
.
bind
(
this
);
```

---

### 605. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```


    throw new RuntimeError(name,
 

        "Undefined property '" + name.lexeme + "'.");
```

---

### 606. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
  
LoxFunction
 
bind
(
LoxInstance
 
instance
) {
    
Environment
 
environment
 = 
new
 
Environment
(
closure
);
    
environment
.
define
(
"this"
, 
instance
);
    
return
 
new
 
LoxFunction
(
declaration
, 
environment
);
  }
```

---

### 607. Classes — 12 . 6 This

**Source:** https://craftinginterpreters.com/classes.html

```
  
@Override

  
public
 
Object
 
visitThisExpr
(
Expr
.
This
 
expr
) {
    
return
 
lookUpVariable
(
expr
.
keyword
, 
expr
);
  }
```

---

### 608. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
print
 
this
;
```

---

### 609. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
fun
 
notAMethod
() {
  
print
 
this
;
}
```

---

### 610. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```


  
private
 
enum
 
ClassType
 {
    
NONE
,
    
CLASS

  }

  
private
 
ClassType
 
currentClass
 = 
ClassType
.
NONE
;
```

---

### 611. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
  public Void visitClassStmt(Stmt.Class stmt) {
```

---

### 612. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
    
ClassType
 
enclosingClass
 = 
currentClass
;
    
currentClass
 = 
ClassType
.
CLASS
;
```

---

### 613. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
    
currentClass
 = 
enclosingClass
;
```

---

### 614. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
  public Void visitThisExpr(Expr.This expr) {
```

---

### 615. Classes — 12 . 6 . 1 Invalid uses of this

**Source:** https://craftinginterpreters.com/classes.html

```
    
if
 (
currentClass
 == 
ClassType
.
NONE
) {
      
Lox
.
error
(
expr
.
keyword
,
          
"Can't use 'this' outside of a class."
);
      
return
 
null
;
    }
```

---

### 616. Classes — 12 . 7 Constructors and Initializers

**Source:** https://craftinginterpreters.com/classes.html

```
                     List<Object> arguments) {
    LoxInstance instance = new LoxInstance(this);
```

---

### 617. Classes — 12 . 7 Constructors and Initializers

**Source:** https://craftinginterpreters.com/classes.html

```
    
LoxFunction
 
initializer
 = 
findMethod
(
"init"
);
    
if
 (
initializer
 != 
null
) {
      
initializer
.
bind
(
instance
).
call
(
interpreter
, 
arguments
);
    }
```

---

### 618. Classes — 12 . 7 Constructors and Initializers

**Source:** https://craftinginterpreters.com/classes.html

```
    
LoxFunction
 
initializer
 = 
findMethod
(
"init"
);
    
if
 (
initializer
 == 
null
) 
return
 
0
;
    
return
 
initializer
.
arity
();
```

---

### 619. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Foo
 {
  
init
() {
    
print
 
this
;
  }
}


var
 
foo
 = 
Foo
();

print
 
foo
.
init
();
```

---

### 620. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
      return returnValue.value;
    }
```

---

### 621. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```


    
if
 (
isInitializer
) 
return
 
closure
.
getAt
(
0
, 
"this"
);
```

---

### 622. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
  
private
 
final
 
boolean
 
isInitializer
;

  
LoxFunction
(
Stmt
.
Function
 
declaration
, 
Environment
 
closure
,
              
boolean
 
isInitializer
) {
    
this
.
isInitializer
 = 
isInitializer
;
```

---

### 623. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
    this.closure = closure;
    this.declaration = declaration;
```

---

### 624. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
  public Void visitFunctionStmt(Stmt.Function stmt) {
```

---

### 625. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
    
LoxFunction
 
function
 = 
new
 
LoxFunction
(
stmt
, 
environment
,
                                           
false
);
```

---

### 626. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
    environment.define(stmt.name.lexeme, function);
```

---

### 627. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
    for (Stmt.Function method : stmt.methods) {
```

---

### 628. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
      
LoxFunction
 
function
 = 
new
 
LoxFunction
(
method
, 
environment
,
          
method
.
name
.
lexeme
.
equals
(
"init"
));
```

---

### 629. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
      methods.put(method.name.lexeme, function);
```

---

### 630. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
    environment.define("this", instance);
```

---

### 631. Classes — 12 . 7 . 1 Invoking init() directly

**Source:** https://craftinginterpreters.com/classes.html

```
    
return
 
new
 
LoxFunction
(
declaration
, 
environment
,
                           
isInitializer
);
```

---

### 632. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Foo
 {
  
init
() {
    
return
 
"something else"
;
  }
}
```

---

### 633. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```
    
INITIALIZER
,
```

---

### 634. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```
      FunctionType declaration = FunctionType.METHOD;
```

---

### 635. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```
      
if
 (
method
.
name
.
lexeme
.
equals
(
"init"
)) {
        
declaration
 = 
FunctionType
.
INITIALIZER
;
      }
```

---

### 636. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```
      resolveFunction(method, declaration);
```

---

### 637. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```
      
if
 (
currentFunction
 == 
FunctionType
.
INITIALIZER
) {
        
Lox
.
error
(
stmt
.
keyword
,
            
"Can't return a value from an initializer."
);
      }
```

---

### 638. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Foo
 {
  
init
() {
    
return
;
  }
}
```

---

### 639. Classes — 12 . 7 . 2 Returning from init()

**Source:** https://craftinginterpreters.com/classes.html

```
      
if
 (
isInitializer
) 
return
 
closure
.
getAt
(
0
, 
"this"
);
```

---

### 640. Classes — Challenges

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Math
 {
  
class
 
square
(
n
) {
    
return
 
n
 * 
n
;
  }
}


print
 
Math
.
square
(
3
); 
// Prints "9".
```

---

### 641. Classes — Challenges

**Source:** https://craftinginterpreters.com/classes.html

```java
class
 
Circle
 {
  
init
(
radius
) {
    
this
.
radius
 = 
radius
;
  }

  
area
 {
    
return
 
3.141592653
 * 
this
.
radius
 * 
this
.
radius
;
  }
}


var
 
circle
 = 
Circle
(
4
);

print
 
circle
.
area
; 
// Prints roughly "50.2655".
```

---

### 642. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
class
 
Doughnut
 {
  
// General doughnut stuff...

}


class
 
BostonCream
 < 
Doughnut
 {
  
// Boston Cream-specific stuff...

}
```

---

### 643. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
classDecl
      â 
"class"
 
IDENTIFIER
 ( 
"<"
 
IDENTIFIER
 )?
                 
"{"
 
function
* 
"}"
 ;
```

---

### 644. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
      "Block      : List<Stmt> statements",
```

---

### 645. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
      
"Class      : Token name, Expr.Variable superclass,"
 +
                  
" List<Stmt.Function> methods"
,
```

---

### 646. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    Token name = consume(IDENTIFIER, "Expect class name.");
```

---

### 647. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
Expr
.
Variable
 
superclass
 = 
null
;
    
if
 (
match
(
LESS
)) {
      
consume
(
IDENTIFIER
, 
"Expect superclass name."
);
      
superclass
 = 
new
 
Expr
.
Variable
(
previous
());
    }
```

---

### 648. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    consume(LEFT_BRACE, "Expect '{' before class body.");
```

---

### 649. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    consume(RIGHT_BRACE, "Expect '}' after class body.");
```

---

### 650. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
return
 
new
 
Stmt
.
Class
(
name
, 
superclass
, 
methods
);
```

---

### 651. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
if
 (
stmt
.
superclass
 != 
null
) {
      
resolve
(
stmt
.
superclass
);
    }
```

---

### 652. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```


    beginScope();
```

---

### 653. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
class
 
Oops
 < 
Oops
 {}
```

---

### 654. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
if
 (
stmt
.
superclass
 != 
null
 &&
        
stmt
.
name
.
lexeme
.
equals
(
stmt
.
superclass
.
name
.
lexeme
)) {
      
Lox
.
error
(
stmt
.
superclass
.
name
,
          
"A class can't inherit from itself."
);
    }
```

---

### 655. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
  public Void visitClassStmt(Stmt.Class stmt) {
```

---

### 656. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
Object
 
superclass
 = 
null
;
    
if
 (
stmt
.
superclass
 != 
null
) {
      
superclass
 = 
evaluate
(
stmt
.
superclass
);
      
if
 (!(
superclass
 
instanceof
 
LoxClass
)) {
        
throw
 
new
 
RuntimeError
(
stmt
.
superclass
.
name
,
            
"Superclass must be a class."
);
      }
    }
```

---

### 657. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    environment.define(stmt.name.lexeme, null);
```

---

### 658. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
var
 
NotAClass
 = 
"I am totally not a class"
;


class
 
Subclass
 < 
NotAClass
 {} 
// ?!
```

---

### 659. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
      methods.put(method.name.lexeme, function);
    }
```

---

### 660. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
LoxClass
 
klass
 = 
new
 
LoxClass
(
stmt
.
name
.
lexeme
,
        (
LoxClass
)
superclass
, 
methods
);
```

---

### 661. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
    environment.assign(stmt.name, klass);
```

---

### 662. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
  
LoxClass
(
String
 
name
, 
LoxClass
 
superclass
,
           
Map
<
String
, 
LoxFunction
> 
methods
) {
    
this
.
superclass
 = 
superclass
;
```

---

### 663. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
  
final
 
LoxClass
 
superclass
;
```

---

### 664. Inheritance — 13 . 1 Superclasses and Subclasses

**Source:** https://craftinginterpreters.com/inheritance.html

```
  private final Map<String, LoxFunction> methods;
```

---

### 665. Inheritance — 13 . 2 Inheriting Methods

**Source:** https://craftinginterpreters.com/inheritance.html

```
      return methods.get(name);
    }
```

---

### 666. Inheritance — 13 . 2 Inheriting Methods

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
if
 (
superclass
 != 
null
) {
      
return
 
superclass
.
findMethod
(
name
);
    }
```

---

### 667. Inheritance — 13 . 2 Inheriting Methods

**Source:** https://craftinginterpreters.com/inheritance.html

```java
class
 
Doughnut
 {
  
cook
() {
    
print
 
"Fry until golden brown."
;
  }
}


class
 
BostonCream
 < 
Doughnut
 {}


BostonCream
().
cook
();
```

---

### 668. Inheritance — 13 . 3 Calling Superclass Methods

**Source:** https://craftinginterpreters.com/inheritance.html

```java
class
 
Doughnut
 {
  
cook
() {
    
print
 
"Fry until golden brown."
;
  }
}


class
 
BostonCream
 < 
Doughnut
 {
  
cook
() {
    
super
.
cook
();
    
print
 
"Pipe full of custard and coat with chocolate."
;
  }
}


BostonCream
().
cook
();
```

---

### 669. Inheritance — 13 . 3 Calling Superclass Methods

**Source:** https://craftinginterpreters.com/inheritance.html

```
Fry until golden brown.
Pipe full of custard and coat with chocolate.
```

---

### 670. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```
print
 
super
; 
// Syntax error.
```

---

### 671. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```
primary
        â 
"true"
 | 
"false"
 | 
"nil"
 | 
"this"

               | 
NUMBER
 | 
STRING
 | 
IDENTIFIER
 | 
"("
 
expression
 
")"

               | 
"super"
 
"."
 
IDENTIFIER
 ;
```

---

### 672. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```
var
 
method
 = 
super
.
cook
;

method
();
```

---

### 673. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```
      "Set      : Expr object, Token name, Expr value",
```

---

### 674. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```
      
"Super    : Token keyword, Token method"
,
```

---

### 675. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```
      return new Expr.Literal(previous().literal);
    }
```

---

### 676. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
if
 (
match
(
SUPER
)) {
      
Token
 
keyword
 = 
previous
();
      
consume
(
DOT
, 
"Expect '.' after 'super'."
);
      
Token
 
method
 = 
consume
(
IDENTIFIER
,
          
"Expect superclass method name."
);
      
return
 
new
 
Expr
.
Super
(
keyword
, 
method
);
    }
```

---

### 677. Inheritance — 13 . 3 . 1 Syntax

**Source:** https://craftinginterpreters.com/inheritance.html

```


    if (match(THIS)) return new Expr.This(previous());
```

---

### 678. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```java
class
 
A
 {
  
method
() {
    
print
 
"A method"
;
  }
}


class
 
B
 < 
A
 {
  
method
() {
    
print
 
"B method"
;
  }

  
test
() {
    
super
.
method
();
  }
}


class
 
C
 < 
B
 {}


C
().
test
();
```

---

### 679. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
      resolve(stmt.superclass);
    }
```

---

### 680. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
if
 (
stmt
.
superclass
 != 
null
) {
      
beginScope
();
      
scopes
.
peek
().
put
(
"super"
, 
true
);
    }
```

---

### 681. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    beginScope();
```

---

### 682. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
if
 (
stmt
.
superclass
 != 
null
) 
endScope
();
```

---

### 683. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
  
@Override

  
public
 
Void
 
visitSuperExpr
(
Expr
.
Super
 
expr
) {
    
resolveLocal
(
expr
, 
expr
.
keyword
);
    
return
 
null
;
  }
```

---

### 684. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
        throw new RuntimeError(stmt.superclass.name,
            "Superclass must be a class.");
      }
    }

    environment.define(stmt.name.lexeme, null);
```

---

### 685. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
if
 (
stmt
.
superclass
 != 
null
) {
      
environment
 = 
new
 
Environment
(
environment
);
      
environment
.
define
(
"super"
, 
superclass
);
    }
```

---

### 686. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    Map<String, LoxFunction> methods = new HashMap<>();
```

---

### 687. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
    LoxClass klass = new LoxClass(stmt.name.lexeme,
        (LoxClass)superclass, methods);
```

---

### 688. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
if
 (
superclass
 != 
null
) {
      
environment
 = 
environment
.
enclosing
;
    }
```

---

### 689. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    environment.assign(stmt.name, klass);
```

---

### 690. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
  
@Override

  
public
 
Object
 
visitSuperExpr
(
Expr
.
Super
 
expr
) {
    
int
 
distance
 = 
locals
.
get
(
expr
);
    
LoxClass
 
superclass
 = (
LoxClass
)
environment
.
getAt
(
        
distance
, 
"super"
);
  }
```

---

### 691. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
    LoxClass superclass = (LoxClass)environment.getAt(
        distance, "super");
```

---

### 692. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
LoxInstance
 
object
 = (
LoxInstance
)
environment
.
getAt
(
        
distance
 - 
1
, 
"this"
);
```

---

### 693. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
    LoxInstance object = (LoxInstance)environment.getAt(
        distance - 1, "this");
```

---

### 694. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
LoxFunction
 
method
 = 
superclass
.
findMethod
(
expr
.
method
.
lexeme
);
    
return
 
method
.
bind
(
object
);
```

---

### 695. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    LoxFunction method = superclass.findMethod(expr.method.lexeme);
```

---

### 696. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```


    
if
 (
method
 == 
null
) {
      
throw
 
new
 
RuntimeError
(
expr
.
method
,
          
"Undefined property '"
 + 
expr
.
method
.
lexeme
 + 
"'."
);
    }
```

---

### 697. Inheritance — 13 . 3 . 2 Semantics

**Source:** https://craftinginterpreters.com/inheritance.html

```
    return method.bind(object);
  }
```

---

### 698. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```java
class
 
Eclair
 {
  
cook
() {
    
super
.
cook
();
    
print
 
"Pipe full of crÃ¨me pÃ¢tissiÃ¨re."
;
  }
}
```

---

### 699. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```
super
.
notEvenInAClass
();
```

---

### 700. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
CLASS
,
```

---

### 701. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
SUBCLASS
```

---

### 702. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```
      
currentClass
 = 
ClassType
.
SUBCLASS
;
```

---

### 703. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```
  public Void visitSuperExpr(Expr.Super expr) {
```

---

### 704. Inheritance — 13 . 3 . 3 Invalid uses of super

**Source:** https://craftinginterpreters.com/inheritance.html

```
    
if
 (
currentClass
 == 
ClassType
.
NONE
) {
      
Lox
.
error
(
expr
.
keyword
,
          
"Can't use 'super' outside of a class."
);
    } 
else
 
if
 (
currentClass
 != 
ClassType
.
SUBCLASS
) {
      
Lox
.
error
(
expr
.
keyword
,
          
"Can't use 'super' in a class with no superclass."
);
    }
```

---

### 705. Inheritance — Challenges

**Source:** https://craftinginterpreters.com/inheritance.html

```java
class
 
Doughnut
 {
  
cook
() {
    
print
 
"Fry until golden brown."
;
    
inner
();
    
print
 
"Place in a nice box."
;
  }
}


class
 
BostonCream
 < 
Doughnut
 {
  
cook
() {
    
print
 
"Pipe full of custard and coat with chocolate."
;
  }
}


BostonCream
().
cook
();
```

---

### 706. Inheritance — Challenges

**Source:** https://craftinginterpreters.com/inheritance.html

```
Fry until golden brown.
Pipe full of custard and coat with chocolate.
Place in a nice box.
```

---

### 707. Chunks of Bytecode — Chunks of Bytecode

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
fun
 
fib
(
n
) {
  
if
 (
n
 < 
2
) 
return
 
n
;
  
return
 
fib
(
n
 - 
1
) + 
fib
(
n
 - 
2
);
 

}


var
 
before
 = 
clock
();

print
 
fib
(
40
);

var
 
after
 = 
clock
();

print
 
after
 - 
before
;
```

---

### 708. Chunks of Bytecode — 14 . 2 Getting Started

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#include "common.h"



int
 
main
(
int
 
argc
, 
const
 
char
* 
argv
[]) {
  
return
 
0
;
}
```

---

### 709. Chunks of Bytecode — 14 . 2 Getting Started

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#ifndef clox_common_h


#define clox_common_h



#include <stdbool.h>


#include <stddef.h>


#include <stdint.h>



#endif
```

---

### 710. Chunks of Bytecode — 14 . 3 Chunks of Instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#ifndef clox_chunk_h


#define clox_chunk_h



#include "common.h"



#endif
```

---

### 711. Chunks of Bytecode — 14 . 3 Chunks of Instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



typedef
 
enum
 {
  
OP_RETURN
,
} 
OpCode
;
```

---

### 712. Chunks of Bytecode — 14 . 3 Chunks of Instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 713. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



typedef
 
struct
 {
  
uint8_t
* 
code
;
} 
Chunk
;
```

---

### 714. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 715. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
int
 
count
;
  
int
 
capacity
;
```

---

### 716. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  uint8_t* code;
} Chunk;
```

---

### 717. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



void
 
initChunk
(
Chunk
* 
chunk
);
```

---

### 718. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 719. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#include <stdlib.h>



#include "chunk.h"



void
 
initChunk
(
Chunk
* 
chunk
) {
  
chunk
->
count
 = 
0
;
  
chunk
->
capacity
 = 
0
;
  
chunk
->
code
 = 
NULL
;
}
```

---

### 720. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
writeChunk
(
Chunk
* 
chunk
, 
uint8_t
 
byte
);
```

---

### 721. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 722. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
writeChunk
(
Chunk
* 
chunk
, 
uint8_t
 
byte
) {
  
if
 (
chunk
->
capacity
 < 
chunk
->
count
 + 
1
) {
    
int
 
oldCapacity
 = 
chunk
->
capacity
;
    
chunk
->
capacity
 = 
GROW_CAPACITY
(
oldCapacity
);
    
chunk
->
code
 = 
GROW_ARRAY
(
uint8_t
, 
chunk
->
code
,
        
oldCapacity
, 
chunk
->
capacity
);
  }

  
chunk
->
code
[
chunk
->
count
] = 
byte
;
  
chunk
->
count
++;
}
```

---

### 723. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


void initChunk(Chunk* chunk) {
```

---

### 724. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#ifndef clox_memory_h


#define clox_memory_h



#include "common.h"



#define GROW_CAPACITY(capacity) \


    ((capacity) < 8 ? 8 : (capacity) * 2)



#endif
```

---

### 725. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
#define GROW_CAPACITY(capacity) \
    ((capacity) < 8 ? 8 : (capacity) * 2)
```

---

### 726. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



#define GROW_ARRAY(type, pointer, oldCount, newCount) \


    (type*)reallocate(pointer, sizeof(type) * (oldCount), \


        sizeof(type) * (newCount))



void
* 
reallocate
(
void
* 
pointer
, 
size_t
 
oldSize
, 
size_t
 
newSize
);
```

---

### 727. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 728. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#include <stdlib.h>



#include "memory.h"



void
* 
reallocate
(
void
* 
pointer
, 
size_t
 
oldSize
, 
size_t
 
newSize
) {
  
if
 (
newSize
 == 
0
) {
    
free
(
pointer
);
    
return
 
NULL
;
  }

  
void
* 
result
 = 
realloc
(
pointer
, 
newSize
);
  
return
 
result
;
}
```

---

### 729. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  void* result = realloc(pointer, newSize);
```

---

### 730. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
if
 (
result
 == 
NULL
) 
exit
(
1
);
```

---

### 731. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
freeChunk
(
Chunk
* 
chunk
);
```

---

### 732. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void writeChunk(Chunk* chunk, uint8_t byte);
```

---

### 733. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
freeChunk
(
Chunk
* 
chunk
) {
  
FREE_ARRAY
(
uint8_t
, 
chunk
->
code
, 
chunk
->
capacity
);
  
initChunk
(
chunk
);
}
```

---

### 734. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
#define GROW_ARRAY(type, pointer, oldCount, newCount) \
    (type*)reallocate(pointer, sizeof(type) * (oldCount), \
        sizeof(type) * (newCount))
```

---

### 735. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



#define FREE_ARRAY(type, pointer, oldCount) \


    reallocate(pointer, sizeof(type) * (oldCount), 0)
```

---

### 736. Chunks of Bytecode — 14 . 3 . 1 A dynamic array of instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

---

### 737. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
int main(int argc, const char* argv[]) {
```

---

### 738. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
Chunk
 
chunk
;
  
initChunk
(&
chunk
);
  
writeChunk
(&
chunk
, 
OP_RETURN
);
  
freeChunk
(&
chunk
);
```

---

### 739. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c


int main(int argc, const char* argv[]) {
```

---

### 740. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  initChunk(&chunk);
  writeChunk(&chunk, OP_RETURN);
```

---

### 741. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


  
disassembleChunk
(&
chunk
, 
"test chunk"
);
```

---

### 742. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c


int main(int argc, const char* argv[]) {
```

---

### 743. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#ifndef clox_debug_h


#define clox_debug_h



#include "chunk.h"



void
 
disassembleChunk
(
Chunk
* 
chunk
, 
const
 
char
* 
name
);

int
 
disassembleInstruction
(
Chunk
* 
chunk
, 
int
 
offset
);


#endif
```

---

### 744. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#include <stdio.h>



#include "debug.h"



void
 
disassembleChunk
(
Chunk
* 
chunk
, 
const
 
char
* 
name
) {
  
printf
(
"== %s ==
\n
"
, 
name
);

  
for
 (
int
 
offset
 = 
0
; 
offset
 < 
chunk
->
count
;) {
    
offset
 = 
disassembleInstruction
(
chunk
, 
offset
);
  }
}
```

---

### 745. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
int
 
disassembleInstruction
(
Chunk
* 
chunk
, 
int
 
offset
) {
  
printf
(
"%04d "
, 
offset
);

  
uint8_t
 
instruction
 = 
chunk
->
code
[
offset
];
  
switch
 (
instruction
) {
    
case
 
OP_RETURN
:
      
return
 
simpleInstruction
(
"OP_RETURN"
, 
offset
);
    
default
:
      
printf
(
"Unknown opcode %d
\n
"
, 
instruction
);
      
return
 
offset
 + 
1
;
  }
}
```

---

### 746. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
static
 
int
 
simpleInstruction
(
const
 
char
* 
name
, 
int
 
offset
) {
  
printf
(
"%s
\n
"
, 
name
);
  
return
 
offset
 + 
1
;
}
```

---

### 747. Chunks of Bytecode — 14 . 4 Disassembling Chunks

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
== test chunk ==
0000 OP_RETURN
```

---

### 748. Chunks of Bytecode — 14 . 5 Constants

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
1
 + 
2
;
```

---

### 749. Chunks of Bytecode — 14 . 5 . 1 Representing values

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#ifndef clox_value_h


#define clox_value_h



#include "common.h"



typedef
 
double
 
Value
;


#endif
```

---

### 750. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



typedef
 
struct
 {
  
int
 
capacity
;
  
int
 
count
;
  
Value
* 
values
;
} 
ValueArray
;
```

---

### 751. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 752. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```



void
 
initValueArray
(
ValueArray
* 
array
);

void
 
writeValueArray
(
ValueArray
* 
array
, 
Value
 
value
);

void
 
freeValueArray
(
ValueArray
* 
array
);
```

---

### 753. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 754. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```c
#include <stdio.h>



#include "memory.h"


#include "value.h"



void
 
initValueArray
(
ValueArray
* 
array
) {
  
array
->
values
 = 
NULL
;
  
array
->
capacity
 = 
0
;
  
array
->
count
 = 
0
;
}
```

---

### 755. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
writeValueArray
(
ValueArray
* 
array
, 
Value
 
value
) {
  
if
 (
array
->
capacity
 < 
array
->
count
 + 
1
) {
    
int
 
oldCapacity
 = 
array
->
capacity
;
    
array
->
capacity
 = 
GROW_CAPACITY
(
oldCapacity
);
    
array
->
values
 = 
GROW_ARRAY
(
Value
, 
array
->
values
,
                               
oldCapacity
, 
array
->
capacity
);
  }

  
array
->
values
[
array
->
count
] = 
value
;
  
array
->
count
++;
}
```

---

### 756. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
freeValueArray
(
ValueArray
* 
array
) {
  
FREE_ARRAY
(
Value
, 
array
->
values
, 
array
->
capacity
);
  
initValueArray
(
array
);
}
```

---

### 757. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
ValueArray
 
constants
;
```

---

### 758. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


typedef enum {
```

---

### 759. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
initValueArray
(&
chunk
->
constants
);
```

---

### 760. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  FREE_ARRAY(uint8_t, chunk->code, chunk->capacity);
```

---

### 761. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
freeValueArray
(&
chunk
->
constants
);
```

---

### 762. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void writeChunk(Chunk* chunk, uint8_t byte);
```

---

### 763. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
int
 
addConstant
(
Chunk
* 
chunk
, 
Value
 
value
);
```

---

### 764. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 765. Chunks of Bytecode — 14 . 5 . 2 Value arrays

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
int
 
addConstant
(
Chunk
* 
chunk
, 
Value
 
value
) {
  
writeValueArray
(&
chunk
->
constants
, 
value
);
  
return
 
chunk
->
constants
.
count
 - 
1
;
}
```

---

### 766. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
print
 
1
;

print
 
2
;
```

---

### 767. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
OP_CONSTANT
,
```

---

### 768. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


  
int
 
constant
 = 
addConstant
(&
chunk
, 
1.2
);
  
writeChunk
(&
chunk
, 
OP_CONSTANT
);
  
writeChunk
(&
chunk
, 
constant
);
```

---

### 769. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
    
case
 
OP_CONSTANT
:
      
return
 
constantInstruction
(
"OP_CONSTANT"
, 
chunk
, 
offset
);
```

---

### 770. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
static
 
int
 
constantInstruction
(
const
 
char
* 
name
, 
Chunk
* 
chunk
,
                               
int
 
offset
) {
  
uint8_t
 
constant
 = 
chunk
->
code
[
offset
 + 
1
];
  
printf
(
"%-16s %4d '"
, 
name
, 
constant
);
  
printValue
(
chunk
->
constants
.
values
[
constant
]);
  
printf
(
"'
\n
"
);
}
```

---

### 771. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


void disassembleChunk(Chunk* chunk, const char* name) {
```

---

### 772. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
printValue
(
Value
 
value
);
```

---

### 773. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


#endif
```

---

### 774. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
printValue
(
Value
 
value
) {
  
printf
(
"%g"
, 
value
);
}
```

---

### 775. Chunks of Bytecode — 14 . 5 . 3 Constant instructions

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
return
 
offset
 + 
2
;
```

---

### 776. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
int
* 
lines
;
```

---

### 777. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
chunk
->
lines
 = 
NULL
;
```

---

### 778. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  FREE_ARRAY(uint8_t, chunk->code, chunk->capacity);
```

---

### 779. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
FREE_ARRAY
(
int
, 
chunk
->
lines
, 
chunk
->
capacity
);
```

---

### 780. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
writeChunk
(
Chunk
* 
chunk
, 
uint8_t
 
byte
, 
int
 
line
);
```

---

### 781. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
int addConstant(Chunk* chunk, Value value);
```

---

### 782. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
writeChunk
(
Chunk
* 
chunk
, 
uint8_t
 
byte
, 
int
 
line
) {
```

---

### 783. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  if (chunk->capacity < chunk->count + 1) {
```

---

### 784. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
    chunk->code = GROW_ARRAY(uint8_t, chunk->code,
        oldCapacity, chunk->capacity);
```

---

### 785. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
    
chunk
->
lines
 = 
GROW_ARRAY
(
int
, 
chunk
->
lines
,
        
oldCapacity
, 
chunk
->
capacity
);
```

---

### 786. Chunks of Bytecode — 14 . 6 Line Information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
chunk
->
lines
[
chunk
->
count
] = 
line
;
```

---

### 787. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  int constant = addConstant(&chunk, 1.2);
```

---

### 788. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
writeChunk
(&
chunk
, 
OP_CONSTANT
, 
123
);
  
writeChunk
(&
chunk
, 
constant
, 
123
);

  
writeChunk
(&
chunk
, 
OP_RETURN
, 
123
);
```

---

### 789. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


  disassembleChunk(&chunk, "test chunk");
```

---

### 790. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
int disassembleInstruction(Chunk* chunk, int offset) {
  printf("%04d ", offset);
```

---

### 791. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
  
if
 (
offset
 > 
0
 &&
      
chunk
->
lines
[
offset
] == 
chunk
->
lines
[
offset
 - 
1
]) {
    
printf
(
"   | "
);
  } 
else
 {
    
printf
(
"%4d "
, 
chunk
->
lines
[
offset
]);
  }
```

---

### 792. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```


  uint8_t instruction = chunk->code[offset];
```

---

### 793. Chunks of Bytecode — 14 . 6 . 1 Disassembling line information

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
== test chunk ==
0000  123 OP_CONSTANT         0 '1.2'
0002    | OP_RETURN
```

---

### 794. Chunks of Bytecode — Challenges

**Source:** https://craftinginterpreters.com/chunks-of-bytecode.html

```
void
 
writeConstant
(
Chunk
* 
chunk
, 
Value
 
value
, 
int
 
line
) {
  
// Implement me...

}
```

---

### 795. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```c
#ifndef clox_vm_h


#define clox_vm_h



#include "chunk.h"



typedef
 
struct
 {
  
Chunk
* 
chunk
;
} 
VM
;


void
 
initVM
();

void
 
freeVM
();


#endif
```

---

### 796. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```c
#include "common.h"


#include "vm.h"



VM
 
vm
;
 



void
 
initVM
() {
}


void
 
freeVM
() {
}
```

---

### 797. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```c
int main(int argc, const char* argv[]) {
```

---

### 798. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
initVM
();
```

---

### 799. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  disassembleChunk(&chunk, "test chunk");
```

---

### 800. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
freeVM
();
```

---

### 801. A Virtual Machine — 15 . 1 An Instruction Execution Machine

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```c


int main(int argc, const char* argv[]) {
```

---

### 802. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  disassembleChunk(&chunk, "test chunk");
```

---

### 803. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
interpret
(&
chunk
);
```

---

### 804. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
InterpretResult
 
interpret
(
Chunk
* 
chunk
);
```

---

### 805. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


#endif
```

---

### 806. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
typedef
 
enum
 {
  
INTERPRET_OK
,
  
INTERPRET_COMPILE_ERROR
,
  
INTERPRET_RUNTIME_ERROR

} 
InterpretResult
;
```

---

### 807. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
void initVM();
void freeVM();
```

---

### 808. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
InterpretResult
 
interpret
(
Chunk
* 
chunk
) {
  
vm
.
chunk
 = 
chunk
;
  
vm
.
ip
 = 
vm
.
chunk
->
code
;
  
return
 
run
();
}
```

---

### 809. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
typedef struct {
  Chunk* chunk;
```

---

### 810. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
uint8_t
* 
ip
;
```

---

### 811. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
static
 
InterpretResult
 
run
() {

#define READ_BYTE() (*vm.ip++)


  
for
 (;;) {
    
uint8_t
 
instruction
;
    
switch
 (
instruction
 = 
READ_BYTE
()) {
      
case
 
OP_RETURN
: {
        
return
 
INTERPRET_OK
;
      }
    }
  }


#undef READ_BYTE

}
```

---

### 812. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
    switch (instruction = READ_BYTE()) {
```

---

### 813. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
      
case
 
OP_CONSTANT
: {
        
Value
 
constant
 = 
READ_CONSTANT
();
        
printValue
(
constant
);
        
printf
(
"
\n
"
);
        
break
;
      }
```

---

### 814. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

---

### 815. A Virtual Machine — 15 . 1 . 1 Executing instructions

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


  for (;;) {
```

---

### 816. A Virtual Machine — 15 . 1 . 2 Execution tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```



#define DEBUG_TRACE_EXECUTION
```

---

### 817. A Virtual Machine — 15 . 1 . 2 Execution tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


#endif
```

---

### 818. A Virtual Machine — 15 . 1 . 2 Execution tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
#ifdef DEBUG_TRACE_EXECUTION

    
disassembleInstruction
(
vm
.
chunk
,
                           (
int
)(
vm
.
ip
 - 
vm
.
chunk
->
code
));

#endif
```

---

### 819. A Virtual Machine — 15 . 2 A Value Stack Manipulator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
print
 
3
 - 
2
;
```

---

### 820. A Virtual Machine — 15 . 2 A Value Stack Manipulator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
fun
 
echo
(
n
) {
  
print
 
n
;
  
return
 
n
;
}


print
 
echo
(
echo
(
1
) + 
echo
(
2
)) + 
echo
(
echo
(
4
) + 
echo
(
5
));
```

---

### 821. A Virtual Machine — 15 . 2 A Value Stack Manipulator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
1  // from echo(1)
2  // from echo(2)
3  // from echo(1 + 2)
4  // from echo(4)
5  // from echo(5)
9  // from echo(4 + 5)
12 // from print 3 + 9
```

---

### 822. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
typedef struct {
  Chunk* chunk;
  uint8_t* ip;
```

---

### 823. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
Value
 
stack
[
STACK_MAX
];
  
Value
* 
stackTop
;
```

---

### 824. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```



#define STACK_MAX 256
```

---

### 825. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


typedef struct {
```

---

### 826. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


#define STACK_MAX 256
```

---

### 827. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
resetStack
();
```

---

### 828. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
static
 
void
 
resetStack
() {
  
vm
.
stackTop
 = 
vm
.
stack
;
}
```

---

### 829. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
InterpretResult interpret(Chunk* chunk);
```

---

### 830. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
void
 
push
(
Value
 
value
);

Value
 
pop
();
```

---

### 831. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


#endif
```

---

### 832. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
void
 
push
(
Value
 
value
) {
  *
vm
.
stackTop
 = 
value
;
  
vm
.
stackTop
++;
}
```

---

### 833. A Virtual Machine — 15 . 2 . 1 The VM’s Stack

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
Value
 
pop
() {
  
vm
.
stackTop
--;
  
return
 *
vm
.
stackTop
;
}
```

---

### 834. A Virtual Machine — 15 . 2 . 2 Stack tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
    
printf
(
"          "
);
    
for
 (
Value
* 
slot
 = 
vm
.
stack
; 
slot
 < 
vm
.
stackTop
; 
slot
++) {
      
printf
(
"[ "
);
      
printValue
(*
slot
);
      
printf
(
" ]"
);
    }
    
printf
(
"
\n
"
);
```

---

### 835. A Virtual Machine — 15 . 2 . 2 Stack tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
      case OP_CONSTANT: {
        Value constant = READ_CONSTANT();
```

---

### 836. A Virtual Machine — 15 . 2 . 2 Stack tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
        
push
(
constant
);
```

---

### 837. A Virtual Machine — 15 . 2 . 2 Stack tracing

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
        
printValue
(
pop
());
        
printf
(
"
\n
"
);
```

---

### 838. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
var
 
a
 = 
1.2
;

print
 -
a
; 
// -1.2.
```

---

### 839. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
OP_NEGATE
,
```

---

### 840. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
      
case
 
OP_NEGATE
:   
push
(-
pop
()); 
break
;
```

---

### 841. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

---

### 842. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
    
case
 
OP_NEGATE
:
      
return
 
simpleInstruction
(
"OP_NEGATE"
, 
offset
);
```

---

### 843. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
writeChunk
(&
chunk
, 
OP_NEGATE
, 
123
);
```

---

### 844. A Virtual Machine — 15 . 3 An Arithmetic Calculator

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


  writeChunk(&chunk, OP_RETURN, 123);
```

---

### 845. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  
OP_ADD
,
  
OP_SUBTRACT
,
  
OP_MULTIPLY
,
  
OP_DIVIDE
,
```

---

### 846. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
      
case
 
OP_ADD
:      
BINARY_OP
(+); 
break
;
      
case
 
OP_SUBTRACT
: 
BINARY_OP
(-); 
break
;
      
case
 
OP_MULTIPLY
: 
BINARY_OP
(*); 
break
;
      
case
 
OP_DIVIDE
:   
BINARY_OP
(/); 
break
;
```

---

### 847. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
      case OP_NEGATE:   push(-pop()); break;
```

---

### 848. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

---

### 849. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
#define BINARY_OP(op) \


    do { \


      double b = pop(); \


      double a = pop(); \


      push(a op b); \


    } while (false)
```

---

### 850. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


  for (;;) {
```

---

### 851. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
#define WAKE_UP() makeCoffee(); drinkCoffee();
```

---

### 852. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
if
 (
morning
) 
WAKE_UP
();
```

---

### 853. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
if
 (
morning
) 
makeCoffee
(); 
drinkCoffee
();;
```

---

### 854. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
#define WAKE_UP() { makeCoffee(); drinkCoffee(); }
```

---

### 855. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
if
 (
morning
)
  
WAKE_UP
();

else

  
sleepIn
();
```

---

### 856. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

---

### 857. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
    
case
 
OP_ADD
:
      
return
 
simpleInstruction
(
"OP_ADD"
, 
offset
);
    
case
 
OP_SUBTRACT
:
      
return
 
simpleInstruction
(
"OP_SUBTRACT"
, 
offset
);
    
case
 
OP_MULTIPLY
:
      
return
 
simpleInstruction
(
"OP_MULTIPLY"
, 
offset
);
    
case
 
OP_DIVIDE
:
      
return
 
simpleInstruction
(
"OP_DIVIDE"
, 
offset
);
```

---

### 858. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  int constant = addConstant(&chunk, 1.2);
  writeChunk(&chunk, OP_CONSTANT, 123);
  writeChunk(&chunk, constant, 123);
```

---

### 859. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```


  
constant
 = 
addConstant
(&
chunk
, 
3.4
);
  
writeChunk
(&
chunk
, 
OP_CONSTANT
, 
123
);
  
writeChunk
(&
chunk
, 
constant
, 
123
);

  
writeChunk
(&
chunk
, 
OP_ADD
, 
123
);

  
constant
 = 
addConstant
(&
chunk
, 
5.6
);
  
writeChunk
(&
chunk
, 
OP_CONSTANT
, 
123
);
  
writeChunk
(&
chunk
, 
constant
, 
123
);

  
writeChunk
(&
chunk
, 
OP_DIVIDE
, 
123
);
```

---

### 860. A Virtual Machine — 15 . 3 . 1 Binary operators

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
  writeChunk(&chunk, OP_NEGATE, 123);

  writeChunk(&chunk, OP_RETURN, 123);
```

---

### 861. A Virtual Machine — Challenges

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
1
 * 
2
 + 
3


1
 + 
2
 * 
3


3
 - 
2
 - 
1


1
 + 
2
 * 
3
 - 
4
 / -
5
```

---

### 862. A Virtual Machine — Challenges

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
4
 - 
3
 * -
2
```

---

### 863. A Virtual Machine — Design Note: Register-Based Bytecode

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
var
 
a
 = 
1
;

var
 
b
 = 
2
;

var
 
c
 = 
a
 + 
b
;
```

---

### 864. A Virtual Machine — Design Note: Register-Based Bytecode

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
load
 <
a
>  
// Read local variable a and push onto stack.


load
 <
b
>  
// Read local variable b and push onto stack.


add
       
// Pop two values, add, push result.


store
 <
c
> 
// Pop value and store in local variable c.
```

---

### 865. A Virtual Machine — Design Note: Register-Based Bytecode

**Source:** https://craftinginterpreters.com/a-virtual-machine.html

```
add
 <
a
> <
b
> <
c
> 
// Read values from a and b, add, store in c.
```

---

### 866. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```c
int main(int argc, const char* argv[]) {
  initVM();
```

---

### 867. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
if
 (
argc
 == 
1
) {
    
repl
();
  } 
else
 
if
 (
argc
 == 
2
) {
    
runFile
(
argv
[
1
]);
  } 
else
 {
    
fprintf
(
stderr
, 
"Usage: clox [path]
\n
"
);
    
exit
(
64
);
  }

  
freeVM
();
```

---

### 868. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  return 0;
}
```

---

### 869. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```c
#include <stdio.h>


#include <stdlib.h>


#include <string.h>
```

---

### 870. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```



static
 
void
 
repl
() {
  
char
 
line
[
1024
];
  
for
 (;;) {
    
printf
(
"> "
);

    
if
 (!
fgets
(
line
, 
sizeof
(
line
), 
stdin
)) {
      
printf
(
"
\n
"
);
      
break
;
    }

    
interpret
(
line
);
  }
}
```

---

### 871. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
void
 
runFile
(
const
 
char
* 
path
) {
  
char
* 
source
 = 
readFile
(
path
);
  
InterpretResult
 
result
 = 
interpret
(
source
);
  
free
(
source
);
 


  
if
 (
result
 == 
INTERPRET_COMPILE_ERROR
) 
exit
(
65
);
  
if
 (
result
 == 
INTERPRET_RUNTIME_ERROR
) 
exit
(
70
);
}
```

---

### 872. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
char
* 
readFile
(
const
 
char
* 
path
) {
  
FILE
* 
file
 = 
fopen
(
path
, 
"rb"
);

  
fseek
(
file
, 
0L
, 
SEEK_END
);
  
size_t
 
fileSize
 = 
ftell
(
file
);
  
rewind
(
file
);

  
char
* 
buffer
 = (
char
*)
malloc
(
fileSize
 + 
1
);
  
size_t
 
bytesRead
 = 
fread
(
buffer
, 
sizeof
(
char
), 
fileSize
, 
file
);
  
buffer
[
bytesRead
] = 
'\0'
;

  
fclose
(
file
);
  
return
 
buffer
;
}
```

---

### 873. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
if
 (
file
 == 
NULL
) {
    
fprintf
(
stderr
, 
"Could not open file 
\"
%s
\"
.
\n
"
, 
path
);
    
exit
(
74
);
  }
```

---

### 874. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


  fseek(file, 0L, SEEK_END);
```

---

### 875. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  char* buffer = (char*)malloc(fileSize + 1);
```

---

### 876. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
if
 (
buffer
 == 
NULL
) {
    
fprintf
(
stderr
, 
"Not enough memory to read 
\"
%s
\"
.
\n
"
, 
path
);
    
exit
(
74
);
  }
```

---

### 877. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  size_t bytesRead = fread(buffer, sizeof(char), fileSize, file);
```

---

### 878. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  size_t bytesRead = fread(buffer, sizeof(char), fileSize, file);
```

---

### 879. Scanning on Demand — 16 . 1 Spinning Up the Interpreter

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
if
 (
bytesRead
 < 
fileSize
) {
    
fprintf
(
stderr
, 
"Could not read file 
\"
%s
\"
.
\n
"
, 
path
);
    
exit
(
74
);
  }
```

---

### 880. Scanning on Demand — 16 . 1 . 1 Opening the compilation pipeline

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
InterpretResult
 
interpret
(
const
 
char
* 
source
);
```

---

### 881. Scanning on Demand — 16 . 1 . 1 Opening the compilation pipeline

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
InterpretResult
 
interpret
(
const
 
char
* 
source
) {
  
compile
(
source
);
  
return
 
INTERPRET_OK
;
```

---

### 882. Scanning on Demand — 16 . 1 . 1 Opening the compilation pipeline

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
#ifndef clox_compiler_h


#define clox_compiler_h



void
 
compile
(
const
 
char
* 
source
);


#endif
```

---

### 883. Scanning on Demand — 16 . 1 . 1 Opening the compilation pipeline

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```c
#include <stdio.h>



#include "common.h"


#include "compiler.h"


#include "scanner.h"



void
 
compile
(
const
 
char
* 
source
) {
  
initScanner
(
source
);
}
```

---

### 884. Scanning on Demand — 16 . 1 . 2 The scanner scans

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
#ifndef clox_scanner_h


#define clox_scanner_h



void
 
initScanner
(
const
 
char
* 
source
);


#endif
```

---

### 885. Scanning on Demand — 16 . 1 . 2 The scanner scans

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```c
#include <stdio.h>


#include <string.h>



#include "common.h"


#include "scanner.h"



typedef
 
struct
 {
  
const
 
char
* 
start
;
  
const
 
char
* 
current
;
  
int
 
line
;
} 
Scanner
;


Scanner
 
scanner
;
```

---

### 886. Scanning on Demand — 16 . 1 . 2 The scanner scans

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
void
 
initScanner
(
const
 
char
* 
source
) {
  
scanner
.
start
 = 
source
;
  
scanner
.
current
 = 
source
;
  
scanner
.
line
 = 
1
;
}
```

---

### 887. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
int
 
line
 = -
1
;
  
for
 (;;) {
    
Token
 
token
 = 
scanToken
();
    
if
 (
token
.
line
 != 
line
) {
      
printf
(
"%4d "
, 
token
.
line
);
      
line
 = 
token
.
line
;
    } 
else
 {
      
printf
(
"   | "
);
    }
    
printf
(
"%2d '%.*s'
\n
"
, 
token
.
type
, 
token
.
length
, 
token
.
start
);
 


    
if
 (
token
.
type
 == 
TOKEN_EOF
) 
break
;
  }
```

---

### 888. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
print
 
1
 + 
2
;
```

---

### 889. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
   1 31 'print'
   | 21 '1'
   |  7 '+'
   | 21 '2'
   |  8 ';'
   2 39 ''
```

---

### 890. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
Token
 
scanToken
();
```

---

### 891. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


#endif
```

---

### 892. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```



typedef
 
struct
 {
  
TokenType
 
type
;
  
const
 
char
* 
start
;
  
int
 
length
;
  
int
 
line
;
} 
Token
;
```

---

### 893. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


void initScanner(const char* source);
```

---

### 894. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
#ifndef clox_scanner_h
#define clox_scanner_h
```

---

### 895. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```



typedef
 
enum
 {
  
// Single-character tokens.

  
TOKEN_LEFT_PAREN
, 
TOKEN_RIGHT_PAREN
,
  
TOKEN_LEFT_BRACE
, 
TOKEN_RIGHT_BRACE
,
  
TOKEN_COMMA
, 
TOKEN_DOT
, 
TOKEN_MINUS
, 
TOKEN_PLUS
,
  
TOKEN_SEMICOLON
, 
TOKEN_SLASH
, 
TOKEN_STAR
,
  
// One or two character tokens.

  
TOKEN_BANG
, 
TOKEN_BANG_EQUAL
,
  
TOKEN_EQUAL
, 
TOKEN_EQUAL_EQUAL
,
  
TOKEN_GREATER
, 
TOKEN_GREATER_EQUAL
,
  
TOKEN_LESS
, 
TOKEN_LESS_EQUAL
,
  
// Literals.

  
TOKEN_IDENTIFIER
, 
TOKEN_STRING
, 
TOKEN_NUMBER
,
  
// Keywords.

  
TOKEN_AND
, 
TOKEN_CLASS
, 
TOKEN_ELSE
, 
TOKEN_FALSE
,
  
TOKEN_FOR
, 
TOKEN_FUN
, 
TOKEN_IF
, 
TOKEN_NIL
, 
TOKEN_OR
,
  
TOKEN_PRINT
, 
TOKEN_RETURN
, 
TOKEN_SUPER
, 
TOKEN_THIS
,
  
TOKEN_TRUE
, 
TOKEN_VAR
, 
TOKEN_WHILE
,

  
TOKEN_ERROR
, 
TOKEN_EOF

} 
TokenType
;
```

---

### 896. Scanning on Demand — 16 . 2 A Token at a Time

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


typedef struct {
```

---

### 897. Scanning on Demand — 16 . 2 . 1 Scanning tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
Token
 
scanToken
() {
  
scanner
.
start
 = 
scanner
.
current
;

  
if
 (
isAtEnd
()) 
return
 
makeToken
(
TOKEN_EOF
);

  
return
 
errorToken
(
"Unexpected character."
);
}
```

---

### 898. Scanning on Demand — 16 . 2 . 1 Scanning tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
bool
 
isAtEnd
() {
  
return
 *
scanner
.
current
 == 
'\0'
;
}
```

---

### 899. Scanning on Demand — 16 . 2 . 1 Scanning tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
Token
 
makeToken
(
TokenType
 
type
) {
  
Token
 
token
;
  
token
.
type
 = 
type
;
  
token
.
start
 = 
scanner
.
start
;
  
token
.
length
 = (
int
)(
scanner
.
current
 - 
scanner
.
start
);
  
token
.
line
 = 
scanner
.
line
;
  
return
 
token
;
}
```

---

### 900. Scanning on Demand — 16 . 2 . 1 Scanning tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
Token
 
errorToken
(
const
 
char
* 
message
) {
  
Token
 
token
;
  
token
.
type
 = 
TOKEN_ERROR
;
  
token
.
start
 = 
message
;
  
token
.
length
 = (
int
)
strlen
(
message
);
  
token
.
line
 = 
scanner
.
line
;
  
return
 
token
;
}
```

---

### 901. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  if (isAtEnd()) return makeToken(TOKEN_EOF);
```

---

### 902. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


  
char
 
c
 = 
advance
();

  
switch
 (
c
) {
    
case
 
'('
: 
return
 
makeToken
(
TOKEN_LEFT_PAREN
);
    
case
 
')'
: 
return
 
makeToken
(
TOKEN_RIGHT_PAREN
);
    
case
 
'{'
: 
return
 
makeToken
(
TOKEN_LEFT_BRACE
);
    
case
 
'}'
: 
return
 
makeToken
(
TOKEN_RIGHT_BRACE
);
    
case
 
';'
: 
return
 
makeToken
(
TOKEN_SEMICOLON
);
    
case
 
','
: 
return
 
makeToken
(
TOKEN_COMMA
);
    
case
 
'.'
: 
return
 
makeToken
(
TOKEN_DOT
);
    
case
 
'-'
: 
return
 
makeToken
(
TOKEN_MINUS
);
    
case
 
'+'
: 
return
 
makeToken
(
TOKEN_PLUS
);
    
case
 
'/'
: 
return
 
makeToken
(
TOKEN_SLASH
);
    
case
 
'*'
: 
return
 
makeToken
(
TOKEN_STAR
);
  }
```

---

### 903. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


  return errorToken("Unexpected character.");
```

---

### 904. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
char
 
advance
() {
  
scanner
.
current
++;
  
return
 
scanner
.
current
[-
1
];
}
```

---

### 905. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    case '*': return makeToken(TOKEN_STAR);
```

---

### 906. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    
case
 
'!'
:
      
return
 
makeToken
(
          
match
(
'='
) ? 
TOKEN_BANG_EQUAL
 : 
TOKEN_BANG
);
    
case
 
'='
:
      
return
 
makeToken
(
          
match
(
'='
) ? 
TOKEN_EQUAL_EQUAL
 : 
TOKEN_EQUAL
);
    
case
 
'<'
:
      
return
 
makeToken
(
          
match
(
'='
) ? 
TOKEN_LESS_EQUAL
 : 
TOKEN_LESS
);
    
case
 
'>'
:
      
return
 
makeToken
(
          
match
(
'='
) ? 
TOKEN_GREATER_EQUAL
 : 
TOKEN_GREATER
);
```

---

### 907. Scanning on Demand — 16 . 3 A Lexical Grammar for Lox

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
bool
 
match
(
char
 
expected
) {
  
if
 (
isAtEnd
()) 
return
 
false
;
  
if
 (*
scanner
.
current
 != 
expected
) 
return
 
false
;
  
scanner
.
current
++;
  
return
 
true
;
}
```

---

### 908. Scanning on Demand — 16 . 3 . 1 Whitespace

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
skipWhitespace
();
```

---

### 909. Scanning on Demand — 16 . 3 . 1 Whitespace

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
void
 
skipWhitespace
() {
  
for
 (;;) {
    
char
 
c
 = 
peek
();
    
switch
 (
c
) {
      
case
 
' '
:
      
case
 
'\r'
:
      
case
 
'\t'
:
        
advance
();
        
break
;
      
default
:
        
return
;
    }
  }
}
```

---

### 910. Scanning on Demand — 16 . 3 . 1 Whitespace

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
char
 
peek
() {
  
return
 *
scanner
.
current
;
}
```

---

### 911. Scanning on Demand — 16 . 3 . 1 Whitespace

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
      
case
 
'\n'
:
        
scanner
.
line
++;
        
advance
();
        
break
;
```

---

### 912. Scanning on Demand — 16 . 3 . 1 Whitespace

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
      default:
        return;
```

---

### 913. Scanning on Demand — 16 . 3 . 2 Comments

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
      
case
 
'/'
:
        
if
 (
peekNext
() == 
'/'
) {
          
// A comment goes until the end of the line.

          
while
 (
peek
() != 
'\n'
 && !
isAtEnd
()) 
advance
();
        } 
else
 {
          
return
;
        }
        
break
;
```

---

### 914. Scanning on Demand — 16 . 3 . 2 Comments

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
      default:
        return;
```

---

### 915. Scanning on Demand — 16 . 3 . 2 Comments

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
char
 
peekNext
() {
  
if
 (
isAtEnd
()) 
return
 
'\0'
;
  
return
 
scanner
.
current
[
1
];
}
```

---

### 916. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
          match('=') ? TOKEN_GREATER_EQUAL : TOKEN_GREATER);
```

---

### 917. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    
case
 
'"'
: 
return
 
string
();
```

---

### 918. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
Token
 
string
() {
  
while
 (
peek
() != 
'"'
 && !
isAtEnd
()) {
    
if
 (
peek
() == 
'\n'
) 
scanner
.
line
++;
    
advance
();
  }

  
if
 (
isAtEnd
()) 
return
 
errorToken
(
"Unterminated string."
);

  
// The closing quote.

  
advance
();
  
return
 
makeToken
(
TOKEN_STRING
);
}
```

---

### 919. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
if
 (
isDigit
(
c
)) 
return
 
number
();
```

---

### 920. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```


  switch (c) {
```

---

### 921. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
bool
 
isDigit
(
char
 
c
) {
  
return
 
c
 >= 
'0'
 && 
c
 <= 
'9'
;
}
```

---

### 922. Scanning on Demand — 16 . 3 . 3 Literal tokens

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
Token
 
number
() {
  
while
 (
isDigit
(
peek
())) 
advance
();

  
// Look for a fractional part.

  
if
 (
peek
() == 
'.'
 && 
isDigit
(
peekNext
())) {
    
// Consume the ".".

    
advance
();

    
while
 (
isDigit
(
peek
())) 
advance
();
  }

  
return
 
makeToken
(
TOKEN_NUMBER
);
}
```

---

### 923. Scanning on Demand — 16 . 4 Identifiers and Keywords

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
if
 (
isAlpha
(
c
)) 
return
 
identifier
();
```

---

### 924. Scanning on Demand — 16 . 4 Identifiers and Keywords

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
bool
 
isAlpha
(
char
 
c
) {
  
return
 (
c
 >= 
'a'
 && 
c
 <= 
'z'
) ||
         (
c
 >= 
'A'
 && 
c
 <= 
'Z'
) ||
          
c
 == 
'_'
;
}
```

---

### 925. Scanning on Demand — 16 . 4 Identifiers and Keywords

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
Token
 
identifier
() {
  
while
 (
isAlpha
(
peek
()) || 
isDigit
(
peek
())) 
advance
();
  
return
 
makeToken
(
identifierType
());
}
```

---

### 926. Scanning on Demand — 16 . 4 Identifiers and Keywords

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
TokenType
 
identifierType
() {
  
return
 
TOKEN_IDENTIFIER
;
}
```

---

### 927. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
  
switch
 (
scanner
.
start
[
0
]) {
    
case
 
'a'
: 
return
 
checkKeyword
(
1
, 
2
, 
"nd"
, 
TOKEN_AND
);
    
case
 
'c'
: 
return
 
checkKeyword
(
1
, 
4
, 
"lass"
, 
TOKEN_CLASS
);
    
case
 
'e'
: 
return
 
checkKeyword
(
1
, 
3
, 
"lse"
, 
TOKEN_ELSE
);
    
case
 
'i'
: 
return
 
checkKeyword
(
1
, 
1
, 
"f"
, 
TOKEN_IF
);
    
case
 
'n'
: 
return
 
checkKeyword
(
1
, 
2
, 
"il"
, 
TOKEN_NIL
);
    
case
 
'o'
: 
return
 
checkKeyword
(
1
, 
1
, 
"r"
, 
TOKEN_OR
);
    
case
 
'p'
: 
return
 
checkKeyword
(
1
, 
4
, 
"rint"
, 
TOKEN_PRINT
);
    
case
 
'r'
: 
return
 
checkKeyword
(
1
, 
5
, 
"eturn"
, 
TOKEN_RETURN
);
    
case
 
's'
: 
return
 
checkKeyword
(
1
, 
4
, 
"uper"
, 
TOKEN_SUPER
);
    
case
 
'v'
: 
return
 
checkKeyword
(
1
, 
2
, 
"ar"
, 
TOKEN_VAR
);
    
case
 
'w'
: 
return
 
checkKeyword
(
1
, 
4
, 
"hile"
, 
TOKEN_WHILE
);
  }
```

---

### 928. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
static
 
TokenType
 
checkKeyword
(
int
 
start
, 
int
 
length
,
    
const
 
char
* 
rest
, 
TokenType
 
type
) {
  
if
 (
scanner
.
current
 - 
scanner
.
start
 == 
start
 + 
length
 &&
      
memcmp
(
scanner
.
start
 + 
start
, 
rest
, 
length
) == 
0
) {
    
return
 
type
;
  }

  
return
 
TOKEN_IDENTIFIER
;
}
```

---

### 929. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    case 'e': return checkKeyword(1, 3, "lse", TOKEN_ELSE);
```

---

### 930. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    
case
 
'f'
:
      
if
 (
scanner
.
current
 - 
scanner
.
start
 > 
1
) {
        
switch
 (
scanner
.
start
[
1
]) {
          
case
 
'a'
: 
return
 
checkKeyword
(
2
, 
3
, 
"lse"
, 
TOKEN_FALSE
);
          
case
 
'o'
: 
return
 
checkKeyword
(
2
, 
1
, 
"r"
, 
TOKEN_FOR
);
          
case
 
'u'
: 
return
 
checkKeyword
(
2
, 
1
, 
"n"
, 
TOKEN_FUN
);
        }
      }
      
break
;
```

---

### 931. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    case 'i': return checkKeyword(1, 1, "f", TOKEN_IF);
```

---

### 932. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    case 's': return checkKeyword(1, 4, "uper", TOKEN_SUPER);
```

---

### 933. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    
case
 
't'
:
      
if
 (
scanner
.
current
 - 
scanner
.
start
 > 
1
) {
        
switch
 (
scanner
.
start
[
1
]) {
          
case
 
'h'
: 
return
 
checkKeyword
(
2
, 
2
, 
"is"
, 
TOKEN_THIS
);
          
case
 
'r'
: 
return
 
checkKeyword
(
2
, 
2
, 
"ue"
, 
TOKEN_TRUE
);
        }
      }
      
break
;
```

---

### 934. Scanning on Demand — 16 . 4 . 1 Tries and state machines

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
    case 'v': return checkKeyword(1, 2, "ar", TOKEN_VAR);
```

---

### 935. Scanning on Demand — Challenges

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
var
 
drink
 = 
"Tea"
;

var
 
steep
 = 
4
;

var
 
cool
 = 
2
;

print
 
"${drink} will be ready in ${steep + cool} minutes."
;
```

---

### 936. Scanning on Demand — Challenges

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
"Nested ${"interpolation?! Are you ${"mad?!"}"}"
```

---

### 937. Scanning on Demand — Challenges

**Source:** https://craftinginterpreters.com/scanning-on-demand.html

```
vector
<
vector
<
string
>> 
nestedVectors
;
```

---

### 938. Compiling Expressions — Compiling Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
InterpretResult interpret(const char* source) {
```

---

### 939. Compiling Expressions — Compiling Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
Chunk
 
chunk
;
  
initChunk
(&
chunk
);

  
if
 (!
compile
(
source
, &
chunk
)) {
    
freeChunk
(&
chunk
);
    
return
 
INTERPRET_COMPILE_ERROR
;
  }

  
vm
.
chunk
 = &
chunk
;
  
vm
.
ip
 = 
vm
.
chunk
->
code
;

  
InterpretResult
 
result
 = 
run
();

  
freeChunk
(&
chunk
);
  
return
 
result
;
```

---

### 940. Compiling Expressions — Compiling Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```c
#include "vm.h"



bool
 
compile
(
const
 
char
* 
source
, 
Chunk
* 
chunk
);
```

---

### 941. Compiling Expressions — Compiling Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


#endif
```

---

### 942. Compiling Expressions — Compiling Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
bool
 
compile
(
const
 
char
* 
source
, 
Chunk
* 
chunk
) {
```

---

### 943. Compiling Expressions — Compiling Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
advance
();
  
expression
();
  
consume
(
TOKEN_EOF
, 
"Expect end of expression."
);
```

---

### 944. Compiling Expressions — 17 . 2 Parsing Tokens

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```



static
 
void
 
advance
() {
  
parser
.
previous
 = 
parser
.
current
;

  
for
 (;;) {
    
parser
.
current
 = 
scanToken
();
    
if
 (
parser
.
current
.
type
 != 
TOKEN_ERROR
) 
break
;

    
errorAtCurrent
(
parser
.
current
.
start
);
  }
}
```

---

### 945. Compiling Expressions — 17 . 2 Parsing Tokens

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```



typedef
 
struct
 {
  
Token
 
current
;
  
Token
 
previous
;
} 
Parser
;


Parser
 
parser
;
```

---

### 946. Compiling Expressions — 17 . 2 Parsing Tokens

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


static void advance() {
```

---

### 947. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
errorAtCurrent
(
const
 
char
* 
message
) {
  
errorAt
(&
parser
.
current
, 
message
);
}
```

---

### 948. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
error
(
const
 
char
* 
message
) {
  
errorAt
(&
parser
.
previous
, 
message
);
}
```

---

### 949. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
errorAt
(
Token
* 
token
, 
const
 
char
* 
message
) {
  
fprintf
(
stderr
, 
"[line %d] Error"
, 
token
->
line
);

  
if
 (
token
->
type
 == 
TOKEN_EOF
) {
    
fprintf
(
stderr
, 
" at end"
);
  } 
else
 
if
 (
token
->
type
 == 
TOKEN_ERROR
) {
    
// Nothing.

  } 
else
 {
    
fprintf
(
stderr
, 
" at '%.*s'"
, 
token
->
length
, 
token
->
start
);
  }

  
fprintf
(
stderr
, 
": %s
\n
"
, 
message
);
  
parser
.
hadError
 = 
true
;
}
```

---

### 950. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
bool
 
hadError
;
```

---

### 951. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  consume(TOKEN_EOF, "Expect end of expression.");
```

---

### 952. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
return
 !
parser
.
hadError
;
```

---

### 953. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
bool
 
panicMode
;
```

---

### 954. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static void errorAt(Token* token, const char* message) {
```

---

### 955. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
parser
.
panicMode
 = 
true
;
```

---

### 956. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  fprintf(stderr, "[line %d] Error", token->line);
```

---

### 957. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static void errorAt(Token* token, const char* message) {
```

---

### 958. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
if
 (
parser
.
panicMode
) 
return
;
```

---

### 959. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


  
parser
.
hadError
 = 
false
;
  
parser
.
panicMode
 = 
false
;
```

---

### 960. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```c


#include "common.h"
```

---

### 961. Compiling Expressions — 17 . 2 . 1 Handling syntax errors

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
consume
(
TokenType
 
type
, 
const
 
char
* 
message
) {
  
if
 (
parser
.
current
.
type
 == 
type
) {
    
advance
();
    
return
;
  }

  
errorAtCurrent
(
message
);
}
```

---

### 962. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
emitByte
(
uint8_t
 
byte
) {
  
writeChunk
(
currentChunk
(), 
byte
, 
parser
.
previous
.
line
);
}
```

---

### 963. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
Chunk
* 
compilingChunk
;


static
 
Chunk
* 
currentChunk
() {
  
return
 
compilingChunk
;
}
```

---

### 964. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static void errorAt(Token* token, const char* message) {
```

---

### 965. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
bool compile(const char* source, Chunk* chunk) {
  initScanner(source);
```

---

### 966. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
compilingChunk
 = 
chunk
;
```

---

### 967. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


  parser.hadError = false;
```

---

### 968. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  consume(TOKEN_EOF, "Expect end of expression.");
```

---

### 969. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
endCompiler
();
```

---

### 970. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
endCompiler
() {
  
emitReturn
();
}
```

---

### 971. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
emitReturn
() {
  
emitByte
(
OP_RETURN
);
}
```

---

### 972. Compiling Expressions — 17 . 3 Emitting Bytecode

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
emitBytes
(
uint8_t
 
byte1
, 
uint8_t
 
byte2
) {
  
emitByte
(
byte1
);
  
emitByte
(
byte2
);
}
```

---

### 973. Compiling Expressions — 17 . 4 Parsing Prefix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
expression
() {
  
// What goes here?

}
```

---

### 974. Compiling Expressions — 17 . 4 . 1 Parsers for tokens

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
number
() {
  
double
 
value
 = 
strtod
(
parser
.
previous
.
start
, 
NULL
);
  
emitConstant
(
value
);
}
```

---

### 975. Compiling Expressions — 17 . 4 . 1 Parsers for tokens

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
emitConstant
(
Value
 
value
) {
  
emitBytes
(
OP_CONSTANT
, 
makeConstant
(
value
));
}
```

---

### 976. Compiling Expressions — 17 . 4 . 1 Parsers for tokens

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
uint8_t
 
makeConstant
(
Value
 
value
) {
  
int
 
constant
 = 
addConstant
(
currentChunk
(), 
value
);
  
if
 (
constant
 > 
UINT8_MAX
) {
    
error
(
"Too many constants in one chunk."
);
    
return
 
0
;
  }

  
return
 (
uint8_t
)
constant
;
}
```

---

### 977. Compiling Expressions — 17 . 4 . 2 Parentheses for grouping

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
grouping
() {
  
expression
();
  
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after expression."
);
}
```

---

### 978. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
unary
() {
  
TokenType
 
operatorType
 = 
parser
.
previous
.
type
;

  
// Compile the operand.

  
expression
();

  
// Emit the operator instruction.

  
switch
 (
operatorType
) {
    
case
 
TOKEN_MINUS
: 
emitByte
(
OP_NEGATE
); 
break
;
    
default
: 
return
; 
// Unreachable.

  }
}
```

---

### 979. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
print
 -
  
true
;
```

---

### 980. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
-
a
.
b
 + 
c
;
```

---

### 981. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
parsePrecedence
(
Precedence
 
precedence
) {
  
// What goes here?

}
```

---

### 982. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```



typedef
 
enum
 {
  
PREC_NONE
,
  
PREC_ASSIGNMENT
,  
// =

  
PREC_OR
,          
// or

  
PREC_AND
,         
// and

  
PREC_EQUALITY
,    
// == !=

  
PREC_COMPARISON
,  
// < > <= >=

  
PREC_TERM
,        
// + -

  
PREC_FACTOR
,      
// * /

  
PREC_UNARY
,       
// ! -

  
PREC_CALL
,        
// . ()

  
PREC_PRIMARY

} 
Precedence
;
```

---

### 983. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


Parser parser;
```

---

### 984. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
-
a
.
b
 + 
c
```

---

### 985. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
parsePrecedence
(
PREC_ASSIGNMENT
);
```

---

### 986. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
parsePrecedence
(
PREC_UNARY
);
```

---

### 987. Compiling Expressions — 17 . 4 . 3 Unary negation

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


  // Emit the operator instruction.
```

---

### 988. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
1
 + 
2
```

---

### 989. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
void
 
binary
() {
  
TokenType
 
operatorType
 = 
parser
.
previous
.
type
;
  
ParseRule
* 
rule
 = 
getRule
(
operatorType
);
  
parsePrecedence
((
Precedence
)(
rule
->
precedence
 + 
1
));

  
switch
 (
operatorType
) {
    
case
 
TOKEN_PLUS
:          
emitByte
(
OP_ADD
); 
break
;
    
case
 
TOKEN_MINUS
:         
emitByte
(
OP_SUBTRACT
); 
break
;
    
case
 
TOKEN_STAR
:          
emitByte
(
OP_MULTIPLY
); 
break
;
    
case
 
TOKEN_SLASH
:         
emitByte
(
OP_DIVIDE
); 
break
;
    
default
: 
return
; 
// Unreachable.

  }
}
```

---

### 990. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
2
 * 
3
 + 
4
```

---

### 991. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
1
 + 
2
 + 
3
 + 
4
```

---

### 992. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
((
1
 + 
2
) + 
3
) + 
4
```

---

### 993. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
a
 = 
b
 = 
c
 = 
d
```

---

### 994. Compiling Expressions — 17 . 5 Parsing Infix Expressions

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
a
 = (
b
 = (
c
 = 
d
))
```

---

### 995. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```



typedef
 
struct
 {
  
ParseFn
 
prefix
;
  
ParseFn
 
infix
;
  
Precedence
 
precedence
;
} 
ParseRule
;
```

---

### 996. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


Parser parser;
```

---

### 997. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```



typedef
 
void
 (*
ParseFn
)();
```

---

### 998. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


typedef struct {
```

---

### 999. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
ParseRule
 
rules
[] = {
  [
TOKEN_LEFT_PAREN
]    = {
grouping
, 
NULL
,   
PREC_NONE
},
  [
TOKEN_RIGHT_PAREN
]   = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_LEFT_BRACE
]    = {
NULL
,     
NULL
,   
PREC_NONE
},
 

  [
TOKEN_RIGHT_BRACE
]   = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_COMMA
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_DOT
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_MINUS
]         = {
unary
,    
binary
, 
PREC_TERM
},
  [
TOKEN_PLUS
]          = {
NULL
,     
binary
, 
PREC_TERM
},
  [
TOKEN_SEMICOLON
]     = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_SLASH
]         = {
NULL
,     
binary
, 
PREC_FACTOR
},
  [
TOKEN_STAR
]          = {
NULL
,     
binary
, 
PREC_FACTOR
},
  [
TOKEN_BANG
]          = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_BANG_EQUAL
]    = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_EQUAL
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_EQUAL_EQUAL
]   = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_GREATER
]       = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_GREATER_EQUAL
] = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_LESS
]          = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_LESS_EQUAL
]    = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_IDENTIFIER
]    = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_STRING
]        = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_NUMBER
]        = {
number
,   
NULL
,   
PREC_NONE
},
  [
TOKEN_AND
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_CLASS
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_ELSE
]          = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_FALSE
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_FOR
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_FUN
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_IF
]            = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_NIL
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_OR
]            = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_PRINT
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_RETURN
]        = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_SUPER
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_THIS
]          = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_TRUE
]          = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_VAR
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_WHILE
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_ERROR
]         = {
NULL
,     
NULL
,   
PREC_NONE
},
  [
TOKEN_EOF
]           = {
NULL
,     
NULL
,   
PREC_NONE
},
};
```

---

### 1000. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static
 
ParseRule
* 
getRule
(
TokenType
 
type
) {
  
return
 &
rules
[
type
];
}
```

---

### 1001. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  emitReturn();
}
```

---

### 1002. Compiling Expressions — 17 . 6 A Pratt Parser

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```



static
 
void
 
expression
();

static
 
ParseRule
* 
getRule
(
TokenType
 
type
);

static
 
void
 
parsePrecedence
(
Precedence
 
precedence
);
```

---

### 1003. Compiling Expressions — 17 . 6 . 1 Parsing with precedence

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
static void parsePrecedence(Precedence precedence) {
```

---

### 1004. Compiling Expressions — 17 . 6 . 1 Parsing with precedence

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
  
advance
();
  
ParseFn
 
prefixRule
 = 
getRule
(
parser
.
previous
.
type
)->
prefix
;
  
if
 (
prefixRule
 == 
NULL
) {
    
error
(
"Expect expression."
);
    
return
;
  }

  
prefixRule
();
```

---

### 1005. Compiling Expressions — 17 . 6 . 1 Parsing with precedence

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


  
while
 (
precedence
 <= 
getRule
(
parser
.
current
.
type
)->
precedence
) {
    
advance
();
    
ParseFn
 
infixRule
 = 
getRule
(
parser
.
previous
.
type
)->
infix
;
    
infixRule
();
  }
```

---

### 1006. Compiling Expressions — 17 . 7 Dumping Chunks

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
#ifdef DEBUG_PRINT_CODE

  
if
 (!
parser
.
hadError
) {
    
disassembleChunk
(
currentChunk
(), 
"code"
);
  }

#endif
```

---

### 1007. Compiling Expressions — 17 . 7 Dumping Chunks

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```c



#ifdef DEBUG_PRINT_CODE


#include "debug.h"


#endif
```

---

### 1008. Compiling Expressions — 17 . 7 Dumping Chunks

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```


typedef struct {
```

---

### 1009. Compiling Expressions — Challenges

**Source:** https://craftinginterpreters.com/compiling-expressions.html

```
(-
1
 + 
2
) * 
3
 - -
4
```

---

### 1010. Types of Values — 18 . 1 Tagged Unions

**Source:** https://craftinginterpreters.com/types-of-values.html

```
typedef
 
enum
 {
  
VAL_BOOL
,
  
VAL_NIL
,
 

  
VAL_NUMBER
,
} 
ValueType
;
```

---

### 1011. Types of Values — 18 . 1 Tagged Unions

**Source:** https://craftinginterpreters.com/types-of-values.html

```
typedef
 
struct
 {
  
ValueType
 
type
;
  
union
 {
    
bool
 
boolean
;
    
double
 
number
;
  } 
as
;
 

} 
Value
;
```

---

### 1012. Types of Values — 18 . 1 Tagged Unions

**Source:** https://craftinginterpreters.com/types-of-values.html

```


typedef struct {
```

---

### 1013. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```



#define BOOL_VAL(value)   ((Value){VAL_BOOL, {.boolean = value}})


#define NIL_VAL           ((Value){VAL_NIL, {.number = 0}})


#define NUMBER_VAL(value) ((Value){VAL_NUMBER, {.number = value}})
```

---

### 1014. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```


typedef struct {
```

---

### 1015. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```



#define AS_BOOL(value)    ((value).as.boolean)


#define AS_NUMBER(value)  ((value).as.number)
```

---

### 1016. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```


#define BOOL_VAL(value)   ((Value){VAL_BOOL, {.boolean = value}})
```

---

### 1017. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```
Value
 
value
 = 
BOOL_VAL
(
true
);

double
 
number
 = 
AS_NUMBER
(
value
);
```

---

### 1018. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```



#define IS_BOOL(value)    ((value).type == VAL_BOOL)


#define IS_NIL(value)     ((value).type == VAL_NIL)


#define IS_NUMBER(value)  ((value).type == VAL_NUMBER)
```

---

### 1019. Types of Values — 18 . 2 Lox Values and C Values

**Source:** https://craftinginterpreters.com/types-of-values.html

```


#define AS_BOOL(value)    ((value).as.boolean)
```

---

### 1020. Types of Values — 18 . 3 Dynamically Typed Numbers

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  double value = strtod(parser.previous.start, NULL);
```

---

### 1021. Types of Values — 18 . 3 Dynamically Typed Numbers

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  
emitConstant
(
NUMBER_VAL
(
value
));
```

---

### 1022. Types of Values — 18 . 3 Dynamically Typed Numbers

**Source:** https://craftinginterpreters.com/types-of-values.html

```
 
printf
(
"%g"
, 
AS_NUMBER
(
value
));
```

---

### 1023. Types of Values — 18 . 3 . 1 Unary negation and runtime errors

**Source:** https://craftinginterpreters.com/types-of-values.html

```
print
 -
false
; 
// Uh...
```

---

### 1024. Types of Values — 18 . 3 . 1 Unary negation and runtime errors

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_DIVIDE:   BINARY_OP(/); break;
```

---

### 1025. Types of Values — 18 . 3 . 1 Unary negation and runtime errors

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      
case
 
OP_NEGATE
:
        
if
 (!
IS_NUMBER
(
peek
(
0
))) {
          
runtimeError
(
"Operand must be a number."
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
push
(
NUMBER_VAL
(-
AS_NUMBER
(
pop
())));
        
break
;
```

---

### 1026. Types of Values — 18 . 3 . 1 Unary negation and runtime errors

**Source:** https://craftinginterpreters.com/types-of-values.html

```
static
 
Value
 
peek
(
int
 
distance
) {
  
return
 
vm
.
stackTop
[-
1
 - 
distance
];
}
```

---

### 1027. Types of Values — 18 . 3 . 1 Unary negation and runtime errors

**Source:** https://craftinginterpreters.com/types-of-values.html

```
static
 
void
 
runtimeError
(
const
 
char
* 
format
, ...) {
  
va_list
 
args
;
  
va_start
(
args
, 
format
);
  
vfprintf
(
stderr
, 
format
, 
args
);
  
va_end
(
args
);
  
fputs
(
"
\n
"
, 
stderr
);

  
size_t
 
instruction
 = 
vm
.
ip
 - 
vm
.
chunk
->
code
 - 
1
;
  
int
 
line
 = 
vm
.
chunk
->
lines
[
instruction
];
  
fprintf
(
stderr
, 
"[line %d] in script
\n
"
, 
line
);
  
resetStack
();
}
```

---

### 1028. Types of Values — 18 . 3 . 2 Binary arithmetic operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

---

### 1029. Types of Values — 18 . 3 . 2 Binary arithmetic operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
#define BINARY_OP(valueType, op) \


    do { \


      if (!IS_NUMBER(peek(0)) || !IS_NUMBER(peek(1))) { \


        runtimeError("Operands must be numbers."); \


        return INTERPRET_RUNTIME_ERROR; \


      } \


      double b = AS_NUMBER(pop()); \


      double a = AS_NUMBER(pop()); \


      push(valueType(a op b)); \


    } while (false)
```

---

### 1030. Types of Values — 18 . 3 . 2 Binary arithmetic operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```


  for (;;) {
```

---

### 1031. Types of Values — 18 . 3 . 2 Binary arithmetic operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      
case
 
OP_ADD
:      
BINARY_OP
(
NUMBER_VAL
, +); 
break
;
      
case
 
OP_SUBTRACT
: 
BINARY_OP
(
NUMBER_VAL
, -); 
break
;
      
case
 
OP_MULTIPLY
: 
BINARY_OP
(
NUMBER_VAL
, *); 
break
;
      
case
 
OP_DIVIDE
:   
BINARY_OP
(
NUMBER_VAL
, /); 
break
;
```

---

### 1032. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  
OP_NIL
,
  
OP_TRUE
,
  
OP_FALSE
,
```

---

### 1033. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_ELSE]          = {NULL,     NULL,   PREC_NONE},
```

---

### 1034. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [
TOKEN_FALSE
]         = {
literal
,  
NULL
,   
PREC_NONE
},
```

---

### 1035. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_FOR]           = {NULL,     NULL,   PREC_NONE},
```

---

### 1036. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_THIS]          = {NULL,     NULL,   PREC_NONE},
```

---

### 1037. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [
TOKEN_TRUE
]          = {
literal
,  
NULL
,   
PREC_NONE
},
```

---

### 1038. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_VAR]           = {NULL,     NULL,   PREC_NONE},
```

---

### 1039. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_IF]            = {NULL,     NULL,   PREC_NONE},
```

---

### 1040. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [
TOKEN_NIL
]           = {
literal
,  
NULL
,   
PREC_NONE
},
```

---

### 1041. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_OR]            = {NULL,     NULL,   PREC_NONE},
```

---

### 1042. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
static
 
void
 
literal
() {
  
switch
 (
parser
.
previous
.
type
) {
    
case
 
TOKEN_FALSE
: 
emitByte
(
OP_FALSE
); 
break
;
    
case
 
TOKEN_NIL
: 
emitByte
(
OP_NIL
); 
break
;
    
case
 
TOKEN_TRUE
: 
emitByte
(
OP_TRUE
); 
break
;
    
default
: 
return
; 
// Unreachable.

  }
}
```

---

### 1043. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_CONSTANT: {
        Value constant = READ_CONSTANT();
        push(constant);
        break;
      }
```

---

### 1044. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      
case
 
OP_NIL
: 
push
(
NIL_VAL
); 
break
;
      
case
 
OP_TRUE
: 
push
(
BOOL_VAL
(
true
)); 
break
;
      
case
 
OP_FALSE
: 
push
(
BOOL_VAL
(
false
)); 
break
;
```

---

### 1045. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
```

---

### 1046. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

---

### 1047. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    
case
 
OP_NIL
:
      
return
 
simpleInstruction
(
"OP_NIL"
, 
offset
);
    
case
 
OP_TRUE
:
      
return
 
simpleInstruction
(
"OP_TRUE"
, 
offset
);
    
case
 
OP_FALSE
:
      
return
 
simpleInstruction
(
"OP_FALSE"
, 
offset
);
```

---

### 1048. Types of Values — 18 . 4 Two New Types

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  
switch
 (
value
.
type
) {
    
case
 
VAL_BOOL
:
      
printf
(
AS_BOOL
(
value
) ? 
"true"
 : 
"false"
);
      
break
;
    
case
 
VAL_NIL
: 
printf
(
"nil"
); 
break
;
    
case
 
VAL_NUMBER
: 
printf
(
"%g"
, 
AS_NUMBER
(
value
)); 
break
;
  }
```

---

### 1049. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
print
 !
true
; 
// "false"
```

---

### 1050. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  
OP_NOT
,
```

---

### 1051. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_STAR]          = {NULL,     binary, PREC_FACTOR},
```

---

### 1052. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [
TOKEN_BANG
]          = {
unary
,    
NULL
,   
PREC_NONE
},
```

---

### 1053. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_BANG_EQUAL]    = {NULL,     NULL,   PREC_NONE},
```

---

### 1054. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    
case
 
TOKEN_BANG
: 
emitByte
(
OP_NOT
); 
break
;
```

---

### 1055. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    case TOKEN_MINUS: emitByte(OP_NEGATE); break;
    default: return; // Unreachable.
  }
```

---

### 1056. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_DIVIDE:   BINARY_OP(NUMBER_VAL, /); break;
```

---

### 1057. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      
case
 
OP_NOT
:
        
push
(
BOOL_VAL
(
isFalsey
(
pop
())));
        
break
;
```

---

### 1058. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
print
 !
nil
;
```

---

### 1059. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
static
 
bool
 
isFalsey
(
Value
 
value
) {
  
return
 
IS_NIL
(
value
) || (
IS_BOOL
(
value
) && !
AS_BOOL
(
value
));
}
```

---

### 1060. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    case OP_DIVIDE:
      return simpleInstruction("OP_DIVIDE", offset);
```

---

### 1061. Types of Values — 18 . 4 . 1 Logical not and falsiness

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    
case
 
OP_NOT
:
      
return
 
simpleInstruction
(
"OP_NOT"
, 
offset
);
```

---

### 1062. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  
OP_EQUAL
,
  
OP_GREATER
,
  
OP_LESS
,
```

---

### 1063. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_BANG]          = {unary,    NULL,   PREC_NONE},
```

---

### 1064. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [
TOKEN_BANG_EQUAL
]    = {
NULL
,     
binary
, 
PREC_EQUALITY
},
```

---

### 1065. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_EQUAL]         = {NULL,     NULL,   PREC_NONE},
```

---

### 1066. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_EQUAL]         = {NULL,     NULL,   PREC_NONE},
```

---

### 1067. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [
TOKEN_EQUAL_EQUAL
]   = {
NULL
,     
binary
, 
PREC_EQUALITY
},
  [
TOKEN_GREATER
]       = {
NULL
,     
binary
, 
PREC_COMPARISON
},
  [
TOKEN_GREATER_EQUAL
] = {
NULL
,     
binary
, 
PREC_COMPARISON
},
  [
TOKEN_LESS
]          = {
NULL
,     
binary
, 
PREC_COMPARISON
},
  [
TOKEN_LESS_EQUAL
]    = {
NULL
,     
binary
, 
PREC_COMPARISON
},
```

---

### 1068. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
  [TOKEN_IDENTIFIER]    = {NULL,     NULL,   PREC_NONE},
```

---

### 1069. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    
case
 
TOKEN_BANG_EQUAL
:    
emitBytes
(
OP_EQUAL
, 
OP_NOT
); 
break
;
    
case
 
TOKEN_EQUAL_EQUAL
:   
emitByte
(
OP_EQUAL
); 
break
;
    
case
 
TOKEN_GREATER
:       
emitByte
(
OP_GREATER
); 
break
;
    
case
 
TOKEN_GREATER_EQUAL
: 
emitBytes
(
OP_LESS
, 
OP_NOT
); 
break
;
    
case
 
TOKEN_LESS
:          
emitByte
(
OP_LESS
); 
break
;
    
case
 
TOKEN_LESS_EQUAL
:    
emitBytes
(
OP_GREATER
, 
OP_NOT
); 
break
;
```

---

### 1070. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    case TOKEN_PLUS:          emitByte(OP_ADD); break;
```

---

### 1071. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_FALSE: push(BOOL_VAL(false)); break;
```

---

### 1072. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      
case
 
OP_EQUAL
: {
        
Value
 
b
 = 
pop
();
        
Value
 
a
 = 
pop
();
        
push
(
BOOL_VAL
(
valuesEqual
(
a
, 
b
)));
        
break
;
      }
```

---

### 1073. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
```

---

### 1074. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
bool
 
valuesEqual
(
Value
 
a
, 
Value
 
b
);
```

---

### 1075. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
bool
 
valuesEqual
(
Value
 
a
, 
Value
 
b
) {
  
if
 (
a
.
type
 != 
b
.
type
) 
return
 
false
;
  
switch
 (
a
.
type
) {
    
case
 
VAL_BOOL
:   
return
 
AS_BOOL
(
a
) == 
AS_BOOL
(
b
);
    
case
 
VAL_NIL
:    
return
 
true
;
    
case
 
VAL_NUMBER
: 
return
 
AS_NUMBER
(
a
) == 
AS_NUMBER
(
b
);
    
default
:         
return
 
false
; 
// Unreachable.

  }
}
```

---

### 1076. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
        push(BOOL_VAL(valuesEqual(a, b)));
        break;
      }
```

---

### 1077. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      
case
 
OP_GREATER
:  
BINARY_OP
(
BOOL_VAL
, >); 
break
;
      
case
 
OP_LESS
:     
BINARY_OP
(
BOOL_VAL
, <); 
break
;
```

---

### 1078. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
```

---

### 1079. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    case OP_FALSE:
      return simpleInstruction("OP_FALSE", offset);
```

---

### 1080. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
    
case
 
OP_EQUAL
:
      
return
 
simpleInstruction
(
"OP_EQUAL"
, 
offset
);
    
case
 
OP_GREATER
:
      
return
 
simpleInstruction
(
"OP_GREATER"
, 
offset
);
    
case
 
OP_LESS
:
      
return
 
simpleInstruction
(
"OP_LESS"
, 
offset
);
```

---

### 1081. Types of Values — 18 . 4 . 2 Equality and comparison operators

**Source:** https://craftinginterpreters.com/types-of-values.html

```
!(
5
 - 
4
 > 
3
 * 
2
 == !
nil
)
```

---

### 1082. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
  
VAL_OBJ
```

---

### 1083. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
    
Obj
* 
obj
;
```

---

### 1084. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define IS_NUMBER(value)  ((value).type == VAL_NUMBER)
```

---

### 1085. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define IS_OBJ(value)     ((value).type == VAL_OBJ)
```

---

### 1086. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```


#define AS_BOOL(value)    ((value).as.boolean)
```

---

### 1087. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define IS_OBJ(value)     ((value).type == VAL_OBJ)
```

---

### 1088. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define AS_OBJ(value)     ((value).as.obj)
```

---

### 1089. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define AS_BOOL(value)    ((value).as.boolean)
```

---

### 1090. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define NUMBER_VAL(value) ((Value){VAL_NUMBER, {.number = value}})
```

---

### 1091. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```
#define OBJ_VAL(object)   ((Value){VAL_OBJ, {.obj = (Obj*)object}})
```

---

### 1092. Strings — 19 . 1 Values and Objects

**Source:** https://craftinginterpreters.com/strings.html

```


typedef struct {
```

---

### 1093. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```
typedef
 
struct
 
Obj
 
Obj
;
```

---

### 1094. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```c
#ifndef clox_object_h


#define clox_object_h



#include "common.h"


#include "value.h"



struct
 
Obj
 {
  
ObjType
 
type
;
};


#endif
```

---

### 1095. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```



typedef
 
enum
 {
  
OBJ_STRING
,
} 
ObjType
;
```

---

### 1096. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```


struct Obj {
```

---

### 1097. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```



#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

---

### 1098. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```


typedef enum {
```

---

### 1099. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```
typedef
 
struct
 
ObjString
 
ObjString
;
```

---

### 1100. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```


typedef enum {
```

---

### 1101. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```



struct
 
ObjString
 {
  
Obj
 
obj
;
  
int
 
length
;
  
char
* 
chars
;
};
```

---

### 1102. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```


#endif
```

---

### 1103. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

---

### 1104. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```



#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1105. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```


typedef enum {
```

---

### 1106. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```
static
 
inline
 
bool
 
isObjType
(
Value
 
value
, 
ObjType
 
type
) {
  
return
 
IS_OBJ
(
value
) && 
AS_OBJ
(
value
)->
type
 == 
type
;
}
```

---

### 1107. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```
IS_STRING
(
POP
())
```

---

### 1108. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1109. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```



#define AS_STRING(value)       ((ObjString*)AS_OBJ(value))


#define AS_CSTRING(value)      (((ObjString*)AS_OBJ(value))->chars)
```

---

### 1110. Strings — 19 . 2 Struct Inheritance

**Source:** https://craftinginterpreters.com/strings.html

```


typedef enum {
```

---

### 1111. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
  [TOKEN_IDENTIFIER]    = {NULL,     NULL,   PREC_NONE},
```

---

### 1112. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
  [
TOKEN_STRING
]        = {
string
,   
NULL
,   
PREC_NONE
},
```

---

### 1113. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
  [TOKEN_NUMBER]        = {number,   NULL,   PREC_NONE},
```

---

### 1114. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
static
 
void
 
string
() {
  
emitConstant
(
OBJ_VAL
(
copyString
(
parser
.
previous
.
start
 + 
1
,
                                  
parser
.
previous
.
length
 - 
2
)));
}
```

---

### 1115. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
ObjString
* 
copyString
(
const
 
char
* 
chars
, 
int
 
length
);
```

---

### 1116. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
static inline bool isObjType(Value value, ObjType type) {
```

---

### 1117. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```c
#include <stdio.h>


#include <string.h>



#include "memory.h"


#include "object.h"


#include "value.h"


#include "vm.h"



ObjString
* 
copyString
(
const
 
char
* 
chars
, 
int
 
length
) {
  
char
* 
heapChars
 = 
ALLOCATE
(
char
, 
length
 + 
1
);
  
memcpy
(
heapChars
, 
chars
, 
length
);
  
heapChars
[
length
] = 
'\0'
;
  
return
 
allocateString
(
heapChars
, 
length
);
}
```

---

### 1118. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
#define ALLOCATE(type, count) \


    (type*)reallocate(NULL, 0, sizeof(type) * (count))
```

---

### 1119. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
static
 
ObjString
* 
allocateString
(
char
* 
chars
, 
int
 
length
) {
  
ObjString
* 
string
 = 
ALLOCATE_OBJ
(
ObjString
, 
OBJ_STRING
);
  
string
->
length
 = 
length
;
  
string
->
chars
 = 
chars
;
  
return
 
string
;
}
```

---

### 1120. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```



#define ALLOCATE_OBJ(type, objectType) \


    (type*)allocateObject(sizeof(type), objectType)
```

---

### 1121. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```


static ObjString* allocateString(char* chars, int length) {
```

---

### 1122. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```
#define ALLOCATE_OBJ(type, objectType) \
    (type*)allocateObject(sizeof(type), objectType)
```

---

### 1123. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```



static
 
Obj
* 
allocateObject
(
size_t
 
size
, 
ObjType
 
type
) {
  
Obj
* 
object
 = (
Obj
*)
reallocate
(
NULL
, 
0
, 
size
);
  
object
->
type
 = 
type
;
  
return
 
object
;
}
```

---

### 1124. Strings — 19 . 3 Strings

**Source:** https://craftinginterpreters.com/strings.html

```


static ObjString* allocateString(char* chars, int length) {
```

---

### 1125. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
    case VAL_NUMBER: printf("%g", AS_NUMBER(value)); break;
```

---

### 1126. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
    
case
 
VAL_OBJ
: 
printObject
(
value
); 
break
;
```

---

### 1127. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
ObjString* copyString(const char* chars, int length);
```

---

### 1128. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
void
 
printObject
(
Value
 
value
);
```

---

### 1129. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```


static inline bool isObjType(Value value, ObjType type) {
```

---

### 1130. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
void
 
printObject
(
Value
 
value
) {
  
switch
 (
OBJ_TYPE
(
value
)) {
    
case
 
OBJ_STRING
:
      
printf
(
"%s"
, 
AS_CSTRING
(
value
));
      
break
;
  }
}
```

---

### 1131. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
"string"
 == 
"string"
```

---

### 1132. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
    case VAL_NUMBER: return AS_NUMBER(a) == AS_NUMBER(b);
```

---

### 1133. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
    
case
 
VAL_OBJ
: {
      
ObjString
* 
aString
 = 
AS_STRING
(
a
);
      
ObjString
* 
bString
 = 
AS_STRING
(
b
);
      
return
 
aString
->
length
 == 
bString
->
length
 &&
          
memcmp
(
aString
->
chars
, 
bString
->
chars
,
                 
aString
->
length
) == 
0
;
    }
```

---

### 1134. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```
    default:         return false; // Unreachable.
```

---

### 1135. Strings — 19 . 4 Operations on Strings

**Source:** https://craftinginterpreters.com/strings.html

```c


#include "memory.h"
```

---

### 1136. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
      case OP_LESS:     BINARY_OP(BOOL_VAL, <); break;
```

---

### 1137. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
      
case
 
OP_ADD
: {
        
if
 (
IS_STRING
(
peek
(
0
)) && 
IS_STRING
(
peek
(
1
))) {
          
concatenate
();
        } 
else
 
if
 (
IS_NUMBER
(
peek
(
0
)) && 
IS_NUMBER
(
peek
(
1
))) {
          
double
 
b
 = 
AS_NUMBER
(
pop
());
          
double
 
a
 = 
AS_NUMBER
(
pop
());
          
push
(
NUMBER_VAL
(
a
 + 
b
));
        } 
else
 {
          
runtimeError
(
              
"Operands must be two numbers or two strings."
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
break
;
      }
```

---

### 1138. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
      case OP_SUBTRACT: BINARY_OP(NUMBER_VAL, -); break;
```

---

### 1139. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
static
 
void
 
concatenate
() {
  
ObjString
* 
b
 = 
AS_STRING
(
pop
());
  
ObjString
* 
a
 = 
AS_STRING
(
pop
());

  
int
 
length
 = 
a
->
length
 + 
b
->
length
;
  
char
* 
chars
 = 
ALLOCATE
(
char
, 
length
 + 
1
);
  
memcpy
(
chars
, 
a
->
chars
, 
a
->
length
);
  
memcpy
(
chars
 + 
a
->
length
, 
b
->
chars
, 
b
->
length
);
  
chars
[
length
] = 
'\0'
;

  
ObjString
* 
result
 = 
takeString
(
chars
, 
length
);
  
push
(
OBJ_VAL
(
result
));
}
```

---

### 1140. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```c


#include "common.h"
```

---

### 1141. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
ObjString
* 
takeString
(
char
* 
chars
, 
int
 
length
);
```

---

### 1142. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
ObjString* copyString(const char* chars, int length);
```

---

### 1143. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```
ObjString
* 
takeString
(
char
* 
chars
, 
int
 
length
) {
  
return
 
allocateString
(
chars
, 
length
);
}
```

---

### 1144. Strings — 19 . 4 . 1 Concatenation

**Source:** https://craftinginterpreters.com/strings.html

```c
#include "object.h"


#include "memory.h"
```

---

### 1145. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
"st"
 + 
"ri"
 + 
"ng"
```

---

### 1146. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
0000    OP_CONSTANT         0 "st"
0002    OP_CONSTANT         1 "ri"
0004    OP_ADD
0005    OP_CONSTANT         2 "ng"
0007    OP_ADD
0008    OP_RETURN
```

---

### 1147. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
struct Obj {
  ObjType type;
```

---

### 1148. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
  
struct
 
Obj
* 
next
;
```

---

### 1149. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
  
Obj
* 
objects
;
```

---

### 1150. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
  
vm
.
objects
 = 
NULL
;
```

---

### 1151. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```


  
object
->
next
 = 
vm
.
objects
;
  
vm
.
objects
 = 
object
;
```

---

### 1152. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
extern
 
VM
 
vm
;
```

---

### 1153. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
  
freeObjects
();
```

---

### 1154. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

---

### 1155. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
void
 
freeObjects
();
```

---

### 1156. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```


#endif
```

---

### 1157. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
void
 
freeObjects
() {
  
Obj
* 
object
 = 
vm
.
objects
;
  
while
 (
object
 != 
NULL
) {
    
Obj
* 
next
 = 
object
->
next
;
    
freeObject
(
object
);
    
object
 = 
next
;
  }
}
```

---

### 1158. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
static
 
void
 
freeObject
(
Obj
* 
object
) {
  
switch
 (
object
->
type
) {
    
case
 
OBJ_STRING
: {
      
ObjString
* 
string
 = (
ObjString
*)
object
;
      
FREE_ARRAY
(
char
, 
string
->
chars
, 
string
->
length
 + 
1
);
      
FREE
(
ObjString
, 
object
);
      
break
;
    }
  }
}
```

---

### 1159. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```
    (type*)reallocate(NULL, 0, sizeof(type) * (count))
```

---

### 1160. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```



#define FREE(type, pointer) reallocate(pointer, sizeof(type), 0)
```

---

### 1161. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```


#define GROW_CAPACITY(capacity) \
```

---

### 1162. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```


#define ALLOCATE(type, count) \
```

---

### 1163. Strings — 19 . 5 Freeing Objects

**Source:** https://craftinginterpreters.com/strings.html

```


void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

---

### 1164. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```c
#ifndef clox_table_h


#define clox_table_h



#include "common.h"


#include "value.h"



typedef
 
struct
 {
  
int
 
count
;
  
int
 
capacity
;
  
Entry
* 
entries
;
} 
Table
;


#endif
```

---

### 1165. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```



typedef
 
struct
 {
  
ObjString
* 
key
;
  
Value
 
value
;
} 
Entry
;
```

---

### 1166. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```


typedef struct {
```

---

### 1167. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void
 
initTable
(
Table
* 
table
);
```

---

### 1168. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```c
#include <stdlib.h>


#include <string.h>



#include "memory.h"


#include "object.h"


#include "table.h"


#include "value.h"



void
 
initTable
(
Table
* 
table
) {
  
table
->
count
 = 
0
;
  
table
->
capacity
 = 
0
;
  
table
->
entries
 = 
NULL
;
}
```

---

### 1169. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void
 
freeTable
(
Table
* 
table
);
```

---

### 1170. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```


#endif
```

---

### 1171. Hash Tables — 20 . 4 Building a Hash Table

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void
 
freeTable
(
Table
* 
table
) {
  
FREE_ARRAY
(
Entry
, 
table
->
entries
, 
table
->
capacity
);
  
initTable
(
table
);
}
```

---

### 1172. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
uint32_t
 
hash
;
```

---

### 1173. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
static
 
ObjString
* 
allocateString
(
char
* 
chars
, 
int
 
length
,
                                 
uint32_t
 
hash
) {
```

---

### 1174. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  ObjString* string = ALLOCATE_OBJ(ObjString, OBJ_STRING);
```

---

### 1175. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
string
->
hash
 = 
hash
;
```

---

### 1176. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  return string;
}
```

---

### 1177. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
ObjString* copyString(const char* chars, int length) {
```

---

### 1178. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
uint32_t
 
hash
 = 
hashString
(
chars
, 
length
);
```

---

### 1179. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  char* heapChars = ALLOCATE(char, length + 1);
```

---

### 1180. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  memcpy(heapChars, chars, length);
  heapChars[length] = '\0';
```

---

### 1181. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
return
 
allocateString
(
heapChars
, 
length
, 
hash
);
```

---

### 1182. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
ObjString* takeString(char* chars, int length) {
```

---

### 1183. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
uint32_t
 
hash
 = 
hashString
(
chars
, 
length
);
  
return
 
allocateString
(
chars
, 
length
, 
hash
);
```

---

### 1184. Hash Tables — 20 . 4 . 1 Hashing strings

**Source:** https://craftinginterpreters.com/hash-tables.html

```
static
 
uint32_t
 
hashString
(
const
 
char
* 
key
, 
int
 
length
) {
  
uint32_t
 
hash
 = 
2166136261u
;
  
for
 (
int
 
i
 = 
0
; 
i
 < 
length
; 
i
++) {
    
hash
 ^= (
uint8_t
)
key
[
i
];
    
hash
 *= 
16777619
;
  }
  
return
 
hash
;
}
```

---

### 1185. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool
 
tableSet
(
Table
* 
table
, 
ObjString
* 
key
, 
Value
 
value
);
```

---

### 1186. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```


#endif
```

---

### 1187. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool
 
tableSet
(
Table
* 
table
, 
ObjString
* 
key
, 
Value
 
value
) {
  
Entry
* 
entry
 = 
findEntry
(
table
->
entries
, 
table
->
capacity
, 
key
);
  
bool
 
isNewKey
 = 
entry
->
key
 == 
NULL
;
  
if
 (
isNewKey
) 
table
->
count
++;

  
entry
->
key
 = 
key
;
  
entry
->
value
 = 
value
;
  
return
 
isNewKey
;
}
```

---

### 1188. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool tableSet(Table* table, ObjString* key, Value value) {
```

---

### 1189. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
if
 (
table
->
count
 + 
1
 > 
table
->
capacity
 * 
TABLE_MAX_LOAD
) {
    
int
 
capacity
 = 
GROW_CAPACITY
(
table
->
capacity
);
    
adjustCapacity
(
table
, 
capacity
);
  }
```

---

### 1190. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  Entry* entry = findEntry(table->entries, table->capacity, key);
```

---

### 1191. Hash Tables — 20 . 4 . 2 Inserting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
static
 
Entry
* 
findEntry
(
Entry
* 
entries
, 
int
 
capacity
,
                        
ObjString
* 
key
) {
  
uint32_t
 
index
 = 
key
->
hash
 % 
capacity
;
  
for
 (;;) {
    
Entry
* 
entry
 = &
entries
[
index
];
    
if
 (
entry
->
key
 == 
key
 || 
entry
->
key
 == 
NULL
) {
      
return
 
entry
;
    }

    
index
 = (
index
 + 
1
) % 
capacity
;
  }
}
```

---

### 1192. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
static
 
void
 
adjustCapacity
(
Table
* 
table
, 
int
 
capacity
) {
  
Entry
* 
entries
 = 
ALLOCATE
(
Entry
, 
capacity
);
  
for
 (
int
 
i
 = 
0
; 
i
 < 
capacity
; 
i
++) {
    
entries
[
i
].
key
 = 
NULL
;
    
entries
[
i
].
value
 = 
NIL_VAL
;
  }

  
table
->
entries
 = 
entries
;
  
table
->
capacity
 = 
capacity
;
}
```

---

### 1193. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    entries[i].value = NIL_VAL;
  }
```

---

### 1194. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```


  
for
 (
int
 
i
 = 
0
; 
i
 < 
table
->
capacity
; 
i
++) {
    
Entry
* 
entry
 = &
table
->
entries
[
i
];
    
if
 (
entry
->
key
 == 
NULL
) 
continue
;

    
Entry
* 
dest
 = 
findEntry
(
entries
, 
capacity
, 
entry
->
key
);
    
dest
->
key
 = 
entry
->
key
;
    
dest
->
value
 = 
entry
->
value
;
  }
```

---

### 1195. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```


  table->entries = entries;
```

---

### 1196. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    dest->value = entry->value;
  }
```

---

### 1197. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
FREE_ARRAY
(
Entry
, 
table
->
entries
, 
table
->
capacity
);
```

---

### 1198. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool tableSet(Table* table, ObjString* key, Value value);
```

---

### 1199. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void
 
tableAddAll
(
Table
* 
from
, 
Table
* 
to
);
```

---

### 1200. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```


#endif
```

---

### 1201. Hash Tables — 20 . 4 . 3 Allocating and resizing

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void
 
tableAddAll
(
Table
* 
from
, 
Table
* 
to
) {
  
for
 (
int
 
i
 = 
0
; 
i
 < 
from
->
capacity
; 
i
++) {
    
Entry
* 
entry
 = &
from
->
entries
[
i
];
    
if
 (
entry
->
key
 != 
NULL
) {
      
tableSet
(
to
, 
entry
->
key
, 
entry
->
value
);
    }
  }
}
```

---

### 1202. Hash Tables — 20 . 4 . 4 Retrieving values

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool
 
tableGet
(
Table
* 
table
, 
ObjString
* 
key
, 
Value
* 
value
);
```

---

### 1203. Hash Tables — 20 . 4 . 4 Retrieving values

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool tableSet(Table* table, ObjString* key, Value value);
```

---

### 1204. Hash Tables — 20 . 4 . 4 Retrieving values

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool
 
tableGet
(
Table
* 
table
, 
ObjString
* 
key
, 
Value
* 
value
) {
  
if
 (
table
->
count
 == 
0
) 
return
 
false
;

  
Entry
* 
entry
 = 
findEntry
(
table
->
entries
, 
table
->
capacity
, 
key
);
  
if
 (
entry
->
key
 == 
NULL
) 
return
 
false
;

  *
value
 = 
entry
->
value
;
  
return
 
true
;
}
```

---

### 1205. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool tableSet(Table* table, ObjString* key, Value value);
```

---

### 1206. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool
 
tableDelete
(
Table
* 
table
, 
ObjString
* 
key
);
```

---

### 1207. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void tableAddAll(Table* from, Table* to);
```

---

### 1208. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
bool
 
tableDelete
(
Table
* 
table
, 
ObjString
* 
key
) {
  
if
 (
table
->
count
 == 
0
) 
return
 
false
;

  
// Find the entry.

  
Entry
* 
entry
 = 
findEntry
(
table
->
entries
, 
table
->
capacity
, 
key
);
  
if
 (
entry
->
key
 == 
NULL
) 
return
 
false
;

  
// Place a tombstone in the entry.

  
entry
->
key
 = 
NULL
;
  
entry
->
value
 = 
BOOL_VAL
(
true
);
  
return
 
true
;
}
```

---

### 1209. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  for (;;) {
    Entry* entry = &entries[index];
```

---

### 1210. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    
if
 (
entry
->
key
 == 
NULL
) {
      
if
 (
IS_NIL
(
entry
->
value
)) {
        
// Empty entry.

        
return
 
tombstone
 != 
NULL
 ? 
tombstone
 : 
entry
;
      } 
else
 {
        
// We found a tombstone.

        
if
 (
tombstone
 == 
NULL
) 
tombstone
 = 
entry
;
      }
    } 
else
 
if
 (
entry
->
key
 == 
key
) {
      
// We found the key.

      
return
 
entry
;
    }
```

---

### 1211. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```


    index = (index + 1) % capacity;
```

---

### 1212. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  uint32_t index = key->hash % capacity;
```

---

### 1213. Hash Tables — 20 . 4 . 5 Deleting entries

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
Entry
* 
tombstone
 = 
NULL
;
```

---

### 1214. Hash Tables — 20 . 4 . 6 Counting tombstones

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
if
 (
isNewKey
 && 
IS_NIL
(
entry
->
value
)) 
table
->
count
++;
```

---

### 1215. Hash Tables — 20 . 4 . 6 Counting tombstones

**Source:** https://craftinginterpreters.com/hash-tables.html

```


  entry->key = key;
```

---

### 1216. Hash Tables — 20 . 4 . 6 Counting tombstones

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
table
->
count
 = 
0
;
```

---

### 1217. Hash Tables — 20 . 4 . 6 Counting tombstones

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  for (int i = 0; i < table->capacity; i++) {
```

---

### 1218. Hash Tables — 20 . 4 . 6 Counting tombstones

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    
table
->
count
++;
```

---

### 1219. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
Table
 
strings
;
```

---

### 1220. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
initTable
(&
vm
.
strings
);
```

---

### 1221. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
freeTable
(&
vm
.
strings
);
```

---

### 1222. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
tableSet
(&
vm
.
strings
, 
string
, 
NIL_VAL
);
```

---

### 1223. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  uint32_t hash = hashString(chars, length);
```

---

### 1224. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
ObjString
* 
interned
 = 
tableFindString
(&
vm
.
strings
, 
chars
, 
length
,
                                        
hash
);
  
if
 (
interned
 != 
NULL
) 
return
 
interned
;
```

---

### 1225. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  char* heapChars = ALLOCATE(char, length + 1);
```

---

### 1226. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  uint32_t hash = hashString(chars, length);
```

---

### 1227. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  
ObjString
* 
interned
 = 
tableFindString
(&
vm
.
strings
, 
chars
, 
length
,
                                        
hash
);
  
if
 (
interned
 != 
NULL
) {
    
FREE_ARRAY
(
char
, 
chars
, 
length
 + 
1
);
    
return
 
interned
;
  }
```

---

### 1228. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
  return allocateString(chars, length, hash);
```

---

### 1229. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
void tableAddAll(Table* from, Table* to);
```

---

### 1230. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
ObjString
* 
tableFindString
(
Table
* 
table
, 
const
 
char
* 
chars
,
                           
int
 
length
, 
uint32_t
 
hash
);
```

---

### 1231. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```


#endif
```

---

### 1232. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
ObjString
* 
tableFindString
(
Table
* 
table
, 
const
 
char
* 
chars
,
                           
int
 
length
, 
uint32_t
 
hash
) {
  
if
 (
table
->
count
 == 
0
) 
return
 
NULL
;

  
uint32_t
 
index
 = 
hash
 % 
table
->
capacity
;
  
for
 (;;) {
    
Entry
* 
entry
 = &
table
->
entries
[
index
];
    
if
 (
entry
->
key
 == 
NULL
) {
      
// Stop if we find an empty non-tombstone entry.

      
if
 (
IS_NIL
(
entry
->
value
)) 
return
 
NULL
;
    } 
else
 
if
 (
entry
->
key
->
length
 == 
length
 &&
        
entry
->
key
->
hash
 == 
hash
 &&
        
memcmp
(
entry
->
key
->
chars
, 
chars
, 
length
) == 
0
) {
      
// We found it.

      
return
 
entry
->
key
;
    }

    
index
 = (
index
 + 
1
) % 
table
->
capacity
;
  }
}
```

---

### 1233. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    case VAL_NUMBER: return AS_NUMBER(a) == AS_NUMBER(b);
```

---

### 1234. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    
case
 
VAL_OBJ
:    
return
 
AS_OBJ
(
a
) == 
AS_OBJ
(
b
);
```

---

### 1235. Hash Tables — 20 . 5 String Interning

**Source:** https://craftinginterpreters.com/hash-tables.html

```
    default:         return false; // Unreachable.
```

---

### 1236. Global Variables — Global Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
fun
 
showVariable
() {
  
print
 
global
;
}


var
 
global
 = 
"after"
;

showVariable
();
```

---

### 1237. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
if
 (
monday
) 
var
 
croissant
 = 
"yes"
; 
// Error.
```

---

### 1238. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
statement
      â 
exprStmt

               | 
forStmt

               | 
ifStmt

               | 
printStmt

               | 
returnStmt

               | 
whileStmt

               | 
block
 ;
```

---

### 1239. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
declaration
    â 
classDecl

               | 
funDecl

               | 
varDecl

               | 
statement
 ;
```

---

### 1240. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
statement
      â 
exprStmt

               | 
printStmt
 ;


declaration
    â 
varDecl

               | 
statement
 ;
```

---

### 1241. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```


  
while
 (!
match
(
TOKEN_EOF
)) {
    
declaration
();
  }
```

---

### 1242. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
declaration
() {
  
statement
();
}
```

---

### 1243. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
statement
() {
  
if
 (
match
(
TOKEN_PRINT
)) {
    
printStatement
();
  }
}
```

---

### 1244. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
statement
();

static
 
void
 
declaration
();
```

---

### 1245. Global Variables — 21 . 1 Statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static ParseRule* getRule(TokenType type);
```

---

### 1246. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
bool
 
match
(
TokenType
 
type
) {
  
if
 (!
check
(
type
)) 
return
 
false
;
  
advance
();
  
return
 
true
;
}
```

---

### 1247. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
bool
 
check
(
TokenType
 
type
) {
  
return
 
parser
.
current
.
type
 == 
type
;
}
```

---

### 1248. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
printStatement
() {
  
expression
();
  
consume
(
TOKEN_SEMICOLON
, 
"Expect ';' after value."
);
  
emitByte
(
OP_PRINT
);
}
```

---

### 1249. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
OP_PRINT
,
```

---

### 1250. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
      
case
 
OP_PRINT
: {
        
printValue
(
pop
());
        
printf
(
"
\n
"
);
        
break
;
      }
```

---

### 1251. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
        
// Exit interpreter.
```

---

### 1252. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
      return simpleInstruction("OP_NEGATE", offset);
```

---

### 1253. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
    
case
 
OP_PRINT
:
      
return
 
simpleInstruction
(
"OP_PRINT"
, 
offset
);
```

---

### 1254. Global Variables — 21 . 1 . 1 Print statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
print
 
1
 + 
2
;

print
 
3
 * 
4
;
```

---

### 1255. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
  } 
else
 {
    
expressionStatement
();
```

---

### 1256. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
expressionStatement
() {
  
expression
();
  
consume
(
TOKEN_SEMICOLON
, 
"Expect ';' after expression."
);
  
emitByte
(
OP_POP
);
}
```

---

### 1257. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
brunch
 = 
"quiche"
;

eat
(
brunch
);
```

---

### 1258. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
OP_POP
,
```

---

### 1259. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
      case OP_FALSE: push(BOOL_VAL(false)); break;
```

---

### 1260. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
      
case
 
OP_POP
: 
pop
(); 
break
;
```

---

### 1261. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
      return simpleInstruction("OP_FALSE", offset);
```

---

### 1262. Global Variables — 21 . 1 . 2 Expression statements

**Source:** https://craftinginterpreters.com/global-variables.html

```
    
case
 
OP_POP
:
      
return
 
simpleInstruction
(
"OP_POP"
, 
offset
);
```

---

### 1263. Global Variables — 21 . 1 . 3 Error synchronization

**Source:** https://craftinginterpreters.com/global-variables.html

```


  
if
 (
parser
.
panicMode
) 
synchronize
();
```

---

### 1264. Global Variables — 21 . 1 . 3 Error synchronization

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
synchronize
() {
  
parser
.
panicMode
 = 
false
;

  
while
 (
parser
.
current
.
type
 != 
TOKEN_EOF
) {
    
if
 (
parser
.
previous
.
type
 == 
TOKEN_SEMICOLON
) 
return
;
    
switch
 (
parser
.
current
.
type
) {
      
case
 
TOKEN_CLASS
:
      
case
 
TOKEN_FUN
:
      
case
 
TOKEN_VAR
:
      
case
 
TOKEN_FOR
:
      
case
 
TOKEN_IF
:
      
case
 
TOKEN_WHILE
:
      
case
 
TOKEN_PRINT
:
      
case
 
TOKEN_RETURN
:
        
return
;

      
default
:
        ; 
// Do nothing.

    }

    
advance
();
  }
}
```

---

### 1265. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
if
 (
match
(
TOKEN_VAR
)) {
    
varDeclaration
();
  } 
else
 {
    
statement
();
  }
```

---

### 1266. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```


  if (parser.panicMode) synchronize();
```

---

### 1267. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
varDeclaration
() {
  
uint8_t
 
global
 = 
parseVariable
(
"Expect variable name."
);

  
if
 (
match
(
TOKEN_EQUAL
)) {
    
expression
();
  } 
else
 {
    
emitByte
(
OP_NIL
);
  }
  
consume
(
TOKEN_SEMICOLON
,
          
"Expect ';' after variable declaration."
);

  
defineVariable
(
global
);
}
```

---

### 1268. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
var
 
a
;
```

---

### 1269. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
var
 
a
 = 
nil
;
```

---

### 1270. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
static void parsePrecedence(Precedence precedence);
```

---

### 1271. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
uint8_t
 
parseVariable
(
const
 
char
* 
errorMessage
) {
  
consume
(
TOKEN_IDENTIFIER
, 
errorMessage
);
  
return
 
identifierConstant
(&
parser
.
previous
);
}
```

---

### 1272. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
static void parsePrecedence(Precedence precedence);
```

---

### 1273. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
uint8_t
 
identifierConstant
(
Token
* 
name
) {
  
return
 
makeConstant
(
OBJ_VAL
(
copyString
(
name
->
start
,
                                         
name
->
length
)));
}
```

---

### 1274. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
defineVariable
(
uint8_t
 
global
) {
  
emitBytes
(
OP_DEFINE_GLOBAL
, 
global
);
}
```

---

### 1275. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
OP_DEFINE_GLOBAL
,
```

---

### 1276. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
      
case
 
OP_DEFINE_GLOBAL
: {
        
ObjString
* 
name
 = 
READ_STRING
();
        
tableSet
(&
vm
.
globals
, 
name
, 
peek
(
0
));
        
pop
();
        
break
;
      }
```

---

### 1277. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

---

### 1278. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
#define READ_STRING() AS_STRING(READ_CONSTANT())
```

---

### 1279. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
Table
 
globals
;
```

---

### 1280. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```


  
initTable
(&
vm
.
globals
);
```

---

### 1281. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
freeTable
(&
vm
.
globals
);
```

---

### 1282. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
      return simpleInstruction("OP_POP", offset);
```

---

### 1283. Global Variables — 21 . 2 Variable Declarations

**Source:** https://craftinginterpreters.com/global-variables.html

```
    
case
 
OP_DEFINE_GLOBAL
:
      
return
 
constantInstruction
(
"OP_DEFINE_GLOBAL"
, 
chunk
,
                                 
offset
);
```

---

### 1284. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
  [TOKEN_LESS_EQUAL]    = {NULL,     binary, PREC_COMPARISON},
```

---

### 1285. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
  [
TOKEN_IDENTIFIER
]    = {
variable
, 
NULL
,   
PREC_NONE
},
```

---

### 1286. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
  [TOKEN_STRING]        = {string,   NULL,   PREC_NONE},
```

---

### 1287. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
variable
() {
  
namedVariable
(
parser
.
previous
);
}
```

---

### 1288. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
namedVariable
(
Token
 
name
) {
  
uint8_t
 
arg
 = 
identifierConstant
(&
name
);
  
emitBytes
(
OP_GET_GLOBAL
, 
arg
);
}
```

---

### 1289. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
OP_GET_GLOBAL
,
```

---

### 1290. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
      
case
 
OP_GET_GLOBAL
: {
        
ObjString
* 
name
 = 
READ_STRING
();
        
Value
 
value
;
        
if
 (!
tableGet
(&
vm
.
globals
, 
name
, &
value
)) {
          
runtimeError
(
"Undefined variable '%s'."
, 
name
->
chars
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
push
(
value
);
        
break
;
      }
```

---

### 1291. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
      return simpleInstruction("OP_POP", offset);
```

---

### 1292. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
    
case
 
OP_GET_GLOBAL
:
      
return
 
constantInstruction
(
"OP_GET_GLOBAL"
, 
chunk
, 
offset
);
```

---

### 1293. Global Variables — 21 . 3 Reading Variables

**Source:** https://craftinginterpreters.com/global-variables.html

```
var
 
beverage
 = 
"cafe au lait"
;

var
 
breakfast
 = 
"beignets with "
 + 
beverage
;

print
 
breakfast
;
```

---

### 1294. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
menu
.
brunch
(
sunday
).
beverage
 = 
"mimosa"
;
```

---

### 1295. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  uint8_t arg = identifierConstant(&name);
```

---

### 1296. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```


  
if
 (
match
(
TOKEN_EQUAL
)) {
    
expression
();
    
emitBytes
(
OP_SET_GLOBAL
, 
arg
);
  } 
else
 {
    
emitBytes
(
OP_GET_GLOBAL
, 
arg
);
  }
```

---

### 1297. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
OP_SET_GLOBAL
,
```

---

### 1298. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
      
case
 
OP_SET_GLOBAL
: {
        
ObjString
* 
name
 = 
READ_STRING
();
        
if
 (
tableSet
(&
vm
.
globals
, 
name
, 
peek
(
0
))) {
          
tableDelete
(&
vm
.
globals
, 
name
);
 

          
runtimeError
(
"Undefined variable '%s'."
, 
name
->
chars
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
break
;
      }
```

---

### 1299. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
      return constantInstruction("OP_DEFINE_GLOBAL", chunk,
                                 offset);
```

---

### 1300. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
    
case
 
OP_SET_GLOBAL
:
      
return
 
constantInstruction
(
"OP_SET_GLOBAL"
, 
chunk
, 
offset
);
```

---

### 1301. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
a
 * 
b
 = 
c
 + 
d
;
```

---

### 1302. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
    error("Expect expression.");
    return;
  }
```

---

### 1303. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
bool
 
canAssign
 = 
precedence
 <= 
PREC_ASSIGNMENT
;
  
prefixRule
(
canAssign
);
```

---

### 1304. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```


  while (precedence <= getRule(parser.current.type)->precedence) {
```

---

### 1305. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
variable
(
bool
 
canAssign
) {
  
namedVariable
(
parser
.
previous
, 
canAssign
);
}
```

---

### 1306. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
namedVariable
(
Token
 
name
, 
bool
 
canAssign
) {
```

---

### 1307. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  uint8_t arg = identifierConstant(&name);
```

---

### 1308. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  uint8_t arg = identifierConstant(&name);
```

---

### 1309. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  
if
 (
canAssign
 && 
match
(
TOKEN_EQUAL
)) {
```

---

### 1310. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
    infixRule();
  }
```

---

### 1311. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```


  
if
 (
canAssign
 && 
match
(
TOKEN_EQUAL
)) {
    
error
(
"Invalid assignment target."
);
  }
```

---

### 1312. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
    ParseFn infixRule = getRule(parser.previous.type)->infix;
```

---

### 1313. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
    
infixRule
(
canAssign
);
```

---

### 1314. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
typedef
 
void
 (*
ParseFn
)(
bool
 
canAssign
);
```

---

### 1315. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```


typedef struct {
```

---

### 1316. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
binary
(
bool
 
canAssign
) {
```

---

### 1317. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  TokenType operatorType = parser.previous.type;
```

---

### 1318. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
literal
(
bool
 
canAssign
) {
```

---

### 1319. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
grouping
(
bool
 
canAssign
) {
```

---

### 1320. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
number
(
bool
 
canAssign
) {
```

---

### 1321. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  double value = strtod(parser.previous.start, NULL);
```

---

### 1322. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
string
(
bool
 
canAssign
) {
```

---

### 1323. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  emitConstant(OBJ_VAL(copyString(parser.previous.start + 1,
```

---

### 1324. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
static
 
void
 
unary
(
bool
 
canAssign
) {
```

---

### 1325. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
  TokenType operatorType = parser.previous.type;
```

---

### 1326. Global Variables — 21 . 4 Assignment

**Source:** https://craftinginterpreters.com/global-variables.html

```
var
 
breakfast
 = 
"beignets"
;

var
 
beverage
 = 
"cafe au lait"
;

breakfast
 = 
"beignets with "
 + 
beverage
;


print
 
breakfast
;
```

---

### 1327. Global Variables — Challenges

**Source:** https://craftinginterpreters.com/global-variables.html

```
fun
 
useVar
() {
  
print
 
oops
;
}


var
 
ooops
 = 
"too many o's!"
;
```

---

### 1328. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```



typedef
 
struct
 {
  
Local
 
locals
[
UINT8_COUNT
];
  
int
 
localCount
;
  
int
 
scopeDepth
;
} 
Compiler
;
```

---

### 1329. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```


Parser parser;
```

---

### 1330. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```



#define UINT8_COUNT (UINT8_MAX + 1)
```

---

### 1331. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```


#endif
```

---

### 1332. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```



typedef
 
struct
 {
  
Token
 
name
;
  
int
 
depth
;
} 
Local
;
```

---

### 1333. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```


typedef struct {
```

---

### 1334. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
Compiler
* 
current
 = 
NULL
;
```

---

### 1335. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
initCompiler
(
Compiler
* 
compiler
) {
  
compiler
->
localCount
 = 
0
;
  
compiler
->
scopeDepth
 = 
0
;
  
current
 = 
compiler
;
}
```

---

### 1336. Local Variables — 22 . 1 Representing Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
Compiler
 
compiler
;
  
initCompiler
(&
compiler
);
```

---

### 1337. Local Variables — 22 . 2 Block Statements

**Source:** https://craftinginterpreters.com/local-variables.html

```
statement
      â 
exprStmt

               | 
printStmt

               | 
block
 ;


block
          â 
"{"
 
declaration
* 
"}"
 ;
```

---

### 1338. Local Variables — 22 . 2 Block Statements

**Source:** https://craftinginterpreters.com/local-variables.html

```
  if (match(TOKEN_PRINT)) {
    printStatement();
```

---

### 1339. Local Variables — 22 . 2 Block Statements

**Source:** https://craftinginterpreters.com/local-variables.html

```
  } 
else
 
if
 (
match
(
TOKEN_LEFT_BRACE
)) {
    
beginScope
();
    
block
();
    
endScope
();
```

---

### 1340. Local Variables — 22 . 2 Block Statements

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
block
() {
  
while
 (!
check
(
TOKEN_RIGHT_BRACE
) && !
check
(
TOKEN_EOF
)) {
    
declaration
();
  }

  
consume
(
TOKEN_RIGHT_BRACE
, 
"Expect '}' after block."
);
}
```

---

### 1341. Local Variables — 22 . 2 Block Statements

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
beginScope
() {
  
current
->
scopeDepth
++;
}
```

---

### 1342. Local Variables — 22 . 2 Block Statements

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
endScope
() {
  
current
->
scopeDepth
--;
}
```

---

### 1343. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  consume(TOKEN_IDENTIFIER, errorMessage);
```

---

### 1344. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```


  
declareVariable
();
  
if
 (
current
->
scopeDepth
 > 
0
) 
return
 
0
;
```

---

### 1345. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  return identifierConstant(&parser.previous);
```

---

### 1346. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
static void defineVariable(uint8_t global) {
```

---

### 1347. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
if
 (
current
->
scopeDepth
 > 
0
) {
    
return
;
  }
```

---

### 1348. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
declareVariable
() {
  
if
 (
current
->
scopeDepth
 == 
0
) 
return
;

  
Token
* 
name
 = &
parser
.
previous
;
  
addLocal
(*
name
);
}
```

---

### 1349. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
addLocal
(
Token
 
name
) {
  
Local
* 
local
 = &
current
->
locals
[
current
->
localCount
++];
  
local
->
name
 = 
name
;
  
local
->
depth
 = 
current
->
scopeDepth
;
}
```

---

### 1350. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
if
 (
current
->
localCount
 == 
UINT8_COUNT
) {
    
error
(
"Too many local variables in function."
);
    
return
;
  }
```

---

### 1351. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  Local* local = &current->locals[current->localCount++];
```

---

### 1352. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
{
  
var
 
a
 = 
"first"
;
  
var
 
a
 = 
"second"
;
}
```

---

### 1353. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
{
  
var
 
a
 = 
"outer"
;
  {
    
var
 
a
 = 
"inner"
;
  }
}
```

---

### 1354. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
for
 (
int
 
i
 = 
current
->
localCount
 - 
1
; 
i
 >= 
0
; 
i
--) {
    
Local
* 
local
 = &
current
->
locals
[
i
];
    
if
 (
local
->
depth
 != -
1
 && 
local
->
depth
 < 
current
->
scopeDepth
) {
      
break
;
 

    }

    
if
 (
identifiersEqual
(
name
, &
local
->
name
)) {
      
error
(
"Already a variable with this name in this scope."
);
    }
  }
```

---

### 1355. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  addLocal(*name);
}
```

---

### 1356. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
bool
 
identifiersEqual
(
Token
* 
a
, 
Token
* 
b
) {
  
if
 (
a
->
length
 != 
b
->
length
) 
return
 
false
;
  
return
 
memcmp
(
a
->
start
, 
b
->
start
, 
a
->
length
) == 
0
;
}
```

---

### 1357. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```c


#include "common.h"
```

---

### 1358. Local Variables — 22 . 3 Declaring Local Variables

**Source:** https://craftinginterpreters.com/local-variables.html

```


  
while
 (
current
->
localCount
 > 
0
 &&
         
current
->
locals
[
current
->
localCount
 - 
1
].
depth
 >
            
current
->
scopeDepth
) {
    
emitByte
(
OP_POP
);
    
current
->
localCount
--;
  }
```

---

### 1359. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
static void namedVariable(Token name, bool canAssign) {
```

---

### 1360. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
uint8_t
 
getOp
, 
setOp
;
  
int
 
arg
 = 
resolveLocal
(
current
, &
name
);
  
if
 (
arg
 != -
1
) {
    
getOp
 = 
OP_GET_LOCAL
;
    
setOp
 = 
OP_SET_LOCAL
;
  } 
else
 {
    
arg
 = 
identifierConstant
(&
name
);
    
getOp
 = 
OP_GET_GLOBAL
;
    
setOp
 = 
OP_SET_GLOBAL
;
  }
```

---

### 1361. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```


  if (canAssign && match(TOKEN_EQUAL)) {
```

---

### 1362. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
  if (canAssign && match(TOKEN_EQUAL)) {
    expression();
```

---

### 1363. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
    
emitBytes
(
setOp
, (
uint8_t
)
arg
);
```

---

### 1364. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
    emitBytes(setOp, (uint8_t)arg);
  } else {
```

---

### 1365. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
    
emitBytes
(
getOp
, (
uint8_t
)
arg
);
```

---

### 1366. Local Variables — 22 . 4 Using Locals

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
int
 
resolveLocal
(
Compiler
* 
compiler
, 
Token
* 
name
) {
  
for
 (
int
 
i
 = 
compiler
->
localCount
 - 
1
; 
i
 >= 
0
; 
i
--) {
    
Local
* 
local
 = &
compiler
->
locals
[
i
];
    
if
 (
identifiersEqual
(
name
, &
local
->
name
)) {
      
return
 
i
;
    }
  }

  
return
 -
1
;
}
```

---

### 1367. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
OP_GET_LOCAL
,
```

---

### 1368. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
      
case
 
OP_GET_LOCAL
: {
        
uint8_t
 
slot
 = 
READ_BYTE
();
        
push
(
vm
.
stack
[
slot
]);
 

        
break
;
      }
```

---

### 1369. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
OP_SET_LOCAL
,
```

---

### 1370. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
      
case
 
OP_SET_LOCAL
: {
        
uint8_t
 
slot
 = 
READ_BYTE
();
        
vm
.
stack
[
slot
] = 
peek
(
0
);
        
break
;
      }
```

---

### 1371. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
      return simpleInstruction("OP_POP", offset);
```

---

### 1372. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
    
case
 
OP_GET_LOCAL
:
      
return
 
byteInstruction
(
"OP_GET_LOCAL"
, 
chunk
, 
offset
);
    
case
 
OP_SET_LOCAL
:
      
return
 
byteInstruction
(
"OP_SET_LOCAL"
, 
chunk
, 
offset
);
```

---

### 1373. Local Variables — 22 . 4 . 1 Interpreting local variables

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
int
 
byteInstruction
(
const
 
char
* 
name
, 
Chunk
* 
chunk
,
                           
int
 
offset
) {
  
uint8_t
 
slot
 = 
chunk
->
code
[
offset
 + 
1
];
  
printf
(
"%-16s %4d
\n
"
, 
name
, 
slot
);
  
return
 
offset
 + 
2
;
 

}
```

---

### 1374. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
{
  
var
 
a
 = 
"outer"
;
  {
    
var
 
a
 = 
a
;
  }
}
```

---

### 1375. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
  
local
->
depth
 = -
1
;
```

---

### 1376. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
    
markInitialized
();
```

---

### 1377. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
    return;
  }
```

---

### 1378. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
static
 
void
 
markInitialized
() {
  
current
->
locals
[
current
->
localCount
 - 
1
].
depth
 =
      
current
->
scopeDepth
;
}
```

---

### 1379. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
    if (identifiersEqual(name, &local->name)) {
```

---

### 1380. Local Variables — 22 . 4 . 2 Another scope edge case

**Source:** https://craftinginterpreters.com/local-variables.html

```
      
if
 (
local
->
depth
 == -
1
) {
        
error
(
"Can't read local variable in its own initializer."
);
      }
```

---

### 1381. Local Variables — Challenges

**Source:** https://craftinginterpreters.com/local-variables.html

```
var
 
a
 = 
a
;
```

---

### 1382. Jumping Back and Forth — Jumping Back and Forth

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
if
 (
condition
) 
print
(
"condition was truthy"
);
```

---

### 1383. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  if (match(TOKEN_PRINT)) {
    printStatement();
```

---

### 1384. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  } 
else
 
if
 (
match
(
TOKEN_IF
)) {
    
ifStatement
();
```

---

### 1385. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
ifStatement
() {
  
consume
(
TOKEN_LEFT_PAREN
, 
"Expect '(' after 'if'."
);
  
expression
();
  
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after condition."
);
 


  
int
 
thenJump
 = 
emitJump
(
OP_JUMP_IF_FALSE
);
  
statement
();

  
patchJump
(
thenJump
);
}
```

---

### 1386. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
if
 
condition
) 
print
(
"looks weird"
);
```

---

### 1387. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
int
 
emitJump
(
uint8_t
 
instruction
) {
  
emitByte
(
instruction
);
  
emitByte
(
0xff
);
  
emitByte
(
0xff
);
  
return
 
currentChunk
()->
count
 - 
2
;
}
```

---

### 1388. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
patchJump
(
int
 
offset
) {
  
// -2 to adjust for the bytecode for the jump offset itself.

  
int
 
jump
 = 
currentChunk
()->
count
 - 
offset
 - 
2
;

  
if
 (
jump
 > 
UINT16_MAX
) {
    
error
(
"Too much code to jump over."
);
  }

  
currentChunk
()->
code
[
offset
] = (
jump
 >> 
8
) & 
0xff
;
  
currentChunk
()->
code
[
offset
 + 
1
] = 
jump
 & 
0xff
;
}
```

---

### 1389. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
OP_JUMP_IF_FALSE
,
```

---

### 1390. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
        break;
      }
```

---

### 1391. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
      
case
 
OP_JUMP_IF_FALSE
: {
        
uint16_t
 
offset
 = 
READ_SHORT
();
        
if
 (
isFalsey
(
peek
(
0
))) 
vm
.
ip
 += 
offset
;
        
break
;
      }
```

---

### 1392. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

---

### 1393. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
#define READ_SHORT() \


    (vm.ip += 2, (uint16_t)((vm.ip[-2] << 8) | vm.ip[-1]))
```

---

### 1394. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
#define READ_STRING() AS_STRING(READ_CONSTANT())
```

---

### 1395. Jumping Back and Forth — 23 . 1 If Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
case
 
OP_JUMP_IF_FALSE
: {
  
uint16_t
 
offset
 = 
READ_SHORT
();
  
vm
.
ip
 += 
falsey
() * 
offset
;
  
break
;
}
```

---

### 1396. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```


  
if
 (
match
(
TOKEN_ELSE
)) 
statement
();
```

---

### 1397. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
int
 
elseJump
 = 
emitJump
(
OP_JUMP
);
```

---

### 1398. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
patchJump
(
elseJump
);
```

---

### 1399. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
OP_JUMP
,
```

---

### 1400. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
        break;
      }
```

---

### 1401. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
      
case
 
OP_JUMP
: {
        
uint16_t
 
offset
 = 
READ_SHORT
();
        
vm
.
ip
 += 
offset
;
        
break
;
      }
```

---

### 1402. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  int thenJump = emitJump(OP_JUMP_IF_FALSE);
```

---

### 1403. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
emitByte
(
OP_POP
);
```

---

### 1404. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
emitByte
(
OP_POP
);
```

---

### 1405. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```


  if (match(TOKEN_ELSE)) statement();
```

---

### 1406. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
      return simpleInstruction("OP_PRINT", offset);
```

---

### 1407. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
    
case
 
OP_JUMP
:
      
return
 
jumpInstruction
(
"OP_JUMP"
, 
1
, 
chunk
, 
offset
);
    
case
 
OP_JUMP_IF_FALSE
:
      
return
 
jumpInstruction
(
"OP_JUMP_IF_FALSE"
, 
1
, 
chunk
, 
offset
);
```

---

### 1408. Jumping Back and Forth — 23 . 1 . 1 Else clauses

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
int
 
jumpInstruction
(
const
 
char
* 
name
, 
int
 
sign
,
                           
Chunk
* 
chunk
, 
int
 
offset
) {
  
uint16_t
 
jump
 = (
uint16_t
)(
chunk
->
code
[
offset
 + 
1
] << 
8
);
  
jump
 |= 
chunk
->
code
[
offset
 + 
2
];
  
printf
(
"%-16s %4d -> %d
\n
"
, 
name
, 
offset
,
         
offset
 + 
3
 + 
sign
 * 
jump
);
  
return
 
offset
 + 
3
;
}
```

---

### 1409. Jumping Back and Forth — 23 . 2 Logical Operators

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  [TOKEN_NUMBER]        = {number,   NULL,   PREC_NONE},
```

---

### 1410. Jumping Back and Forth — 23 . 2 Logical Operators

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  [
TOKEN_AND
]           = {
NULL
,     
and_
,   
PREC_AND
},
```

---

### 1411. Jumping Back and Forth — 23 . 2 Logical Operators

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  [TOKEN_CLASS]         = {NULL,     NULL,   PREC_NONE},
```

---

### 1412. Jumping Back and Forth — 23 . 2 Logical Operators

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
and_
(
bool
 
canAssign
) {
  
int
 
endJump
 = 
emitJump
(
OP_JUMP_IF_FALSE
);

  
emitByte
(
OP_POP
);
  
parsePrecedence
(
PREC_AND
);

  
patchJump
(
endJump
);
}
```

---

### 1413. Jumping Back and Forth — 23 . 2 . 1 Logical or operator

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  [TOKEN_NIL]           = {literal,  NULL,   PREC_NONE},
```

---

### 1414. Jumping Back and Forth — 23 . 2 . 1 Logical or operator

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  [
TOKEN_OR
]            = {
NULL
,     
or_
,    
PREC_OR
},
```

---

### 1415. Jumping Back and Forth — 23 . 2 . 1 Logical or operator

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  [TOKEN_PRINT]         = {NULL,     NULL,   PREC_NONE},
```

---

### 1416. Jumping Back and Forth — 23 . 2 . 1 Logical or operator

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
or_
(
bool
 
canAssign
) {
  
int
 
elseJump
 = 
emitJump
(
OP_JUMP_IF_FALSE
);
  
int
 
endJump
 = 
emitJump
(
OP_JUMP
);

  
patchJump
(
elseJump
);
  
emitByte
(
OP_POP
);

  
parsePrecedence
(
PREC_OR
);
  
patchJump
(
endJump
);
}
```

---

### 1417. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  } 
else
 
if
 (
match
(
TOKEN_WHILE
)) {
    
whileStatement
();
```

---

### 1418. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
whileStatement
() {
  
consume
(
TOKEN_LEFT_PAREN
, 
"Expect '(' after 'while'."
);
  
expression
();
  
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after condition."
);

  
int
 
exitJump
 = 
emitJump
(
OP_JUMP_IF_FALSE
);
  
emitByte
(
OP_POP
);
  
statement
();

  
patchJump
(
exitJump
);
  
emitByte
(
OP_POP
);
}
```

---

### 1419. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
emitLoop
(
loopStart
);
```

---

### 1420. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```


  patchJump(exitJump);
```

---

### 1421. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
int
 
loopStart
 = 
currentChunk
()->
count
;
```

---

### 1422. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'while'.");
```

---

### 1423. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
emitLoop
(
int
 
loopStart
) {
  
emitByte
(
OP_LOOP
);

  
int
 
offset
 = 
currentChunk
()->
count
 - 
loopStart
 + 
2
;
  
if
 (
offset
 > 
UINT16_MAX
) 
error
(
"Loop body too large."
);

  
emitByte
((
offset
 >> 
8
) & 
0xff
);
  
emitByte
(
offset
 & 
0xff
);
}
```

---

### 1424. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
OP_LOOP
,
```

---

### 1425. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
      
case
 
OP_LOOP
: {
        
uint16_t
 
offset
 = 
READ_SHORT
();
        
vm
.
ip
 -= 
offset
;
        
break
;
      }
```

---

### 1426. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
      return jumpInstruction("OP_JUMP_IF_FALSE", 1, chunk, offset);
```

---

### 1427. Jumping Back and Forth — 23 . 3 While Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
    
case
 
OP_LOOP
:
      
return
 
jumpInstruction
(
"OP_LOOP"
, -
1
, 
chunk
, 
offset
);
```

---

### 1428. Jumping Back and Forth — 23 . 4 For Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  } 
else
 
if
 (
match
(
TOKEN_FOR
)) {
    
forStatement
();
```

---

### 1429. Jumping Back and Forth — 23 . 4 For Statements

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
static
 
void
 
forStatement
() {
  
consume
(
TOKEN_LEFT_PAREN
, 
"Expect '(' after 'for'."
);
  
consume
(
TOKEN_SEMICOLON
, 
"Expect ';'."
);

  
int
 
loopStart
 = 
currentChunk
()->
count
;
  
consume
(
TOKEN_SEMICOLON
, 
"Expect ';'."
);
  
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after for clauses."
);

  
statement
();
  
emitLoop
(
loopStart
);
}
```

---

### 1430. Jumping Back and Forth — 23 . 4 . 1 Initializer clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'for'.");
```

---

### 1431. Jumping Back and Forth — 23 . 4 . 1 Initializer clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
if
 (
match
(
TOKEN_SEMICOLON
)) {
    
// No initializer.

  } 
else
 
if
 (
match
(
TOKEN_VAR
)) {
    
varDeclaration
();
  } 
else
 {
    
expressionStatement
();
  }
```

---

### 1432. Jumping Back and Forth — 23 . 4 . 1 Initializer clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```


  int loopStart = currentChunk()->count;
```

---

### 1433. Jumping Back and Forth — 23 . 4 . 1 Initializer clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
beginScope
();
```

---

### 1434. Jumping Back and Forth — 23 . 4 . 1 Initializer clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after 'for'.");
```

---

### 1435. Jumping Back and Forth — 23 . 4 . 1 Initializer clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
endScope
();
```

---

### 1436. Jumping Back and Forth — 23 . 4 . 2 Condition clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  int loopStart = currentChunk()->count;
```

---

### 1437. Jumping Back and Forth — 23 . 4 . 2 Condition clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
int
 
exitJump
 = -
1
;
  
if
 (!
match
(
TOKEN_SEMICOLON
)) {
    
expression
();
    
consume
(
TOKEN_SEMICOLON
, 
"Expect ';' after loop condition."
);

    
// Jump out of the loop if the condition is false.

    
exitJump
 = 
emitJump
(
OP_JUMP_IF_FALSE
);
    
emitByte
(
OP_POP
); 
// Condition.

  }
```

---

### 1438. Jumping Back and Forth — 23 . 4 . 2 Condition clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after for clauses.");
```

---

### 1439. Jumping Back and Forth — 23 . 4 . 2 Condition clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```


  
if
 (
exitJump
 != -
1
) {
    
patchJump
(
exitJump
);
    
emitByte
(
OP_POP
); 
// Condition.

  }
```

---

### 1440. Jumping Back and Forth — 23 . 4 . 2 Condition clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  endScope();
}
```

---

### 1441. Jumping Back and Forth — 23 . 4 . 3 Increment clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
  
if
 (!
match
(
TOKEN_RIGHT_PAREN
)) {
    
int
 
bodyJump
 = 
emitJump
(
OP_JUMP
);
    
int
 
incrementStart
 = 
currentChunk
()->
count
;
    
expression
();
    
emitByte
(
OP_POP
);
    
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after for clauses."
);

    
emitLoop
(
loopStart
);
    
loopStart
 = 
incrementStart
;
    
patchJump
(
bodyJump
);
  }
```

---

### 1442. Jumping Back and Forth — 23 . 4 . 3 Increment clause

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```


  statement();
```

---

### 1443. Jumping Back and Forth — Challenges

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
switchStmt
     â 
"switch"
 
"("
 
expression
 
")"

                 
"{"
 
switchCase
* 
defaultCase
? 
"}"
 ;

switchCase
     â 
"case"
 
expression
 
":"
 
statement
* ;

defaultCase
    â 
"default"
 
":"
 
statement
* ;
```

---

### 1444. Jumping Back and Forth — Challenges

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
continueStmt
   â 
"continue"
 
";"
 ;
```

---

### 1445. Jumping Back and Forth — Design Note: Considering Goto Harmful

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
// See if the matrix contains a zero.


bool
 
found
 = 
false
;

for
 (
int
 
x
 = 
0
; 
x
 < 
xSize
; 
x
++) {
  
for
 (
int
 
y
 = 
0
; 
y
 < 
ySize
; 
y
++) {
    
for
 (
int
 
z
 = 
0
; 
z
 < 
zSize
; 
z
++) {
      
if
 (
matrix
[
x
][
y
][
z
] == 
0
) {
        
printf
(
"found"
);
        
found
 = 
true
;
        
break
;
      }
    }
    
if
 (
found
) 
break
;
  }
  
if
 (
found
) 
break
;
}
```

---

### 1446. Jumping Back and Forth — Design Note: Considering Goto Harmful

**Source:** https://craftinginterpreters.com/jumping-back-and-forth.html

```
for
 (
int
 
x
 = 
0
; 
x
 < 
xSize
; 
x
++) {
  
for
 (
int
 
y
 = 
0
; 
y
 < 
ySize
; 
y
++) {
    
for
 (
int
 
z
 = 
0
; 
z
 < 
zSize
; 
z
++) {
      
if
 (
matrix
[
x
][
y
][
z
] == 
0
) {
        
printf
(
"found"
);
        
goto
 
done
;
      }
    }
  }
}

done
:
```

---

### 1447. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  struct Obj* next;
};
```

---

### 1448. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```



typedef
 
struct
 {
  
Obj
 
obj
;
  
int
 
arity
;
  
Chunk
 
chunk
;
  
ObjString
* 
name
;
} 
ObjFunction
;
```

---

### 1449. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


struct ObjString {
```

---

### 1450. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  uint32_t hash;
};
```

---

### 1451. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjFunction
* 
newFunction
();
```

---

### 1452. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjString* takeString(char* chars, int length);
```

---

### 1453. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjFunction
* 
newFunction
() {
  
ObjFunction
* 
function
 = 
ALLOCATE_OBJ
(
ObjFunction
, 
OBJ_FUNCTION
);
  
function
->
arity
 = 
0
;
  
function
->
name
 = 
NULL
;
  
initChunk
(&
function
->
chunk
);
  
return
 
function
;
}
```

---

### 1454. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
OBJ_FUNCTION
,
```

---

### 1455. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  OBJ_STRING,
} ObjType;
```

---

### 1456. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
case
 
OBJ_FUNCTION
: {
      
ObjFunction
* 
function
 = (
ObjFunction
*)
object
;
      
freeChunk
(&
function
->
chunk
);
      
FREE
(
ObjFunction
, 
object
);
      
break
;
    }
```

---

### 1457. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
case
 
OBJ_FUNCTION
:
      
printFunction
(
AS_FUNCTION
(
value
));
      
break
;
```

---

### 1458. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
printFunction
(
ObjFunction
* 
function
) {
  
printf
(
"<fn %s>"
, 
function
->
name
->
chars
);
}
```

---

### 1459. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

---

### 1460. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

---

### 1461. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1462. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1463. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

---

### 1464. Calls and Functions — 24 . 1 Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define AS_STRING(value)       ((ObjString*)AS_OBJ(value))
```

---

### 1465. Calls and Functions — 24 . 2 Compiling to Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
ObjFunction
* 
function
;
  
FunctionType
 
type
;
```

---

### 1466. Calls and Functions — 24 . 2 Compiling to Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
typedef
 
enum
 {
  
TYPE_FUNCTION
,
  
TYPE_SCRIPT

} 
FunctionType
;
```

---

### 1467. Calls and Functions — 24 . 2 Compiling to Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```



static
 
Chunk
* 
currentChunk
() {
  
return
 &
current
->
function
->
chunk
;
}
```

---

### 1468. Calls and Functions — 24 . 2 Compiling to Function Objects

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


static void errorAt(Token* token, const char* message) {
```

---

### 1469. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
initCompiler
(&
compiler
, 
TYPE_SCRIPT
);
```

---

### 1470. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  parser.hadError = false;
```

---

### 1471. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
initCompiler
(
Compiler
* 
compiler
, 
FunctionType
 
type
) {
  
compiler
->
function
 = 
NULL
;
  
compiler
->
type
 = 
type
;
```

---

### 1472. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
compiler
->
function
 = 
newFunction
();
```

---

### 1473. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  
Local
* 
local
 = &
current
->
locals
[
current
->
localCount
++];
  
local
->
depth
 = 
0
;
  
local
->
name
.
start
 = 
""
;
  
local
->
name
.
length
 = 
0
;
```

---

### 1474. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
ObjFunction
* 
endCompiler
() {
```

---

### 1475. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
ObjFunction
* 
function
 = 
current
->
function
;
```

---

### 1476. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  
return
 
function
;
```

---

### 1477. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#ifdef DEBUG_PRINT_CODE
  if (!parser.hadError) {
```

---

### 1478. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
disassembleChunk
(
currentChunk
(), 
function
->
name
 != 
NULL

        ? 
function
->
name
->
chars
 : 
"<script>"
);
```

---

### 1479. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  }
#endif
```

---

### 1480. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static void printFunction(ObjFunction* function) {
```

---

### 1481. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
function
->
name
 == 
NULL
) {
    
printf
(
"<script>"
);
    
return
;
  }
```

---

### 1482. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  printf("<fn %s>", function->name->chars);
```

---

### 1483. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjFunction
* 
compile
(
const
 
char
* 
source
);
```

---

### 1484. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


#endif
```

---

### 1485. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjFunction
* 
compile
(
const
 
char
* 
source
) {
```

---

### 1486. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  while (!match(TOKEN_EOF)) {
    declaration();
  }
```

---

### 1487. Calls and Functions — 24 . 2 . 1 Creating functions at compile time

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
ObjFunction
* 
function
 = 
endCompiler
();
  
return
 
parser
.
hadError
 ? 
NULL
 : 
function
;
```

---

### 1488. Calls and Functions — 24 . 3 . 1 Allocating local variables

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
first
() {
  
var
 
a
 = 
1
;
  
second
();
  
var
 
b
 = 
2
;
}


fun
 
second
() {
  
var
 
c
 = 
3
;
  
var
 
d
 = 
4
;
}


first
();
```

---

### 1489. Calls and Functions — 24 . 3 . 1 Allocating local variables

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
first
() {
  
var
 
a
 = 
1
;
  
second
();
  
var
 
b
 = 
2
;
  
second
();
}


fun
 
second
() {
  
var
 
c
 = 
3
;
  
var
 
d
 = 
4
;
}


first
();
```

---

### 1490. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```



typedef
 
struct
 {
  
ObjFunction
* 
function
;
  
uint8_t
* 
ip
;
  
Value
* 
slots
;
} 
CallFrame
;
```

---

### 1491. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


typedef struct {
```

---

### 1492. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
CallFrame
 
frames
[
FRAMES_MAX
];
  
int
 
frameCount
;
```

---

### 1493. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define FRAMES_MAX 64


#define STACK_MAX (FRAMES_MAX * UINT8_COUNT)
```

---

### 1494. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


typedef struct {
```

---

### 1495. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
vm
.
frameCount
 = 
0
;
```

---

### 1496. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
CallFrame
* 
frame
 = &
vm
.
frames
[
vm
.
frameCount
 - 
1
];


#define READ_BYTE() (*frame->ip++)



#define READ_SHORT() \


    (frame->ip += 2, \


    (uint16_t)((frame->ip[-2] << 8) | frame->ip[-1]))



#define READ_CONSTANT() \


    (frame->function->chunk.constants.values[READ_BYTE()])
```

---

### 1497. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define READ_STRING() AS_STRING(READ_CONSTANT())
```

---

### 1498. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      case OP_GET_LOCAL: {
        uint8_t slot = READ_BYTE();
```

---

### 1499. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
push
(
frame
->
slots
[
slot
]);
```

---

### 1500. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      case OP_SET_LOCAL: {
        uint8_t slot = READ_BYTE();
```

---

### 1501. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
frame
->
slots
[
slot
] = 
peek
(
0
);
```

---

### 1502. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      case OP_JUMP: {
        uint16_t offset = READ_SHORT();
```

---

### 1503. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
frame
->
ip
 += 
offset
;
```

---

### 1504. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      case OP_JUMP_IF_FALSE: {
        uint16_t offset = READ_SHORT();
```

---

### 1505. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
if
 (
isFalsey
(
peek
(
0
))) 
frame
->
ip
 += 
offset
;
```

---

### 1506. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      case OP_LOOP: {
        uint16_t offset = READ_SHORT();
```

---

### 1507. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
frame
->
ip
 -= 
offset
;
```

---

### 1508. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
disassembleInstruction
(&
frame
->
function
->
chunk
,
        (
int
)(
frame
->
ip
 - 
frame
->
function
->
chunk
.
code
));
```

---

### 1509. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
InterpretResult interpret(const char* source) {
```

---

### 1510. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
ObjFunction
* 
function
 = 
compile
(
source
);
  
if
 (
function
 == 
NULL
) 
return
 
INTERPRET_COMPILE_ERROR
;

  
push
(
OBJ_VAL
(
function
));
  
CallFrame
* 
frame
 = &
vm
.
frames
[
vm
.
frameCount
++];
  
frame
->
function
 = 
function
;
  
frame
->
ip
 = 
function
->
chunk
.
code
;
  
frame
->
slots
 = 
vm
.
stack
;
```

---

### 1511. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  InterpretResult result = run();
```

---

### 1512. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
return
 
run
();
```

---

### 1513. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
CallFrame
* 
frame
 = &
vm
.
frames
[
vm
.
frameCount
 - 
1
];
  
size_t
 
instruction
 = 
frame
->
ip
 - 
frame
->
function
->
chunk
.
code
 - 
1
;
  
int
 
line
 = 
frame
->
function
->
chunk
.
lines
[
instruction
];
```

---

### 1514. Calls and Functions — 24 . 3 . 3 The call stack

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  fprintf(stderr, "[line %d] in script\n", line);
```

---

### 1515. Calls and Functions — 24 . 4 Function Declarations

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
match
(
TOKEN_FUN
)) {
    
funDeclaration
();
  } 
else
 
if
 (
match
(
TOKEN_VAR
)) {
```

---

### 1516. Calls and Functions — 24 . 4 Function Declarations

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
funDeclaration
() {
  
uint8_t
 
global
 = 
parseVariable
(
"Expect function name."
);
  
markInitialized
();
  
function
(
TYPE_FUNCTION
);
  
defineVariable
(
global
);
}
```

---

### 1517. Calls and Functions — 24 . 4 Function Declarations

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
current
->
scopeDepth
 == 
0
) 
return
;
```

---

### 1518. Calls and Functions — 24 . 4 Function Declarations

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  current->locals[current->localCount - 1].depth =
```

---

### 1519. Calls and Functions — 24 . 4 Function Declarations

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
function
(
FunctionType
 
type
) {
  
Compiler
 
compiler
;
  
initCompiler
(&
compiler
, 
type
);
  
beginScope
();
 


  
consume
(
TOKEN_LEFT_PAREN
, 
"Expect '(' after function name."
);
  
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after parameters."
);
  
consume
(
TOKEN_LEFT_BRACE
, 
"Expect '{' before function body."
);
  
block
();

  
ObjFunction
* 
function
 = 
endCompiler
();
  
emitBytes
(
OP_CONSTANT
, 
makeConstant
(
OBJ_VAL
(
function
)));
}
```

---

### 1520. Calls and Functions — 24 . 4 . 1 A stack of compilers

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
typedef
 
struct
 
Compiler
 {
  
struct
 
Compiler
* 
enclosing
;
```

---

### 1521. Calls and Functions — 24 . 4 . 1 A stack of compilers

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static void initCompiler(Compiler* compiler, FunctionType type) {
```

---

### 1522. Calls and Functions — 24 . 4 . 1 A stack of compilers

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
compiler
->
enclosing
 = 
current
;
```

---

### 1523. Calls and Functions — 24 . 4 . 1 A stack of compilers

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
current
 = 
current
->
enclosing
;
```

---

### 1524. Calls and Functions — 24 . 4 . 2 Function parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  consume(TOKEN_LEFT_PAREN, "Expect '(' after function name.");
```

---

### 1525. Calls and Functions — 24 . 4 . 2 Function parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (!
check
(
TOKEN_RIGHT_PAREN
)) {
    
do
 {
      
current
->
function
->
arity
++;
      
if
 (
current
->
function
->
arity
 > 
255
) {
        
errorAtCurrent
(
"Can't have more than 255 parameters."
);
      }
      
uint8_t
 
constant
 = 
parseVariable
(
"Expect parameter name."
);
      
defineVariable
(
constant
);
    } 
while
 (
match
(
TOKEN_COMMA
));
  }
```

---

### 1526. Calls and Functions — 24 . 4 . 2 Function parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  consume(TOKEN_RIGHT_PAREN, "Expect ')' after parameters.");
```

---

### 1527. Calls and Functions — 24 . 4 . 2 Function parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
type
 != 
TYPE_SCRIPT
) {
    
current
->
function
->
name
 = 
copyString
(
parser
.
previous
.
start
,
                                         
parser
.
previous
.
length
);
  }
```

---

### 1528. Calls and Functions — 24 . 4 . 2 Function parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  Local* local = &current->locals[current->localCount++];
```

---

### 1529. Calls and Functions — 24 . 4 . 2 Function parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
areWeHavingItYet
() {
  
print
 
"Yes we are!"
;
}


print
 
areWeHavingItYet
;
```

---

### 1530. Calls and Functions — 24 . 5 Function Calls

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  [
TOKEN_LEFT_PAREN
]    = {
grouping
, 
call
,   
PREC_CALL
},
```

---

### 1531. Calls and Functions — 24 . 5 Function Calls

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  [TOKEN_RIGHT_PAREN]   = {NULL,     NULL,   PREC_NONE},
```

---

### 1532. Calls and Functions — 24 . 5 Function Calls

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
call
(
bool
 
canAssign
) {
  
uint8_t
 
argCount
 = 
argumentList
();
  
emitBytes
(
OP_CALL
, 
argCount
);
}
```

---

### 1533. Calls and Functions — 24 . 5 Function Calls

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
uint8_t
 
argumentList
() {
  
uint8_t
 
argCount
 = 
0
;
  
if
 (!
check
(
TOKEN_RIGHT_PAREN
)) {
    
do
 {
      
expression
();
      
argCount
++;
    } 
while
 (
match
(
TOKEN_COMMA
));
  }
  
consume
(
TOKEN_RIGHT_PAREN
, 
"Expect ')' after arguments."
);
  
return
 
argCount
;
}
```

---

### 1534. Calls and Functions — 24 . 5 Function Calls

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      
if
 (
argCount
 == 
255
) {
        
error
(
"Can't have more than 255 arguments."
);
      }
```

---

### 1535. Calls and Functions — 24 . 5 Function Calls

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
OP_CALL
,
```

---

### 1536. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
sum
(
a
, 
b
, 
c
) {
  
return
 
a
 + 
b
 + 
c
;
}


print
 
4
 + 
sum
(
5
, 
6
, 
7
);
```

---

### 1537. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      
case
 
OP_CALL
: {
        
int
 
argCount
 = 
READ_BYTE
();
        
if
 (!
callValue
(
peek
(
argCount
), 
argCount
)) {
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
break
;
      }
```

---

### 1538. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
          return INTERPRET_RUNTIME_ERROR;
        }
```

---

### 1539. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
frame
 = &
vm
.
frames
[
vm
.
frameCount
 - 
1
];
```

---

### 1540. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
bool
 
callValue
(
Value
 
callee
, 
int
 
argCount
) {
  
if
 (
IS_OBJ
(
callee
)) {
    
switch
 (
OBJ_TYPE
(
callee
)) {
      
case
 
OBJ_FUNCTION
:
 

        
return
 
call
(
AS_FUNCTION
(
callee
), 
argCount
);
      
default
:
        
break
; 
// Non-callable object type.

    }
  }
  
runtimeError
(
"Can only call functions and classes."
);
  
return
 
false
;
}
```

---

### 1541. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
var
 
notAFunction
 = 
123
;

notAFunction
();
```

---

### 1542. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
bool
 
call
(
ObjFunction
* 
function
, 
int
 
argCount
) {
  
CallFrame
* 
frame
 = &
vm
.
frames
[
vm
.
frameCount
++];
  
frame
->
function
 = 
function
;
  
frame
->
ip
 = 
function
->
chunk
.
code
;
  
frame
->
slots
 = 
vm
.
stackTop
 - 
argCount
 - 
1
;
  
return
 
true
;
}
```

---

### 1543. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      return jumpInstruction("OP_LOOP", -1, chunk, offset);
```

---

### 1544. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
case
 
OP_CALL
:
      
return
 
byteInstruction
(
"OP_CALL"
, 
chunk
, 
offset
);
```

---

### 1545. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
call
(
function
, 
0
);
```

---

### 1546. Calls and Functions — 24 . 5 . 1 Binding arguments to parameters

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  return run();
```

---

### 1547. Calls and Functions — 24 . 5 . 2 Runtime error checking

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static bool call(ObjFunction* function, int argCount) {
```

---

### 1548. Calls and Functions — 24 . 5 . 2 Runtime error checking

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
argCount
 != 
function
->
arity
) {
    
runtimeError
(
"Expected %d arguments but got %d."
,
        
function
->
arity
, 
argCount
);
    
return
 
false
;
  }
```

---

### 1549. Calls and Functions — 24 . 5 . 2 Runtime error checking

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  CallFrame* frame = &vm.frames[vm.frameCount++];
```

---

### 1550. Calls and Functions — 24 . 5 . 2 Runtime error checking

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
vm
.
frameCount
 == 
FRAMES_MAX
) {
    
runtimeError
(
"Stack overflow."
);
    
return
 
false
;
  }
```

---

### 1551. Calls and Functions — 24 . 5 . 2 Runtime error checking

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  CallFrame* frame = &vm.frames[vm.frameCount++];
```

---

### 1552. Calls and Functions — 24 . 5 . 3 Printing stack traces

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
for
 (
int
 
i
 = 
vm
.
frameCount
 - 
1
; 
i
 >= 
0
; 
i
--) {
    
CallFrame
* 
frame
 = &
vm
.
frames
[
i
];
    
ObjFunction
* 
function
 = 
frame
->
function
;
    
size_t
 
instruction
 = 
frame
->
ip
 - 
function
->
chunk
.
code
 - 
1
;
    
fprintf
(
stderr
, 
"[line %d] in "
,
 

            
function
->
chunk
.
lines
[
instruction
]);
    
if
 (
function
->
name
 == 
NULL
) {
      
fprintf
(
stderr
, 
"script
\n
"
);
    } 
else
 {
      
fprintf
(
stderr
, 
"%s()
\n
"
, 
function
->
name
->
chars
);
    }
  }
```

---

### 1553. Calls and Functions — 24 . 5 . 3 Printing stack traces

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  resetStack();
}
```

---

### 1554. Calls and Functions — 24 . 5 . 3 Printing stack traces

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
a
() { 
b
(); }

fun
 
b
() { 
c
(); }

fun
 
c
() {
  
c
(
"too"
, 
"many"
);
}


a
();
```

---

### 1555. Calls and Functions — 24 . 5 . 3 Printing stack traces

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
Expected 0 arguments but got 2.
[line 4] in c()
[line 2] in b()
[line 1] in a()
[line 7] in script
```

---

### 1556. Calls and Functions — 24 . 5 . 4 Returning from functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
        
Value
 
result
 = 
pop
();
        
vm
.
frameCount
--;
        
if
 (
vm
.
frameCount
 == 
0
) {
          
pop
();
          
return
 
INTERPRET_OK
;
        }

        
vm
.
stackTop
 = 
frame
->
slots
;
        
push
(
result
);
        
frame
 = &
vm
.
frames
[
vm
.
frameCount
 - 
1
];
        
break
;
```

---

### 1557. Calls and Functions — 24 . 5 . 4 Returning from functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
noReturn
() {
  
print
 
"Do stuff"
;
  
// No return here.

}


print
 
noReturn
(); 
// ???
```

---

### 1558. Calls and Functions — 24 . 5 . 4 Returning from functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
emitByte
(
OP_NIL
);
```

---

### 1559. Calls and Functions — 24 . 5 . 4 Returning from functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  emitByte(OP_RETURN);
}
```

---

### 1560. Calls and Functions — 24 . 6 Return Statements

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  } 
else
 
if
 (
match
(
TOKEN_RETURN
)) {
    
returnStatement
();
```

---

### 1561. Calls and Functions — 24 . 6 Return Statements

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
returnStatement
() {
  
if
 (
match
(
TOKEN_SEMICOLON
)) {
    
emitReturn
();
  } 
else
 {
    
expression
();
    
consume
(
TOKEN_SEMICOLON
, 
"Expect ';' after return value."
);
    
emitByte
(
OP_RETURN
);
  }
}
```

---

### 1562. Calls and Functions — 24 . 6 Return Statements

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
return
 
"What?!"
;
```

---

### 1563. Calls and Functions — 24 . 6 Return Statements

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
if
 (
current
->
type
 == 
TYPE_SCRIPT
) {
    
error
(
"Can't return from top-level code."
);
  }
```

---

### 1564. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```



typedef
 
Value
 (*
NativeFn
)(
int
 
argCount
, 
Value
* 
args
);


typedef
 
struct
 {
  
Obj
 
obj
;
  
NativeFn
 
function
;
} 
ObjNative
;
```

---

### 1565. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


struct ObjString {
```

---

### 1566. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjNative
* 
newNative
(
NativeFn
 
function
);
```

---

### 1567. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjString* takeString(char* chars, int length);
```

---

### 1568. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
ObjNative
* 
newNative
(
NativeFn
 
function
) {
  
ObjNative
* 
native
 = 
ALLOCATE_OBJ
(
ObjNative
, 
OBJ_NATIVE
);
  
native
->
function
 = 
function
;
  
return
 
native
;
}
```

---

### 1569. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
typedef enum {
  OBJ_FUNCTION,
```

---

### 1570. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  
OBJ_NATIVE
,
```

---

### 1571. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
  OBJ_STRING,
} ObjType;
```

---

### 1572. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
case
 
OBJ_NATIVE
:
      
FREE
(
ObjNative
, 
object
);
      
break
;
```

---

### 1573. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
    
case
 
OBJ_NATIVE
:
      
printf
(
"<native fn>"
);
      
break
;
```

---

### 1574. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

---

### 1575. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define IS_NATIVE(value)       isObjType(value, OBJ_NATIVE)
```

---

### 1576. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1577. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

---

### 1578. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define AS_NATIVE(value) \


    (((ObjNative*)AS_OBJ(value))->function)
```

---

### 1579. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
#define AS_STRING(value)       ((ObjString*)AS_OBJ(value))
```

---

### 1580. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      case OBJ_FUNCTION:
 

        return call(AS_FUNCTION(callee), argCount);
```

---

### 1581. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
      
case
 
OBJ_NATIVE
: {
        
NativeFn
 
native
 = 
AS_NATIVE
(
callee
);
        
Value
 
result
 = 
native
(
argCount
, 
vm
.
stackTop
 - 
argCount
);
        
vm
.
stackTop
 -= 
argCount
 + 
1
;
        
push
(
result
);
        
return
 
true
;
      }
```

---

### 1582. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
void
 
defineNative
(
const
 
char
* 
name
, 
NativeFn
 
function
) {
  
push
(
OBJ_VAL
(
copyString
(
name
, (
int
)
strlen
(
name
))));
  
push
(
OBJ_VAL
(
newNative
(
function
)));
  
tableSet
(&
vm
.
globals
, 
AS_STRING
(
vm
.
stack
[
0
]), 
vm
.
stack
[
1
]);
  
pop
();
  
pop
();
}
```

---

### 1583. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
static
 
Value
 
clockNative
(
int
 
argCount
, 
Value
* 
args
) {
  
return
 
NUMBER_VAL
((
double
)
clock
() / 
CLOCKS_PER_SEC
);
}
```

---

### 1584. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```


  
defineNative
(
"clock"
, 
clockNative
);
```

---

### 1585. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```c


#include "common.h"
```

---

### 1586. Calls and Functions — 24 . 7 Native Functions

**Source:** https://craftinginterpreters.com/calls-and-functions.html

```
fun
 
fib
(
n
) {
  
if
 (
n
 < 
2
) 
return
 
n
;
  
return
 
fib
(
n
 - 
2
) + 
fib
(
n
 - 
1
);
}


var
 
start
 = 
clock
();

print
 
fib
(
35
);

print
 
clock
() - 
start
;
```

---

### 1587. Closures — Closures

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
x
 = 
"global"
;

fun
 
outer
() {
  
var
 
x
 = 
"outer"
;
  
fun
 
inner
() {
    
print
 
x
;
  }
  
inner
();
}

outer
();
```

---

### 1588. Closures — Closures

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
makeClosure
() {
  
var
 
local
 = 
"local"
;
  
fun
 
closure
() {
    
print
 
local
;
  }
  
return
 
closure
;
}


var
 
closure
 = 
makeClosure
();

closure
();
```

---

### 1589. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
makeClosure
(
value
) {
  
fun
 
closure
() {
    
print
 
value
;
  }
  
return
 
closure
;
}


var
 
doughnut
 = 
makeClosure
(
"doughnut"
);

var
 
bagel
 = 
makeClosure
(
"bagel"
);

doughnut
();

bagel
();
```

---

### 1590. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
typedef
 
struct
 {
  
Obj
 
obj
;
  
ObjFunction
* 
function
;
} 
ObjClosure
;
```

---

### 1591. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
ObjClosure
* 
newClosure
(
ObjFunction
* 
function
);
```

---

### 1592. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
ObjClosure
* 
newClosure
(
ObjFunction
* 
function
) {
  
ObjClosure
* 
closure
 = 
ALLOCATE_OBJ
(
ObjClosure
, 
OBJ_CLOSURE
);
  
closure
->
function
 = 
function
;
  
return
 
closure
;
}
```

---

### 1593. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
  
OBJ_CLOSURE
,
```

---

### 1594. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OBJ_CLOSURE
: {
      
FREE
(
ObjClosure
, 
object
);
      
break
;
    }
```

---

### 1595. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

---

### 1596. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
#define IS_CLOSURE(value)      isObjType(value, OBJ_CLOSURE)
```

---

### 1597. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

---

### 1598. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1599. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
#define AS_CLOSURE(value)      ((ObjClosure*)AS_OBJ(value))
```

---

### 1600. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

---

### 1601. Closures — 25 . 1 Closure Objects

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OBJ_CLOSURE
:
      
printFunction
(
AS_CLOSURE
(
value
)->
function
);
      
break
;
```

---

### 1602. Closures — 25 . 1 . 1 Compiling to closure objects

**Source:** https://craftinginterpreters.com/closures.html

```
  ObjFunction* function = endCompiler();
```

---

### 1603. Closures — 25 . 1 . 1 Compiling to closure objects

**Source:** https://craftinginterpreters.com/closures.html

```
  
emitBytes
(
OP_CLOSURE
, 
makeConstant
(
OBJ_VAL
(
function
)));
```

---

### 1604. Closures — 25 . 1 . 1 Compiling to closure objects

**Source:** https://craftinginterpreters.com/closures.html

```
  
OP_CLOSURE
,
```

---

### 1605. Closures — 25 . 1 . 1 Compiling to closure objects

**Source:** https://craftinginterpreters.com/closures.html

```
    case OP_CALL:
      return byteInstruction("OP_CALL", chunk, offset);
```

---

### 1606. Closures — 25 . 1 . 1 Compiling to closure objects

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OP_CLOSURE
: {
      
offset
++;
      
uint8_t
 
constant
 = 
chunk
->
code
[
offset
++];
      
printf
(
"%-16s %4d "
, 
"OP_CLOSURE"
, 
constant
);
      
printValue
(
chunk
->
constants
.
values
[
constant
]);
      
printf
(
"
\n
"
);
      
return
 
offset
;
    }
```

---

### 1607. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
      
case
 
OP_CLOSURE
: {
        
ObjFunction
* 
function
 = 
AS_FUNCTION
(
READ_CONSTANT
());
        
ObjClosure
* 
closure
 = 
newClosure
(
function
);
        
push
(
OBJ_VAL
(
closure
));
        
break
;
      }
```

---

### 1608. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
      
case
 
OBJ_CLOSURE
:
        
return
 
call
(
AS_CLOSURE
(
callee
), 
argCount
);
```

---

### 1609. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
static
 
bool
 
call
(
ObjClosure
* 
closure
, 
int
 
argCount
) {
```

---

### 1610. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
static bool call(ObjClosure* closure, int argCount) {
```

---

### 1611. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
  
if
 (
argCount
 != 
closure
->
function
->
arity
) {
    
runtimeError
(
"Expected %d arguments but got %d."
,
        
closure
->
function
->
arity
, 
argCount
);
```

---

### 1612. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
  CallFrame* frame = &vm.frames[vm.frameCount++];
```

---

### 1613. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
  
frame
->
closure
 = 
closure
;
  
frame
->
ip
 = 
closure
->
function
->
chunk
.
code
;
```

---

### 1614. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
  frame->slots = vm.stackTop - argCount - 1;
```

---

### 1615. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
  
ObjClosure
* 
closure
;
```

---

### 1616. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
    (uint16_t)((frame->ip[-2] << 8) | frame->ip[-1]))
```

---

### 1617. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
#define READ_CONSTANT() \


    (frame->closure->function->chunk.constants.values[READ_BYTE()])
```

---

### 1618. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```


#define READ_STRING() AS_STRING(READ_CONSTANT())
```

---

### 1619. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
    
disassembleInstruction
(&
frame
->
closure
->
function
->
chunk
,
        (
int
)(
frame
->
ip
 - 
frame
->
closure
->
function
->
chunk
.
code
));
```

---

### 1620. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
    
ObjFunction
* 
function
 = 
frame
->
closure
->
function
;
```

---

### 1621. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
    size_t instruction = frame->ip - function->chunk.code - 1;
```

---

### 1622. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```
  
ObjClosure
* 
closure
 = 
newClosure
(
function
);
  
pop
();
  
push
(
OBJ_VAL
(
closure
));
  
call
(
closure
, 
0
);
```

---

### 1623. Closures — 25 . 1 . 2 Interpreting function declarations

**Source:** https://craftinginterpreters.com/closures.html

```


  return run();
```

---

### 1624. Closures — 25 . 2 Upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
1
;    
// (1)

  
x
 = 
2
;        
// (2)

  
fun
 
inner
() { 
// (3)

    
print
 
x
;
  }
  
inner
();
}
```

---

### 1625. Closures — 25 . 2 Upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
{
  
var
 
a
 = 
3
;
  
fun
 
f
() {
    
print
 
a
;
  }
}
```

---

### 1626. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  if (arg != -1) {
    getOp = OP_GET_LOCAL;
    setOp = OP_SET_LOCAL;
```

---

### 1627. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  } 
else
 
if
 ((
arg
 = 
resolveUpvalue
(
current
, &
name
)) != -
1
) {
    
getOp
 = 
OP_GET_UPVALUE
;
    
setOp
 = 
OP_SET_UPVALUE
;
```

---

### 1628. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
OP_GET_UPVALUE
,
  
OP_SET_UPVALUE
,
```

---

### 1629. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
static
 
int
 
resolveUpvalue
(
Compiler
* 
compiler
, 
Token
* 
name
) {
  
if
 (
compiler
->
enclosing
 == 
NULL
) 
return
 -
1
;

  
int
 
local
 = 
resolveLocal
(
compiler
->
enclosing
, 
name
);
  
if
 (
local
 != -
1
) {
    
return
 
addUpvalue
(
compiler
, (
uint8_t
)
local
, 
true
);
  }

  
return
 -
1
;
}
```

---

### 1630. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
1
;
  
fun
 
inner
() {
    
print
 
x
; 
// (1)

  }
  
inner
();
}
```

---

### 1631. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
static
 
int
 
addUpvalue
(
Compiler
* 
compiler
, 
uint8_t
 
index
,
                      
bool
 
isLocal
) {
  
int
 
upvalueCount
 = 
compiler
->
function
->
upvalueCount
;
  
compiler
->
upvalues
[
upvalueCount
].
isLocal
 = 
isLocal
;
  
compiler
->
upvalues
[
upvalueCount
].
index
 = 
index
;
  
return
 
compiler
->
function
->
upvalueCount
++;
}
```

---

### 1632. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  int upvalueCount = compiler->function->upvalueCount;
```

---

### 1633. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```


  
for
 (
int
 
i
 = 
0
; 
i
 < 
upvalueCount
; 
i
++) {
    
Upvalue
* 
upvalue
 = &
compiler
->
upvalues
[
i
];
    
if
 (
upvalue
->
index
 == 
index
 && 
upvalue
->
isLocal
 == 
isLocal
) {
      
return
 
i
;
    }
  }
```

---

### 1634. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  compiler->upvalues[upvalueCount].isLocal = isLocal;
```

---

### 1635. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
int
 
upvalueCount
;
```

---

### 1636. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
function
->
upvalueCount
 = 
0
;
```

---

### 1637. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
Upvalue
 
upvalues
[
UINT8_COUNT
];
```

---

### 1638. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    if (upvalue->index == index && upvalue->isLocal == isLocal) {
      return i;
    }
  }
```

---

### 1639. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
if
 (
upvalueCount
 == 
UINT8_COUNT
) {
    
error
(
"Too many closure variables in function."
);
    
return
 
0
;
  }
```

---

### 1640. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  compiler->upvalues[upvalueCount].isLocal = isLocal;
```

---

### 1641. Closures — 25 . 2 . 1 Compiling upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
typedef
 
struct
 {
  
uint8_t
 
index
;
  
bool
 
isLocal
;
} 
Upvalue
;
```

---

### 1642. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
1
;
  
fun
 
middle
() {
    
fun
 
inner
() {
      
print
 
x
;
    }
  }
}
```

---

### 1643. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
"value"
;
  
fun
 
middle
() {
    
fun
 
inner
() {
      
print
 
x
;
    }

    
print
 
"create inner closure"
;
    
return
 
inner
;
  }

  
print
 
"return from outer"
;
  
return
 
middle
;
}


var
 
mid
 = 
outer
();

var
 
in
 = 
mid
();

in
();
```

---

### 1644. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
return from outer
create inner closure
value
```

---

### 1645. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  if (local != -1) {
    return addUpvalue(compiler, (uint8_t)local, true);
  }
```

---

### 1646. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
int
 
upvalue
 = 
resolveUpvalue
(
compiler
->
enclosing
, 
name
);
  
if
 (
upvalue
 != -
1
) {
    
return
 
addUpvalue
(
compiler
, (
uint8_t
)
upvalue
, 
false
);
  }
```

---

### 1647. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  emitBytes(OP_CLOSURE, makeConstant(OBJ_VAL(function)));
```

---

### 1648. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```


  
for
 (
int
 
i
 = 
0
; 
i
 < 
function
->
upvalueCount
; 
i
++) {
    
emitByte
(
compiler
.
upvalues
[
i
].
isLocal
 ? 
1
 : 
0
);
    
emitByte
(
compiler
.
upvalues
[
i
].
index
);
  }
```

---

### 1649. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```


      
ObjFunction
* 
function
 = 
AS_FUNCTION
(
          
chunk
->
constants
.
values
[
constant
]);
      
for
 (
int
 
j
 = 
0
; 
j
 < 
function
->
upvalueCount
; 
j
++) {
        
int
 
isLocal
 = 
chunk
->
code
[
offset
++];
        
int
 
index
 = 
chunk
->
code
[
offset
++];
        
printf
(
"%04d      |                     %s %d
\n
"
,
               
offset
 - 
2
, 
isLocal
 ? 
"local"
 : 
"upvalue"
, 
index
);
      }
```

---

### 1650. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
a
 = 
1
;
  
var
 
b
 = 
2
;
  
fun
 
middle
() {
    
var
 
c
 = 
3
;
    
var
 
d
 = 
4
;
    
fun
 
inner
() {
      
print
 
a
 + 
c
 + 
b
 + 
d
;
    }
  }
}
```

---

### 1651. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
0004    9 OP_CLOSURE          2 <fn inner>
0006      |                     upvalue 0
0008      |                     local 1
0010      |                     upvalue 1
0012      |                     local 2
```

---

### 1652. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    case OP_SET_GLOBAL:
      return constantInstruction("OP_SET_GLOBAL", chunk, offset);
```

---

### 1653. Closures — 25 . 2 . 2 Flattening upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OP_GET_UPVALUE
:
      
return
 
byteInstruction
(
"OP_GET_UPVALUE"
, 
chunk
, 
offset
);
    
case
 
OP_SET_UPVALUE
:
      
return
 
byteInstruction
(
"OP_SET_UPVALUE"
, 
chunk
, 
offset
);
```

---

### 1654. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
typedef
 
struct
 
ObjUpvalue
 {
  
Obj
 
obj
;
  
Value
* 
location
;
} 
ObjUpvalue
;
```

---

### 1655. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
"before"
;
  
fun
 
inner
() {
    
x
 = 
"assigned"
;
  }
  
inner
();
  
print
 
x
;
}

outer
();
```

---

### 1656. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
ObjString* copyString(const char* chars, int length);
```

---

### 1657. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
ObjUpvalue
* 
newUpvalue
(
Value
* 
slot
);
```

---

### 1658. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
ObjUpvalue
* 
newUpvalue
(
Value
* 
slot
) {
  
ObjUpvalue
* 
upvalue
 = 
ALLOCATE_OBJ
(
ObjUpvalue
, 
OBJ_UPVALUE
);
  
upvalue
->
location
 = 
slot
;
  
return
 
upvalue
;
}
```

---

### 1659. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
  
OBJ_UPVALUE
```

---

### 1660. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
      FREE(ObjString, object);
      break;
    }
```

---

### 1661. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OBJ_UPVALUE
:
      
FREE
(
ObjUpvalue
, 
object
);
      
break
;
```

---

### 1662. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
    case OBJ_STRING:
      printf("%s", AS_CSTRING(value));
      break;
```

---

### 1663. Closures — 25 . 3 Upvalue Objects

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OBJ_UPVALUE
:
      
printf
(
"upvalue"
);
      
break
;
```

---

### 1664. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
  
ObjUpvalue
** 
upvalues
;
  
int
 
upvalueCount
;
```

---

### 1665. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
ObjClosure* newClosure(ObjFunction* function) {
```

---

### 1666. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
  
ObjUpvalue
** 
upvalues
 = 
ALLOCATE
(
ObjUpvalue
*,
                                   
function
->
upvalueCount
);
  
for
 (
int
 
i
 = 
0
; 
i
 < 
function
->
upvalueCount
; 
i
++) {
    
upvalues
[
i
] = 
NULL
;
  }
```

---

### 1667. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
  ObjClosure* closure = ALLOCATE_OBJ(ObjClosure, OBJ_CLOSURE);
```

---

### 1668. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
  
closure
->
upvalues
 = 
upvalues
;
  
closure
->
upvalueCount
 = 
function
->
upvalueCount
;
```

---

### 1669. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
      
ObjClosure
* 
closure
 = (
ObjClosure
*)
object
;
      
FREE_ARRAY
(
ObjUpvalue
*, 
closure
->
upvalues
,
                 
closure
->
upvalueCount
);
```

---

### 1670. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
        
for
 (
int
 
i
 = 
0
; 
i
 < 
closure
->
upvalueCount
; 
i
++) {
          
uint8_t
 
isLocal
 = 
READ_BYTE
();
          
uint8_t
 
index
 = 
READ_BYTE
();
          
if
 (
isLocal
) {
            
closure
->
upvalues
[
i
] =
                
captureUpvalue
(
frame
->
slots
 + 
index
);
          } 
else
 {
            
closure
->
upvalues
[
i
] = 
frame
->
closure
->
upvalues
[
index
];
          }
        }
```

---

### 1671. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
static
 
ObjUpvalue
* 
captureUpvalue
(
Value
* 
local
) {
  
ObjUpvalue
* 
createdUpvalue
 = 
newUpvalue
(
local
);
  
return
 
createdUpvalue
;
}
```

---

### 1672. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
      
case
 
OP_GET_UPVALUE
: {
        
uint8_t
 
slot
 = 
READ_BYTE
();
        
push
(*
frame
->
closure
->
upvalues
[
slot
]->
location
);
        
break
;
      }
```

---

### 1673. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
      
case
 
OP_SET_UPVALUE
: {
        
uint8_t
 
slot
 = 
READ_BYTE
();
        *
frame
->
closure
->
upvalues
[
slot
]->
location
 = 
peek
(
0
);
        
break
;
      }
```

---

### 1674. Closures — 25 . 3 . 1 Upvalues in closures

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
"outside"
;
  
fun
 
inner
() {
    
print
 
x
;
  }
  
inner
();
}

outer
();
```

---

### 1675. Closures — 25 . 4 Closed Upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
fun
 
outer
() {
  
var
 
x
 = 
"outside"
;
  
fun
 
inner
() {
    
print
 
x
;
  }

  
return
 
inner
;
}


var
 
closure
 = 
outer
();

closure
();
```

---

### 1676. Closures — 25 . 4 . 1 Values and variables

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
globalSet
;

var
 
globalGet
;


fun
 
main
() {
  
var
 
a
 = 
"initial"
;

  
fun
 
set
() { 
a
 = 
"updated"
; }
  
fun
 
get
() { 
print
 
a
; }

  
globalSet
 = 
set
;
  
globalGet
 = 
get
;
}


main
();

globalSet
();

globalGet
();
```

---

### 1677. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
bool
 
isCaptured
;
```

---

### 1678. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
local
->
isCaptured
 = 
false
;
```

---

### 1679. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
local
->
isCaptured
 = 
false
;
```

---

### 1680. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    
compiler
->
enclosing
->
locals
[
local
].
isCaptured
 = 
true
;
```

---

### 1681. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    return addUpvalue(compiler, (uint8_t)local, true);
```

---

### 1682. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  while (current->localCount > 0 &&
         current->locals[current->localCount - 1].depth >
            current->scopeDepth) {
```

---

### 1683. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    
if
 (
current
->
locals
[
current
->
localCount
 - 
1
].
isCaptured
) {
      
emitByte
(
OP_CLOSE_UPVALUE
);
    } 
else
 {
      
emitByte
(
OP_POP
);
    }
```

---

### 1684. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    current->localCount--;
  }
```

---

### 1685. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
OP_CLOSE_UPVALUE
,
```

---

### 1686. Closures — 25 . 4 . 2 Closing upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
    
case
 
OP_CLOSE_UPVALUE
:
      
return
 
simpleInstruction
(
"OP_CLOSE_UPVALUE"
, 
offset
);
```

---

### 1687. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
struct
 
ObjUpvalue
* 
next
;
```

---

### 1688. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
upvalue
->
next
 = 
NULL
;
```

---

### 1689. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
ObjUpvalue
* 
openUpvalues
;
```

---

### 1690. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
vm
.
openUpvalues
 = 
NULL
;
```

---

### 1691. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
{
  
var
 
a
 = 
1
;
  
fun
 
f
() {
    
print
 
a
;
  }
  
var
 
b
 = 
2
;
  
fun
 
g
() {
    
print
 
b
;
  }
  
var
 
c
 = 
3
;
  
fun
 
h
() {
    
print
 
c
;
  }
}
```

---

### 1692. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
static ObjUpvalue* captureUpvalue(Value* local) {
```

---

### 1693. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
ObjUpvalue
* 
prevUpvalue
 = 
NULL
;
  
ObjUpvalue
* 
upvalue
 = 
vm
.
openUpvalues
;
  
while
 (
upvalue
 != 
NULL
 && 
upvalue
->
location
 > 
local
) {
    
prevUpvalue
 = 
upvalue
;
    
upvalue
 = 
upvalue
->
next
;
  }

  
if
 (
upvalue
 != 
NULL
 && 
upvalue
->
location
 == 
local
) {
    
return
 
upvalue
;
  }
```

---

### 1694. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  ObjUpvalue* createdUpvalue = newUpvalue(local);
```

---

### 1695. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  ObjUpvalue* createdUpvalue = newUpvalue(local);
```

---

### 1696. Closures — 25 . 4 . 3 Tracking open upvalues

**Source:** https://craftinginterpreters.com/closures.html

```
  
createdUpvalue
->
next
 = 
upvalue
;

  
if
 (
prevUpvalue
 == 
NULL
) {
    
vm
.
openUpvalues
 = 
createdUpvalue
;
  } 
else
 {
    
prevUpvalue
->
next
 = 
createdUpvalue
;
  }
```

---

### 1697. Closures — 25 . 4 . 4 Closing upvalues at runtime

**Source:** https://craftinginterpreters.com/closures.html

```
      
case
 
OP_CLOSE_UPVALUE
:
        
closeUpvalues
(
vm
.
stackTop
 - 
1
);
        
pop
();
        
break
;
```

---

### 1698. Closures — 25 . 4 . 4 Closing upvalues at runtime

**Source:** https://craftinginterpreters.com/closures.html

```
static
 
void
 
closeUpvalues
(
Value
* 
last
) {
  
while
 (
vm
.
openUpvalues
 != 
NULL
 &&
         
vm
.
openUpvalues
->
location
 >= 
last
) {
    
ObjUpvalue
* 
upvalue
 = 
vm
.
openUpvalues
;
    
upvalue
->
closed
 = *
upvalue
->
location
;
    
upvalue
->
location
 = &
upvalue
->
closed
;
    
vm
.
openUpvalues
 = 
upvalue
->
next
;
  }
}
```

---

### 1699. Closures — 25 . 4 . 4 Closing upvalues at runtime

**Source:** https://craftinginterpreters.com/closures.html

```
  
Value
 
closed
;
```

---

### 1700. Closures — 25 . 4 . 4 Closing upvalues at runtime

**Source:** https://craftinginterpreters.com/closures.html

```
  ObjUpvalue* upvalue = ALLOCATE_OBJ(ObjUpvalue, OBJ_UPVALUE);
```

---

### 1701. Closures — 25 . 4 . 4 Closing upvalues at runtime

**Source:** https://craftinginterpreters.com/closures.html

```
  
upvalue
->
closed
 = 
NIL_VAL
;
```

---

### 1702. Closures — 25 . 4 . 4 Closing upvalues at runtime

**Source:** https://craftinginterpreters.com/closures.html

```
        
closeUpvalues
(
frame
->
slots
);
```

---

### 1703. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
globalOne
;

var
 
globalTwo
;


fun
 
main
() {
  {
    
var
 
a
 = 
"one"
;
    
fun
 
one
() {
      
print
 
a
;
    }
    
globalOne
 = 
one
;
  }

  {
    
var
 
a
 = 
"two"
;
    
fun
 
two
() {
      
print
 
a
;
    }
    
globalTwo
 = 
two
;
  }
}


main
();

globalOne
();

globalTwo
();
```

---

### 1704. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
globalOne
;

var
 
globalTwo
;


fun
 
main
() {
  
for
 (
var
 
a
 = 
1
; 
a
 <= 
2
; 
a
 = 
a
 + 
1
) {
    
fun
 
closure
() {
      
print
 
a
;
    }
    
if
 (
globalOne
 == 
nil
) {
      
globalOne
 = 
closure
;
    } 
else
 {
      
globalTwo
 = 
closure
;
    }
  }
}


main
();

globalOne
();

globalTwo
();
```

---

### 1705. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
closures
 = [];

for
 (
var
 
i
 = 
1
; 
i
 <= 
2
; 
i
++) {
  
closures
.
push
(
function
 () { 
console
.
log
(
i
); });
}


closures
[
0
]();

closures
[
1
]();
```

---

### 1706. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
closures
 = [];

var
 
i
;

for
 (
i
 = 
1
; 
i
 <= 
2
; 
i
++) {
  
closures
.
push
(
function
 () { 
console
.
log
(
i
); });
}


closures
[
0
]();

closures
[
1
]();
```

---

### 1707. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
var
 
closures
 = [];

for
 (
let
 
i
 = 
1
; 
i
 <= 
2
; 
i
++) {
  
closures
.
push
(
function
 () { 
console
.
log
(
i
); });
}


closures
[
0
]();

closures
[
1
]();
```

---

### 1708. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
closures
 = []

for
 
i
 
in
 
range
(
1
, 
3
):
  
closures
.
append
(
lambda
: 
print
(
i
))


closures
[
0
]()

closures
[
1
]()
```

---

### 1709. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
closures
 = []

for
 
i
 
in
 
1
..
2
 
do

  
closures
 << 
lambda
 { 
puts
 
i
 }

end



closures
[
0
].
call


closures
[
1
].
call
```

---

### 1710. Closures — Design Note: Closing Over the Loop Variable

**Source:** https://craftinginterpreters.com/closures.html

```
closures
 = []
(
1
..
2
).
each
 
do
 |
i
|
  
closures
 << 
lambda
 { 
puts
 
i
 }

end



closures
[
0
].
call


closures
[
1
].
call
```

---

### 1711. Garbage Collection — 26 . 1 Reachability

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
var
 
a
 = 
"first value"
;

a
 = 
"updated"
;

// GC here.


print
 
a
;
```

---

### 1712. Garbage Collection — 26 . 1 Reachability

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
var
 
global
 = 
"string"
;
{
  
var
 
local
 = 
"another"
;
  
print
 
global
 + 
local
;
}
```

---

### 1713. Garbage Collection — 26 . 1 Reachability

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
fun
 
makeClosure
() {
  
var
 
a
 = 
"data"
;

  
fun
 
f
() { 
print
 
a
; }
  
return
 
f
;
}

{
  
var
 
closure
 = 
makeClosure
();
  
// GC here.

  
closure
();
}
```

---

### 1714. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

---

### 1715. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
collectGarbage
();
```

---

### 1716. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
collectGarbage
() {
}
```

---

### 1717. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```



#define DEBUG_STRESS_GC
```

---

### 1718. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#define UINT8_COUNT (UINT8_MAX + 1)
```

---

### 1719. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

---

### 1720. Garbage Collection — 26 . 2 . 1 Collecting garbage

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
if
 (
newSize
 > 
oldSize
) {

#ifdef DEBUG_STRESS_GC

    
collectGarbage
();

#endif

  }
```

---

### 1721. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#define UINT8_COUNT (UINT8_MAX + 1)
```

---

### 1722. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```c



#ifdef DEBUG_LOG_GC


#include <stdio.h>


#include "debug.h"


#endif
```

---

### 1723. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

---

### 1724. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
#ifdef DEBUG_LOG_GC

  
printf
(
"-- gc begin
\n
"
);

#endif
```

---

### 1725. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  printf("-- gc begin\n");
#endif
```

---

### 1726. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```



#ifdef DEBUG_LOG_GC

  
printf
(
"-- gc end
\n
"
);

#endif
```

---

### 1727. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```



#ifdef DEBUG_LOG_GC

  
printf
(
"%p allocate %zu for %d
\n
"
, (
void
*)
object
, 
size
, 
type
);

#endif
```

---

### 1728. Garbage Collection — 26 . 2 . 2 Debug logging

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
#ifdef DEBUG_LOG_GC

  
printf
(
"%p free type %d
\n
"
, (
void
*)
object
, 
object
->
type
);

#endif
```

---

### 1729. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
#ifdef DEBUG_LOG_GC
  printf("-- gc begin\n");
#endif
```

---

### 1730. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
markRoots
();
```

---

### 1731. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#ifdef DEBUG_LOG_GC
```

---

### 1732. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static
 
void
 
markRoots
() {
  
for
 (
Value
* 
slot
 = 
vm
.
stack
; 
slot
 < 
vm
.
stackTop
; 
slot
++) {
    
markValue
(*
slot
);
  }
}
```

---

### 1733. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

---

### 1734. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markValue
(
Value
 
value
);
```

---

### 1735. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markValue
(
Value
 
value
) {
  
if
 (
IS_OBJ
(
value
)) 
markObject
(
AS_OBJ
(
value
));
}
```

---

### 1736. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

---

### 1737. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markObject
(
Obj
* 
object
);
```

---

### 1738. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markObject
(
Obj
* 
object
) {
  
if
 (
object
 == 
NULL
) 
return
;
  
object
->
isMarked
 = 
true
;
}
```

---

### 1739. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
bool
 
isMarked
;
```

---

### 1740. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
object
->
isMarked
 = 
false
;
```

---

### 1741. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  object->next = vm.objects;
```

---

### 1742. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void markObject(Obj* object) {
  if (object == NULL) return;
```

---

### 1743. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
#ifdef DEBUG_LOG_GC

  
printf
(
"%p mark "
, (
void
*)
object
);
  
printValue
(
OBJ_VAL
(
object
));
  
printf
(
"
\n
"
);

#endif
```

---

### 1744. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    markValue(*slot);
  }
```

---

### 1745. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
markTable
(&
vm
.
globals
);
```

---

### 1746. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
ObjString* tableFindString(Table* table, const char* chars,
                           int length, uint32_t hash);
```

---

### 1747. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markTable
(
Table
* 
table
);
```

---

### 1748. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#endif
```

---

### 1749. Garbage Collection — 26 . 3 Marking the Roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markTable
(
Table
* 
table
) {
  
for
 (
int
 
i
 = 
0
; 
i
 < 
table
->
capacity
; 
i
++) {
    
Entry
* 
entry
 = &
table
->
entries
[
i
];
    
markObject
((
Obj
*)
entry
->
key
);
    
markValue
(
entry
->
value
);
  }
}
```

---

### 1750. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
for
 (
int
 
i
 = 
0
; 
i
 < 
vm
.
frameCount
; 
i
++) {
    
markObject
((
Obj
*)
vm
.
frames
[
i
].
closure
);
  }
```

---

### 1751. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  markTable(&vm.globals);
```

---

### 1752. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  for (int i = 0; i < vm.frameCount; i++) {
    markObject((Obj*)vm.frames[i].closure);
  }
```

---

### 1753. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
for
 (
ObjUpvalue
* 
upvalue
 = 
vm
.
openUpvalues
;
       
upvalue
 != 
NULL
;
       
upvalue
 = 
upvalue
->
next
) {
    
markObject
((
Obj
*)
upvalue
);
  }
```

---

### 1754. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  markTable(&vm.globals);
```

---

### 1755. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
markCompilerRoots
();
```

---

### 1756. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
ObjFunction* compile(const char* source);
```

---

### 1757. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markCompilerRoots
();
```

---

### 1758. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#endif
```

---

### 1759. Garbage Collection — 26 . 3 . 1 Less obvious roots

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
markCompilerRoots
() {
  
Compiler
* 
compiler
 = 
current
;
  
while
 (
compiler
 != 
NULL
) {
    
markObject
((
Obj
*)
compiler
->
function
);
    
compiler
 = 
compiler
->
enclosing
;
  }
}
```

---

### 1760. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
if
 (
vm
.
grayCapacity
 < 
vm
.
grayCount
 + 
1
) {
    
vm
.
grayCapacity
 = 
GROW_CAPACITY
(
vm
.
grayCapacity
);
    
vm
.
grayStack
 = (
Obj
**)
realloc
(
vm
.
grayStack
,
                                  
sizeof
(
Obj
*) * 
vm
.
grayCapacity
);
  }

  
vm
.
grayStack
[
vm
.
grayCount
++] = 
object
;
```

---

### 1761. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
int
 
grayCount
;
  
int
 
grayCapacity
;
  
Obj
** 
grayStack
;
```

---

### 1762. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
vm
.
grayCount
 = 
0
;
  
vm
.
grayCapacity
 = 
0
;
  
vm
.
grayStack
 = 
NULL
;
```

---

### 1763. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  initTable(&vm.globals);
```

---

### 1764. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    object = next;
  }
```

---

### 1765. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
free
(
vm
.
grayStack
);
```

---

### 1766. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    vm.grayStack = (Obj**)realloc(vm.grayStack,
                                  sizeof(Obj*) * vm.grayCapacity);
```

---

### 1767. Garbage Collection — 26 . 4 . 2 A worklist for gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


    
if
 (
vm
.
grayStack
 == 
NULL
) 
exit
(
1
);
```

---

### 1768. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
traceReferences
();
```

---

### 1769. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#ifdef DEBUG_LOG_GC
```

---

### 1770. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static
 
void
 
traceReferences
() {
  
while
 (
vm
.
grayCount
 > 
0
) {
    
Obj
* 
object
 = 
vm
.
grayStack
[--
vm
.
grayCount
];
    
blackenObject
(
object
);
  }
}
```

---

### 1771. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static
 
void
 
blackenObject
(
Obj
* 
object
) {
  
switch
 (
object
->
type
) {
    
case
 
OBJ_NATIVE
:
    
case
 
OBJ_STRING
:
      
break
;
  }
}
```

---

### 1772. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static void blackenObject(Obj* object) {
  switch (object->type) {
```

---

### 1773. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    
case
 
OBJ_UPVALUE
:
      
markValue
(((
ObjUpvalue
*)
object
)->
closed
);
      
break
;
```

---

### 1774. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    
case
 
OBJ_FUNCTION
: {
      
ObjFunction
* 
function
 = (
ObjFunction
*)
object
;
      
markObject
((
Obj
*)
function
->
name
);
      
markArray
(&
function
->
chunk
.
constants
);
      
break
;
    }
```

---

### 1775. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static
 
void
 
markArray
(
ValueArray
* 
array
) {
  
for
 (
int
 
i
 = 
0
; 
i
 < 
array
->
count
; 
i
++) {
    
markValue
(
array
->
values
[
i
]);
  }
}
```

---

### 1776. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    
case
 
OBJ_CLOSURE
: {
      
ObjClosure
* 
closure
 = (
ObjClosure
*)
object
;
      
markObject
((
Obj
*)
closure
->
function
);
      
for
 (
int
 
i
 = 
0
; 
i
 < 
closure
->
upvalueCount
; 
i
++) {
        
markObject
((
Obj
*)
closure
->
upvalues
[
i
]);
      }
      
break
;
    }
```

---

### 1777. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static void blackenObject(Obj* object) {
```

---

### 1778. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
#ifdef DEBUG_LOG_GC

  
printf
(
"%p blacken "
, (
void
*)
object
);
  
printValue
(
OBJ_VAL
(
object
));
  
printf
(
"
\n
"
);

#endif
```

---

### 1779. Garbage Collection — 26 . 4 . 3 Processing gray objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
if
 (
object
->
isMarked
) 
return
;
```

---

### 1780. Garbage Collection — 26 . 5 Sweeping Unused Objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
sweep
();
```

---

### 1781. Garbage Collection — 26 . 5 Sweeping Unused Objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#ifdef DEBUG_LOG_GC
```

---

### 1782. Garbage Collection — 26 . 5 Sweeping Unused Objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
static
 
void
 
sweep
() {
  
Obj
* 
previous
 = 
NULL
;
  
Obj
* 
object
 = 
vm
.
objects
;
  
while
 (
object
 != 
NULL
) {
    
if
 (
object
->
isMarked
) {
      
previous
 = 
object
;
      
object
 = 
object
->
next
;
    } 
else
 {
      
Obj
* 
unreached
 = 
object
;
      
object
 = 
object
->
next
;
      
if
 (
previous
 != 
NULL
) {
        
previous
->
next
 = 
object
;
      } 
else
 {
        
vm
.
objects
 = 
object
;
      }

      
freeObject
(
unreached
);
    }
  }
}
```

---

### 1783. Garbage Collection — 26 . 5 Sweeping Unused Objects

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
      
object
->
isMarked
 = 
false
;
```

---

### 1784. Garbage Collection — 26 . 5 . 1 Weak references and the string pool

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
tableRemoveWhite
(&
vm
.
strings
);
```

---

### 1785. Garbage Collection — 26 . 5 . 1 Weak references and the string pool

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
ObjString* tableFindString(Table* table, const char* chars,
                           int length, uint32_t hash);
```

---

### 1786. Garbage Collection — 26 . 5 . 1 Weak references and the string pool

**Source:** https://craftinginterpreters.com/garbage-collection.html

```



void
 
tableRemoveWhite
(
Table
* 
table
);
```

---

### 1787. Garbage Collection — 26 . 5 . 1 Weak references and the string pool

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void
 
tableRemoveWhite
(
Table
* 
table
) {
  
for
 (
int
 
i
 = 
0
; 
i
 < 
table
->
capacity
; 
i
++) {
    
Entry
* 
entry
 = &
table
->
entries
[
i
];
    
if
 (
entry
->
key
 != 
NULL
 && !
entry
->
key
->
obj
.
isMarked
) {
      
tableDelete
(
table
, 
entry
->
key
);
    }
  }
}
```

---

### 1788. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
size_t
 
bytesAllocated
;
  
size_t
 
nextGC
;
```

---

### 1789. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
vm
.
bytesAllocated
 = 
0
;
  
vm
.
nextGC
 = 
1024
 * 
1024
;
```

---

### 1790. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  vm.grayCount = 0;
```

---

### 1791. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

---

### 1792. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
vm
.
bytesAllocated
 += 
newSize
 - 
oldSize
;
```

---

### 1793. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
    collectGarbage();
#endif
```

---

### 1794. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


    
if
 (
vm
.
bytesAllocated
 > 
vm
.
nextGC
) {
      
collectGarbage
();
    }
```

---

### 1795. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
vm
.
nextGC
 = 
vm
.
bytesAllocated
 * 
GC_HEAP_GROW_FACTOR
;
```

---

### 1796. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


#ifdef DEBUG_LOG_GC
```

---

### 1797. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```



#define GC_HEAP_GROW_FACTOR 2
```

---

### 1798. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

---

### 1799. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
size_t
 
before
 = 
vm
.
bytesAllocated
;
```

---

### 1800. Garbage Collection — 26 . 6 . 2 Self-adjusting heap

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
printf
(
"   collected %zu bytes (from %zu to %zu) next at %zu
\n
"
,
         
before
 - 
vm
.
bytesAllocated
, 
before
, 
vm
.
bytesAllocated
,
         
vm
.
nextGC
);
```

---

### 1801. Garbage Collection — 26 . 7 . 1 Adding to the constant table

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
int addConstant(Chunk* chunk, Value value) {
```

---

### 1802. Garbage Collection — 26 . 7 . 1 Adding to the constant table

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
push
(
value
);
```

---

### 1803. Garbage Collection — 26 . 7 . 1 Adding to the constant table

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  writeValueArray(&chunk->constants, value);
```

---

### 1804. Garbage Collection — 26 . 7 . 1 Adding to the constant table

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  writeValueArray(&chunk->constants, value);
```

---

### 1805. Garbage Collection — 26 . 7 . 1 Adding to the constant table

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
pop
();
```

---

### 1806. Garbage Collection — 26 . 7 . 1 Adding to the constant table

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


void initChunk(Chunk* chunk) {
```

---

### 1807. Garbage Collection — 26 . 7 . 2 Interning strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  string->chars = chars;
  string->hash = hash;
```

---

### 1808. Garbage Collection — 26 . 7 . 2 Interning strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  
push
(
OBJ_VAL
(
string
));
```

---

### 1809. Garbage Collection — 26 . 7 . 2 Interning strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  tableSet(&vm.strings, string, NIL_VAL);
```

---

### 1810. Garbage Collection — 26 . 7 . 2 Interning strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  tableSet(&vm.strings, string, NIL_VAL);
```

---

### 1811. Garbage Collection — 26 . 7 . 2 Interning strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
pop
();
```

---

### 1812. Garbage Collection — 26 . 7 . 2 Interning strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  return string;
}
```

---

### 1813. Garbage Collection — 26 . 7 . 3 Concatenating strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
ObjString
* 
b
 = 
AS_STRING
(
peek
(
0
));
  
ObjString
* 
a
 = 
AS_STRING
(
peek
(
1
));
```

---

### 1814. Garbage Collection — 26 . 7 . 3 Concatenating strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```


  int length = a->length + b->length;
```

---

### 1815. Garbage Collection — 26 . 7 . 3 Concatenating strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  ObjString* result = takeString(chars, length);
```

---

### 1816. Garbage Collection — 26 . 7 . 3 Concatenating strings

**Source:** https://craftinginterpreters.com/garbage-collection.html

```
  
pop
();
  
pop
();
```

---

### 1817. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```



typedef
 
struct
 {
  
Obj
 
obj
;
  
ObjString
* 
name
;
} 
ObjClass
;
```

---

### 1818. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```


ObjClosure* newClosure(ObjFunction* function);
```

---

### 1819. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  
OBJ_CLASS
,
```

---

### 1820. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

---

### 1821. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define IS_CLASS(value)        isObjType(value, OBJ_CLASS)
```

---

### 1822. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define IS_CLOSURE(value)      isObjType(value, OBJ_CLOSURE)
```

---

### 1823. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1824. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define AS_CLASS(value)        ((ObjClass*)AS_OBJ(value))
```

---

### 1825. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define AS_CLOSURE(value)      ((ObjClosure*)AS_OBJ(value))
```

---

### 1826. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
ObjClass
* 
newClass
(
ObjString
* 
name
);
```

---

### 1827. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
ObjClosure* newClosure(ObjFunction* function);
```

---

### 1828. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
ObjClass
* 
newClass
(
ObjString
* 
name
) {
  
ObjClass
* 
klass
 = 
ALLOCATE_OBJ
(
ObjClass
, 
OBJ_CLASS
);
  
klass
->
name
 = 
name
;
 

  
return
 
klass
;
}
```

---

### 1829. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OBJ_CLASS
: {
      
FREE
(
ObjClass
, 
object
);
      
break
;
    }
```

---

### 1830. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OBJ_CLASS
: {
      
ObjClass
* 
klass
 = (
ObjClass
*)
object
;
      
markObject
((
Obj
*)
klass
->
name
);
      
break
;
    }
```

---

### 1831. Classes and Instances — 27 . 1 Class Objects

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OBJ_CLASS
:
      
printf
(
"%s"
, 
AS_CLASS
(
value
)->
name
->
chars
);
      
break
;
```

---

### 1832. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  
if
 (
match
(
TOKEN_CLASS
)) {
    
classDeclaration
();
  } 
else
 
if
 (
match
(
TOKEN_FUN
)) {
```

---

### 1833. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
static
 
void
 
classDeclaration
() {
  
consume
(
TOKEN_IDENTIFIER
, 
"Expect class name."
);
  
uint8_t
 
nameConstant
 = 
identifierConstant
(&
parser
.
previous
);
  
declareVariable
();

  
emitBytes
(
OP_CLASS
, 
nameConstant
);
  
defineVariable
(
nameConstant
);

  
consume
(
TOKEN_LEFT_BRACE
, 
"Expect '{' before class body."
);
  
consume
(
TOKEN_RIGHT_BRACE
, 
"Expect '}' after class body."
);
}
```

---

### 1834. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
var
 
Pie
 = 
class
 {}
```

---

### 1835. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  
OP_CLASS
,
```

---

### 1836. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    case OP_RETURN:
      return simpleInstruction("OP_RETURN", offset);
```

---

### 1837. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OP_CLASS
:
      
return
 
constantInstruction
(
"OP_CLASS"
, 
chunk
, 
offset
);
```

---

### 1838. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
        break;
      }
```

---

### 1839. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      
case
 
OP_CLASS
:
        
push
(
OBJ_VAL
(
newClass
(
READ_STRING
())));
        
break
;
```

---

### 1840. Classes and Instances — 27 . 2 Class Declarations

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
class
 
Brioche
 {}

print
 
Brioche
;
```

---

### 1841. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```



typedef
 
struct
 {
  
Obj
 
obj
;
  
ObjClass
* 
klass
;
  
Table
 
fields
;
 

} 
ObjInstance
;
```

---

### 1842. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```


ObjClass* newClass(ObjString* name);
```

---

### 1843. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  
OBJ_INSTANCE
,
```

---

### 1844. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define IS_FUNCTION(value)     isObjType(value, OBJ_FUNCTION)
```

---

### 1845. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define IS_INSTANCE(value)     isObjType(value, OBJ_INSTANCE)
```

---

### 1846. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define IS_NATIVE(value)       isObjType(value, OBJ_NATIVE)
```

---

### 1847. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define AS_FUNCTION(value)     ((ObjFunction*)AS_OBJ(value))
```

---

### 1848. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
#define AS_INSTANCE(value)     ((ObjInstance*)AS_OBJ(value))
```

---

### 1849. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
ObjInstance
* 
newInstance
(
ObjClass
* 
klass
);
```

---

### 1850. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
ObjNative* newNative(NativeFn function);
```

---

### 1851. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
ObjInstance
* 
newInstance
(
ObjClass
* 
klass
) {
  
ObjInstance
* 
instance
 = 
ALLOCATE_OBJ
(
ObjInstance
, 
OBJ_INSTANCE
);
  
instance
->
klass
 = 
klass
;
  
initTable
(&
instance
->
fields
);
  
return
 
instance
;
}
```

---

### 1852. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      FREE(ObjFunction, object);
      break;
    }
```

---

### 1853. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OBJ_INSTANCE
: {
      
ObjInstance
* 
instance
 = (
ObjInstance
*)
object
;
      
freeTable
(&
instance
->
fields
);
      
FREE
(
ObjInstance
, 
object
);
      
break
;
    }
```

---

### 1854. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      markArray(&function->chunk.constants);
      break;
    }
```

---

### 1855. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OBJ_INSTANCE
: {
      
ObjInstance
* 
instance
 = (
ObjInstance
*)
object
;
      
markObject
((
Obj
*)
instance
->
klass
);
      
markTable
(&
instance
->
fields
);
      
break
;
    }
```

---

### 1856. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OBJ_INSTANCE
:
      
printf
(
"%s instance"
,
             
AS_INSTANCE
(
value
)->
klass
->
name
->
chars
);
      
break
;
```

---

### 1857. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      
case
 
OBJ_CLASS
: {
        
ObjClass
* 
klass
 = 
AS_CLASS
(
callee
);
        
vm
.
stackTop
[-
argCount
 - 
1
] = 
OBJ_VAL
(
newInstance
(
klass
));
        
return
 
true
;
      }
```

---

### 1858. Classes and Instances — 27 . 3 Instances of Classes

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```java
class
 
Brioche
 {}

print
 
Brioche
();
```

---

### 1859. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
eclair
.
filling
 = 
"pastry creme"
;

print
 
eclair
.
filling
;
```

---

### 1860. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  [TOKEN_COMMA]         = {NULL,     NULL,   PREC_NONE},
```

---

### 1861. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  [
TOKEN_DOT
]           = {
NULL
,     
dot
,    
PREC_CALL
},
```

---

### 1862. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  [TOKEN_MINUS]         = {unary,    binary, PREC_TERM},
```

---

### 1863. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
static
 
void
 
dot
(
bool
 
canAssign
) {
  
consume
(
TOKEN_IDENTIFIER
, 
"Expect property name after '.'."
);
  
uint8_t
 
name
 = 
identifierConstant
(&
parser
.
previous
);

  
if
 (
canAssign
 && 
match
(
TOKEN_EQUAL
)) {
    
expression
();
    
emitBytes
(
OP_SET_PROPERTY
, 
name
);
  } 
else
 {
    
emitBytes
(
OP_GET_PROPERTY
, 
name
);
  }
}
```

---

### 1864. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
a
 + 
b
.
c
 = 
3
```

---

### 1865. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
a
 + (
b
.
c
 = 
3
)
```

---

### 1866. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
  
OP_GET_PROPERTY
,
  
OP_SET_PROPERTY
,
```

---

### 1867. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      return byteInstruction("OP_SET_UPVALUE", chunk, offset);
```

---

### 1868. Classes and Instances — 27 . 4 Get and Set Expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
    
case
 
OP_GET_PROPERTY
:
      
return
 
constantInstruction
(
"OP_GET_PROPERTY"
, 
chunk
, 
offset
);
    
case
 
OP_SET_PROPERTY
:
      
return
 
constantInstruction
(
"OP_SET_PROPERTY"
, 
chunk
, 
offset
);
```

---

### 1869. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      
case
 
OP_GET_PROPERTY
: {
        
ObjInstance
* 
instance
 = 
AS_INSTANCE
(
peek
(
0
));
        
ObjString
* 
name
 = 
READ_STRING
();

        
Value
 
value
;
        
if
 (
tableGet
(&
instance
->
fields
, 
name
, &
value
)) {
          
pop
(); 
// Instance.

          
push
(
value
);
          
break
;
        }
      }
```

---

### 1870. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
          push(value);
          break;
        }
```

---

### 1871. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```


        
runtimeError
(
"Undefined property '%s'."
, 
name
->
chars
);
        
return
 
INTERPRET_RUNTIME_ERROR
;
```

---

### 1872. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      }
      case OP_EQUAL: {
```

---

### 1873. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
var
 
obj
 = 
"not an instance"
;

print
 
obj
.
field
;
```

---

### 1874. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
        
if
 (!
IS_INSTANCE
(
peek
(
0
))) {
          
runtimeError
(
"Only instances have properties."
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
```

---

### 1875. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
        ObjInstance* instance = AS_INSTANCE(peek(0));
```

---

### 1876. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
        return INTERPRET_RUNTIME_ERROR;
      }
```

---

### 1877. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
      
case
 
OP_SET_PROPERTY
: {
        
ObjInstance
* 
instance
 = 
AS_INSTANCE
(
peek
(
1
));
        
tableSet
(&
instance
->
fields
, 
READ_STRING
(), 
peek
(
0
));
        
Value
 
value
 = 
pop
();
        
pop
();
        
push
(
value
);
        
break
;
      }
```

---

### 1878. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```java
class
 
Toast
 {}

var
 
toast
 = 
Toast
();

print
 
toast
.
jam
 = 
"grape"
; 
// Prints "grape".
```

---

### 1879. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
        
if
 (!
IS_INSTANCE
(
peek
(
1
))) {
          
runtimeError
(
"Only instances have fields."
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
```

---

### 1880. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```
        ObjInstance* instance = AS_INSTANCE(peek(1));
```

---

### 1881. Classes and Instances — 27 . 4 . 1 Interpreting getter and setter expressions

**Source:** https://craftinginterpreters.com/classes-and-instances.html

```java
class
 
Pair
 {}


var
 
pair
 = 
Pair
();

pair
.
first
 = 
1
;

pair
.
second
 = 
2
;

print
 
pair
.
first
 + 
pair
.
second
; 
// 3.
```

---

### 1882. Methods and Initializers — 28 . 1 . 1 Representing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
typedef struct {
  Obj obj;
  ObjString* name;
```

---

### 1883. Methods and Initializers — 28 . 1 . 1 Representing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
Table
 
methods
;
```

---

### 1884. Methods and Initializers — 28 . 1 . 1 Representing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
initTable
(&
klass
->
methods
);
```

---

### 1885. Methods and Initializers — 28 . 1 . 1 Representing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
      
ObjClass
* 
klass
 = (
ObjClass
*)
object
;
      
freeTable
(&
klass
->
methods
);
```

---

### 1886. Methods and Initializers — 28 . 1 . 1 Representing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
      
markTable
(&
klass
->
methods
);
```

---

### 1887. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  consume(TOKEN_LEFT_BRACE, "Expect '{' before class body.");
```

---

### 1888. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
while
 (!
check
(
TOKEN_RIGHT_BRACE
) && !
check
(
TOKEN_EOF
)) {
    
method
();
  }
```

---

### 1889. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  consume(TOKEN_RIGHT_BRACE, "Expect '}' after class body.");
```

---

### 1890. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
void
 
method
() {
  
consume
(
TOKEN_IDENTIFIER
, 
"Expect method name."
);
  
uint8_t
 
constant
 = 
identifierConstant
(&
parser
.
previous
);
  
emitBytes
(
OP_METHOD
, 
constant
);
}
```

---

### 1891. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  uint8_t constant = identifierConstant(&parser.previous);
```

---

### 1892. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


  
FunctionType
 
type
 = 
TYPE_FUNCTION
;
  
function
(
type
);
```

---

### 1893. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  consume(TOKEN_IDENTIFIER, "Expect class name.");
```

---

### 1894. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
Token
 
className
 = 
parser
.
previous
;
```

---

### 1895. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  uint8_t nameConstant = identifierConstant(&parser.previous);
```

---

### 1896. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
namedVariable
(
className
, 
false
);
```

---

### 1897. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  consume(TOKEN_LEFT_BRACE, "Expect '{' before class body.");
```

---

### 1898. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  consume(TOKEN_RIGHT_BRACE, "Expect '}' after class body.");
```

---

### 1899. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
emitByte
(
OP_POP
);
```

---

### 1900. Methods and Initializers — 28 . 1 . 2 Compiling method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
class
 
Brunch
 {
  
bacon
() {}
  
eggs
() {}
}
```

---

### 1901. Methods and Initializers — 28 . 1 . 3 Executing method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
OP_METHOD
```

---

### 1902. Methods and Initializers — 28 . 1 . 3 Executing method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    case OP_CLASS:
      return constantInstruction("OP_CLASS", chunk, offset);
```

---

### 1903. Methods and Initializers — 28 . 1 . 3 Executing method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    
case
 
OP_METHOD
:
      
return
 
constantInstruction
(
"OP_METHOD"
, 
chunk
, 
offset
);
```

---

### 1904. Methods and Initializers — 28 . 1 . 3 Executing method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
      
case
 
OP_METHOD
:
        
defineMethod
(
READ_STRING
());
        
break
;
```

---

### 1905. Methods and Initializers — 28 . 1 . 3 Executing method declarations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
void
 
defineMethod
(
ObjString
* 
name
) {
  
Value
 
method
 = 
peek
(
0
);
  
ObjClass
* 
klass
 = 
AS_CLASS
(
peek
(
1
));
  
tableSet
(&
klass
->
methods
, 
name
, 
method
);
  
pop
();
}
```

---

### 1906. Methods and Initializers — 28 . 2 Method References

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
instance
.
method
(
argument
);
```

---

### 1907. Methods and Initializers — 28 . 2 Method References

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
var
 
closure
 = 
instance
.
method
;

closure
(
argument
);
```

---

### 1908. Methods and Initializers — 28 . 2 Method References

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
Person
 {
  
sayName
() {
    
print
 
this
.
name
;
  }
}


var
 
jane
 = 
Person
();

jane
.
name
 = 
"Jane"
;


var
 
method
 = 
jane
.
sayName
;

method
(); 
// ?
```

---

### 1909. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
typedef
 
struct
 {
  
Obj
 
obj
;
  
Value
 
receiver
;
  
ObjClosure
* 
method
;
} 
ObjBoundMethod
;
```

---

### 1910. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
OBJ_BOUND_METHOD
,
```

---

### 1911. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

---

### 1912. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
#define IS_BOUND_METHOD(value) isObjType(value, OBJ_BOUND_METHOD)
```

---

### 1913. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
#define IS_CLASS(value)        isObjType(value, OBJ_CLASS)
```

---

### 1914. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

---

### 1915. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
#define AS_BOUND_METHOD(value) ((ObjBoundMethod*)AS_OBJ(value))
```

---

### 1916. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
#define AS_CLASS(value)        ((ObjClass*)AS_OBJ(value))
```

---

### 1917. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
ObjBoundMethod
* 
newBoundMethod
(
Value
 
receiver
,
                               
ObjClosure
* 
method
);
```

---

### 1918. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
ObjBoundMethod
* 
newBoundMethod
(
Value
 
receiver
,
                               
ObjClosure
* 
method
) {
  
ObjBoundMethod
* 
bound
 = 
ALLOCATE_OBJ
(
ObjBoundMethod
,
                                       
OBJ_BOUND_METHOD
);
  
bound
->
receiver
 = 
receiver
;
  
bound
->
method
 = 
method
;
  
return
 
bound
;
}
```

---

### 1919. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    
case
 
OBJ_BOUND_METHOD
:
      
FREE
(
ObjBoundMethod
, 
object
);
      
break
;
```

---

### 1920. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    
case
 
OBJ_BOUND_METHOD
: {
      
ObjBoundMethod
* 
bound
 = (
ObjBoundMethod
*)
object
;
      
markValue
(
bound
->
receiver
);
      
markObject
((
Obj
*)
bound
->
method
);
      
break
;
    }
```

---

### 1921. Methods and Initializers — 28 . 2 . 1 Bound methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    
case
 
OBJ_BOUND_METHOD
:
      
printFunction
(
AS_BOUND_METHOD
(
value
)->
method
->
function
);
      
break
;
```

---

### 1922. Methods and Initializers — 28 . 2 . 2 Accessing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
          pop(); // Instance.
          push(value);
          break;
        }
```

---

### 1923. Methods and Initializers — 28 . 2 . 2 Accessing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
        
if
 (!
bindMethod
(
instance
->
klass
, 
name
)) {
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
break
;
```

---

### 1924. Methods and Initializers — 28 . 2 . 2 Accessing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
bool
 
bindMethod
(
ObjClass
* 
klass
, 
ObjString
* 
name
) {
  
Value
 
method
;
  
if
 (!
tableGet
(&
klass
->
methods
, 
name
, &
method
)) {
    
runtimeError
(
"Undefined property '%s'."
, 
name
->
chars
);
    
return
 
false
;
  }

  
ObjBoundMethod
* 
bound
 = 
newBoundMethod
(
peek
(
0
),
                                         
AS_CLOSURE
(
method
));
  
pop
();
  
push
(
OBJ_VAL
(
bound
));
  
return
 
true
;
}
```

---

### 1925. Methods and Initializers — 28 . 2 . 2 Accessing methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
Brunch
 {
  
eggs
() {}
}


var
 
brunch
 = 
Brunch
();

var
 
eggs
 = 
brunch
.
eggs
;
```

---

### 1926. Methods and Initializers — 28 . 2 . 3 Calling methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
      
case
 
OBJ_BOUND_METHOD
: {
        
ObjBoundMethod
* 
bound
 = 
AS_BOUND_METHOD
(
callee
);
        
return
 
call
(
bound
->
method
, 
argCount
);
      }
```

---

### 1927. Methods and Initializers — 28 . 2 . 3 Calling methods

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
Scone
 {
  
topping
(
first
, 
second
) {
    
print
 
"scone with "
 + 
first
 + 
" and "
 + 
second
;
  }
}


var
 
scone
 = 
Scone
();

scone
.
topping
(
"berries"
, 
"cream"
);
```

---

### 1928. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  [TOKEN_SUPER]         = {NULL,     NULL,   PREC_NONE},
```

---

### 1929. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  [
TOKEN_THIS
]          = {
this_
,    
NULL
,   
PREC_NONE
},
```

---

### 1930. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  [TOKEN_TRUE]          = {literal,  NULL,   PREC_NONE},
```

---

### 1931. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
void
 
this_
(
bool
 
canAssign
) {
  
variable
(
false
);
}
```

---

### 1932. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
if
 (
type
 != 
TYPE_FUNCTION
) {
    
local
->
name
.
start
 = 
"this"
;
    
local
->
name
.
length
 = 
4
;
  } 
else
 {
    
local
->
name
.
start
 = 
""
;
    
local
->
name
.
length
 = 
0
;
  }
```

---

### 1933. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
Nested
 {
  
method
() {
    
fun
 
function
() {
      
print
 
this
;
    }

    
function
();
  }
}


Nested
().
method
();
```

---

### 1934. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
TYPE_METHOD
,
```

---

### 1935. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  uint8_t constant = identifierConstant(&parser.previous);
```

---

### 1936. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
FunctionType
 
type
 = 
TYPE_METHOD
;
```

---

### 1937. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
      case OBJ_BOUND_METHOD: {
        ObjBoundMethod* bound = AS_BOUND_METHOD(callee);
```

---

### 1938. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
        
vm
.
stackTop
[-
argCount
 - 
1
] = 
bound
->
receiver
;
```

---

### 1939. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
        return call(bound->method, argCount);
      }
```

---

### 1940. Methods and Initializers — 28 . 3 This

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
scone
.
topping
(
"berries"
, 
"cream"
);
```

---

### 1941. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
print
 
this
; 
// At top level.



fun
 
notMethod
() {
  
print
 
this
; 
// In a function.

}
```

---

### 1942. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
ClassCompiler
* 
currentClass
 = 
NULL
;
```

---

### 1943. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


static Chunk* currentChunk() {
```

---

### 1944. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```



typedef
 
struct
 
ClassCompiler
 {
  
struct
 
ClassCompiler
* 
enclosing
;
} 
ClassCompiler
;
```

---

### 1945. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


Parser parser;
```

---

### 1946. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
ClassCompiler
 
classCompiler
;
  
classCompiler
.
enclosing
 = 
currentClass
;
  
currentClass
 = &
classCompiler
;
```

---

### 1947. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


  
currentClass
 = 
currentClass
->
enclosing
;
```

---

### 1948. Methods and Initializers — 28 . 3 . 1 Misusing this

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
if
 (
currentClass
 == 
NULL
) {
    
error
(
"Can't use 'this' outside of a class."
);
    
return
;
  }
```

---

### 1949. Methods and Initializers — 28 . 4 Instance Initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
fun
 
create
(
klass
) {
  
var
 
obj
 = 
newInstance
(
klass
);
  
obj
.
init
();
  
return
 
obj
;
}
```

---

### 1950. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
        vm.stackTop[-argCount - 1] = OBJ_VAL(newInstance(klass));
```

---

### 1951. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
        
Value
 
initializer
;
        
if
 (
tableGet
(&
klass
->
methods
, 
vm
.
initString
,
                     &
initializer
)) {
          
return
 
call
(
AS_CLOSURE
(
initializer
), 
argCount
);
        }
```

---

### 1952. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
Brunch
 {
  
init
(
food
, 
drink
) {}
}


Brunch
(
"eggs"
, 
"coffee"
);
```

---

### 1953. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
          return call(AS_CLOSURE(initializer), argCount);
```

---

### 1954. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
        } 
else
 
if
 (
argCount
 != 
0
) {
          
runtimeError
(
"Expected 0 arguments but got %d."
,
                       
argCount
);
          
return
 
false
;
```

---

### 1955. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
ObjString
* 
initString
;
```

---

### 1956. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


  
vm
.
initString
 = 
copyString
(
"init"
, 
4
);
```

---

### 1957. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


  defineNative("clock", clockNative);
```

---

### 1958. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
markObject
((
Obj
*)
vm
.
initString
);
```

---

### 1959. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
vm
.
initString
 = 
NULL
;
```

---

### 1960. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  vm.initString = copyString("init", 4);
```

---

### 1961. Methods and Initializers — 28 . 4 . 1 Invoking initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
vm
.
initString
 = 
NULL
;
```

---

### 1962. Methods and Initializers — 28 . 4 . 2 Initializer return values

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
if
 (
parser
.
previous
.
length
 == 
4
 &&
      
memcmp
(
parser
.
previous
.
start
, 
"init"
, 
4
) == 
0
) {
    
type
 = 
TYPE_INITIALIZER
;
  }
```

---

### 1963. Methods and Initializers — 28 . 4 . 2 Initializer return values

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
TYPE_INITIALIZER
,
```

---

### 1964. Methods and Initializers — 28 . 4 . 2 Initializer return values

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
if
 (
current
->
type
 == 
TYPE_INITIALIZER
) {
    
emitBytes
(
OP_GET_LOCAL
, 
0
);
  } 
else
 {
    
emitByte
(
OP_NIL
);
  }
```

---

### 1965. Methods and Initializers — 28 . 4 . 3 Incorrect returns in initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  if (match(TOKEN_SEMICOLON)) {
    emitReturn();
  } else {
```

---

### 1966. Methods and Initializers — 28 . 4 . 3 Incorrect returns in initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    
if
 (
current
->
type
 == 
TYPE_INITIALIZER
) {
      
error
(
"Can't return a value from an initializer."
);
    }
```

---

### 1967. Methods and Initializers — 28 . 4 . 3 Incorrect returns in initializers

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
CoffeeMaker
 {
  
init
(
coffee
) {
    
this
.
coffee
 = 
coffee
;
  }

  
brew
() {
    
print
 
"Enjoy your cup of "
 + 
this
.
coffee
;

    
// No reusing the grounds!

    
this
.
coffee
 = 
nil
;
  }
}


var
 
maker
 = 
CoffeeMaker
(
"coffee and chicory"
);

maker
.
brew
();
```

---

### 1968. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  if (canAssign && match(TOKEN_EQUAL)) {
    expression();
    emitBytes(OP_SET_PROPERTY, name);
```

---

### 1969. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  } 
else
 
if
 (
match
(
TOKEN_LEFT_PAREN
)) {
    
uint8_t
 
argCount
 = 
argumentList
();
    
emitBytes
(
OP_INVOKE
, 
name
);
    
emitByte
(
argCount
);
```

---

### 1970. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  
OP_INVOKE
,
```

---

### 1971. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    case OP_CALL:
      return byteInstruction("OP_CALL", chunk, offset);
```

---

### 1972. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
    
case
 
OP_INVOKE
:
      
return
 
invokeInstruction
(
"OP_INVOKE"
, 
chunk
, 
offset
);
```

---

### 1973. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
int
 
invokeInstruction
(
const
 
char
* 
name
, 
Chunk
* 
chunk
,
                                
int
 
offset
) {
  
uint8_t
 
constant
 = 
chunk
->
code
[
offset
 + 
1
];
  
uint8_t
 
argCount
 = 
chunk
->
code
[
offset
 + 
2
];
  
printf
(
"%-16s (%d args) %4d '"
, 
name
, 
argCount
, 
constant
);
  
printValue
(
chunk
->
constants
.
values
[
constant
]);
  
printf
(
"'
\n
"
);
  
return
 
offset
 + 
3
;
}
```

---

### 1974. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
      
case
 
OP_INVOKE
: {
        
ObjString
* 
method
 = 
READ_STRING
();
        
int
 
argCount
 = 
READ_BYTE
();
        
if
 (!
invoke
(
method
, 
argCount
)) {
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
frame
 = &
vm
.
frames
[
vm
.
frameCount
 - 
1
];
        
break
;
      }
```

---

### 1975. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
bool
 
invoke
(
ObjString
* 
name
, 
int
 
argCount
) {
  
Value
 
receiver
 = 
peek
(
argCount
);
  
ObjInstance
* 
instance
 = 
AS_INSTANCE
(
receiver
);
  
return
 
invokeFromClass
(
instance
->
klass
, 
name
, 
argCount
);
}
```

---

### 1976. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


  
if
 (!
IS_INSTANCE
(
receiver
)) {
    
runtimeError
(
"Only instances have methods."
);
    
return
 
false
;
  }
```

---

### 1977. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  ObjInstance* instance = AS_INSTANCE(receiver);
```

---

### 1978. Methods and Initializers — 28 . 5 Optimized Invocations

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
static
 
bool
 
invokeFromClass
(
ObjClass
* 
klass
, 
ObjString
* 
name
,
                            
int
 
argCount
) {
  
Value
 
method
;
  
if
 (!
tableGet
(&
klass
->
methods
, 
name
, &
method
)) {
    
runtimeError
(
"Undefined property '%s'."
, 
name
->
chars
);
    
return
 
false
;
  }
  
return
 
call
(
AS_CLOSURE
(
method
), 
argCount
);
}
```

---

### 1979. Methods and Initializers — 28 . 5 . 1 Invoking fields

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```java
class
 
Oops
 {
  
init
() {
    
fun
 
f
() {
      
print
 
"not a method"
;
    }

    
this
.
field
 = 
f
;
  }
}


var
 
oops
 = 
Oops
();

oops
.
field
();
```

---

### 1980. Methods and Initializers — 28 . 5 . 1 Invoking fields

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  ObjInstance* instance = AS_INSTANCE(receiver);
```

---

### 1981. Methods and Initializers — 28 . 5 . 1 Invoking fields

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```


  
Value
 
value
;
  
if
 (
tableGet
(&
instance
->
fields
, 
name
, &
value
)) {
    
vm
.
stackTop
[-
argCount
 - 
1
] = 
value
;
    
return
 
callValue
(
value
, 
argCount
);
  }
```

---

### 1982. Methods and Initializers — 28 . 5 . 1 Invoking fields

**Source:** https://craftinginterpreters.com/methods-and-initializers.html

```
  return invokeFromClass(instance->klass, name, argCount);
```

---

### 1983. Superclasses — 29 . 1 Inheriting Methods

**Source:** https://craftinginterpreters.com/superclasses.html

```java
class
 
Doughnut
 {
  
cook
() {
    
print
 
"Dunk in the fryer."
;
  }
}


class
 
Cruller
 < 
Doughnut
 {
  
finish
() {
    
print
 
"Glaze with icing."
;
  }
}
```

---

### 1984. Superclasses — 29 . 1 Inheriting Methods

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
if
 (
match
(
TOKEN_LESS
)) {
    
consume
(
TOKEN_IDENTIFIER
, 
"Expect superclass name."
);
    
variable
(
false
);
    
namedVariable
(
className
, 
false
);
    
emitByte
(
OP_INHERIT
);
  }
```

---

### 1985. Superclasses — 29 . 1 Inheriting Methods

**Source:** https://craftinginterpreters.com/superclasses.html

```
class
 
Cruller
 < 
Doughnut
 {
```

---

### 1986. Superclasses — 29 . 1 Inheriting Methods

**Source:** https://craftinginterpreters.com/superclasses.html

```


    
if
 (
identifiersEqual
(&
className
, &
parser
.
previous
)) {
      
error
(
"A class can't inherit from itself."
);
    }
```

---

### 1987. Superclasses — 29 . 1 . 1 Executing inheritance

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
OP_INHERIT
,
```

---

### 1988. Superclasses — 29 . 1 . 1 Executing inheritance

**Source:** https://craftinginterpreters.com/superclasses.html

```
      return constantInstruction("OP_CLASS", chunk, offset);
```

---

### 1989. Superclasses — 29 . 1 . 1 Executing inheritance

**Source:** https://craftinginterpreters.com/superclasses.html

```
    
case
 
OP_INHERIT
:
      
return
 
simpleInstruction
(
"OP_INHERIT"
, 
offset
);
```

---

### 1990. Superclasses — 29 . 1 . 1 Executing inheritance

**Source:** https://craftinginterpreters.com/superclasses.html

```
      
case
 
OP_INHERIT
: {
        
Value
 
superclass
 = 
peek
(
1
);
        
ObjClass
* 
subclass
 = 
AS_CLASS
(
peek
(
0
));
        
tableAddAll
(&
AS_CLASS
(
superclass
)->
methods
,
                    &
subclass
->
methods
);
        
pop
(); 
// Subclass.

        
break
;
      }
```

---

### 1991. Superclasses — 29 . 1 . 2 Invalid superclasses

**Source:** https://craftinginterpreters.com/superclasses.html

```
var
 
NotClass
 = 
"So not a class"
;

class
 
OhNo
 < 
NotClass
 {}
```

---

### 1992. Superclasses — 29 . 1 . 2 Invalid superclasses

**Source:** https://craftinginterpreters.com/superclasses.html

```
        
if
 (!
IS_CLASS
(
superclass
)) {
          
runtimeError
(
"Superclass must be a class."
);
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
```

---

### 1993. Superclasses — 29 . 1 . 2 Invalid superclasses

**Source:** https://craftinginterpreters.com/superclasses.html

```
        ObjClass* subclass = AS_CLASS(peek(0));
```

---

### 1994. Superclasses — 29 . 2 Storing Superclasses

**Source:** https://craftinginterpreters.com/superclasses.html

```java
class
 
A
 {
  
method
() {
    
print
 
"A method"
;
  }
}


class
 
B
 < 
A
 {
  
method
() {
    
print
 
"B method"
;
  }

  
test
() {
    
super
.
method
();
  }
}


class
 
C
 < 
B
 {}


C
().
test
();
```

---

### 1995. Superclasses — 29 . 2 Storing Superclasses

**Source:** https://craftinginterpreters.com/superclasses.html

```java
class
 
A
 {
  
method
() {
    
print
 
"A method"
;
  }
}


var
 
Bs_super
 = 
A
;

class
 
B
 < 
A
 {
  
method
() {
    
print
 
"B method"
;
  }

  
test
() {
    
runtimeSuperCall
(
Bs_super
, 
"method"
);
  }
}


var
 
Cs_super
 = 
B
;

class
 
C
 < 
B
 {}


C
().
test
();
```

---

### 1996. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
    
beginScope
();
    
addLocal
(
syntheticToken
(
"super"
));
    
defineVariable
(
0
);
```

---

### 1997. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
    namedVariable(className, false);
    emitByte(OP_INHERIT);
```

---

### 1998. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
static
 
Token
 
syntheticToken
(
const
 
char
* 
text
) {
  
Token
 
token
;
  
token
.
start
 = 
text
;
  
token
.
length
 = (
int
)
strlen
(
text
);
  
return
 
token
;
}
```

---

### 1999. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```


  
if
 (
classCompiler
.
hasSuperclass
) {
    
endScope
();
  }
```

---

### 2000. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```


  currentClass = currentClass->enclosing;
```

---

### 2001. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
typedef struct ClassCompiler {
  struct ClassCompiler* enclosing;
```

---

### 2002. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
bool
 
hasSuperclass
;
```

---

### 2003. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
classCompiler
.
hasSuperclass
 = 
false
;
```

---

### 2004. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
  classCompiler.enclosing = currentClass;
```

---

### 2005. Superclasses — 29 . 2 . 1 A superclass local variable

**Source:** https://craftinginterpreters.com/superclasses.html

```
    
classCompiler
.
hasSuperclass
 = 
true
;
```

---

### 2006. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  [TOKEN_RETURN]        = {NULL,     NULL,   PREC_NONE},
```

---

### 2007. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  [
TOKEN_SUPER
]         = {
super_
,   
NULL
,   
PREC_NONE
},
```

---

### 2008. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  [TOKEN_THIS]          = {this_,    NULL,   PREC_NONE},
```

---

### 2009. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
static
 
void
 
super_
(
bool
 
canAssign
) {
  
consume
(
TOKEN_DOT
, 
"Expect '.' after 'super'."
);
  
consume
(
TOKEN_IDENTIFIER
, 
"Expect superclass method name."
);
  
uint8_t
 
name
 = 
identifierConstant
(&
parser
.
previous
);
}
```

---

### 2010. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```java
class
 
A
 {
  
method
() {
    
print
 
"A"
;
  }
}


class
 
B
 < 
A
 {
  
method
() {
    
var
 
closure
 = 
super
.
method
;
    
closure
(); 
// Prints "A".

  }
}
```

---

### 2011. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  uint8_t name = identifierConstant(&parser.previous);
```

---

### 2012. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```


  
namedVariable
(
syntheticToken
(
"this"
), 
false
);
  
namedVariable
(
syntheticToken
(
"super"
), 
false
);
  
emitBytes
(
OP_GET_SUPER
, 
name
);
```

---

### 2013. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```java
class
 
Doughnut
 {
  
cook
() {
    
print
 
"Dunk in the fryer."
;
    
this
.
finish
(
"sprinkles"
);
  }

  
finish
(
ingredient
) {
    
print
 
"Finish with "
 + 
ingredient
;
  }
}


class
 
Cruller
 < 
Doughnut
 {
  
finish
(
ingredient
) {
    
// No sprinkles, always icing.

    
super
.
finish
(
"icing"
);
  }
}
```

---

### 2014. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
if
 (
currentClass
 == 
NULL
) {
    
error
(
"Can't use 'super' outside of a class."
);
  } 
else
 
if
 (!
currentClass
->
hasSuperclass
) {
    
error
(
"Can't use 'super' in a class with no superclass."
);
  }
```

---

### 2015. Superclasses — 29 . 3 Super Calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  consume(TOKEN_DOT, "Expect '.' after 'super'.");
```

---

### 2016. Superclasses — 29 . 3 . 1 Executing super accesses

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
OP_GET_SUPER
,
```

---

### 2017. Superclasses — 29 . 3 . 1 Executing super accesses

**Source:** https://craftinginterpreters.com/superclasses.html

```
      return constantInstruction("OP_SET_PROPERTY", chunk, offset);
```

---

### 2018. Superclasses — 29 . 3 . 1 Executing super accesses

**Source:** https://craftinginterpreters.com/superclasses.html

```
    
case
 
OP_GET_SUPER
:
      
return
 
constantInstruction
(
"OP_GET_SUPER"
, 
chunk
, 
offset
);
```

---

### 2019. Superclasses — 29 . 3 . 1 Executing super accesses

**Source:** https://craftinginterpreters.com/superclasses.html

```
      
case
 
OP_GET_SUPER
: {
        
ObjString
* 
name
 = 
READ_STRING
();
        
ObjClass
* 
superclass
 = 
AS_CLASS
(
pop
());

        
if
 (!
bindMethod
(
superclass
, 
name
)) {
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
break
;
      }
```

---

### 2020. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  namedVariable(syntheticToken("this"), false);
```

---

### 2021. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
if
 (
match
(
TOKEN_LEFT_PAREN
)) {
    
uint8_t
 
argCount
 = 
argumentList
();
    
namedVariable
(
syntheticToken
(
"super"
), 
false
);
    
emitBytes
(
OP_SUPER_INVOKE
, 
name
);
    
emitByte
(
argCount
);
  } 
else
 {
    
namedVariable
(
syntheticToken
(
"super"
), 
false
);
    
emitBytes
(
OP_GET_SUPER
, 
name
);
  }
```

---

### 2022. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
  
OP_SUPER_INVOKE
,
```

---

### 2023. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
      return invokeInstruction("OP_INVOKE", chunk, offset);
```

---

### 2024. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
    
case
 
OP_SUPER_INVOKE
:
      
return
 
invokeInstruction
(
"OP_SUPER_INVOKE"
, 
chunk
, 
offset
);
```

---

### 2025. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
        break;
      }
```

---

### 2026. Superclasses — 29 . 3 . 2 Faster super calls

**Source:** https://craftinginterpreters.com/superclasses.html

```
      
case
 
OP_SUPER_INVOKE
: {
        
ObjString
* 
method
 = 
READ_STRING
();
        
int
 
argCount
 = 
READ_BYTE
();
        
ObjClass
* 
superclass
 = 
AS_CLASS
(
pop
());
        
if
 (!
invokeFromClass
(
superclass
, 
method
, 
argCount
)) {
          
return
 
INTERPRET_RUNTIME_ERROR
;
        }
        
frame
 = &
vm
.
frames
[
vm
.
frameCount
 - 
1
];
        
break
;
      }
```

---

### 2027. Superclasses — Challenges

**Source:** https://craftinginterpreters.com/superclasses.html

```java
class
 
Doughnut
 {
  
cook
() {
    
print
 
"Fry until golden brown."
;
    
inner
();
    
print
 
"Place in a nice box."
;
  }
}


class
 
BostonCream
 < 
Doughnut
 {
  
cook
() {
    
print
 
"Pipe full of custard and coat with chocolate."
;
  }
}


BostonCream
().
cook
();
```

---

### 2028. Superclasses — Challenges

**Source:** https://craftinginterpreters.com/superclasses.html

```
Fry until golden brown.
Pipe full of custard and coat with chocolate.
Place in a nice box.
```

---

### 2029. Optimization — 30 . 1 Measuring Performance

**Source:** https://craftinginterpreters.com/optimization.html

```
printf
(
"Hello, world!"
);
```

---

### 2030. Optimization — 30 . 2 Faster Hash Table Probing

**Source:** https://craftinginterpreters.com/optimization.html

```java
class
 
Zoo
 {
  
init
() {
    
this
.
aardvark
 = 
1
;
    
this
.
baboon
   = 
1
;
    
this
.
cat
      = 
1
;
    
this
.
donkey
   = 
1
;
    
this
.
elephant
 = 
1
;
    
this
.
fox
      = 
1
;
  }
  
ant
()    { 
return
 
this
.
aardvark
; }
  
banana
() { 
return
 
this
.
baboon
; }
  
tuna
()   { 
return
 
this
.
cat
; }
  
hay
()    { 
return
 
this
.
donkey
; }
  
grass
()  { 
return
 
this
.
elephant
; }
  
mouse
()  { 
return
 
this
.
fox
; }
}


var
 
zoo
 = 
Zoo
();

var
 
sum
 = 
0
;

var
 
start
 = 
clock
();

while
 (
sum
 < 
100000000
) {
  
sum
 = 
sum
 + 
zoo
.
ant
()
            + 
zoo
.
banana
()
            + 
zoo
.
tuna
()
            + 
zoo
.
hay
()
            + 
zoo
.
grass
()
            + 
zoo
.
mouse
();
}


print
 
clock
() - 
start
;

print
 
sum
;
```

---

### 2031. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
static
 
Entry
* 
findEntry
(
Entry
* 
entries
, 
int
 
capacity
,
                        
ObjString
* 
key
) {
  
uint32_t
 
index
 = 
key
->
hash
 % 
capacity
;
  
Entry
* 
tombstone
 = 
NULL
;

  
for
 (;;) {
    
Entry
* 
entry
 = &
entries
[
index
];
    
if
 (
entry
->
key
 == 
NULL
) {
      
if
 (
IS_NIL
(
entry
->
value
)) {
        
// Empty entry.

        
return
 
tombstone
 != 
NULL
 ? 
tombstone
 : 
entry
;
      } 
else
 {
        
// We found a tombstone.

        
if
 (
tombstone
 == 
NULL
) 
tombstone
 = 
entry
;
      }
    } 
else
 
if
 (
entry
->
key
 == 
key
) {
      
// We found the key.

      
return
 
entry
;
    }

    
index
 = (
index
 + 
1
) % 
capacity
;
  }
}
```

---

### 2032. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
  
uint32_t
 
index
 = 
key
->
hash
 % 
capacity
;
```

---

### 2033. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
static Entry* findEntry(Entry* entries, int capacity,
                        ObjString* key) {
```

---

### 2034. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
  
uint32_t
 
index
 = 
key
->
hash
 & (
capacity
 - 
1
);
```

---

### 2035. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
      // We found the key.
      return entry;
    }
```

---

### 2036. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
    
index
 = (
index
 + 
1
) & (
capacity
 - 
1
);
```

---

### 2037. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
  
uint32_t
 
index
 = 
hash
 & (
table
->
capacity
 - 
1
);
```

---

### 2038. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
  for (;;) {
    Entry* entry = &table->entries[index];
```

---

### 2039. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
      return entry->key;
    }
```

---

### 2040. Optimization — 30 . 2 . 1 Slow key wrapping

**Source:** https://craftinginterpreters.com/optimization.html

```
    
index
 = (
index
 + 
1
) & (
table
->
capacity
 - 
1
);
```

---

### 2041. Optimization — 30 . 3 . 2 Conditional support

**Source:** https://craftinginterpreters.com/optimization.html

```
#ifdef NAN_BOXING



typedef
 
uint64_t
 
Value
;


#else
```

---

### 2042. Optimization — 30 . 3 . 2 Conditional support

**Source:** https://craftinginterpreters.com/optimization.html

```
#define OBJ_VAL(object)   ((Value){VAL_OBJ, {.obj = (Obj*)object}})
```

---

### 2043. Optimization — 30 . 3 . 2 Conditional support

**Source:** https://craftinginterpreters.com/optimization.html

```



#endif
```

---

### 2044. Optimization — 30 . 3 . 2 Conditional support

**Source:** https://craftinginterpreters.com/optimization.html

```


typedef struct {
```

---

### 2045. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```



#define NUMBER_VAL(num) numToValue(num)
```

---

### 2046. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```


#else
```

---

### 2047. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```



static
 
inline
 
Value
 
numToValue
(
double
 
num
) {
  
Value
 
value
;
  
memcpy
(&
value
, &
num
, 
sizeof
(
double
));
  
return
 
value
;
}
```

---

### 2048. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```


#else
```

---

### 2049. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```



#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2050. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```


#define NUMBER_VAL(num) numToValue(num)
```

---

### 2051. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```



static
 
inline
 
double
 
valueToNum
(
Value
 
value
) {
  
double
 
num
;
  
memcpy
(&
num
, &
value
, 
sizeof
(
Value
));
  
return
 
num
;
}
```

---

### 2052. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```


static inline Value numToValue(double num) {
```

---

### 2053. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```
double
 
valueToNum
(
Value
 
value
) {
  
union
 {
    
uint64_t
 
bits
;
    
double
 
num
;
  } 
data
;
  
data
.
bits
 = 
value
;
  
return
 
data
.
num
;
}
```

---

### 2054. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```c



#include <string.h>
```

---

### 2055. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```c


#include "common.h"
```

---

### 2056. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```



#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

---

### 2057. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```


#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2058. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```



#define QNAN     ((uint64_t)0x7ffc000000000000)
```

---

### 2059. Optimization — 30 . 3 . 3 Numbers

**Source:** https://craftinginterpreters.com/optimization.html

```


typedef uint64_t Value;
```

---

### 2060. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define QNAN     ((uint64_t)0x7ffc000000000000)
```

---

### 2061. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```



#define TAG_NIL   1 
// 01.


#define TAG_FALSE 2 
// 10.


#define TAG_TRUE  3 
// 11.
```

---

### 2062. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```


typedef uint64_t Value;
```

---

### 2063. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2064. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define NIL_VAL         ((Value)(uint64_t)(QNAN | TAG_NIL))
```

---

### 2065. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_NIL(value)       ((value) == NIL_VAL)
```

---

### 2066. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

---

### 2067. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2068. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define FALSE_VAL       ((Value)(uint64_t)(QNAN | TAG_FALSE))


#define TRUE_VAL        ((Value)(uint64_t)(QNAN | TAG_TRUE))
```

---

### 2069. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define NIL_VAL         ((Value)(uint64_t)(QNAN | TAG_NIL))
```

---

### 2070. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2071. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define BOOL_VAL(b)     ((b) ? TRUE_VAL : FALSE_VAL)
```

---

### 2072. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define FALSE_VAL       ((Value)(uint64_t)(QNAN | TAG_FALSE))
```

---

### 2073. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

---

### 2074. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_BOOL(value)      ((value) == TRUE_VAL)
```

---

### 2075. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2076. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_BOOL(value)      (((value) | 1) == TRUE_VAL)
```

---

### 2077. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_NIL(value)       ((value) == NIL_VAL)
```

---

### 2078. Optimization — 30 . 3 . 4 Nil, true, and false

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_BOOL(v) ((v) == TRUE_VAL || (v) == FALSE_VAL)
```

---

### 2079. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define OBJ_VAL(obj) \


    (Value)(SIGN_BIT | QNAN | (uint64_t)(uintptr_t)(obj))
```

---

### 2080. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```


static inline double valueToNum(Value value) {
```

---

### 2081. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define SIGN_BIT ((uint64_t)0x8000000000000000)
```

---

### 2082. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define QNAN     ((uint64_t)0x7ffc000000000000)
```

---

### 2083. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_NUMBER(value)    valueToNum(value)
```

---

### 2084. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define AS_OBJ(value) \


    ((Obj*)(uintptr_t)((value) & ~(SIGN_BIT | QNAN)))
```

---

### 2085. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```


#define BOOL_VAL(b)     ((b) ? TRUE_VAL : FALSE_VAL)
```

---

### 2086. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

---

### 2087. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```
#define IS_OBJ(value) \


    (((value) & (QNAN | SIGN_BIT)) == (QNAN | SIGN_BIT))
```

---

### 2088. Optimization — 30 . 3 . 5 Objects

**Source:** https://craftinginterpreters.com/optimization.html

```


#define AS_BOOL(value)      ((value) == TRUE_VAL)
```

---

### 2089. Optimization — 30 . 3 . 6 Value functions

**Source:** https://craftinginterpreters.com/optimization.html

```
#ifdef NAN_BOXING

  
if
 (
IS_BOOL
(
value
)) {
    
printf
(
AS_BOOL
(
value
) ? 
"true"
 : 
"false"
);
  } 
else
 
if
 (
IS_NIL
(
value
)) {
    
printf
(
"nil"
);
  } 
else
 
if
 (
IS_NUMBER
(
value
)) {
    
printf
(
"%g"
, 
AS_NUMBER
(
value
));
  } 
else
 
if
 (
IS_OBJ
(
value
)) {
    
printObject
(
value
);
  }

#else
```

---

### 2090. Optimization — 30 . 3 . 6 Value functions

**Source:** https://craftinginterpreters.com/optimization.html

```
#ifdef NAN_BOXING

  
return
 
a
 == 
b
;

#else
```

---

### 2091. Optimization — 30 . 3 . 6 Value functions

**Source:** https://craftinginterpreters.com/optimization.html

```
var
 
nan
 = 
0
/
0
;

print
 
nan
 == 
nan
;
```

---

### 2092. Optimization — 30 . 3 . 6 Value functions

**Source:** https://craftinginterpreters.com/optimization.html

```
  
if
 (
IS_NUMBER
(
a
) && 
IS_NUMBER
(
b
)) {
    
return
 
AS_NUMBER
(
a
) == 
AS_NUMBER
(
b
);
  }
```

---

### 2093. Appendix I — A1 . 1 Syntax Grammar

**Source:** https://craftinginterpreters.com/appendix-i.html

```
program
        â 
declaration
* 
EOF
 ;
```

---

### 2094. Appendix I — A1 . 1 . 1 Declarations

**Source:** https://craftinginterpreters.com/appendix-i.html

```
declaration
    â 
classDecl

               | 
funDecl

               | 
varDecl

               | 
statement
 ;


classDecl
      â 
"class"
 
IDENTIFIER
 ( 
"<"
 
IDENTIFIER
 )?
                 
"{"
 
function
* 
"}"
 ;

funDecl
        â 
"fun"
 
function
 ;

varDecl
        â 
"var"
 
IDENTIFIER
 ( 
"="
 
expression
 )? 
";"
 ;
```

---

### 2095. Appendix I — A1 . 1 . 2 Statements

**Source:** https://craftinginterpreters.com/appendix-i.html

```
statement
      â 
exprStmt

               | 
forStmt

               | 
ifStmt

               | 
printStmt

               | 
returnStmt

               | 
whileStmt

               | 
block
 ;


exprStmt
       â 
expression
 
";"
 ;

forStmt
        â 
"for"
 
"("
 ( 
varDecl
 | 
exprStmt
 | 
";"
 )
                           
expression
? 
";"

                           
expression
? 
")"
 
statement
 ;

ifStmt
         â 
"if"
 
"("
 
expression
 
")"
 
statement

                 ( 
"else"
 
statement
 )? ;

printStmt
      â 
"print"
 
expression
 
";"
 ;

returnStmt
     â 
"return"
 
expression
? 
";"
 ;

whileStmt
      â 
"while"
 
"("
 
expression
 
")"
 
statement
 ;

block
          â 
"{"
 
declaration
* 
"}"
 ;
```

---

### 2096. Appendix I — A1 . 1 . 3 Expressions

**Source:** https://craftinginterpreters.com/appendix-i.html

```
expression
     â 
assignment
 ;


assignment
     â ( 
call
 
"."
 )? 
IDENTIFIER
 
"="
 
assignment

               | 
logic_or
 ;


logic_or
       â 
logic_and
 ( 
"or"
 
logic_and
 )* ;

logic_and
      â 
equality
 ( 
"and"
 
equality
 )* ;

equality
       â 
comparison
 ( ( 
"!="
 | 
"=="
 ) 
comparison
 )* ;

comparison
     â 
term
 ( ( 
">"
 | 
">="
 | 
"<"
 | 
"<="
 ) 
term
 )* ;

term
           â 
factor
 ( ( 
"-"
 | 
"+"
 ) 
factor
 )* ;

factor
         â 
unary
 ( ( 
"/"
 | 
"*"
 ) 
unary
 )* ;


unary
          â ( 
"!"
 | 
"-"
 ) 
unary
 | 
call
 ;

call
           â 
primary
 ( 
"("
 
arguments
? 
")"
 | 
"."
 
IDENTIFIER
 )* ;

primary
        â 
"true"
 | 
"false"
 | 
"nil"
 | 
"this"

               | 
NUMBER
 | 
STRING
 | 
IDENTIFIER
 | 
"("
 
expression
 
")"

               | 
"super"
 
"."
 
IDENTIFIER
 ;
```

---

### 2097. Appendix I — A1 . 1 . 4 Utility rules

**Source:** https://craftinginterpreters.com/appendix-i.html

```
function
       â 
IDENTIFIER
 
"("
 
parameters
? 
")"
 
block
 ;

parameters
     â 
IDENTIFIER
 ( 
","
 
IDENTIFIER
 )* ;

arguments
      â 
expression
 ( 
","
 
expression
 )* ;
```

---

### 2098. Appendix I — A1 . 2 Lexical Grammar

**Source:** https://craftinginterpreters.com/appendix-i.html

```
NUMBER
         â 
DIGIT
+ ( 
"."
 
DIGIT
+ )? ;

STRING
         â 
"
\"
"
 <
any
 
char
 
except
 
"
\"
"
>* 
"
\"
"
 ;

IDENTIFIER
     â 
ALPHA
 ( 
ALPHA
 | 
DIGIT
 )* ;

ALPHA
          â 
"a"
 ... 
"z"
 | 
"A"
 ... 
"Z"
 | 
"_"
 ;

DIGIT
          â 
"0"
 ... 
"9"
 ;
```

---

### 2099. Appendix II — A2 . 1 Expressions

**Source:** https://craftinginterpreters.com/appendix-ii.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.List
;


abstract
 
class
 
Expr
 {
  
interface
 
Visitor
<
R
> {
    
R
 
visitAssignExpr
(
Assign
 
expr
);
    
R
 
visitBinaryExpr
(
Binary
 
expr
);
    
R
 
visitCallExpr
(
Call
 
expr
);
    
R
 
visitGetExpr
(
Get
 
expr
);
    
R
 
visitGroupingExpr
(
Grouping
 
expr
);
    
R
 
visitLiteralExpr
(
Literal
 
expr
);
    
R
 
visitLogicalExpr
(
Logical
 
expr
);
    
R
 
visitSetExpr
(
Set
 
expr
);
    
R
 
visitSuperExpr
(
Super
 
expr
);
    
R
 
visitThisExpr
(
This
 
expr
);
    
R
 
visitUnaryExpr
(
Unary
 
expr
);
    
R
 
visitVariableExpr
(
Variable
 
expr
);
  }

  
// Nested Expr classes here...


  
abstract
 <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
);
}
```

---

### 2100. Appendix II — A2 . 1 . 1 Assign expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Assign
 
extends
 
Expr
 {
    
Assign
(
Token
 
name
, 
Expr
 
value
) {
      
this
.
name
 = 
name
;
      
this
.
value
 = 
value
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitAssignExpr
(
this
);
    }

    
final
 
Token
 
name
;
    
final
 
Expr
 
value
;
  }
```

---

### 2101. Appendix II — A2 . 1 . 2 Binary expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Binary
 
extends
 
Expr
 {
    
Binary
(
Expr
 
left
, 
Token
 
operator
, 
Expr
 
right
) {
      
this
.
left
 = 
left
;
      
this
.
operator
 = 
operator
;
      
this
.
right
 = 
right
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitBinaryExpr
(
this
);
    }

    
final
 
Expr
 
left
;
    
final
 
Token
 
operator
;
    
final
 
Expr
 
right
;
  }
```

---

### 2102. Appendix II — A2 . 1 . 3 Call expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Call
 
extends
 
Expr
 {
    
Call
(
Expr
 
callee
, 
Token
 
paren
, 
List
<
Expr
> 
arguments
) {
      
this
.
callee
 = 
callee
;
      
this
.
paren
 = 
paren
;
      
this
.
arguments
 = 
arguments
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitCallExpr
(
this
);
    }

    
final
 
Expr
 
callee
;
    
final
 
Token
 
paren
;
    
final
 
List
<
Expr
> 
arguments
;
  }
```

---

### 2103. Appendix II — A2 . 1 . 4 Get expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Get
 
extends
 
Expr
 {
    
Get
(
Expr
 
object
, 
Token
 
name
) {
      
this
.
object
 = 
object
;
      
this
.
name
 = 
name
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitGetExpr
(
this
);
    }

    
final
 
Expr
 
object
;
    
final
 
Token
 
name
;
  }
```

---

### 2104. Appendix II — A2 . 1 . 5 Grouping expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Grouping
 
extends
 
Expr
 {
    
Grouping
(
Expr
 
expression
) {
      
this
.
expression
 = 
expression
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitGroupingExpr
(
this
);
    }

    
final
 
Expr
 
expression
;
  }
```

---

### 2105. Appendix II — A2 . 1 . 6 Literal expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Literal
 
extends
 
Expr
 {
    
Literal
(
Object
 
value
) {
      
this
.
value
 = 
value
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitLiteralExpr
(
this
);
    }

    
final
 
Object
 
value
;
  }
```

---

### 2106. Appendix II — A2 . 1 . 7 Logical expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Logical
 
extends
 
Expr
 {
    
Logical
(
Expr
 
left
, 
Token
 
operator
, 
Expr
 
right
) {
      
this
.
left
 = 
left
;
      
this
.
operator
 = 
operator
;
      
this
.
right
 = 
right
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitLogicalExpr
(
this
);
    }

    
final
 
Expr
 
left
;
    
final
 
Token
 
operator
;
    
final
 
Expr
 
right
;
  }
```

---

### 2107. Appendix II — A2 . 1 . 8 Set expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Set
 
extends
 
Expr
 {
    
Set
(
Expr
 
object
, 
Token
 
name
, 
Expr
 
value
) {
      
this
.
object
 = 
object
;
      
this
.
name
 = 
name
;
      
this
.
value
 = 
value
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitSetExpr
(
this
);
    }

    
final
 
Expr
 
object
;
    
final
 
Token
 
name
;
    
final
 
Expr
 
value
;
  }
```

---

### 2108. Appendix II — A2 . 1 . 9 Super expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Super
 
extends
 
Expr
 {
    
Super
(
Token
 
keyword
, 
Token
 
method
) {
      
this
.
keyword
 = 
keyword
;
      
this
.
method
 = 
method
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitSuperExpr
(
this
);
    }

    
final
 
Token
 
keyword
;
    
final
 
Token
 
method
;
  }
```

---

### 2109. Appendix II — A2 . 1 . 10 This expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
This
 
extends
 
Expr
 {
    
This
(
Token
 
keyword
) {
      
this
.
keyword
 = 
keyword
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitThisExpr
(
this
);
    }

    
final
 
Token
 
keyword
;
  }
```

---

### 2110. Appendix II — A2 . 1 . 11 Unary expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Unary
 
extends
 
Expr
 {
    
Unary
(
Token
 
operator
, 
Expr
 
right
) {
      
this
.
operator
 = 
operator
;
      
this
.
right
 = 
right
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitUnaryExpr
(
this
);
    }

    
final
 
Token
 
operator
;
    
final
 
Expr
 
right
;
  }
```

---

### 2111. Appendix II — A2 . 1 . 12 Variable expression

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Variable
 
extends
 
Expr
 {
    
Variable
(
Token
 
name
) {
      
this
.
name
 = 
name
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitVariableExpr
(
this
);
    }

    
final
 
Token
 
name
;
  }
```

---

### 2112. Appendix II — A2 . 2 Statements

**Source:** https://craftinginterpreters.com/appendix-ii.html

```java
package
 
com.craftinginterpreters.lox
;


import
 
java.util.List
;


abstract
 
class
 
Stmt
 {
  
interface
 
Visitor
<
R
> {
    
R
 
visitBlockStmt
(
Block
 
stmt
);
    
R
 
visitClassStmt
(
Class
 
stmt
);
    
R
 
visitExpressionStmt
(
Expression
 
stmt
);
    
R
 
visitFunctionStmt
(
Function
 
stmt
);
    
R
 
visitIfStmt
(
If
 
stmt
);
    
R
 
visitPrintStmt
(
Print
 
stmt
);
    
R
 
visitReturnStmt
(
Return
 
stmt
);
    
R
 
visitVarStmt
(
Var
 
stmt
);
    
R
 
visitWhileStmt
(
While
 
stmt
);
  }

  
// Nested Stmt classes here...


  
abstract
 <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
);
}
```

---

### 2113. Appendix II — A2 . 2 . 1 Block statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Block
 
extends
 
Stmt
 {
    
Block
(
List
<
Stmt
> 
statements
) {
      
this
.
statements
 = 
statements
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitBlockStmt
(
this
);
    }

    
final
 
List
<
Stmt
> 
statements
;
  }
```

---

### 2114. Appendix II — A2 . 2 . 2 Class statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Class
 
extends
 
Stmt
 {
    
Class
(
Token
 
name
,
          
Expr
.
Variable
 
superclass
,
          
List
<
Stmt
.
Function
> 
methods
) {
      
this
.
name
 = 
name
;
      
this
.
superclass
 = 
superclass
;
      
this
.
methods
 = 
methods
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitClassStmt
(
this
);
    }

    
final
 
Token
 
name
;
    
final
 
Expr
.
Variable
 
superclass
;
    
final
 
List
<
Stmt
.
Function
> 
methods
;
  }
```

---

### 2115. Appendix II — A2 . 2 . 3 Expression statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Expression
 
extends
 
Stmt
 {
    
Expression
(
Expr
 
expression
) {
      
this
.
expression
 = 
expression
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitExpressionStmt
(
this
);
    }

    
final
 
Expr
 
expression
;
  }
```

---

### 2116. Appendix II — A2 . 2 . 4 Function statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Function
 
extends
 
Stmt
 {
    
Function
(
Token
 
name
, 
List
<
Token
> 
params
, 
List
<
Stmt
> 
body
) {
      
this
.
name
 = 
name
;
      
this
.
params
 = 
params
;
      
this
.
body
 = 
body
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitFunctionStmt
(
this
);
    }

    
final
 
Token
 
name
;
    
final
 
List
<
Token
> 
params
;
    
final
 
List
<
Stmt
> 
body
;
  }
```

---

### 2117. Appendix II — A2 . 2 . 5 If statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
If
 
extends
 
Stmt
 {
    
If
(
Expr
 
condition
, 
Stmt
 
thenBranch
, 
Stmt
 
elseBranch
) {
      
this
.
condition
 = 
condition
;
      
this
.
thenBranch
 = 
thenBranch
;
      
this
.
elseBranch
 = 
elseBranch
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitIfStmt
(
this
);
    }

    
final
 
Expr
 
condition
;
    
final
 
Stmt
 
thenBranch
;
    
final
 
Stmt
 
elseBranch
;
  }
```

---

### 2118. Appendix II — A2 . 2 . 6 Print statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Print
 
extends
 
Stmt
 {
    
Print
(
Expr
 
expression
) {
      
this
.
expression
 = 
expression
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitPrintStmt
(
this
);
    }

    
final
 
Expr
 
expression
;
  }
```

---

### 2119. Appendix II — A2 . 2 . 7 Return statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Return
 
extends
 
Stmt
 {
    
Return
(
Token
 
keyword
, 
Expr
 
value
) {
      
this
.
keyword
 = 
keyword
;
      
this
.
value
 = 
value
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitReturnStmt
(
this
);
    }

    
final
 
Token
 
keyword
;
    
final
 
Expr
 
value
;
  }
```

---

### 2120. Appendix II — A2 . 2 . 8 Variable statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
Var
 
extends
 
Stmt
 {
    
Var
(
Token
 
name
, 
Expr
 
initializer
) {
      
this
.
name
 = 
name
;
      
this
.
initializer
 = 
initializer
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitVarStmt
(
this
);
    }

    
final
 
Token
 
name
;
    
final
 
Expr
 
initializer
;
  }
```

---

### 2121. Appendix II — A2 . 2 . 9 While statement

**Source:** https://craftinginterpreters.com/appendix-ii.html

```
  
static
 
class
 
While
 
extends
 
Stmt
 {
    
While
(
Expr
 
condition
, 
Stmt
 
body
) {
      
this
.
condition
 = 
condition
;
      
this
.
body
 = 
body
;
    }

    
@Override

    <
R
> 
R
 
accept
(
Visitor
<
R
> 
visitor
) {
      
return
 
visitor
.
visitWhileStmt
(
this
);
    }

    
final
 
Expr
 
condition
;
    
final
 
Stmt
 
body
;
  }
```

