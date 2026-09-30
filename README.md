# Variable Memory Allocation and Deallocation

This README explains how variables use memory in Python and Node.js, how memory is allocated, and when it is released.

## 1. What is a variable?
A variable is a name that stores a value in memory. The variable does not hold the data directly in all languages; instead, it points to a memory location where the value is stored.

### Example in Python
```python
price = 100
name = "Laptop"
```

Here:
- `price` stores the integer value `100`
- `name` stores the string value `"Laptop"`
- Python keeps track of where these values are stored in memory

### Example in Node.js
```javascript
let price = 100;
let name = "Laptop";
```

In JavaScript (Node.js), variables also point to memory locations, but the exact allocation behavior is managed by the JavaScript engine (V8).

---

## 2. How is memory associated with variables?
Memory is divided into different regions depending on the language and runtime:

- Stack memory: used for simple values and function execution
- Heap memory: used for objects, arrays, large structures, and dynamic data
- Variables keep references to values stored in memory

### Example in Python
```python
x = 10
y = [1, 2, 3]
```

- `x` is a simple integer value
- `y` is a list stored in heap memory
- `y` is referenced by variable `y`

### Example in Node.js
```javascript
let count = 10;          // primitive value
let student = { name: "Asha" }; // object stored in heap
```

- `count` is a primitive value
- `student` points to an object created in heap memory
---


## 3. How long does variable memory stay valid?
The validity or lifetime of a variable depends on its scope and the runtime memory management rules.

### Python lifetime
A variable exists as long as there is a reference to it.

```python
x = 5
print(x)   # x is alive
```

When there are no references left, Python deallocates the memory automatically.

```python
x = [1, 2, 3]
del x
# memory for the list is released when no references remain
```

### Node.js lifetime
In JavaScript, variables live as long as their scope is active.

```javascript
function demo() {
  let value = 20;
  return value;
}

console.log(demo());
// value is no longer accessible after the function ends
```

The memory is then eligible for garbage collection by the engine.

---

## 4. How does memory allocation work in Python?
Python uses dynamic memory allocation. It allocates memory based on the type and size of the value.

### Example
```python
num = 42
name = "Alice"
items = [10, 20, 30]
```

- `42` is stored as an integer object
- `"Alice"` is stored as a string object
- `[10, 20, 30]` is stored as a list object in heap memory

### Reference counting
Python keeps track of how many references a value has.

```python
a = [1, 2, 3]
b = a
```

Here, both `a` and `b` refer to the same list object. When references are removed, memory is cleaned up automatically.

```python
x = [1, 2, 3]
del x
# object is removed when no references remain
```

### Cyclic garbage collection
Python also handles circular references, where objects refer to each other.

```python
a = []
b = []
a.append(b)
b.append(a)

del a, b
# Python garbage collector later removes unreachable cyclic objects
```

This is important because reference counting alone may not clean circular structures.

---

## 5. How does memory allocation work in Node.js?
Node.js runs JavaScript using the V8 engine. V8 manages memory automatically using a garbage collector.

### Example
```javascript
let name = "Rahul";
let person = { firstName: "Rahul", age: 25 };
```

- `name` is a string value
- `person` is an object stored in heap memory
- `person` is referenced by the variable `person`

### Garbage collection in Node.js
When an object is no longer used, it becomes unreachable and is collected by the garbage collector.

```javascript
let user = { id: 1, name: "Aman" };
user = null; // no reference remains, memory can be reused
```

This means the object is no longer accessible and the engine can free the memory later.

---

## 6. Deallocation and memory cleanup
Memory deallocation means releasing the memory used by data when it is no longer needed.

### Python
```python
items = [1, 2, 3]
items = None
```

Now the old list is no longer referenced, so Python can free that memory.

### Node.js
```javascript
let arr = [1, 2, 3];
arr = null;
```

The original array becomes unreachable and can be freed by the garbage collector.

---

## 7. Scope and lifetime
The lifetime of a variable usually depends on its scope.

### Python example
```python
def show():
    value = 99
    return value

print(show())
# value exists only inside the function call
```

### Node.js example
```javascript
function show() {
  let value = 99;
  return value;
}

console.log(show());
// value is released after the function completes
```

---

## 8. Summary
- Variables store references to memory locations.
- Python uses dynamic memory allocation and automatic deallocation.
- Node.js uses V8's heap and garbage collection.
- Memory is freed when variables go out of scope or no longer have references.
- The life of a variable depends on scope, references, and runtime memory management.

## 9. Short comparison

| Topic | Python | Node.js (JavaScript) |
|---|---|---|
| Memory model | Dynamic + heap allocation | V8 heap + stack for execution |
| Deallocation | Reference counting + cyclic GC | Garbage collector |
| Example | `x = [1,2,3]` | `let x = [1,2,3]` |
| Memory release | When no references remain | When unreachable by GC |

---

## 10. Final note
Understanding memory allocation helps in writing efficient and bug-free code. Variables are not just names; they are connections to memory that must be managed safely by the language runtime.

This project is useful for learning the relationship between variables, memory, and lifetime in both Python and Node.js.
