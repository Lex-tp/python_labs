def generate_array(length):
    vector_temp = []
    if length > 0:
        print('Введите элементы вектора:')
        for i in range(1, length + 1):
            try:
                element: float = float(input(f'A[{i}] = '))
                vector_temp.append(element)
            except ValueError:
                print('Ошибка: Вектор может содержать только вещественные числа!')
                break
        return vector_temp
    else:
        print('Ошибка: Размерность массива не может быть меньше 1!')
        return vector_temp


def get_count_min(vector):
    min_el: float = vector[0]
    count: int = 0

    for i in vector:
        if min_el > i:
            min_el = i

    for i in vector:
        if min_el == i:
            count += 1
    return min_el, count


vector_a = []
n: int = 0

try:
    n = int(input('Введите размерность вещественного вектора: '))
except ValueError:
    print('Ошибка: Размерность вектора не является целым числом!')

vector_a = generate_array(n)

print('Вектора: ')
print(f'A={vector_a}')

result = get_count_min(vector_a)

print(f'Минимальное число ({result[0]}) встречается в вещественном векторе А: {result[1]} ')
