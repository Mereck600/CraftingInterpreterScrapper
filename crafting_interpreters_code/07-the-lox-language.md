# The Lox Language
_From: https://craftinginterpreters.com/the-lox-language.html_

#### 1. 3 . 1 Hello, Lox — [source](https://craftinginterpreters.com/the-lox-language.html)
```
// Your first Lox program!
print "Hello, world!";
```

#### 2. 3 . 3 Data Types — [source](https://craftinginterpreters.com/the-lox-language.html)
```
true;  // Not false.
false; // Not *not* false.
```

#### 3. 3 . 3 Data Types — [source](https://craftinginterpreters.com/the-lox-language.html)
```
1234;  // An integer.
12.34; // A decimal number.
```

#### 4. 3 . 3 Data Types — [source](https://craftinginterpreters.com/the-lox-language.html)
```
"I am a string";
"";    // The empty string.
"123"; // This is a string, not a number.
```

#### 5. 3 . 4 . 1 Arithmetic — [source](https://craftinginterpreters.com/the-lox-language.html)
```
add + me;
subtract - me;
multiply * me;
divide / me;
```

#### 6. 3 . 4 . 1 Arithmetic — [source](https://craftinginterpreters.com/the-lox-language.html)
```
condition ? thenArm : elseArm;
```

#### 7. 3 . 4 . 1 Arithmetic — [source](https://craftinginterpreters.com/the-lox-language.html)
```
-negateMe;
```

#### 8. 3 . 4 . 2 Comparison and equality — [source](https://craftinginterpreters.com/the-lox-language.html)
```
less < than;
lessThan <= orEqual;
greater > than;
greaterThan >= orEqual;
```

#### 9. 3 . 4 . 2 Comparison and equality — [source](https://craftinginterpreters.com/the-lox-language.html)
```
1 == 2;         // false.
"cat" != "dog"; // true.
```

#### 10. 3 . 4 . 2 Comparison and equality — [source](https://craftinginterpreters.com/the-lox-language.html)
```
314 == "pi"; // false.
```

#### 11. 3 . 4 . 2 Comparison and equality — [source](https://craftinginterpreters.com/the-lox-language.html)
```
123 == "123"; // false.
```

#### 12. 3 . 4 . 3 Logical operators — [source](https://craftinginterpreters.com/the-lox-language.html)
```
!true;  // false.
!false; // true.
```

#### 13. 3 . 4 . 3 Logical operators — [source](https://craftinginterpreters.com/the-lox-language.html)
```
true and false; // false.
true and true;  // true.
```

#### 14. 3 . 4 . 3 Logical operators — [source](https://craftinginterpreters.com/the-lox-language.html)
```
false or false; // false.
true or false;  // true.
```

#### 15. 3 . 4 . 4 Precedence and grouping — [source](https://craftinginterpreters.com/the-lox-language.html)
```
var average = (min + max) / 2;
```

#### 16. 3 . 5 Statements — [source](https://craftinginterpreters.com/the-lox-language.html)
```
print "Hello, world!";
```

#### 17. 3 . 5 Statements — [source](https://craftinginterpreters.com/the-lox-language.html)
```
"some expression";
```

#### 18. 3 . 5 Statements — [source](https://craftinginterpreters.com/the-lox-language.html)
```
{
  print "One statement.";
  print "Two statements.";
}
```

#### 19. 3 . 6 Variables — [source](https://craftinginterpreters.com/the-lox-language.html)
```
var imAVariable = "here is my value";
var iAmNil;
```

#### 20. 3 . 6 Variables — [source](https://craftinginterpreters.com/the-lox-language.html)
```
var breakfast = "bagels";
print breakfast; // "bagels".
breakfast = "beignets";
print breakfast; // "beignets".
```

#### 21. 3 . 7 Control Flow — [source](https://craftinginterpreters.com/the-lox-language.html)
```
if (condition) {
  print "yes";
} else {
  print "no";
}
```

#### 22. 3 . 7 Control Flow — [source](https://craftinginterpreters.com/the-lox-language.html)
```
var a = 1;
while (a < 10) {
  print a;
  a = a + 1;
}
```

#### 23. 3 . 7 Control Flow — [source](https://craftinginterpreters.com/the-lox-language.html)
```
for (var a = 1; a < 10; a = a + 1) {
  print a;
}
```

#### 24. 3 . 8 Functions — [source](https://craftinginterpreters.com/the-lox-language.html)
```
makeBreakfast(bacon, eggs, toast);
```

#### 25. 3 . 8 Functions — [source](https://craftinginterpreters.com/the-lox-language.html)
```
makeBreakfast();
```

#### 26. 3 . 8 Functions — [source](https://craftinginterpreters.com/the-lox-language.html)
```
fun printSum(a, b) {
  print a + b;
}
```

#### 27. 3 . 8 Functions — [source](https://craftinginterpreters.com/the-lox-language.html)
```
fun returnSum(a, b) {
  return a + b;
}
```

#### 28. 3 . 8 . 1 Closures — [source](https://craftinginterpreters.com/the-lox-language.html)
```
fun addPair(a, b) {
  return a + b;
}

fun identity(a) {
  return a;
}

print identity(addPair)(1, 2); // Prints "3".
```

#### 29. 3 . 8 . 1 Closures — [source](https://craftinginterpreters.com/the-lox-language.html)
```
fun outerFunction() {
  fun localFunction() {
    print "I'm local!";
  }

  localFunction();
}
```

#### 30. 3 . 8 . 1 Closures — [source](https://craftinginterpreters.com/the-lox-language.html)
```
fun returnFunction() {
  var outside = "outside";

  fun inner() {
    print outside;
  }

  return inner;
}

var fn = returnFunction();
fn();
```

#### 31. 3 . 9 . 4 Classes in Lox — [source](https://craftinginterpreters.com/the-lox-language.html)
```java
class Breakfast {
  cook() {
    print "Eggs a-fryin'!";
  }

  serve(who) {
    print "Enjoy your breakfast, " + who + ".";
  }
}
```

#### 32. 3 . 9 . 4 Classes in Lox — [source](https://craftinginterpreters.com/the-lox-language.html)
```
// Store it in variables.
var someVariable = Breakfast;

// Pass it to functions.
someFunction(Breakfast);
```

#### 33. 3 . 9 . 4 Classes in Lox — [source](https://craftinginterpreters.com/the-lox-language.html)
```
var breakfast = Breakfast();
print breakfast; // "Breakfast instance".
```

#### 34. 3 . 9 . 5 Instantiation and initialization — [source](https://craftinginterpreters.com/the-lox-language.html)
```
breakfast.meat = "sausage";
breakfast.bread = "sourdough";
```

#### 35. 3 . 9 . 5 Instantiation and initialization — [source](https://craftinginterpreters.com/the-lox-language.html)
```java
class Breakfast {
  serve(who) {
    print "Enjoy your " + this.meat + " and " +
        this.bread + ", " + who + ".";
  }

  // ...
}
```

#### 36. 3 . 9 . 5 Instantiation and initialization — [source](https://craftinginterpreters.com/the-lox-language.html)
```java
class Breakfast {
  init(meat, bread) {
    this.meat = meat;
    this.bread = bread;
  }

  // ...
}

var baconAndToast = Breakfast("bacon", "toast");
baconAndToast.serve("Dear Reader");
// "Enjoy your bacon and toast, Dear Reader."
```

#### 37. 3 . 9 . 6 Inheritance — [source](https://craftinginterpreters.com/the-lox-language.html)
```
class Brunch < Breakfast {
  drink() {
    print "How about a Bloody Mary?";
  }
}
```

#### 38. 3 . 9 . 6 Inheritance — [source](https://craftinginterpreters.com/the-lox-language.html)
```
var benedict = Brunch("ham", "English muffin");
benedict.serve("Noble Reader");
```

#### 39. 3 . 9 . 6 Inheritance — [source](https://craftinginterpreters.com/the-lox-language.html)
```
class Brunch < Breakfast {
  init(meat, bread, drink) {
    super.init(meat, bread);
    this.drink = drink;
  }
}
```

#### 40. Design Note: Expressions and Statements — [source](https://craftinginterpreters.com/the-lox-language.html)
```
puts 1 + if true then 2 else 3 end + 4
```

