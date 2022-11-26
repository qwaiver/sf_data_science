#Напишите функцию get_unique_words(), которая избавляется от знаков препинания в тексте и возвращает
#упорядоченный список (слова расположены по алфавиту) из уникальных (неповторяющихся) слов. Учтите, что слова,
#написанные в разных регистрах считаются одним и тем же словом.

punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. " \
               "This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, " \
               "then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, " \
               "Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. " \
               "Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. " \
               "Arrakis, the planet known as Dune, is forever his place."

def get_unique_words(text):
    for n in range(0, len(punctuation_list)):
        text = text.replace(punctuation_list[n], '')
    text = text.lower()
    list_text = list(text.split(' '))
    list_text.sort()
    new_list = list()
    for word in range(0, len(list_text)):
        if list_text[word] not in new_list:
            new_list.append(list_text[word])
    return new_list

print(get_unique_words(text_example))


