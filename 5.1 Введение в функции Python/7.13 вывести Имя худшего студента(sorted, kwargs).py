#Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов имена
# студентов и их номера в рейтинге (нагляднее в примере).
#Необходимо вернуть фамилию студента с минимальным номером по рейтингу.


def best_student(**kwargs):
    bad = sorted(kwargs.items(), key = lambda x: x[1])
    return bad[0][0]


print(best_student(Tom=12, Mike=3))
print(best_student(Tom=12))
print(best_student(Tom=12, Jerry=1, Jane=2))
# Mike
# Tom
# Jerry