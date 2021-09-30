vector_a = []
n: int = 0

try:
    n = int(input('Введите размерность целочисленого вектора: '))
except ValueError:
    print('Ошибка: Размерность вектора не является целым числом!')

if n > 0:
    print('Введите элементы вектора:')
    for i in range(1, n + 1):
        try:
            element: int = int(input(f'A[{i}] = '))
            vector_a.append(element)
        except ValueError:
            print('Ошибка: Вектор может содержать только целые числа!')
            break

    print('Вектора: ')
    print(f'A={vector_a}')

    negative_numbers = list(filter(lambda el: el < 0, vector_a))
    positive_numbers = list(filter(lambda el: el > 0, vector_a))

    vector_b = negative_numbers + positive_numbers
    print(f'B={vector_b}')
else:
    print('Ошибка: Размерность массива не может быть меньше 1!')
