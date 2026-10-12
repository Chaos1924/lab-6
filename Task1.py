def even_in_range(start: int, end: int):
    cur = start if start % 2 == 0 else start + 1
    while cur <= end:
        yield cur
        cur += 2

print("Цикл for:")
for x in even_in_range(3, 11):
    print(x, end=" ")
print("\nlist():", list(even_in_range(10, 20)))
print("Від'ємний діапазон:", list(even_in_range(-5, 3)))