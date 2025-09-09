# Garbage Collection
_From: https://craftinginterpreters.com/garbage-collection.html_

#### 1. 26 . 1 Reachability — [source](https://craftinginterpreters.com/garbage-collection.html)
```
var a = "first value";
a = "updated";
// GC here.
print a;
```

#### 2. 26 . 1 Reachability — [source](https://craftinginterpreters.com/garbage-collection.html)
```
var global = "string";
{
  var local = "another";
  print global + local;
}
```

#### 3. 26 . 1 Reachability — [source](https://craftinginterpreters.com/garbage-collection.html)
```
fun makeClosure() {
  var a = "data";

  fun f() { print a; }
  return f;
}

{
  var closure = makeClosure();
  // GC here.
  closure();
}
```

#### 4. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

#### 5. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void collectGarbage();
```

#### 6. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void freeObjects();
```

#### 7. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void collectGarbage() {
}
```

#### 8. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#define DEBUG_TRACE_EXECUTION
```

#### 9. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#define DEBUG_STRESS_GC
```

#### 10. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#define UINT8_COUNT (UINT8_MAX + 1)
```

#### 11. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

#### 12. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  if (newSize > oldSize) {
#ifdef DEBUG_STRESS_GC
    collectGarbage();
#endif
  }

```

#### 13. 26 . 2 . 1 Collecting garbage — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  if (newSize == 0) {
```

#### 14. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#define DEBUG_STRESS_GC
```

#### 15. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#define DEBUG_LOG_GC
```

#### 16. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#define UINT8_COUNT (UINT8_MAX + 1)
```

#### 17. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "vm.h"
```

#### 18. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```c


#ifdef DEBUG_LOG_GC
#include <stdio.h>
#include "debug.h"
#endif
```

#### 19. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```


void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

#### 20. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void collectGarbage() {
```

#### 21. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#ifdef DEBUG_LOG_GC
  printf("-- gc begin\n");
#endif
```

#### 22. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
}
```

#### 23. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  printf("-- gc begin\n");
#endif
```

#### 24. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#ifdef DEBUG_LOG_GC
  printf("-- gc end\n");
#endif
```

#### 25. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
}
```

#### 26. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  vm.objects = object;
```

#### 27. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#ifdef DEBUG_LOG_GC
  printf("%p allocate %zu for %d\n", (void*)object, size, type);
#endif

```

#### 28. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  return object;
```

#### 29. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void freeObject(Obj* object) {
```

#### 30. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#ifdef DEBUG_LOG_GC
  printf("%p free type %d\n", (void*)object, object->type);
#endif

```

#### 31. 26 . 2 . 2 Debug logging — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  switch (object->type) {
```

#### 32. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#ifdef DEBUG_LOG_GC
  printf("-- gc begin\n");
#endif
```

#### 33. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  markRoots();
```

#### 34. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#ifdef DEBUG_LOG_GC
```

#### 35. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void markRoots() {
  for (Value* slot = vm.stack; slot < vm.stackTop; slot++) {
    markValue(*slot);
  }
}
```

#### 36. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

#### 37. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markValue(Value value);
```

#### 38. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void collectGarbage();
```

#### 39. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markValue(Value value) {
  if (IS_OBJ(value)) markObject(AS_OBJ(value));
}
```

#### 40. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void* reallocate(void* pointer, size_t oldSize, size_t newSize);
```

#### 41. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markObject(Obj* object);
```

#### 42. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markValue(Value value);
```

#### 43. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markObject(Obj* object) {
  if (object == NULL) return;
  object->isMarked = true;
}
```

#### 44. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  ObjType type;
```

#### 45. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  bool isMarked;
```

#### 46. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  struct Obj* next;
```

#### 47. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  object->type = type;
```

#### 48. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  object->isMarked = false;
```

#### 49. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  object->next = vm.objects;
```

#### 50. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markObject(Obj* object) {
  if (object == NULL) return;
```

#### 51. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#ifdef DEBUG_LOG_GC
  printf("%p mark ", (void*)object);
  printValue(OBJ_VAL(object));
  printf("\n");
#endif

```

#### 52. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  object->isMarked = true;
```

#### 53. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    markValue(*slot);
  }
```

#### 54. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  markTable(&vm.globals);
```

#### 55. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
}
```

#### 56. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
ObjString* tableFindString(Table* table, const char* chars,
                           int length, uint32_t hash);
```

#### 57. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markTable(Table* table);
```

#### 58. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#endif
```

#### 59. 26 . 3 Marking the Roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markTable(Table* table) {
  for (int i = 0; i < table->capacity; i++) {
    Entry* entry = &table->entries[i];
    markObject((Obj*)entry->key);
    markValue(entry->value);
  }
}
```

#### 60. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  }
```

#### 61. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  for (int i = 0; i < vm.frameCount; i++) {
    markObject((Obj*)vm.frames[i].closure);
  }
```

#### 62. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  markTable(&vm.globals);
```

#### 63. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  for (int i = 0; i < vm.frameCount; i++) {
    markObject((Obj*)vm.frames[i].closure);
  }
```

#### 64. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  for (ObjUpvalue* upvalue = vm.openUpvalues;
       upvalue != NULL;
       upvalue = upvalue->next) {
    markObject((Obj*)upvalue);
  }
```

#### 65. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  markTable(&vm.globals);
```

#### 66. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  markTable(&vm.globals);
```

#### 67. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  markCompilerRoots();
```

#### 68. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
}
```

#### 69. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
ObjFunction* compile(const char* source);
```

#### 70. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markCompilerRoots();
```

#### 71. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#endif
```

#### 72. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include <stdlib.h>

```

#### 73. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "compiler.h"
```

#### 74. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "memory.h"
```

#### 75. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markCompilerRoots() {
  Compiler* compiler = current;
  while (compiler != NULL) {
    markObject((Obj*)compiler->function);
    compiler = compiler->enclosing;
  }
}
```

#### 76. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "compiler.h"
```

#### 77. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "memory.h"
```

#### 78. 26 . 3 . 1 Less obvious roots — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "scanner.h"
```

#### 79. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  object->isMarked = true;
```

#### 80. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  if (vm.grayCapacity < vm.grayCount + 1) {
    vm.grayCapacity = GROW_CAPACITY(vm.grayCapacity);
    vm.grayStack = (Obj**)realloc(vm.grayStack,
                                  sizeof(Obj*) * vm.grayCapacity);
  }

  vm.grayStack[vm.grayCount++] = object;
```

#### 81. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
}
```

#### 82. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  Obj* objects;
```

#### 83. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  int grayCount;
  int grayCapacity;
  Obj** grayStack;
```

#### 84. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
} VM;
```

#### 85. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  vm.objects = NULL;
```

#### 86. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  vm.grayCount = 0;
  vm.grayCapacity = 0;
  vm.grayStack = NULL;
```

#### 87. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  initTable(&vm.globals);
```

#### 88. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    object = next;
  }
```

#### 89. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  free(vm.grayStack);
```

#### 90. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
}
```

#### 91. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    vm.grayStack = (Obj**)realloc(vm.grayStack,
                                  sizeof(Obj*) * vm.grayCapacity);
```

#### 92. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


    if (vm.grayStack == NULL) exit(1);
```

#### 93. 26 . 4 . 2 A worklist for gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  }
```

#### 94. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  markRoots();
```

#### 95. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  traceReferences();
```

#### 96. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#ifdef DEBUG_LOG_GC
```

#### 97. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void traceReferences() {
  while (vm.grayCount > 0) {
    Obj* object = vm.grayStack[--vm.grayCount];
    blackenObject(object);
  }
}
```

#### 98. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void blackenObject(Obj* object) {
  switch (object->type) {
    case OBJ_NATIVE:
    case OBJ_STRING:
      break;
  }
}
```

#### 99. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void blackenObject(Obj* object) {
  switch (object->type) {
```

#### 100. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    case OBJ_UPVALUE:
      markValue(((ObjUpvalue*)object)->closed);
      break;
```

#### 101. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    case OBJ_NATIVE:
```

#### 102. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  switch (object->type) {
```

#### 103. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    case OBJ_FUNCTION: {
      ObjFunction* function = (ObjFunction*)object;
      markObject((Obj*)function->name);
      markArray(&function->chunk.constants);
      break;
    }
```

#### 104. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    case OBJ_UPVALUE:
```

#### 105. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void markArray(ValueArray* array) {
  for (int i = 0; i < array->count; i++) {
    markValue(array->values[i]);
  }
}
```

#### 106. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  switch (object->type) {
```

#### 107. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    case OBJ_CLOSURE: {
      ObjClosure* closure = (ObjClosure*)object;
      markObject((Obj*)closure->function);
      for (int i = 0; i < closure->upvalueCount; i++) {
        markObject((Obj*)closure->upvalues[i]);
      }
      break;
    }
```

#### 108. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    case OBJ_FUNCTION: {
```

#### 109. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void blackenObject(Obj* object) {
```

#### 110. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#ifdef DEBUG_LOG_GC
  printf("%p blacken ", (void*)object);
  printValue(OBJ_VAL(object));
  printf("\n");
#endif

```

#### 111. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  switch (object->type) {
```

#### 112. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  if (object == NULL) return;
```

#### 113. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  if (object->isMarked) return;

```

#### 114. 26 . 4 . 3 Processing gray objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#ifdef DEBUG_LOG_GC
```

#### 115. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  traceReferences();
```

#### 116. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  sweep();
```

#### 117. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#ifdef DEBUG_LOG_GC
```

#### 118. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void sweep() {
  Obj* previous = NULL;
  Obj* object = vm.objects;
  while (object != NULL) {
    if (object->isMarked) {
      previous = object;
      object = object->next;
    } else {
      Obj* unreached = object;
      object = object->next;
      if (previous != NULL) {
        previous->next = object;
      } else {
        vm.objects = object;
      }

      freeObject(unreached);
    }
  }
}
```

#### 119. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    if (object->isMarked) {
```

#### 120. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
      object->isMarked = false;
```

#### 121. 26 . 5 Sweeping Unused Objects — [source](https://craftinginterpreters.com/garbage-collection.html)
```
      previous = object;
```

#### 122. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  traceReferences();
```

#### 123. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  tableRemoveWhite(&vm.strings);
```

#### 124. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  sweep();
```

#### 125. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```
ObjString* tableFindString(Table* table, const char* chars,
                           int length, uint32_t hash);
```

#### 126. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```


void tableRemoveWhite(Table* table);
```

#### 127. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void markTable(Table* table);

```

#### 128. 26 . 5 . 1 Weak references and the string pool — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void tableRemoveWhite(Table* table) {
  for (int i = 0; i < table->capacity; i++) {
    Entry* entry = &table->entries[i];
    if (entry->key != NULL && !entry->key->obj.isMarked) {
      tableDelete(table, entry->key);
    }
  }
}
```

#### 129. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  ObjUpvalue* openUpvalues;
```

#### 130. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  size_t bytesAllocated;
  size_t nextGC;
```

#### 131. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  Obj* objects;
```

#### 132. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  vm.objects = NULL;
```

#### 133. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  vm.bytesAllocated = 0;
  vm.nextGC = 1024 * 1024;
```

#### 134. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  vm.grayCount = 0;
```

#### 135. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

#### 136. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  vm.bytesAllocated += newSize - oldSize;
```

#### 137. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  if (newSize > oldSize) {
```

#### 138. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
    collectGarbage();
#endif
```

#### 139. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


    if (vm.bytesAllocated > vm.nextGC) {
      collectGarbage();
    }
```

#### 140. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  }
```

#### 141. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  sweep();
```

#### 142. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  vm.nextGC = vm.bytesAllocated * GC_HEAP_GROW_FACTOR;
```

#### 143. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#ifdef DEBUG_LOG_GC
```

#### 144. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#endif
```

#### 145. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


#define GC_HEAP_GROW_FACTOR 2
```

#### 146. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```


void* reallocate(void* pointer, size_t oldSize, size_t newSize) {
```

#### 147. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  printf("-- gc begin\n");
```

#### 148. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  size_t before = vm.bytesAllocated;
```

#### 149. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#endif
```

#### 150. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  printf("-- gc end\n");
```

#### 151. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  printf("   collected %zu bytes (from %zu to %zu) next at %zu\n",
         before - vm.bytesAllocated, before, vm.bytesAllocated,
         vm.nextGC);
```

#### 152. 26 . 6 . 2 Self-adjusting heap — [source](https://craftinginterpreters.com/garbage-collection.html)
```
#endif
```

#### 153. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```
int addConstant(Chunk* chunk, Value value) {
```

#### 154. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  push(value);
```

#### 155. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  writeValueArray(&chunk->constants, value);
```

#### 156. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  writeValueArray(&chunk->constants, value);
```

#### 157. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  pop();
```

#### 158. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  return chunk->constants.count - 1;
```

#### 159. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "memory.h"
```

#### 160. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```c
#include "vm.h"
```

#### 161. 26 . 7 . 1 Adding to the constant table — [source](https://craftinginterpreters.com/garbage-collection.html)
```


void initChunk(Chunk* chunk) {
```

#### 162. 26 . 7 . 2 Interning strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  string->chars = chars;
  string->hash = hash;
```

#### 163. 26 . 7 . 2 Interning strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  push(OBJ_VAL(string));
```

#### 164. 26 . 7 . 2 Interning strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  tableSet(&vm.strings, string, NIL_VAL);
```

#### 165. 26 . 7 . 2 Interning strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  tableSet(&vm.strings, string, NIL_VAL);
```

#### 166. 26 . 7 . 2 Interning strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  pop();

```

#### 167. 26 . 7 . 2 Interning strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  return string;
}
```

#### 168. 26 . 7 . 3 Concatenating strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
static void concatenate() {
```

#### 169. 26 . 7 . 3 Concatenating strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  ObjString* b = AS_STRING(peek(0));
  ObjString* a = AS_STRING(peek(1));
```

#### 170. 26 . 7 . 3 Concatenating strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```


  int length = a->length + b->length;
```

#### 171. 26 . 7 . 3 Concatenating strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  ObjString* result = takeString(chars, length);
```

#### 172. 26 . 7 . 3 Concatenating strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  pop();
  pop();
```

#### 173. 26 . 7 . 3 Concatenating strings — [source](https://craftinginterpreters.com/garbage-collection.html)
```
  push(OBJ_VAL(result));
```

