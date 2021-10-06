def generate_array(length):
    vector_temp = []
    if length > 0:
        print('Введите элементы вектора:')
        for i in range(1, length + 1):
            try:
                element: int = int(input(f'A[{i}] = '))
                vector_temp.append(element)
            except ValueError:
                print('Ошибка: Вектор может содержать только целые числа!')
                break
        return vector_temp
    else:
        print('Ошибка: Размерность массива не может быть меньше 1!')
        return vector_temp


def filter_negative(element):
    return element < 0


def filter_positive(element):
    return element > 0


def merge_arrays(first_array, second_array):
    vector_temp = first_array + second_array
    return vector_temp


vector_a = []
n: int = 0

try:
    n = int(input('Введите размерность целочисленого вектора: '))
except ValueError:
    print('Ошибка: Размерность вектора не является целым числом!')

vector_a = generate_array(n)

print('Вектора: ')
print(f'A={vector_a}')

negative_numbers = list(filter(filter_negative, vector_a))
positive_numbers = list(filter(filter_positive, vector_a))

vector_b = merge_arrays(negative_numbers, positive_numbers)
print(f'B={vector_b}')


