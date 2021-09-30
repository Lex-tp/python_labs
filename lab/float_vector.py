vector_a = []
n: int = 0

try:
    n = int(input('Введите размерность вещественного вектора: '))
except ValueError:
    print('Ошибка: Размерность вектора не является целым числом!')

if n > 0:
    print('Введите элементы вектора:')
    for i in range(1, n + 1):
        try:
            element: float = float(input(f'A[{i}] = '))
            vector_a.append(element)
        except ValueError:
            print('Ошибка: Вектор может содержать только вещественные числа!')
            break

    print('Вектора: ')
    print(f'A={vector_a}')

    min_element: float = min(vector_a)
    countMin: int = vector_a.count(min_element)

    print(f'Минимальное число ({min_element}) встречается в вещественном векторе А: {countMin} ')
else:
    print('Ошибка: Размерность массива не может быть меньше 1!')
