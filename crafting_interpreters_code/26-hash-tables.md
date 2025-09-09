# Hash Tables
_From: https://craftinginterpreters.com/hash-tables.html_

#### 1. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#ifndef clox_table_h
#define clox_table_h

#include "common.h"
#include "value.h"

typedef struct {
  int count;
  int capacity;
  Entry* entries;
} Table;

#endif
```

#### 2. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "value.h"
```

#### 3. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```


typedef struct {
  ObjString* key;
  Value value;
} Entry;
```

#### 4. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```


typedef struct {
```

#### 5. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```
} Table;

```

#### 6. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```
void initTable(Table* table);

```

#### 7. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```
#endif
```

#### 8. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include <stdlib.h>
#include <string.h>

#include "memory.h"
#include "object.h"
#include "table.h"
#include "value.h"

void initTable(Table* table) {
  table->count = 0;
  table->capacity = 0;
  table->entries = NULL;
}
```

#### 9. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```
void initTable(Table* table);
```

#### 10. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```
void freeTable(Table* table);
```

#### 11. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```


#endif
```

#### 12. 20 . 4 Building a Hash Table — [source](https://craftinginterpreters.com/hash-tables.html)
```
void freeTable(Table* table) {
  FREE_ARRAY(Entry, table->entries, table->capacity);
  initTable(table);
}
```

#### 13. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  char* chars;
```

#### 14. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  uint32_t hash;
```

#### 15. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
};
```

#### 16. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
static ObjString* allocateString(char* chars, int length,
                                 uint32_t hash) {
```

#### 17. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  ObjString* string = ALLOCATE_OBJ(ObjString, OBJ_STRING);
```

#### 18. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  string->chars = chars;
```

#### 19. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  string->hash = hash;
```

#### 20. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  return string;
}
```

#### 21. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
ObjString* copyString(const char* chars, int length) {
```

#### 22. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  uint32_t hash = hashString(chars, length);
```

#### 23. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  char* heapChars = ALLOCATE(char, length + 1);
```

#### 24. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  memcpy(heapChars, chars, length);
  heapChars[length] = '\0';
```

#### 25. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  return allocateString(heapChars, length, hash);
```

#### 26. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
}
```

#### 27. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
ObjString* takeString(char* chars, int length) {
```

#### 28. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
  uint32_t hash = hashString(chars, length);
  return allocateString(chars, length, hash);
```

#### 29. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
}
```

#### 30. 20 . 4 . 1 Hashing strings — [source](https://craftinginterpreters.com/hash-tables.html)
```
static uint32_t hashString(const char* key, int length) {
  uint32_t hash = 2166136261u;
  for (int i = 0; i < length; i++) {
    hash ^= (uint8_t)key[i];
    hash *= 16777619;
  }
  return hash;
}
```

#### 31. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
void freeTable(Table* table);
```

#### 32. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableSet(Table* table, ObjString* key, Value value);
```

#### 33. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```


#endif
```

#### 34. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableSet(Table* table, ObjString* key, Value value) {
  Entry* entry = findEntry(table->entries, table->capacity, key);
  bool isNewKey = entry->key == NULL;
  if (isNewKey) table->count++;

  entry->key = key;
  entry->value = value;
  return isNewKey;
}
```

#### 35. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableSet(Table* table, ObjString* key, Value value) {
```

#### 36. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
  if (table->count + 1 > table->capacity * TABLE_MAX_LOAD) {
    int capacity = GROW_CAPACITY(table->capacity);
    adjustCapacity(table, capacity);
  }

```

#### 37. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
  Entry* entry = findEntry(table->entries, table->capacity, key);
```

#### 38. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "value.h"

```

#### 39. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
#define TABLE_MAX_LOAD 0.75

```

#### 40. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
void initTable(Table* table) {
```

#### 41. 20 . 4 . 2 Inserting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
static Entry* findEntry(Entry* entries, int capacity,
                        ObjString* key) {
  uint32_t index = key->hash % capacity;
  for (;;) {
    Entry* entry = &entries[index];
    if (entry->key == key || entry->key == NULL) {
      return entry;
    }

    index = (index + 1) % capacity;
  }
}
```

#### 42. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
static void adjustCapacity(Table* table, int capacity) {
  Entry* entries = ALLOCATE(Entry, capacity);
  for (int i = 0; i < capacity; i++) {
    entries[i].key = NULL;
    entries[i].value = NIL_VAL;
  }

  table->entries = entries;
  table->capacity = capacity;
}
```

#### 43. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
    entries[i].value = NIL_VAL;
  }
```

#### 44. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```


  for (int i = 0; i < table->capacity; i++) {
    Entry* entry = &table->entries[i];
    if (entry->key == NULL) continue;

    Entry* dest = findEntry(entries, capacity, entry->key);
    dest->key = entry->key;
    dest->value = entry->value;
  }
```

#### 45. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```


  table->entries = entries;
```

#### 46. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
    dest->value = entry->value;
  }

```

#### 47. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
  FREE_ARRAY(Entry, table->entries, table->capacity);
```

#### 48. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
  table->entries = entries;
```

#### 49. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableSet(Table* table, ObjString* key, Value value);
```

#### 50. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
void tableAddAll(Table* from, Table* to);
```

#### 51. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```


#endif
```

#### 52. 20 . 4 . 3 Allocating and resizing — [source](https://craftinginterpreters.com/hash-tables.html)
```
void tableAddAll(Table* from, Table* to) {
  for (int i = 0; i < from->capacity; i++) {
    Entry* entry = &from->entries[i];
    if (entry->key != NULL) {
      tableSet(to, entry->key, entry->value);
    }
  }
}
```

#### 53. 20 . 4 . 4 Retrieving values — [source](https://craftinginterpreters.com/hash-tables.html)
```
void freeTable(Table* table);
```

#### 54. 20 . 4 . 4 Retrieving values — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableGet(Table* table, ObjString* key, Value* value);
```

#### 55. 20 . 4 . 4 Retrieving values — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableSet(Table* table, ObjString* key, Value value);
```

#### 56. 20 . 4 . 4 Retrieving values — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableGet(Table* table, ObjString* key, Value* value) {
  if (table->count == 0) return false;

  Entry* entry = findEntry(table->entries, table->capacity, key);
  if (entry->key == NULL) return false;

  *value = entry->value;
  return true;
}
```

#### 57. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableSet(Table* table, ObjString* key, Value value);
```

#### 58. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableDelete(Table* table, ObjString* key);
```

#### 59. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
void tableAddAll(Table* from, Table* to);
```

#### 60. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
bool tableDelete(Table* table, ObjString* key) {
  if (table->count == 0) return false;

  // Find the entry.
  Entry* entry = findEntry(table->entries, table->capacity, key);
  if (entry->key == NULL) return false;

  // Place a tombstone in the entry.
  entry->key = NULL;
  entry->value = BOOL_VAL(true);
  return true;
}
```

#### 61. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
  for (;;) {
    Entry* entry = &entries[index];
```

#### 62. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
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
```

#### 63. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```


    index = (index + 1) % capacity;
```

#### 64. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
  uint32_t index = key->hash % capacity;
```

#### 65. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
  Entry* tombstone = NULL;

```

#### 66. 20 . 4 . 5 Deleting entries — [source](https://craftinginterpreters.com/hash-tables.html)
```
  for (;;) {
```

#### 67. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
  bool isNewKey = entry->key == NULL;
```

#### 68. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
  if (isNewKey && IS_NIL(entry->value)) table->count++;
```

#### 69. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```


  entry->key = key;
```

#### 70. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
  }

```

#### 71. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
  table->count = 0;
```

#### 72. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
  for (int i = 0; i < table->capacity; i++) {
```

#### 73. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
    dest->value = entry->value;
```

#### 74. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
    table->count++;
```

#### 75. 20 . 4 . 6 Counting tombstones — [source](https://craftinginterpreters.com/hash-tables.html)
```
  }
```

#### 76. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  Value* stackTop;
```

#### 77. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  Table strings;
```

#### 78. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  Obj* objects;
```

#### 79. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "chunk.h"
```

#### 80. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "table.h"
```

#### 81. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "value.h"
```

#### 82. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  vm.objects = NULL;
```

#### 83. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  initTable(&vm.strings);
```

#### 84. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
}
```

#### 85. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
void freeVM() {
```

#### 86. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  freeTable(&vm.strings);
```

#### 87. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  freeObjects();
```

#### 88. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  string->hash = hash;
```

#### 89. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  tableSet(&vm.strings, string, NIL_VAL);
```

#### 90. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  return string;
```

#### 91. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  uint32_t hash = hashString(chars, length);
```

#### 92. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  ObjString* interned = tableFindString(&vm.strings, chars, length,
                                        hash);
  if (interned != NULL) return interned;

```

#### 93. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  char* heapChars = ALLOCATE(char, length + 1);
```

#### 94. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  uint32_t hash = hashString(chars, length);
```

#### 95. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  ObjString* interned = tableFindString(&vm.strings, chars, length,
                                        hash);
  if (interned != NULL) {
    FREE_ARRAY(char, chars, length + 1);
    return interned;
  }

```

#### 96. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
  return allocateString(chars, length, hash);
```

#### 97. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "object.h"
```

#### 98. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "table.h"
```

#### 99. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```c
#include "value.h"
```

#### 100. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
void tableAddAll(Table* from, Table* to);
```

#### 101. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
ObjString* tableFindString(Table* table, const char* chars,
                           int length, uint32_t hash);
```

#### 102. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```


#endif
```

#### 103. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
ObjString* tableFindString(Table* table, const char* chars,
                           int length, uint32_t hash) {
  if (table->count == 0) return NULL;

  uint32_t index = hash % table->capacity;
  for (;;) {
    Entry* entry = &table->entries[index];
    if (entry->key == NULL) {
      // Stop if we find an empty non-tombstone entry.
      if (IS_NIL(entry->value)) return NULL;
    } else if (entry->key->length == length &&
        entry->key->hash == hash &&
        memcmp(entry->key->chars, chars, length) == 0) {
      // We found it.
      return entry->key;
    }

    index = (index + 1) % table->capacity;
  }
}
```

#### 104. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
    case VAL_NUMBER: return AS_NUMBER(a) == AS_NUMBER(b);
```

#### 105. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
    case VAL_OBJ:    return AS_OBJ(a) == AS_OBJ(b);
```

#### 106. 20 . 5 String Interning — [source](https://craftinginterpreters.com/hash-tables.html)
```
    default:         return false; // Unreachable.
```

