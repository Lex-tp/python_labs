template_set = set('abcdefghijklmnopqrstuvwxyz0123456789 ')

user_str = input('Введите строку: ')

is_success = not set(user_str.lower()).issubset(template_set)

print(f'Исходная строка: {user_str}')
print(f'Значение логической переменной: {is_success}')
