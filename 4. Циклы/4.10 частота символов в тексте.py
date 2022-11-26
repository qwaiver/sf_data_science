#Попробуйте посчитать частоту каждого символа в следующем тексте:

text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""

text = text.lower()
text = text.replace(' ', '')
text = text.replace('\n', '')
count_dict = {}

for symbol in text:
    if symbol not in count_dict:
        count_dict[symbol] = 1
    else:
        count_dict[symbol] += 1

print(count_dict)