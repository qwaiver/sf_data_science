# Напишите функцию def even_numbers_in_matrix(),
# которая получает на вход матрицу (список из списков)
# и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    x = 0
    for i in matrix:
        for j in i:
            if j % 2 == 0:
                x += 1
    return x
print(even_numbers_in_matrix(matrix_example))
