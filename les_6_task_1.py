'''Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
 Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.'''
# ох незнаю как на счет шикарного варианта... но как-то решила))

import random
import sys

def show(obj):
    res = sys.getsizeof(obj)
    print(f'type={type(obj)}, size={sys.getsizeof(obj)}, {obj}=')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                res_1 = show(key)
                res += res_1
                res_2 = show(value)
                res += res_2
        elif not isinstance(obj, str):
            for item in obj:
                res_3 = show(item)
                res += res_3

    return res

MIN_ITEM = -800
MAX_ITEM = -758

def max_min_item(SIZE):
    rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  #204

    max_i = MIN_ITEM
    min_i = MAX_ITEM
    sum_arr = 0
    for i in rand_arr:
        for b in rand_arr:
            if i >= b and i >= max_i:
                max_i = i
                max_ind_arr = rand_arr.index(i)
            if i < b and i <= min_i:
                min_i = i
                min_ind_arr = rand_arr.index(i)

    if max_ind_arr < min_ind_arr:
        for z in rand_arr[max_ind_arr + 1:min_ind_arr]:
            sum_arr += z
    else:
        for z in rand_arr[min_ind_arr + 1:max_ind_arr]:
            sum_arr += z
    # нашла информацию, что так можно собирать локальные переменные в кучу, надеюсь и правда можно))
    variable_1 = locals()
    return f'вариант 1 - {rand_arr}\n максимальное значение -  {max_i}, его индекс {max_ind_arr}\n минимальное значение {min_i},' \
           f' его индекс {min_ind_arr}\n сумма значений между ними -  {sum_arr}\n в памяти функция с указанными аргументами занимает {show(variable_1)} байт'

print(max_min_item(10)) #в памяти функция с указанными аргументами занимает 832 байт


#вариант 2.
def max_min_item_2(SIZE):
    rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    max_i = max(rand_arr)
    max_ind_arr = rand_arr.index(max_i)
    min_i = min(rand_arr)
    min_ind_arr = rand_arr.index(min_i)

    if max_ind_arr < min_ind_arr:
        sum_arr = sum(rand_arr[max_ind_arr + 1:min_ind_arr])
    else:
        sum_arr = sum(rand_arr[min_ind_arr + 1:max_ind_arr])
    variable_2 = locals()
    return f'вариант 2 - {rand_arr}\n максимальное значение -  {max_i}, его индекс {max_ind_arr}\n минимальное значение {min_i},' \
           f' его индекс {min_ind_arr}\n сумма значений между ними -  {sum_arr}\n' \
           f'в памяти функция с указанными аргументами занимает {show(variable_2)} байт'

print(max_min_item_2(10)) # в памяти функция с указанными аргументами занимает 752 байт



# вариант 3
def max_min_item_3(SIZE):
    rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    max_ind = 0
    min_ind = 0
    for i in range(len(rand_arr)):
        if rand_arr[i] > rand_arr[max_ind]:
            max_ind = i
        if rand_arr[i] < rand_arr[min_ind]:
            min_ind = i

    if max_ind < min_ind:
        sum_arr = sum(rand_arr[max_ind + 1:min_ind])
    else:
        sum_arr = sum(rand_arr[min_ind + 1:max_ind])

    variable_3 = locals()
    return f'вариант 3 - {rand_arr}\n максимальное значение -  {rand_arr[max_ind]}, его индекс {max_ind}\n' \
           f' минимальное значение {rand_arr[min_ind]}, его индекс {min_ind}\n сумма значений между ними -  {sum_arr}\n ' \
           f'в памяти функция с указанными аргументами занимает {show(variable_3)} байт'

print(max_min_item_3(10)) #в памяти функция с указанными аргументами занимает 696 байт

'''Вывод. Проанализировала 3 задачи, которые мы уже проверяли на скорость на 4 уроке, путем добавления переменной variable
 И если по скорости на моих значениях 
быстрее было решение №2, то по занимаемой памяти решение №3 выходит в лидеры, т.к. занимет меньше памяти. оно и понятно, 
нет моих "замечательных" вложенных циклов как впервой задаче, с постоянным обновлением переменных, и меньше переменных в сравнении
со второй задачей, обращение по индексу. Больше всего места занимает диапазон случайных чисел - оно и понятно, и переменные,
которые применяются в коде по несколько раз.
Версия Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32'''