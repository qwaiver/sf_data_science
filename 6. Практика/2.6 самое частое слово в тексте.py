# Модифицируем предыдущую задачу(2.5).
# Теперь необходимо написать функцию get_most_frequent_word, которое возвращает самое часто встречающееся слово в тексте.



text_example = "A beginning is the time for taking the most delicate care that the balances are correct. " \
               "This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, " \
               "then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, " \
               "Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. " \
               "Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. " \
               "Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    text = text.lower()
    text = text.split(' ')
    word_dict = {}
    for word in text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    max_word = max(word_dict, key=word_dict.get)
    return max_word

print(get_most_frequent_word(text_example))