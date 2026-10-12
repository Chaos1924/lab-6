def filter_dict(d: dict[str, int], threshold: int) -> dict[str, int]:
    return {k: v for k, v in d.items() if v > threshold}

products = {"apple": 25, "banana": 40, "orange": 30, "kiwi": 55}
print("Товари дорожчі за 30:", filter_dict(products, 30))  