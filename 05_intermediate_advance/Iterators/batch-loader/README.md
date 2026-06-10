# 🧩 Batch Loader

A lightweight Python iterator utility that efficiently splits large datasets into fixed-size batches.

Perfect for learning Python iterators and processing data in chunks without complex logic.

---

## 🚀 Features

* Simple and intuitive API
* Memory-efficient batch iteration
* Reusable iterator implementation
* Supports datasets of any size
* Demonstrates Python's Iterator Protocol
* Beginner-friendly codebase

---

## 📦 Installation

```bash
git clone https://github.com/faizank3199/batch-loader.git
cd batch-loader
```

---

## 🧑‍💻 Quick Start

```python
from batch_loader import BatchLoader

data = list(range(1, 51))

loader = BatchLoader(
    data=data,
    batch_size=10
)

for batch in loader:
    print(batch)
```

---

## 🧪 Example Output

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
[41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
```

---

## ⚙️ How It Works

The loader implements Python's iterator protocol:

* `__iter__()` returns the iterator object
* `__next__()` returns the next batch
* Raises `StopIteration` when all data has been processed

This allows seamless use inside `for` loops.

---

## 📌 Real-World Use Cases

### Backend Development

* API pagination
* Processing database records in chunks
* Bulk email processing

### Data Engineering

* ETL pipelines
* Log processing
* Data migration jobs

### Machine Learning

* Mini-batch training
* Dataset preprocessing
* Feature generation pipelines

---

## 🏗️ Concepts Demonstrated

* Classes & Objects
* Iterator Protocol (`__iter__`, `__next__`)
* Encapsulation
* Exception Handling (`StopIteration`)
* List Slicing
* Clean API Design

---

## 📂 Project Structure

```text
batch-loader/
│
├── batch_loader/
│   └── loader.py
│
├── examples/
│   └── demo.py
│
├── tests/
│   └── test_loader.py
│
├── README.md
└── LICENSE
```

---

## 🔥 Future Improvements

* Generator-based implementation
* Async batch processing
* CSV streaming support
* Database cursor support
* Django integration
* Custom iterable support

---

## ▶️ Run Demo

```bash
python examples/demo.py
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

Licensed under the MIT License.

---

## ⭐ Why This Project Matters

This project demonstrates a practical implementation of Python iterators and batch processing—concepts commonly used in backend systems, data pipelines, and large-scale applications.

It serves as an excellent beginner-to-intermediate portfolio project for aspiring Python Backend Developers.
