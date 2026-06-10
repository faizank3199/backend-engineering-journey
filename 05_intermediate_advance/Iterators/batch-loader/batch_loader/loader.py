class BatchLoader:
    """
    A simple iterator that yields data in batches.
    Useful for pagination, ML training loops, and large datasets.
    """

    def __init__(self, data, batch_size):
        if batch_size <= 0:
            raise ValueError("batch_size must be greater than 0")

        self.data = data
        self.batch_size = batch_size
        self.current = 0

    def __iter__(self):
        self.current = 0  # reset for reusability
        return self

    def __next__(self):
        if self.current >= len(self.data):
            raise StopIteration

        start = self.current
        end = self.current + self.batch_size

        batch = self.data[start:end]
        self.current = end

        return batch