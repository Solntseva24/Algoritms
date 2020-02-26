'''Задача 6. В одномерном массиве найти сумму элементов, находящихся между
 минимальным и максимальным элементами. Сами минимальный и максимальный
  элементы в сумму не включать.
  еле решила, вроде работает, но прямо чувствую как хорошо у меня налажено
   производство пятиколесных...'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_i = 0
min_i = MAX_ITEM
for i in rand_arr:
    for b in rand_arr:
        if i >= b and i >= max_i:
            max_i = i
            max_ind_arr = rand_arr.index(i)
        if i < b and i <= min_i:
            min_i = i
            min_ind_arr = rand_arr.index(i)

print(rand_arr)
print('максимальное число', max_i)
print('минимальное число', min_i)
print('индекс максимального числа', max_ind_arr)
print('индекс минимального числа', min_ind_arr)

sum_arr = 0
if max_ind_arr < min_ind_arr:
    for z in rand_arr[max_ind_arr+1:min_ind_arr]:
        sum_arr += z
else:
    for z in rand_arr[min_ind_arr+1:max_ind_arr]:
        sum_arr += z
print(sum_arr)