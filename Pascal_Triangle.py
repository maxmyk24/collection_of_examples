N = int(input("Введіть кількість рівнів трикутника: "))
P = []

# Обчислення елементів трикутника Паскаля
for i in range(N):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)

# Виведення трикутника Паскаля з відступами
max_val = P[-1][len(P[-1]) // 2]
max_len = len(str(max_val))

for row in P:
    # Визначення відступу для кожного рядка
    indent = (N - len(row)) * (max_len + 1) // 2
    # Форматування та виведення рядка
    print(" " * indent + " ".join(["{0:>{1}}".format(val, max_len) for val in row]))
