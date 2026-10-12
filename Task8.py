def name_score_pairs(names: list[str], scores: dict[str, int]):
    """
    Генерує кортежі (name, score).
    Якщо ім'я відсутнє у scores, повертає (name, None).
    """
    for name in names:
        yield (name, scores.get(name, None))

names = ["Іван", "Ольга", "Богдан", "Дмитро"]
scores = {"Іван": 90, "Ольга": 85, "Богдан": 78}
for n, sc in name_score_pairs(names, scores):
    print(f"{n}: {sc}")