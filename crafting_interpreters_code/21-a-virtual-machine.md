# A Virtual Machine
_From: https://craftinginterpreters.com/a-virtual-machine.html_

#### 1. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#ifndef clox_vm_h
#define clox_vm_h

#include "chunk.h"

typedef struct {
  Chunk* chunk;
} VM;

void initVM();
void freeVM();

#endif
```

#### 2. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "common.h"
#include "vm.h"

VM vm; 

void initVM() {
}

void freeVM() {
}
```

#### 3. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
int main(int argc, const char* argv[]) {
```

#### 4. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  initVM();

```

#### 5. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  Chunk chunk;
```

#### 6. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  disassembleChunk(&chunk, "test chunk");
```

#### 7. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  freeVM();
```

#### 8. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  freeChunk(&chunk);
```

#### 9. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "debug.h"
```

#### 10. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "vm.h"
```

#### 11. 15 . 1 An Instruction Execution Machine — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c


int main(int argc, const char* argv[]) {
```

#### 12. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  disassembleChunk(&chunk, "test chunk");
```

#### 13. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  interpret(&chunk);
```

#### 14. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  freeVM();
```

#### 15. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
void freeVM();
```

#### 16. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
InterpretResult interpret(Chunk* chunk);
```

#### 17. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


#endif
```

#### 18. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
} VM;

```

#### 19. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
typedef enum {
  INTERPRET_OK,
  INTERPRET_COMPILE_ERROR,
  INTERPRET_RUNTIME_ERROR
} InterpretResult;

```

#### 20. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
void initVM();
void freeVM();
```

#### 21. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
InterpretResult interpret(Chunk* chunk) {
  vm.chunk = chunk;
  vm.ip = vm.chunk->code;
  return run();
}
```

#### 22. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
typedef struct {
  Chunk* chunk;
```

#### 23. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  uint8_t* ip;
```

#### 24. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
} VM;
```

#### 25. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
static InterpretResult run() {
#define READ_BYTE() (*vm.ip++)

  for (;;) {
    uint8_t instruction;
    switch (instruction = READ_BYTE()) {
      case OP_RETURN: {
        return INTERPRET_OK;
      }
    }
  }

#undef READ_BYTE
}
```

#### 26. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    switch (instruction = READ_BYTE()) {
```

#### 27. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_CONSTANT: {
        Value constant = READ_CONSTANT();
        printValue(constant);
        printf("\n");
        break;
      }
```

#### 28. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_RETURN: {
```

#### 29. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include <stdio.h>

```

#### 30. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "common.h"
```

#### 31. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#define READ_BYTE() (*vm.ip++)
```

#### 32. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

#### 33. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


  for (;;) {
```

#### 34. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#undef READ_BYTE
```

#### 35. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#undef READ_CONSTANT
```

#### 36. 15 . 1 . 1 Executing instructions — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
}
```

#### 37. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include <stdint.h>
```

#### 38. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


#define DEBUG_TRACE_EXECUTION
```

#### 39. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


#endif
```

#### 40. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  for (;;) {
```

#### 41. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#ifdef DEBUG_TRACE_EXECUTION
    disassembleInstruction(vm.chunk,
                           (int)(vm.ip - vm.chunk->code));
#endif

```

#### 42. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    uint8_t instruction;
```

#### 43. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "common.h"
```

#### 44. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "debug.h"
```

#### 45. 15 . 1 . 2 Execution tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "vm.h"
```

#### 46. 15 . 2 A Value Stack Manipulator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
print 3 - 2;
```

#### 47. 15 . 2 A Value Stack Manipulator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
fun echo(n) {
  print n;
  return n;
}

print echo(echo(1) + echo(2)) + echo(echo(4) + echo(5));
```

#### 48. 15 . 2 A Value Stack Manipulator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
1  // from echo(1)
2  // from echo(2)
3  // from echo(1 + 2)
4  // from echo(4)
5  // from echo(5)
9  // from echo(4 + 5)
12 // from print 3 + 9
```

#### 49. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
typedef struct {
  Chunk* chunk;
  uint8_t* ip;
```

#### 50. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  Value stack[STACK_MAX];
  Value* stackTop;
```

#### 51. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
} VM;
```

#### 52. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "chunk.h"
```

#### 53. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


#define STACK_MAX 256
```

#### 54. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


typedef struct {
```

#### 55. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "chunk.h"
```

#### 56. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```c
#include "value.h"
```

#### 57. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


#define STACK_MAX 256
```

#### 58. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
void initVM() {
```

#### 59. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  resetStack();
```

#### 60. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
}
```

#### 61. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
static void resetStack() {
  vm.stackTop = vm.stack;
}
```

#### 62. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
InterpretResult interpret(Chunk* chunk);
```

#### 63. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
void push(Value value);
Value pop();
```

#### 64. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


#endif
```

#### 65. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
void push(Value value) {
  *vm.stackTop = value;
  vm.stackTop++;
}
```

#### 66. 15 . 2 . 1 The VM’s Stack — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
Value pop() {
  vm.stackTop--;
  return *vm.stackTop;
}
```

#### 67. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#ifdef DEBUG_TRACE_EXECUTION
```

#### 68. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    printf("          ");
    for (Value* slot = vm.stack; slot < vm.stackTop; slot++) {
      printf("[ ");
      printValue(*slot);
      printf(" ]");
    }
    printf("\n");
```

#### 69. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    disassembleInstruction(vm.chunk,
```

#### 70. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_CONSTANT: {
        Value constant = READ_CONSTANT();
```

#### 71. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
        push(constant);
```

#### 72. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
        break;
```

#### 73. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_RETURN: {
```

#### 74. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
        printValue(pop());
        printf("\n");
```

#### 75. 15 . 2 . 2 Stack tracing — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
        return INTERPRET_OK;
```

#### 76. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
var a = 1.2;
print -a; // -1.2.
```

#### 77. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  OP_CONSTANT,
```

#### 78. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  OP_NEGATE,
```

#### 79. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  OP_RETURN,
```

#### 80. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      }
```

#### 81. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_NEGATE:   push(-pop()); break;
```

#### 82. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_RETURN: {
```

#### 83. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

#### 84. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    case OP_NEGATE:
      return simpleInstruction("OP_NEGATE", offset);
```

#### 85. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    case OP_RETURN:
```

#### 86. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  writeChunk(&chunk, constant, 123);
```

#### 87. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  writeChunk(&chunk, OP_NEGATE, 123);
```

#### 88. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


  writeChunk(&chunk, OP_RETURN, 123);
```

#### 89. 15 . 3 An Arithmetic Calculator — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
-1.2
```

#### 90. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  OP_CONSTANT,
```

#### 91. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  OP_ADD,
  OP_SUBTRACT,
  OP_MULTIPLY,
  OP_DIVIDE,
```

#### 92. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  OP_NEGATE,
```

#### 93. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      }
```

#### 94. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_ADD:      BINARY_OP(+); break;
      case OP_SUBTRACT: BINARY_OP(-); break;
      case OP_MULTIPLY: BINARY_OP(*); break;
      case OP_DIVIDE:   BINARY_OP(/); break;
```

#### 95. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
      case OP_NEGATE:   push(-pop()); break;
```

#### 96. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])
```

#### 97. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#define BINARY_OP(op) \
    do { \
      double b = pop(); \
      double a = pop(); \
      push(a op b); \
    } while (false)
```

#### 98. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


  for (;;) {
```

#### 99. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#define WAKE_UP() makeCoffee(); drinkCoffee();
```

#### 100. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
if (morning) WAKE_UP();
```

#### 101. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
if (morning) makeCoffee(); drinkCoffee();;
```

#### 102. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#define WAKE_UP() { makeCoffee(); drinkCoffee(); }
```

#### 103. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
if (morning)
  WAKE_UP();
else
  sleepIn();
```

#### 104. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#undef READ_CONSTANT
```

#### 105. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
#undef BINARY_OP
```

#### 106. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
}
```

#### 107. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    case OP_CONSTANT:
      return constantInstruction("OP_CONSTANT", chunk, offset);
```

#### 108. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    case OP_ADD:
      return simpleInstruction("OP_ADD", offset);
    case OP_SUBTRACT:
      return simpleInstruction("OP_SUBTRACT", offset);
    case OP_MULTIPLY:
      return simpleInstruction("OP_MULTIPLY", offset);
    case OP_DIVIDE:
      return simpleInstruction("OP_DIVIDE", offset);
```

#### 109. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
    case OP_NEGATE:
```

#### 110. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  int constant = addConstant(&chunk, 1.2);
  writeChunk(&chunk, OP_CONSTANT, 123);
  writeChunk(&chunk, constant, 123);
```

#### 111. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```


  constant = addConstant(&chunk, 3.4);
  writeChunk(&chunk, OP_CONSTANT, 123);
  writeChunk(&chunk, constant, 123);

  writeChunk(&chunk, OP_ADD, 123);

  constant = addConstant(&chunk, 5.6);
  writeChunk(&chunk, OP_CONSTANT, 123);
  writeChunk(&chunk, constant, 123);

  writeChunk(&chunk, OP_DIVIDE, 123);
```

#### 112. 15 . 3 . 1 Binary operators — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
  writeChunk(&chunk, OP_NEGATE, 123);

  writeChunk(&chunk, OP_RETURN, 123);
```

#### 113. Challenges — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
1 * 2 + 3
1 + 2 * 3
3 - 2 - 1
1 + 2 * 3 - 4 / -5
```

#### 114. Challenges — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
4 - 3 * -2
```

#### 115. Design Note: Register-Based Bytecode — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
var a = 1;
var b = 2;
var c = a + b;
```

#### 116. Design Note: Register-Based Bytecode — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
load <a>  // Read local variable a and push onto stack.
load <b>  // Read local variable b and push onto stack.
add       // Pop two values, add, push result.
store <c> // Pop value and store in local variable c.
```

#### 117. Design Note: Register-Based Bytecode — [source](https://craftinginterpreters.com/a-virtual-machine.html)
```
add <a> <b> <c> // Read values from a and b, add, store in c.
```

