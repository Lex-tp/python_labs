user_string = input('Введите строку: ')

user_string = user_string.replace(',', '').replace('?', '').replace('!', '').lower()
list_words = user_string.split(' ')
len_max_word = len(max(list_words))

for element in list_words:
    if len(element) < len_max_word:
        list_words.pop(list_words.index(element))

print(f'Максимальное слова {list_words} встречается в тексте - {len(list_words)} раз(а)')

