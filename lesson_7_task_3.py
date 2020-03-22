'''Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой —
не больше медианы. Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
 используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).'''
import random

MIN_ITEM = 0
MAX_ITEM = 10
SIZE = 4
array = [random.randint(MIN_ITEM, (MAX_ITEM)) for _ in range((2*SIZE) + 1)]
print(array)

n = int(len(array) // 2)
#print(n)

#вариант без сортировки - то до чего додумалась, найти первую половину минимальных значений, и следующее минимальное после
#первой половины будет как раз медианой
def func(array):
    array = array.copy()

    while len(array) > (n + 1):
        k = min(array)
        k = array.index(k)
        array.pop(k)
    mid = min(array)
    return f'медиана, найденная без сортировки {mid}'

print(func(array))

#вариант 2. с сортировкой у меня получилось быстрее)) взяла гномью
def func_gnome(array):
    i = 1
    while i < len(array):
        if not i or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

print(func_gnome(array))
mid_2 = array[n]
print(f'медиана, найденная после сортировки {mid_2}')