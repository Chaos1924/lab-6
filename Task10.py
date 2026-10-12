def running_stats(numbers: list[float]):
    cnt = 0
    total = 0.0
    for x in numbers:
        cnt += 1
        total += x
        yield (cnt, total, total / cnt)

vals = [10, 20, 30]
for stat in running_stats(vals):
    print(f"Кількість: {stat[0]}, Сума: {stat[1]}, Середнє: {stat[2]}")