def aggregate_pairs(pairs: list[tuple[str, int]]) -> dict[str, int]:
    res: dict[str, int] = {}
    for k, v in pairs:
        res[k] = res.get(k, 0) + v
    return res

pairs = [("apple", 3), ("banana", 5), ("apple", 2), ("orange", 4)]
print("Агрегація:", aggregate_pairs(pairs)) 