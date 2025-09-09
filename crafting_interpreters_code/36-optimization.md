# Optimization
_From: https://craftinginterpreters.com/optimization.html_

#### 1. 30 . 1 Measuring Performance — [source](https://craftinginterpreters.com/optimization.html)
```
printf("Hello, world!");
```

#### 2. 30 . 2 Faster Hash Table Probing — [source](https://craftinginterpreters.com/optimization.html)
```java
class Zoo {
  init() {
    this.aardvark = 1;
    this.baboon   = 1;
    this.cat      = 1;
    this.donkey   = 1;
    this.elephant = 1;
    this.fox      = 1;
  }
  ant()    { return this.aardvark; }
  banana() { return this.baboon; }
  tuna()   { return this.cat; }
  hay()    { return this.donkey; }
  grass()  { return this.elephant; }
  mouse()  { return this.fox; }
}

var zoo = Zoo();
var sum = 0;
var start = clock();
while (sum < 100000000) {
  sum = sum + zoo.ant()
            + zoo.banana()
            + zoo.tuna()
            + zoo.hay()
            + zoo.grass()
            + zoo.mouse();
}

print clock() - start;
print sum;
```

#### 3. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
static Entry* findEntry(Entry* entries, int capacity,
                        ObjString* key) {
  uint32_t index = key->hash % capacity;
  Entry* tombstone = NULL;

  for (;;) {
    Entry* entry = &entries[index];
    if (entry->key == NULL) {
      if (IS_NIL(entry->value)) {
        // Empty entry.
        return tombstone != NULL ? tombstone : entry;
      } else {
        // We found a tombstone.
        if (tombstone == NULL) tombstone = entry;
      }
    } else if (entry->key == key) {
      // We found the key.
      return entry;
    }

    index = (index + 1) % capacity;
  }
}
```

#### 4. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  uint32_t index = key->hash % capacity;
```

#### 5. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
static Entry* findEntry(Entry* entries, int capacity,
                        ObjString* key) {
```

#### 6. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  uint32_t index = key->hash & (capacity - 1);
```

#### 7. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  Entry* tombstone = NULL;
```

#### 8. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
      // We found the key.
      return entry;
    }

```

#### 9. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
    index = (index + 1) & (capacity - 1);
```

#### 10. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  }
```

#### 11. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  if (table->count == 0) return NULL;

```

#### 12. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  uint32_t index = hash & (table->capacity - 1);
```

#### 13. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  for (;;) {
    Entry* entry = &table->entries[index];
```

#### 14. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
      return entry->key;
    }

```

#### 15. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
    index = (index + 1) & (table->capacity - 1);
```

#### 16. 30 . 2 . 1 Slow key wrapping — [source](https://craftinginterpreters.com/optimization.html)
```
  }
```

#### 17. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```c
#include <stdint.h>

```

#### 18. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```
#define NAN_BOXING
```

#### 19. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```
#define DEBUG_PRINT_CODE
```

#### 20. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```
typedef struct ObjString ObjString;

```

#### 21. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```
#ifdef NAN_BOXING

typedef uint64_t Value;

#else

```

#### 22. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```
typedef enum {
```

#### 23. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```
#define OBJ_VAL(object)   ((Value){VAL_OBJ, {.obj = (Obj*)object}})
```

#### 24. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```


#endif
```

#### 25. 30 . 3 . 2 Conditional support — [source](https://craftinginterpreters.com/optimization.html)
```


typedef struct {
```

#### 26. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
typedef uint64_t Value;
```

#### 27. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#define NUMBER_VAL(num) numToValue(num)
```

#### 28. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#else
```

#### 29. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
#define NUMBER_VAL(num) numToValue(num)
```

#### 30. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


static inline Value numToValue(double num) {
  Value value;
  memcpy(&value, &num, sizeof(double));
  return value;
}
```

#### 31. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#else
```

#### 32. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
typedef uint64_t Value;
```

#### 33. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#define AS_NUMBER(value)    valueToNum(value)
```

#### 34. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#define NUMBER_VAL(num) numToValue(num)
```

#### 35. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
#define NUMBER_VAL(num) numToValue(num)
```

#### 36. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


static inline double valueToNum(Value value) {
  double num;
  memcpy(&num, &value, sizeof(Value));
  return num;
}
```

#### 37. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


static inline Value numToValue(double num) {
```

#### 38. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
double valueToNum(Value value) {
  union {
    uint64_t bits;
    double num;
  } data;
  data.bits = value;
  return data.num;
}
```

#### 39. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
#define clox_value_h
```

#### 40. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```c


#include <string.h>
```

#### 41. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```c


#include "common.h"
```

#### 42. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
typedef uint64_t Value;
```

#### 43. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

#### 44. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#define AS_NUMBER(value)    valueToNum(value)
```

#### 45. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```
#ifdef NAN_BOXING
```

#### 46. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


#define QNAN     ((uint64_t)0x7ffc000000000000)
```

#### 47. 30 . 3 . 3 Numbers — [source](https://craftinginterpreters.com/optimization.html)
```


typedef uint64_t Value;
```

#### 48. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define QNAN     ((uint64_t)0x7ffc000000000000)
```

#### 49. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```


#define TAG_NIL   1 // 01.
#define TAG_FALSE 2 // 10.
#define TAG_TRUE  3 // 11.
```

#### 50. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```


typedef uint64_t Value;
```

#### 51. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_NUMBER(value)    valueToNum(value)

```

#### 52. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define NIL_VAL         ((Value)(uint64_t)(QNAN | TAG_NIL))
```

#### 53. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define NUMBER_VAL(num) numToValue(num)
```

#### 54. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
typedef uint64_t Value;

```

#### 55. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_NIL(value)       ((value) == NIL_VAL)
```

#### 56. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

#### 57. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_NUMBER(value)    valueToNum(value)

```

#### 58. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define FALSE_VAL       ((Value)(uint64_t)(QNAN | TAG_FALSE))
#define TRUE_VAL        ((Value)(uint64_t)(QNAN | TAG_TRUE))
```

#### 59. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define NIL_VAL         ((Value)(uint64_t)(QNAN | TAG_NIL))
```

#### 60. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_NUMBER(value)    valueToNum(value)

```

#### 61. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define BOOL_VAL(b)     ((b) ? TRUE_VAL : FALSE_VAL)
```

#### 62. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define FALSE_VAL       ((Value)(uint64_t)(QNAN | TAG_FALSE))
```

#### 63. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)

```

#### 64. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_BOOL(value)      ((value) == TRUE_VAL)
```

#### 65. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_NUMBER(value)    valueToNum(value)
```

#### 66. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
typedef uint64_t Value;

```

#### 67. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_BOOL(value)      (((value) | 1) == TRUE_VAL)
```

#### 68. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_NIL(value)       ((value) == NIL_VAL)
```

#### 69. 30 . 3 . 4 Nil, true, and false — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_BOOL(v) ((v) == TRUE_VAL || (v) == FALSE_VAL)
```

#### 70. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define NUMBER_VAL(num) numToValue(num)
```

#### 71. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define OBJ_VAL(obj) \
    (Value)(SIGN_BIT | QNAN | (uint64_t)(uintptr_t)(obj))
```

#### 72. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```


static inline double valueToNum(Value value) {
```

#### 73. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#ifdef NAN_BOXING

```

#### 74. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define SIGN_BIT ((uint64_t)0x8000000000000000)
```

#### 75. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define QNAN     ((uint64_t)0x7ffc000000000000)

```

#### 76. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_NUMBER(value)    valueToNum(value)
```

#### 77. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define AS_OBJ(value) \
    ((Obj*)(uintptr_t)((value) & ~(SIGN_BIT | QNAN)))
```

#### 78. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```


#define BOOL_VAL(b)     ((b) ? TRUE_VAL : FALSE_VAL)
```

#### 79. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_NUMBER(value)    (((value) & QNAN) != QNAN)
```

#### 80. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```
#define IS_OBJ(value) \
    (((value) & (QNAN | SIGN_BIT)) == (QNAN | SIGN_BIT))
```

#### 81. 30 . 3 . 5 Objects — [source](https://craftinginterpreters.com/optimization.html)
```


#define AS_BOOL(value)      ((value) == TRUE_VAL)
```

#### 82. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
void printValue(Value value) {
```

#### 83. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
#ifdef NAN_BOXING
  if (IS_BOOL(value)) {
    printf(AS_BOOL(value) ? "true" : "false");
  } else if (IS_NIL(value)) {
    printf("nil");
  } else if (IS_NUMBER(value)) {
    printf("%g", AS_NUMBER(value));
  } else if (IS_OBJ(value)) {
    printObject(value);
  }
#else
```

#### 84. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
  switch (value.type) {
```

#### 85. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
  }
```

#### 86. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
#endif
```

#### 87. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
}
```

#### 88. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
bool valuesEqual(Value a, Value b) {
```

#### 89. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
#ifdef NAN_BOXING
  return a == b;
#else
```

#### 90. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
  if (a.type != b.type) return false;
```

#### 91. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
var nan = 0/0;
print nan == nan;
```

#### 92. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
#ifdef NAN_BOXING
```

#### 93. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
  if (IS_NUMBER(a) && IS_NUMBER(b)) {
    return AS_NUMBER(a) == AS_NUMBER(b);
  }
```

#### 94. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
  return a == b;
```

#### 95. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
  }
```

#### 96. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
#endif
```

#### 97. 30 . 3 . 6 Value functions — [source](https://craftinginterpreters.com/optimization.html)
```
}
```

