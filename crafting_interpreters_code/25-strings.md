# Strings
_From: https://craftinginterpreters.com/strings.html_

#### 1. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
  VAL_NUMBER,
```

#### 2. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
  VAL_OBJ
```

#### 3. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
} ValueType;
```

#### 4. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
    double number;
```

#### 5. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
    Obj* obj;
```

#### 6. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
  } as; 
```

#### 7. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define IS_NUMBER(value)  ((value).type == VAL_NUMBER)
```

#### 8. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define IS_OBJ(value)     ((value).type == VAL_OBJ)
```

#### 9. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```


#define AS_BOOL(value)    ((value).as.boolean)
```

#### 10. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define IS_OBJ(value)     ((value).type == VAL_OBJ)

```

#### 11. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define AS_OBJ(value)     ((value).as.obj)
```

#### 12. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define AS_BOOL(value)    ((value).as.boolean)
```

#### 13. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define NUMBER_VAL(value) ((Value){VAL_NUMBER, {.number = value}})
```

#### 14. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```
#define OBJ_VAL(object)   ((Value){VAL_OBJ, {.obj = (Obj*)object}})
```

#### 15. 19 . 1 Values and Objects — [source](https://craftinginterpreters.com/strings.html)
```


typedef struct {
```

#### 16. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```c
#include "common.h"

```

#### 17. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
typedef struct Obj Obj;

```

#### 18. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
typedef enum {
```

#### 19. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```c
#ifndef clox_object_h
#define clox_object_h

#include "common.h"
#include "value.h"

struct Obj {
  ObjType type;
};

#endif
```

#### 20. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```c
#include "value.h"
```

#### 21. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


typedef enum {
  OBJ_STRING,
} ObjType;
```

#### 22. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


struct Obj {
```

#### 23. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```c
#include "value.h"
```

#### 24. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

#### 25. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


typedef enum {
```

#### 26. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
typedef struct Obj Obj;
```

#### 27. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
typedef struct ObjString ObjString;
```

#### 28. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


typedef enum {
```

#### 29. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
};
```

#### 30. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


struct ObjString {
  Obj obj;
  int length;
  char* chars;
};
```

#### 31. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


#endif
```

#### 32. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
#define OBJ_TYPE(value)        (AS_OBJ(value)->type)
```

#### 33. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

#### 34. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


typedef enum {
```

#### 35. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
};

```

#### 36. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
static inline bool isObjType(Value value, ObjType type) {
  return IS_OBJ(value) && AS_OBJ(value)->type == type;
}

```

#### 37. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
#endif
```

#### 38. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
IS_STRING(POP())
```

#### 39. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```
#define IS_STRING(value)       isObjType(value, OBJ_STRING)
```

#### 40. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


#define AS_STRING(value)       ((ObjString*)AS_OBJ(value))
#define AS_CSTRING(value)      (((ObjString*)AS_OBJ(value))->chars)
```

#### 41. 19 . 2 Struct Inheritance — [source](https://craftinginterpreters.com/strings.html)
```


typedef enum {
```

#### 42. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
  [TOKEN_IDENTIFIER]    = {NULL,     NULL,   PREC_NONE},
```

#### 43. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
  [TOKEN_STRING]        = {string,   NULL,   PREC_NONE},
```

#### 44. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
  [TOKEN_NUMBER]        = {number,   NULL,   PREC_NONE},
```

#### 45. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
static void string() {
  emitConstant(OBJ_VAL(copyString(parser.previous.start + 1,
                                  parser.previous.length - 2)));
}
```

#### 46. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
};

```

#### 47. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
ObjString* copyString(const char* chars, int length);

```

#### 48. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
static inline bool isObjType(Value value, ObjType type) {
```

#### 49. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
#define clox_compiler_h

```

#### 50. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "object.h"
```

#### 51. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "vm.h"
```

#### 52. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include <stdio.h>
#include <string.h>

#include "memory.h"
#include "object.h"
#include "value.h"
#include "vm.h"

ObjString* copyString(const char* chars, int length) {
  char* heapChars = ALLOCATE(char, length + 1);
  memcpy(heapChars, chars, length);
  heapChars[length] = '\0';
  return allocateString(heapChars, length);
}
```

#### 53. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "common.h"

```

#### 54. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
#define ALLOCATE(type, count) \
    (type*)reallocate(NULL, 0, sizeof(type) * (count))

```

#### 55. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
#define GROW_CAPACITY(capacity) \
```

#### 56. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "vm.h"

```

#### 57. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
static ObjString* allocateString(char* chars, int length) {
  ObjString* string = ALLOCATE_OBJ(ObjString, OBJ_STRING);
  string->length = length;
  string->chars = chars;
  return string;
}
```

#### 58. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "vm.h"
```

#### 59. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```


#define ALLOCATE_OBJ(type, objectType) \
    (type*)allocateObject(sizeof(type), objectType)
```

#### 60. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```


static ObjString* allocateString(char* chars, int length) {
```

#### 61. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```
#define ALLOCATE_OBJ(type, objectType) \
    (type*)allocateObject(sizeof(type), objectType)
```

#### 62. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```


static Obj* allocateObject(size_t size, ObjType type) {
  Obj* object = (Obj*)reallocate(NULL, 0, size);
  object->type = type;
  return object;
}
```

#### 63. 19 . 3 Strings — [source](https://craftinginterpreters.com/strings.html)
```


static ObjString* allocateString(char* chars, int length) {
```

#### 64. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
    case VAL_NUMBER: printf("%g", AS_NUMBER(value)); break;
```

#### 65. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
    case VAL_OBJ: printObject(value); break;
```

#### 66. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
  }
```

#### 67. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
ObjString* copyString(const char* chars, int length);
```

#### 68. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
void printObject(Value value);
```

#### 69. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```


static inline bool isObjType(Value value, ObjType type) {
```

#### 70. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
void printObject(Value value) {
  switch (OBJ_TYPE(value)) {
    case OBJ_STRING:
      printf("%s", AS_CSTRING(value));
      break;
  }
}
```

#### 71. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
"string" == "string"
```

#### 72. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
    case VAL_NUMBER: return AS_NUMBER(a) == AS_NUMBER(b);
```

#### 73. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
    case VAL_OBJ: {
      ObjString* aString = AS_STRING(a);
      ObjString* bString = AS_STRING(b);
      return aString->length == bString->length &&
          memcmp(aString->chars, bString->chars,
                 aString->length) == 0;
    }
```

#### 74. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```
    default:         return false; // Unreachable.
```

#### 75. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include <stdio.h>
```

#### 76. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include <string.h>
```

#### 77. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```c


#include "memory.h"
```

#### 78. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include <string.h>

```

#### 79. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "object.h"
```

#### 80. 19 . 4 Operations on Strings — [source](https://craftinginterpreters.com/strings.html)
```c
#include "memory.h"
```

#### 81. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
      case OP_LESS:     BINARY_OP(BOOL_VAL, <); break;
```

#### 82. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
      case OP_ADD: {
        if (IS_STRING(peek(0)) && IS_STRING(peek(1))) {
          concatenate();
        } else if (IS_NUMBER(peek(0)) && IS_NUMBER(peek(1))) {
          double b = AS_NUMBER(pop());
          double a = AS_NUMBER(pop());
          push(NUMBER_VAL(a + b));
        } else {
          runtimeError(
              "Operands must be two numbers or two strings.");
          return INTERPRET_RUNTIME_ERROR;
        }
        break;
      }
```

#### 83. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
      case OP_SUBTRACT: BINARY_OP(NUMBER_VAL, -); break;
```

#### 84. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
static void concatenate() {
  ObjString* b = AS_STRING(pop());
  ObjString* a = AS_STRING(pop());

  int length = a->length + b->length;
  char* chars = ALLOCATE(char, length + 1);
  memcpy(chars, a->chars, a->length);
  memcpy(chars + a->length, b->chars, b->length);
  chars[length] = '\0';

  ObjString* result = takeString(chars, length);
  push(OBJ_VAL(result));
}
```

#### 85. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```c
#include <stdio.h>
```

#### 86. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```c
#include <string.h>
```

#### 87. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```c


#include "common.h"
```

#### 88. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
};

```

#### 89. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
ObjString* takeString(char* chars, int length);
```

#### 90. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
ObjString* copyString(const char* chars, int length);
```

#### 91. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```
ObjString* takeString(char* chars, int length) {
  return allocateString(chars, length);
}
```

#### 92. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```c
#include "debug.h"
```

#### 93. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```c
#include "object.h"
#include "memory.h"
```

#### 94. 19 . 4 . 1 Concatenation — [source](https://craftinginterpreters.com/strings.html)
```c
#include "vm.h"
```

#### 95. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
"st" + "ri" + "ng"
```

#### 96. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
0000    OP_CONSTANT         0 "st"
0002    OP_CONSTANT         1 "ri"
0004    OP_ADD
0005    OP_CONSTANT         2 "ng"
0007    OP_ADD
0008    OP_RETURN
```

#### 97. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
struct Obj {
  ObjType type;
```

#### 98. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  struct Obj* next;
```

#### 99. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
};
```

#### 100. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  Value* stackTop;
```

#### 101. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  Obj* objects;
```

#### 102. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
} VM;
```

#### 103. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  resetStack();
```

#### 104. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  vm.objects = NULL;
```

#### 105. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
}
```

#### 106. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  object->type = type;
```

#### 107. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```


  object->next = vm.objects;
  vm.objects = object;
```

#### 108. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  return object;
```

#### 109. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
} InterpretResult;

```

#### 110. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
extern VM vm;

```

#### 111. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
void initVM();
```

#### 112. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
void freeVM() {
```

#### 113. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
  freeObjects();
```

#### 114. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
}
```

#### 115. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

#### 116. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
void freeObjects();
```

#### 117. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```


#endif
```

#### 118. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
void freeObjects() {
  Obj* object = vm.objects;
  while (object != NULL) {
    Obj* next = object->next;
    freeObject(object);
    object = next;
  }
}
```

#### 119. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
static void freeObject(Obj* object) {
  switch (object->type) {
    case OBJ_STRING: {
      ObjString* string = (ObjString*)object;
      FREE_ARRAY(char, string->chars, string->length + 1);
      FREE(ObjString, object);
      break;
    }
  }
}
```

#### 120. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```
    (type*)reallocate(NULL, 0, sizeof(type) * (count))
```

#### 121. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```


#define FREE(type, pointer) reallocate(pointer, sizeof(type), 0)
```

#### 122. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```


#define GROW_CAPACITY(capacity) \
```

#### 123. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```c
#include "common.h"
```

#### 124. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```c
#include "object.h"
```

#### 125. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```


#define ALLOCATE(type, count) \
```

#### 126. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```c
#include "memory.h"
```

#### 127. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```c
#include "vm.h"
```

#### 128. 19 . 5 Freeing Objects — [source](https://craftinginterpreters.com/strings.html)
```


void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

