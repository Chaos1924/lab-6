class KeyFilterIterator:
    def __init__(self, d: dict, allowed_keys):
        self.d = d
        self.allowed = set(allowed_keys)
        self._gen = ((k, self.d[k]) for k in self.d if k in self.allowed)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._gen)

d = {"a": 1, "b": 2, "c": 3, "d": 4}
allowed = {"b", "c", "x"}
print("Пари:", list(KeyFilterIterator(d, allowed)))  