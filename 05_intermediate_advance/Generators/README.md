# Python Generators 

A complete guide to Python Generators, covering fundamentals, advanced concepts, real-world examples, and backend-oriented mini projects.

This repository was built as part of my journey toward becoming a Python Backend Developer.

---

## 📚 Topics Covered

### 1. Basic Generator

Learn how generators pause execution using `yield`.

### 2. Generator Exhaustion

Understand why generators can only be consumed once.

### 3. `next()` vs `for` Loop

Different ways to iterate through generators.

### 4. State Persistence

See how generators remember where they stopped.

### 5. `yield` vs `return`

Understand the core difference between generators and regular functions.

### 6. `send()` Method

Pass values back into a generator.

### 7. Infinite Generators

Generate unlimited sequences efficiently.

### 8. Generator Calculator

Interactive generator example using `send()`.

### 9. `yield from`

Combine multiple generators cleanly.

### 10. Generator Expressions

Memory-efficient alternative to list comprehensions.

### 11. Memory Optimization

Compare memory usage between lists and generators.

### 12. Generator Pipelines

Chain multiple generators together.

### 13. Log Aggregation Project

Combine logs from multiple services using generators.

### 14. File Streaming Project

Process large files efficiently without loading everything into memory.

---

## 📁 Project Structure

```text
Generators/
│
├── generators.py
│
└── log_file_reader_project/
    ├── logs.txt
    └── log_reader.py
```

---

## ⚡ Why Generators?

Generators are useful when working with:

* Large files
* API responses
* Database records
* Data pipelines
* Streaming systems
* Background workers
* Memory-sensitive applications

Instead of loading everything into memory, generators produce values only when needed.

---

## 🔥 Example

```python
def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
```

Output:

```text
1
2
3
```

---

## 🧠 Generator Lifecycle

```text
Create Generator
        │
        ▼
Call next()
        │
        ▼
Run Until yield
        │
        ▼
Pause Execution
        │
        ▼
Store State
        │
        ▼
Resume On Next Call
```

---

## 💾 Memory Comparison

### List

```python
nums = [x for x in range(100000)]
```

* Stores all values immediately
* Higher memory consumption

### Generator

```python
nums = (x for x in range(100000))
```

* Produces values on demand
* Extremely memory efficient

---

## 🏗 Backend Use Cases

### File Processing

```python
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line
```

### Database Records

```python
def fetch_users(cursor):
    for user in cursor:
        yield user
```

### API Pagination

```python
def paginate():
    page = 1

    while page <= 5:
        yield page
        page += 1
```

### Log Streaming

```python
def service_logs():
    yield from auth_logs()
    yield from database_logs()
    yield from payment_logs()
```

---

## 🚀 Running The Project

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Generators
```

Run:

```bash
python generators.py
```

---

## 🎯 Skills Learned

* Iterators
* Generators
* Lazy Evaluation
* Memory Optimization
* Infinite Sequences
* Yield Delegation
* Generator Expressions
* Data Streaming
* File Processing
* Backend Data Pipelines



## 👨‍💻 Author

**Mohammad Faizan**

Currently learning:

* Python
* SQL
* Flask
* Django
* SQLAlchemy
* Data Structures & Algorithms

---

## ⭐ If you found this useful

Give the repository a star and follow my backend development journey.
