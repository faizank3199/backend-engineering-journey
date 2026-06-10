from batch_loader import BatchLoader

data = list(range(1, 51))

loader = BatchLoader(data, 10)

for batch in loader:
    print(batch)