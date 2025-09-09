# Chunks of Bytecode
_From: https://craftinginterpreters.com/chunks-of-bytecode.html_

#### 1. Chunks of Bytecode — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
fun fib(n) {
  if (n < 2) return n;
  return fib(n - 1) + fib(n - 2); 
}

var before = clock();
print fib(40);
var after = clock();
print after - before;
```

#### 2. 14 . 2 Getting Started — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "common.h"

int main(int argc, const char* argv[]) {
  return 0;
}
```

#### 3. 14 . 2 Getting Started — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#ifndef clox_common_h
#define clox_common_h

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#endif
```

#### 4. 14 . 3 Chunks of Instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#ifndef clox_chunk_h
#define clox_chunk_h

#include "common.h"

#endif
```

#### 5. 14 . 3 Chunks of Instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "common.h"
```

#### 6. 14 . 3 Chunks of Instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


typedef enum {
  OP_RETURN,
} OpCode;
```

#### 7. 14 . 3 Chunks of Instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 8. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
} OpCode;
```

#### 9. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


typedef struct {
  uint8_t* code;
} Chunk;
```

#### 10. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 11. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
typedef struct {
```

#### 12. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  int count;
  int capacity;
```

#### 13. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  uint8_t* code;
} Chunk;
```

#### 14. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
} Chunk;
```

#### 15. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


void initChunk(Chunk* chunk);
```

#### 16. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 17. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include <stdlib.h>

#include "chunk.h"

void initChunk(Chunk* chunk) {
  chunk->count = 0;
  chunk->capacity = 0;
  chunk->code = NULL;
}
```

#### 18. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void initChunk(Chunk* chunk);
```

#### 19. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeChunk(Chunk* chunk, uint8_t byte);
```

#### 20. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 21. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeChunk(Chunk* chunk, uint8_t byte) {
  if (chunk->capacity < chunk->count + 1) {
    int oldCapacity = chunk->capacity;
    chunk->capacity = GROW_CAPACITY(oldCapacity);
    chunk->code = GROW_ARRAY(uint8_t, chunk->code,
        oldCapacity, chunk->capacity);
  }

  chunk->code[chunk->count] = byte;
  chunk->count++;
}
```

#### 22. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "chunk.h"
```

#### 23. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "memory.h"
```

#### 24. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


void initChunk(Chunk* chunk) {
```

#### 25. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#ifndef clox_memory_h
#define clox_memory_h

#include "common.h"

#define GROW_CAPACITY(capacity) \
    ((capacity) < 8 ? 8 : (capacity) * 2)

#endif
```

#### 26. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
#define GROW_CAPACITY(capacity) \
    ((capacity) < 8 ? 8 : (capacity) * 2)
```

#### 27. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#define GROW_ARRAY(type, pointer, oldCount, newCount) \
    (type*)reallocate(pointer, sizeof(type) * (oldCount), \
        sizeof(type) * (newCount))

void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

#### 28. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 29. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include <stdlib.h>

#include "memory.h"

void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
  if (newSize == 0) {
    free(pointer);
    return NULL;
  }

  void* result = realloc(pointer, newSize);
  return result;
}
```

#### 30. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  void* result = realloc(pointer, newSize);
```

#### 31. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  if (result == NULL) exit(1);
```

#### 32. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  return result;
```

#### 33. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void initChunk(Chunk* chunk);
```

#### 34. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void freeChunk(Chunk* chunk);
```

#### 35. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeChunk(Chunk* chunk, uint8_t byte);
```

#### 36. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void freeChunk(Chunk* chunk) {
  FREE_ARRAY(uint8_t, chunk->code, chunk->capacity);
  initChunk(chunk);
}
```

#### 37. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
#define GROW_ARRAY(type, pointer, oldCount, newCount) \
    (type*)reallocate(pointer, sizeof(type) * (oldCount), \
        sizeof(type) * (newCount))
```

#### 38. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#define FREE_ARRAY(type, pointer, oldCount) \
    reallocate(pointer, sizeof(type) * (oldCount), 0)
```

#### 39. 14 . 3 . 1 A dynamic array of instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

#### 40. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
int main(int argc, const char* argv[]) {
```

#### 41. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  Chunk chunk;
  initChunk(&chunk);
  writeChunk(&chunk, OP_RETURN);
  freeChunk(&chunk);
```

#### 42. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  return 0;
```

#### 43. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "common.h"
```

#### 44. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "chunk.h"
```

#### 45. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c


int main(int argc, const char* argv[]) {
```

#### 46. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  initChunk(&chunk);
  writeChunk(&chunk, OP_RETURN);
```

#### 47. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


  disassembleChunk(&chunk, "test chunk");
```

#### 48. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  freeChunk(&chunk);
```

#### 49. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "chunk.h"
```

#### 50. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "debug.h"
```

#### 51. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c


int main(int argc, const char* argv[]) {
```

#### 52. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#ifndef clox_debug_h
#define clox_debug_h

#include "chunk.h"

void disassembleChunk(Chunk* chunk, const char* name);
int disassembleInstruction(Chunk* chunk, int offset);

#endif
```

#### 53. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include <stdio.h>

#include "debug.h"

void disassembleChunk(Chunk* chunk, const char* name) {
  printf("== %s ==\n", name);

  for (int offset = 0; offset < chunk->count;) {
    offset = disassembleInstruction(chunk, offset);
  }
}
```

#### 54. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
int disassembleInstruction(Chunk* chunk, int offset) {
  printf("%04d ", offset);

  uint8_t instruction = chunk->code[offset];
  switch (instruction) {
    case OP_RETURN:
      return simpleInstruction("OP_RETURN", offset);
    default:
      printf("Unknown opcode %d\n", instruction);
      return offset + 1;
  }
}
```

#### 55. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
static int simpleInstruction(const char* name, int offset) {
  printf("%s\n", name);
  return offset + 1;
}
```

#### 56. 14 . 4 Disassembling Chunks — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
== test chunk ==
0000 OP_RETURN
```

#### 57. 14 . 5 Constants — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
1 + 2;
```

#### 58. 14 . 5 . 1 Representing values — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#ifndef clox_value_h
#define clox_value_h

#include "common.h"

typedef double Value;

#endif
```

#### 59. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
typedef double Value;
```

#### 60. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


typedef struct {
  int capacity;
  int count;
  Value* values;
} ValueArray;
```

#### 61. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 62. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
} ValueArray;
```

#### 63. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


void initValueArray(ValueArray* array);
void writeValueArray(ValueArray* array, Value value);
void freeValueArray(ValueArray* array);
```

#### 64. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 65. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include <stdio.h>

#include "memory.h"
#include "value.h"

void initValueArray(ValueArray* array) {
  array->values = NULL;
  array->capacity = 0;
  array->count = 0;
}
```

#### 66. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeValueArray(ValueArray* array, Value value) {
  if (array->capacity < array->count + 1) {
    int oldCapacity = array->capacity;
    array->capacity = GROW_CAPACITY(oldCapacity);
    array->values = GROW_ARRAY(Value, array->values,
                               oldCapacity, array->capacity);
  }

  array->values[array->count] = value;
  array->count++;
}
```

#### 67. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void freeValueArray(ValueArray* array) {
  FREE_ARRAY(Value, array->values, array->capacity);
  initValueArray(array);
}
```

#### 68. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  uint8_t* code;
```

#### 69. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  ValueArray constants;
```

#### 70. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
} Chunk;
```

#### 71. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "common.h"
```

#### 72. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "value.h"
```

#### 73. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


typedef enum {
```

#### 74. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  chunk->code = NULL;
```

#### 75. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  initValueArray(&chunk->constants);
```

#### 76. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
}
```

#### 77. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  FREE_ARRAY(uint8_t, chunk->code, chunk->capacity);
```

#### 78. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  freeValueArray(&chunk->constants);
```

#### 79. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  initChunk(chunk);
```

#### 80. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeChunk(Chunk* chunk, uint8_t byte);
```

#### 81. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
int addConstant(Chunk* chunk, Value value);
```

#### 82. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 83. 14 . 5 . 2 Value arrays — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
int addConstant(Chunk* chunk, Value value) {
  writeValueArray(&chunk->constants, value);
  return chunk->constants.count - 1;
}
```

#### 84. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
print 1;
print 2;
```

#### 85. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
typedef enum {
```

#### 86. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  OP_CONSTANT,
```

#### 87. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  OP_RETURN,
```

#### 88. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  initChunk(&chunk);
```

#### 89. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


  int constant = addConstant(&chunk, 1.2);
  writeChunk(&chunk, OP_CONSTANT);
  writeChunk(&chunk, constant);

```

#### 90. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  writeChunk(&chunk, OP_RETURN);
```

#### 91. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  switch (instruction) {
```

#### 92. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

#### 93. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
    case OP_RETURN:
```

#### 94. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
static int constantInstruction(const char* name, Chunk* chunk,
                               int offset) {
  uint8_t constant = chunk->code[offset + 1];
  printf("%-16s %4d '", name, constant);
  printValue(chunk->constants.values[constant]);
  printf("'\n");
}
```

#### 95. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "debug.h"
```

#### 96. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```c
#include "value.h"
```

#### 97. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


void disassembleChunk(Chunk* chunk, const char* name) {
```

#### 98. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void freeValueArray(ValueArray* array);
```

#### 99. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void printValue(Value value);
```

#### 100. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


#endif
```

#### 101. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void printValue(Value value) {
  printf("%g", value);
}
```

#### 102. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  printf("'\n");
```

#### 103. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  return offset + 2;
```

#### 104. 14 . 5 . 3 Constant instructions — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
}
```

#### 105. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  uint8_t* code;
```

#### 106. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  int* lines;
```

#### 107. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  ValueArray constants;
```

#### 108. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  chunk->code = NULL;
```

#### 109. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  chunk->lines = NULL;
```

#### 110. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  initValueArray(&chunk->constants);
```

#### 111. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  FREE_ARRAY(uint8_t, chunk->code, chunk->capacity);
```

#### 112. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  FREE_ARRAY(int, chunk->lines, chunk->capacity);
```

#### 113. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  freeValueArray(&chunk->constants);
```

#### 114. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void freeChunk(Chunk* chunk);
```

#### 115. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeChunk(Chunk* chunk, uint8_t byte, int line);
```

#### 116. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
int addConstant(Chunk* chunk, Value value);
```

#### 117. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeChunk(Chunk* chunk, uint8_t byte, int line) {
```

#### 118. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  if (chunk->capacity < chunk->count + 1) {
```

#### 119. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
    chunk->code = GROW_ARRAY(uint8_t, chunk->code,
        oldCapacity, chunk->capacity);
```

#### 120. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
    chunk->lines = GROW_ARRAY(int, chunk->lines,
        oldCapacity, chunk->capacity);
```

#### 121. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  }
```

#### 122. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  chunk->code[chunk->count] = byte;
```

#### 123. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  chunk->lines[chunk->count] = line;
```

#### 124. 14 . 6 Line Information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  chunk->count++;
```

#### 125. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  int constant = addConstant(&chunk, 1.2);
```

#### 126. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  writeChunk(&chunk, OP_CONSTANT, 123);
  writeChunk(&chunk, constant, 123);

  writeChunk(&chunk, OP_RETURN, 123);
```

#### 127. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


  disassembleChunk(&chunk, "test chunk");
```

#### 128. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
int disassembleInstruction(Chunk* chunk, int offset) {
  printf("%04d ", offset);
```

#### 129. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
  if (offset > 0 &&
      chunk->lines[offset] == chunk->lines[offset - 1]) {
    printf("   | ");
  } else {
    printf("%4d ", chunk->lines[offset]);
  }
```

#### 130. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```


  uint8_t instruction = chunk->code[offset];
```

#### 131. 14 . 6 . 1 Disassembling line information — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
== test chunk ==
0000  123 OP_CONSTANT         0 '1.2'
0002    | OP_RETURN
```

#### 132. Challenges — [source](https://craftinginterpreters.com/chunks-of-bytecode.html)
```
void writeConstant(Chunk* chunk, Value value, int line) {
  // Implement me...
}
```

