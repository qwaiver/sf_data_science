# Подсчитайте количество вхождений символа 't' в каждую из строк этого списка.
# Для подсчёта используйте словарь word_dict: в качестве ключа запишите в него строку,
# в качестве значения — число вхождений буквы 't' в эту строку.
# В результате работы вашей программы в переменной word_dict должен храниться результирующий словарь.

str_list = ["text", "morning", "notepad", "television", "ornament"]  # заданный список слов
symbol_to_check = "t"  # задаём символ, который будем искать
words_dict = {}  # задаём пустой словарь для подсчёта

# ваш код здесь
for word in str_list:
    words_dict[word] = 0
    for symbol in word:
        if symbol == symbol_to_check:
            words_dict[word] += 1
print(words_dict)