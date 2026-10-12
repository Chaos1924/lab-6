def dict_to_tuples(d: dict) -> list[tuple]:
    return [(k, v) for k, v in d.items()]

def tuples_to_dict(pairs: list[tuple]) -> dict:
    res = {}
    for k, v in pairs:
        res[k] = v
    return res

d = {"cpu": 8, "ram": 32, "storage": 1024}
tuples = dict_to_tuples(d)
print("Словник -> кортежі:", tuples)
print("Кортежі -> словник (з перезаписом ram):", tuples_to_dict(tuples + [("ram", 64)]))