#Перепишите алгоритм из примера №3 так, чтобы он искал максимумы в строках таблицы random_matrix

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
max_rows = []

for row in random_matrix:
    max_value = row[0]
    for elem in row:
        if elem > max_value:
            max_value = elem
    max_rows.append(max_value)
print(f'Max values: {max_rows}')