''' 1 Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
 задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы
 проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
К 3 уроку Задача 6. В одномерном массиве найти сумму элементов, находящихся между
 минимальным и максимальным элементами. Сами минимальный и максимальный
  элементы в сумму не включать.
 '''
import random
import timeit
import cProfile

#вариант 1. Все свое прошлое решение сначала вставила в одну функцию(без функций решала).

MIN_ITEM = -800
MAX_ITEM = -758
def max_min_item(SIZE):
    rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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

    return f'вариант 1 - {rand_arr}\n максимальное значение -  {max_i}, его индекс {max_ind_arr}\n минимальное значение {min_i}, его индекс {min_ind_arr}\n сумма значений между ними -  {sum_arr}'


print(max_min_item(10))

print(timeit.timeit('max_min_item(10)', number=100, globals=globals()))  #0.0042756129999999976
print(timeit.timeit('max_min_item(20)', number=100, globals=globals()))  #0.011755294
print(timeit.timeit('max_min_item(30)', number=100, globals=globals()))  #0.020897456000000002
print(timeit.timeit('max_min_item(100)', number=100, globals=globals()))  #0.16855739599999997
#print(timeit.timeit('max_min_item(1000)', number=100, globals=globals()))  #14.162134067999999
#закомментировала последнюю, т.к. долго думает

cProfile.run('max_min_item(10)') #1    0.000    0.000    0.000    0.000 les_4.1.py:22(max_min_item)
cProfile.run('max_min_item(20)') #1    0.000    0.000    0.000    0.000 les_4.1.py:22(max_min_item)
cProfile.run('max_min_item(30)') #1    0.000    0.000    0.000    0.000 les_4.1.py:22(max_min_item)
cProfile.run('max_min_item(100)') #1    0.001    0.001    0.003    0.003 les_4.1.py:22(max_min_item)


#вариант 2. использовала sum() как вариант, раз можно теперь воспользоваться, вместо своих косячных вложенных циклов))
def max_min_item_2(SIZE):
    rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    max_i = max(rand_arr)
    max_ind_arr = rand_arr.index(max_i)
    min_i = min(rand_arr)
    min_ind_arr = rand_arr.index(min_i)

    if max_ind_arr < min_ind_arr:
        sum_arr = sum(rand_arr[max_ind_arr + 1:min_ind_arr])
    else:
        sum_arr= sum(rand_arr[min_ind_arr + 1:max_ind_arr])

    return f'вариант 2 - {rand_arr}\n максимальное значение -  {max_i}, его индекс {max_ind_arr}\n минимальное значение {min_i}, его индекс {min_ind_arr}\n сумма значений между ними -  {sum_arr}'


print(max_min_item_2(10))

print(timeit.timeit('max_min_item_2(10)', number=100, globals=globals()))  #0.002577786999999887
print(timeit.timeit('max_min_item_2(20)', number=100, globals=globals()))  #0.004567612999999859
print(timeit.timeit('max_min_item_2(30)', number=100, globals=globals()))  #0.00646924300000018
print(timeit.timeit('max_min_item_2(100)', number=100, globals=globals())) #0.020337239000000007
print(timeit.timeit('max_min_item_2(1000)', number=100, globals=globals()))  #0.20001440200000004
#print(timeit.timeit('max_min_item_2(10000)', number=100, globals=globals()))  #1.9584009660000001
#print(timeit.timeit('max_min_item_2(1000000)', number=100, globals=globals()))  #191.253307291
#закомментирую, т.к. последние 2 очень долго думают

cProfile.run('max_min_item_2(10)') # 1    0.000    0.000    0.000    0.000 les_4.1.py:63(max_min_item_2)
cProfile.run('max_min_item_2(20)') # 1    0.000    0.000    0.000    0.000 les_4.1.py:63(max_min_item_2)
cProfile.run('max_min_item_2(30)') # 1    0.000    0.000    0.000    0.000 les_4.1.py:63(max_min_item_2)
cProfile.run('max_min_item_2(100)') # 1    0.000    0.000    0.000    0.000 les_4.1.py:63(max_min_item_2)
cProfile.run('max_min_item_2(1000)') # 1    0.000    0.000    0.003    0.003 les_4.1.py:63(max_min_item_2)

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
        sum_arr= sum(rand_arr[min_ind + 1:max_ind])

    return f'вариант 3 - {rand_arr}\n максимальное значение -  {rand_arr[max_ind]}, его индекс {max_ind}\n минимальное значение {rand_arr[min_ind]}, его индекс {min_ind}\n сумма значений между ними -  {sum_arr}'

print(max_min_item_3(10))

print(timeit.timeit('max_min_item_3(10)', number=100, globals=globals()))  #0.002545746999999654
print(timeit.timeit('max_min_item_3(20)', number=100, globals=globals()))  #0.004713281999999985
print(timeit.timeit('max_min_item_3(30)', number=100, globals=globals()))  #0.006570319999980256
print(timeit.timeit('max_min_item_3(100)', number=100, globals=globals())) #0.02085154200000261
print(timeit.timeit('max_min_item_3(1000)', number=100, globals=globals()))  #0.2080348100000151
#print(timeit.timeit('max_min_item_3(10000)', number=100, globals=globals()))  #2.113552478999992
#print(timeit.timeit('max_min_item_3(1000000)', number=100, globals=globals()))  #210.97019490700004
#закомментирую, т.к. последние 2 очень долго думают

cProfile.run('max_min_item_3(10)')  #1    0.000    0.000    0.000    0.000 les_4.1.py:97(max_min_item_3)
cProfile.run('max_min_item_3(20)')  #1    0.000    0.000    0.000    0.000 les_4.1.py:97(max_min_item_3)
cProfile.run('max_min_item_3(30)')  #1    0.000    0.000    0.000    0.000 les_4.1.py:97(max_min_item_3)
cProfile.run('max_min_item_3(100)')  # 1    0.000    0.000    0.000    0.000 les_4.1.py:97(max_min_item_3)
cProfile.run('max_min_item_3(1000)')  #1    0.000    0.000    0.003    0.003 les_4.1.py:97(max_min_item_3)

'''Как выяснилось, мое решение 6 задачи, не только косячное в плане двух вложенных циклов, но и по времени довольно медленное,
по сравнению с двумя другими решениями и сложность у него квадратичная.
В двух других реализациях сложность линейная. Причем у второго скорость выполнения выше, правда когда я попыталась проверить 
на сумме 10000000, ответа не дождалась, так что возможно третье решение на больших данных возможно и будет лучше второго, но на моих
маленьких цифрах второе пока получилось быстрее.
Если сравнивать результаты cProfile на более больших диапазонах, время занимет random,
но в данном случае его никуда не вынесешь (имею ввиду за пределы функции, т.к.
анализированть я взялась как раз разные диапазоны случайных чисел'''