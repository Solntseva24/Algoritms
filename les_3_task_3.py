'''задача3. В массиве случайных целых чисел поменять местами минимальный
 и максимальный элементы.
 не скажу сколько это займет памяти... зато "вручную" '''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

#count_arr = -1

max_i = 0
min_i = MAX_ITEM
for i in rand_arr:
    #count_arr += 1
    for b in rand_arr:
        if i >= b and i >= max_i:
            max_i = i
            max_ind_arr = rand_arr.index(i)
            #max_ind_arr = count_arr
        if i < b and i <= min_i:
            min_i = i
            min_ind_arr = rand_arr.index(i)
            #min_ind_arr = count_arr

print(rand_arr)
print('максимальное число', max_i)
print('минимальное число', min_i)
print('индекс максимального числа', max_ind_arr)
print('индекс минимального числа', min_ind_arr)

rand_arr[max_ind_arr] = min_i
rand_arr[min_ind_arr] = max_i

print('если поменять местами', rand_arr)