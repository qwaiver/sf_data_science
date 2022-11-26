#Напишите генератор group_gen(n). Он должен при каждом вызове выдавать порядковый номер от 1 до n (включая n).
# После достижения n генератор должен снова возвращать номера, начиная с 1.


def group_gen(n):
    while True:
        for numb in range(1, n+1):
            yield numb

groups = group_gen(3)
for _ in range(10):
    print(next(groups))