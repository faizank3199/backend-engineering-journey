# Batch Loader 🧩

A simple Python iterator utility to split data into batches.

## 🚀 Features

- Easy batching of lists
- Memory efficient iteration
- Reusable iterator
- Clean and simple API

## 📦 Installation

```bash
git clone https://github.com/faizank3199/batch-loader.git 

🧑‍💻 Usage
from batch_loader import BatchLoader

data = list(range(1, 51))

loader = BatchLoader(data, 10)

for batch in loader:
    print(batch)

🧪 Example Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
[41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

📌 Use Cases
Pagination systems in web apps
Machine learning batch training
API response chunking
Processing large datasets efficiently
Log processing in chunks
ETL pipelines (Extract, Transform, Load)

⭐ Why this project is useful
Real-world iterator pattern
Helps understand Python iterators & generators
Useful in backend development
Useful in ML/data processing
Great for GitHub portfolio & interviews

🔥 Future Improvements (optional)
Generator-based BatchLoader (more memory efficient)
Async BatchLoader for APIs
File/CSV batch processing
Django pagination integration

---
## ▶️ How to Run

Follow these steps:

1. Clone the repo
2. Go into folder
3. Run `examples/demo.py`