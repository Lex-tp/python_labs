vector_a = []
n: int = 0

try:
    n = int(input('Введите размерность целочисленого вектора: '))
except TypeError:
    print('Размерность должно быть число и больше 0!')

print('Введите элементы вектора:')

if n > 0:
    for i in range(1, n + 1):
        try:
            element: int = int(input(f'A[{i}] = '))
            vector_a.append(element)
        except TypeError:
            print('Введено не число!')

    print('Исходный массив: ')
    print(f'A={vector_a}')

    negative_numbers = list(filter(lambda el: el < 0, vector_a))
    positive_numbers = list(filter(lambda el: el > 0, vector_a))

    vector_b = negative_numbers + positive_numbers
    print(f'B={vector_b}')
else:
    print('Размерность массива не может быть меньше 1!')
