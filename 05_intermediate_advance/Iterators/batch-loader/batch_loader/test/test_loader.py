from batch_loader import BatchLoader

def test_batch_loader():
    data = list(range(1, 11))
    loader = BatchLoader(data, 3)

    batches = list(loader)

    assert batches == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10]
    ]