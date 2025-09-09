# Types of Values
_From: https://craftinginterpreters.com/types-of-values.html_

#### 1. 18 . 1 Tagged Unions — [source](https://craftinginterpreters.com/types-of-values.html)
```c
#include "common.h"

```

#### 2. 18 . 1 Tagged Unions — [source](https://craftinginterpreters.com/types-of-values.html)
```
typedef enum {
  VAL_BOOL,
  VAL_NIL, 
  VAL_NUMBER,
} ValueType;

```

#### 3. 18 . 1 Tagged Unions — [source](https://craftinginterpreters.com/types-of-values.html)
```
typedef double Value;
```

#### 4. 18 . 1 Tagged Unions — [source](https://craftinginterpreters.com/types-of-values.html)
```
} ValueType;

```

#### 5. 18 . 1 Tagged Unions — [source](https://craftinginterpreters.com/types-of-values.html)
```
typedef struct {
  ValueType type;
  union {
    bool boolean;
    double number;
  } as; 
} Value;
```

#### 6. 18 . 1 Tagged Unions — [source](https://craftinginterpreters.com/types-of-values.html)
```


typedef struct {
```

#### 7. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```
} Value;
```

#### 8. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```


#define BOOL_VAL(value)   ((Value){VAL_BOOL, {.boolean = value}})
#define NIL_VAL           ((Value){VAL_NIL, {.number = 0}})
#define NUMBER_VAL(value) ((Value){VAL_NUMBER, {.number = value}})
```

#### 9. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```


typedef struct {
```

#### 10. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```
} Value;
```

#### 11. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```


#define AS_BOOL(value)    ((value).as.boolean)
#define AS_NUMBER(value)  ((value).as.number)
```

#### 12. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```


#define BOOL_VAL(value)   ((Value){VAL_BOOL, {.boolean = value}})
```

#### 13. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```
Value value = BOOL_VAL(true);
double number = AS_NUMBER(value);
```

#### 14. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```
} Value;
```

#### 15. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```


#define IS_BOOL(value)    ((value).type == VAL_BOOL)
#define IS_NIL(value)     ((value).type == VAL_NIL)
#define IS_NUMBER(value)  ((value).type == VAL_NUMBER)
```

#### 16. 18 . 2 Lox Values and C Values — [source](https://craftinginterpreters.com/types-of-values.html)
```


#define AS_BOOL(value)    ((value).as.boolean)
```

#### 17. 18 . 3 Dynamically Typed Numbers — [source](https://craftinginterpreters.com/types-of-values.html)
```
  double value = strtod(parser.previous.start, NULL);
```

#### 18. 18 . 3 Dynamically Typed Numbers — [source](https://craftinginterpreters.com/types-of-values.html)
```
  emitConstant(NUMBER_VAL(value));
```

#### 19. 18 . 3 Dynamically Typed Numbers — [source](https://craftinginterpreters.com/types-of-values.html)
```
}
```

#### 20. 18 . 3 Dynamically Typed Numbers — [source](https://craftinginterpreters.com/types-of-values.html)
```
void printValue(Value value) {
```

#### 21. 18 . 3 Dynamically Typed Numbers — [source](https://craftinginterpreters.com/types-of-values.html)
```
 printf("%g", AS_NUMBER(value));
```

#### 22. 18 . 3 Dynamically Typed Numbers — [source](https://craftinginterpreters.com/types-of-values.html)
```
}
```

#### 23. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```
print -false; // Uh...
```

#### 24. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_DIVIDE:   BINARY_OP(/); break;
```

#### 25. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_NEGATE:
        if (!IS_NUMBER(peek(0))) {
          runtimeError("Operand must be a number.");
          return INTERPRET_RUNTIME_ERROR;
        }
        push(NUMBER_VAL(-AS_NUMBER(pop())));
        break;
```

#### 26. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_RETURN: {
```

#### 27. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```
static Value peek(int distance) {
  return vm.stackTop[-1 - distance];
}
```

#### 28. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```
static void runtimeError(const char* format, ...) {
  va_list args;
  va_start(args, format);
  vfprintf(stderr, format, args);
  va_end(args);
  fputs("\n", stderr);

  size_t instruction = vm.ip - vm.chunk->code - 1;
  int line = vm.chunk->lines[instruction];
  fprintf(stderr, "[line %d] in script\n", line);
  resetStack();
}
```

#### 29. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```c
#include <stdarg.h>
```

#### 30. 18 . 3 . 1 Unary negation and runtime errors — [source](https://craftinginterpreters.com/types-of-values.html)
```c
#include <stdio.h>
```

#### 31. 18 . 3 . 2 Binary arithmetic operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

#### 32. 18 . 3 . 2 Binary arithmetic operators — [source](https://craftinginterpreters.com/types-of-values.html)
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

#### 33. 18 . 3 . 2 Binary arithmetic operators — [source](https://craftinginterpreters.com/types-of-values.html)
```


  for (;;) {
```

#### 34. 18 . 3 . 2 Binary arithmetic operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      }
```

#### 35. 18 . 3 . 2 Binary arithmetic operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
      case OP_SUBTRACT: BINARY_OP(NUMBER_VAL, -); break;
      case OP_MULTIPLY: BINARY_OP(NUMBER_VAL, *); break;
      case OP_DIVIDE:   BINARY_OP(NUMBER_VAL, /); break;
```

#### 36. 18 . 3 . 2 Binary arithmetic operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_NEGATE:
```

#### 37. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_CONSTANT,
```

#### 38. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_NIL,
  OP_TRUE,
  OP_FALSE,
```

#### 39. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_ADD,
```

#### 40. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_ELSE]          = {NULL,     NULL,   PREC_NONE},
```

#### 41. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_FALSE]         = {literal,  NULL,   PREC_NONE},
```

#### 42. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_FOR]           = {NULL,     NULL,   PREC_NONE},
```

#### 43. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_THIS]          = {NULL,     NULL,   PREC_NONE},
```

#### 44. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_TRUE]          = {literal,  NULL,   PREC_NONE},
```

#### 45. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_VAR]           = {NULL,     NULL,   PREC_NONE},
```

#### 46. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_IF]            = {NULL,     NULL,   PREC_NONE},
```

#### 47. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_NIL]           = {literal,  NULL,   PREC_NONE},
```

#### 48. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_OR]            = {NULL,     NULL,   PREC_NONE},
```

#### 49. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
static void literal() {
  switch (parser.previous.type) {
    case TOKEN_FALSE: emitByte(OP_FALSE); break;
    case TOKEN_NIL: emitByte(OP_NIL); break;
    case TOKEN_TRUE: emitByte(OP_TRUE); break;
    default: return; // Unreachable.
  }
}
```

#### 50. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_CONSTANT: {
        Value constant = READ_CONSTANT();
        push(constant);
        break;
      }
```

#### 51. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_NIL: push(NIL_VAL); break;
      case OP_TRUE: push(BOOL_VAL(true)); break;
      case OP_FALSE: push(BOOL_VAL(false)); break;
```

#### 52. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
```

#### 53. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

#### 54. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_NIL:
      return simpleInstruction("OP_NIL", offset);
    case OP_TRUE:
      return simpleInstruction("OP_TRUE", offset);
    case OP_FALSE:
      return simpleInstruction("OP_FALSE", offset);
```

#### 55. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_ADD:
```

#### 56. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
true
```

#### 57. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
void printValue(Value value) {
```

#### 58. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
  switch (value.type) {
    case VAL_BOOL:
      printf(AS_BOOL(value) ? "true" : "false");
      break;
    case VAL_NIL: printf("nil"); break;
    case VAL_NUMBER: printf("%g", AS_NUMBER(value)); break;
  }
```

#### 59. 18 . 4 Two New Types — [source](https://craftinginterpreters.com/types-of-values.html)
```
}
```

#### 60. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
print !true; // "false"
```

#### 61. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_DIVIDE,
```

#### 62. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_NOT,
```

#### 63. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_NEGATE,
```

#### 64. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_STAR]          = {NULL,     binary, PREC_FACTOR},
```

#### 65. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_BANG]          = {unary,    NULL,   PREC_NONE},
```

#### 66. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_BANG_EQUAL]    = {NULL,     NULL,   PREC_NONE},
```

#### 67. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
  switch (operatorType) {
```

#### 68. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case TOKEN_BANG: emitByte(OP_NOT); break;
```

#### 69. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case TOKEN_MINUS: emitByte(OP_NEGATE); break;
    default: return; // Unreachable.
  }
```

#### 70. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_DIVIDE:   BINARY_OP(NUMBER_VAL, /); break;
```

#### 71. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_NOT:
        push(BOOL_VAL(isFalsey(pop())));
        break;
```

#### 72. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_NEGATE:
```

#### 73. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
print !nil;
```

#### 74. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
static bool isFalsey(Value value) {
  return IS_NIL(value) || (IS_BOOL(value) && !AS_BOOL(value));
}
```

#### 75. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_DIVIDE:
      return simpleInstruction("OP_DIVIDE", offset);
```

#### 76. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_NOT:
      return simpleInstruction("OP_NOT", offset);
```

#### 77. 18 . 4 . 1 Logical not and falsiness — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_NEGATE:
```

#### 78. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_FALSE,
```

#### 79. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_EQUAL,
  OP_GREATER,
  OP_LESS,
```

#### 80. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  OP_ADD,
```

#### 81. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_BANG]          = {unary,    NULL,   PREC_NONE},
```

#### 82. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_BANG_EQUAL]    = {NULL,     binary, PREC_EQUALITY},
```

#### 83. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_EQUAL]         = {NULL,     NULL,   PREC_NONE},
```

#### 84. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_EQUAL]         = {NULL,     NULL,   PREC_NONE},
```

#### 85. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_EQUAL_EQUAL]   = {NULL,     binary, PREC_EQUALITY},
  [TOKEN_GREATER]       = {NULL,     binary, PREC_COMPARISON},
  [TOKEN_GREATER_EQUAL] = {NULL,     binary, PREC_COMPARISON},
  [TOKEN_LESS]          = {NULL,     binary, PREC_COMPARISON},
  [TOKEN_LESS_EQUAL]    = {NULL,     binary, PREC_COMPARISON},
```

#### 86. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  [TOKEN_IDENTIFIER]    = {NULL,     NULL,   PREC_NONE},
```

#### 87. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
  switch (operatorType) {
```

#### 88. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case TOKEN_BANG_EQUAL:    emitBytes(OP_EQUAL, OP_NOT); break;
    case TOKEN_EQUAL_EQUAL:   emitByte(OP_EQUAL); break;
    case TOKEN_GREATER:       emitByte(OP_GREATER); break;
    case TOKEN_GREATER_EQUAL: emitBytes(OP_LESS, OP_NOT); break;
    case TOKEN_LESS:          emitByte(OP_LESS); break;
    case TOKEN_LESS_EQUAL:    emitBytes(OP_GREATER, OP_NOT); break;
```

#### 89. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case TOKEN_PLUS:          emitByte(OP_ADD); break;
```

#### 90. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_FALSE: push(BOOL_VAL(false)); break;
```

#### 91. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_EQUAL: {
        Value b = pop();
        Value a = pop();
        push(BOOL_VAL(valuesEqual(a, b)));
        break;
      }
```

#### 92. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
```

#### 93. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
} ValueArray;

```

#### 94. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
bool valuesEqual(Value a, Value b);
```

#### 95. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
void initValueArray(ValueArray* array);
```

#### 96. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
bool valuesEqual(Value a, Value b) {
  if (a.type != b.type) return false;
  switch (a.type) {
    case VAL_BOOL:   return AS_BOOL(a) == AS_BOOL(b);
    case VAL_NIL:    return true;
    case VAL_NUMBER: return AS_NUMBER(a) == AS_NUMBER(b);
    default:         return false; // Unreachable.
  }
}
```

#### 97. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
        push(BOOL_VAL(valuesEqual(a, b)));
        break;
      }
```

#### 98. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_GREATER:  BINARY_OP(BOOL_VAL, >); break;
      case OP_LESS:     BINARY_OP(BOOL_VAL, <); break;
```

#### 99. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
      case OP_ADD:      BINARY_OP(NUMBER_VAL, +); break;
```

#### 100. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_FALSE:
      return simpleInstruction("OP_FALSE", offset);
```

#### 101. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_EQUAL:
      return simpleInstruction("OP_EQUAL", offset);
    case OP_GREATER:
      return simpleInstruction("OP_GREATER", offset);
    case OP_LESS:
      return simpleInstruction("OP_LESS", offset);
```

#### 102. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
    case OP_ADD:
```

#### 103. 18 . 4 . 2 Equality and comparison operators — [source](https://craftinginterpreters.com/types-of-values.html)
```
!(5 - 4 > 3 * 2 == !nil)
```

