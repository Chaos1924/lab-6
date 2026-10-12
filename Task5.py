def flatten(data):
    for item in data:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

data = [1, [2, 3], [4, [5, 6]], 7]
print("Розплющений список:", list(flatten(data)))  