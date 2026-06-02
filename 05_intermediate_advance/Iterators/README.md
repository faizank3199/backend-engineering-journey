# 🔁 Python Iterators

A beginner-to-intermediate Python project that demonstrates how iterators work internally and how to build custom iterators from scratch using the iterator protocol.

---

## 📚 What Are Iterators?

An iterator is an object that:

- Stores its current state
- Produces values one at a time
- Remembers where it stopped
- Implements the iterator protocol

### Iterator Protocol

Every iterator must implement:

```python
__iter__()
__next__()
```

- `__iter__()` → Returns the iterator object itself
- `__next__()` → Returns the next value or raises `StopIteration`

---

## 🎯 Learning Goals

This project helps you understand:

- Iterables vs Iterators
- How `for` loops work internally
- The iterator protocol
- Custom iterator implementation
- Lazy evaluation concepts
- Memory-efficient data processing
- Backend-related iterator patterns

---

## 📂 Project Structure

```text
Iterators/
│
├── iterators.py
└── README.md
```

---

## 🚀 Topics Covered

### 1. Simple Iterator

Learn how built-in iterables become iterators using `iter()`.

```python
numbers = [120, 343, 232]

iterator = iter(numbers)
```

---

### 2. Custom Counter Iterator

Counts from `1` to a specified limit.

Example:

```text
1
2
3
4
5
...
```

---

### 3. Reverse Counter Iterator

Counts backwards.

Example:

```text
5
4
3
2
1
```

---

### 4. Even Number Iterator

Generates even numbers up to a given limit.

Example:

```text
2
4
6
8
10
```

---

### 5. Configurable Even Range Iterator

Generates even numbers between a start value and limit.

Example:

```text
2
4
6
8
10
12
14
16
18
20
```

---

### 6. Reverse String Iterator

Iterates through a string in reverse order.

Example:

```text
hello

Output:
o
l
l
e
h
```

---

### 7. Infinite Iterator

Generates numbers indefinitely until manually stopped.

Example:

```text
1
2
3
4
5
...
```

---

## ▶️ Running The Project

Run the file:

```bash
python iterators.py
```

---

## 🖥️ Sample Output

```text
=== Simple Iterator ===
120
343
232

=== Counter Iterator ===
1
2
3
4
5
6
7
8
9
10

=== Reverse Counter Iterator ===
5
4
3
2
1

=== Even Number Iterator ===
2
4
6
8
10

=== Reverse String Iterator ===
o
l
l
e
h
```

---

## 🧠 Backend Engineering Concepts

This project introduces several concepts commonly used in backend development:

### Lazy Evaluation

Values are produced only when requested.

```python
next(iterator)
```

---

### State Management

Iterators remember their current position.

```python
self.current
```

---

### Memory Efficiency

Instead of loading everything into memory at once, iterators generate values one at a time.

Useful for:

- Large files
- Database records
- API pagination
- Streaming systems

---

### Data Streaming

Iterators simulate how backend systems process data streams.

Examples:

- Log processing
- Database cursors
- Pagination
- Event streaming

---

## 🔥 Key Takeaways

After completing this project, you should understand:

✅ How iterators work internally

✅ How Python's `for` loop uses iterators

✅ The difference between iterables and iterators

✅ How to build custom iterators

✅ How state is maintained between iterations

✅ Why iterators are memory efficient

✅ Real-world backend use cases of iterators

---

## 📖 Author

**Mohammad Faizan**

Aspiring Python Backend Developer

---

## 🎯 Next Step

After mastering iterators, continue with:

1. Generators
2. Generator Expressions
3. `yield from`
4. Context Managers
5. File Streaming
6. Flask / FastAPI

These topics build the foundation of modern Python backend development.