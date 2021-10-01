FILE_INPUT = 'input.txt'
FILE_OUTPUT = 'output.txt'

words_dict = {}

try:

    with open(FILE_INPUT, encoding='utf-8') as file_input:
        for line in file_input:
            words_list = line.split('-')
            word = words_list.pop(0).strip()
            for key in ''.join(words_list).split(','):
                key = key.strip()
                words = str(words_dict.get(key, False))
                unique_words = f'{words}, ' if words != 'False' else ''
                words_dict[key] = f'{unique_words}{word}'
    with open(FILE_OUTPUT, 'w', encoding='utf-8') as file_output:
        file_output.write(f'Количество английских слов: {len(words_dict)}\n\n')
        for key in sorted(words_dict):
            file_output.write(f'{key} - {words_dict[key]}\n')
    print(f'Программа сгенерировала файл c результатом - {FILE_OUTPUT}')
except Exception as ex:
    print(ex)
