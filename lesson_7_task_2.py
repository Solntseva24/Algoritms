''' Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.'''

''' тут пришлось поломать голову, принцип действия я поняла - нужно сначала разделить на две половины, а затем на группы,
чтоб потом сравнивая в группах, а затем в половинах соединить поочередно в один массив. Оставлю закомментированный код 
своих попыток, две функции я сделала не сразу... прилично запуталась. потом наткнулась на хабре на инфу про слияние Боуза Нельсона
 - он то мне и помог... могу поделиться с ним оценкой))'''
'''но потом я решила, что у Боуза можно запутаться в переменных, и еще почитала и подумала - 3й вариант мне самой более 
понятен'''
import random
#import numpy
#import math

MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 10
array = [(random.uniform(MIN_ITEM, (MAX_ITEM - 0.00000000000001))) for _ in range(SIZE)]
#array = numpy.around(array, decimals=2) #я numpy в pycharm добавила, не поняла почему округляет без запятых - результат портит
print(array)

#вариант 3
def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    leftar = merge_sort(array[:mid])
    rightar = merge_sort(array[mid:])

    return merger(leftar, rightar)

def merger(leftar, rightar):
    res = []
    while len(leftar) > 0 and len(rightar) > 0:
        if leftar[0] <= rightar[0]:
            res.append(leftar[0])
            leftar = leftar[1:]
        else:
            res.append(rightar[0])
            rightar = rightar[1:]

    # если что-то осталось - добавить к результату
    if len(leftar) > 0:
        res += leftar
    if len(rightar) > 0:
        res += rightar
    return res

print(merge_sort(array))

#вариант 2 слияние Боуза Нельсона
'''def merge_sort(array):
    m = 1
    while m < len(array):
        j = 0
        while j + m < len(array):
            merge(j, m, m)
            j = j + m + m
        m = m + m
    return array

def merge(j, r, m):
    if j + r < len(array):
        if m == 1:
            if array[j] > array[j + r]:
                array[j], array[j + r] = array[j + r], array[j]
        else:
            m = m // 2
            merge(j, r, m)
            if j + r + m < len(array):
                merge(j + m, r, m)
            merge(j + m, r - m, m)
    return array

print(merge_sort(array))'''

#вариант 1
'''def merge_sort(array):
    print(array)
    if len(array) < 2:
        return array
    if len(array) > 1:
        mid = len(array) // 2
        leftar = array[:mid]
        rightar = array[mid:]
        print(f'Левая{leftar}')
        print(f'правая {rightar}')

        leftar = merge_sort(leftar)
        rightar = merge_sort(rightar)
    #while len(leftar) + len(rightar) != len(array):
        #array_res = merger(leftar, rightar)
    return array

def merger(leftar, rightar):
    res = []
    i = 0
    j = 0
        #k = 0
    while i < len(leftar) and j < len(rightar):
        if leftar[i] <= rightar[j]:
            res.append(leftar[i])
            i += 1
        else:
            res.append(rightar[j])
            j += 1
            #k += 1

        #while i < len(leftar):
        #    array[k] = leftar[i]
        #    i += 1
        #    k += 1

        #while i < len(rightar):
        #    array[k] = rightar[j]
        #    j += 1
        #    k += 1
    res += leftar[i:]
    res += rightar[:j]
    return res

print(merge_sort(array))'''

