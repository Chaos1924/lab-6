class SkipIterator:
    def __init__(self, data: list, step: int = 1):
        if step <= 0:
            raise ValueError("step must be positive")
        self.data = data
        self.step = step
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration
        val = self.data[self.idx]
        self.idx += self.step
        return val

it = SkipIterator([10, 20, 30, 40, 50], step=2)
print("Результат:", list(it))  