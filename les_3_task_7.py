'''Задача 7. В одномерном массиве целых чисел определить два наименьших элемента.
 Они могут быть как равны между собой (оба являться минимальными), так и различаться.
 хотела всавить функцию, но пока не сообразила, как ничего не нарушить'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

rand_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_ind_arr = 0
min_i = MAX_ITEM

for i in rand_arr:
    for b in rand_arr:
        if i < b and i <= min_i:
            min_i = i
            min_ind_arr = rand_arr.index(i)

print(rand_arr)
print(min_ind_arr)

#del rand_arr[min_ind_arr]
rand_arr.pop(min_ind_arr)
min_i_2 = MAX_ITEM
for k in rand_arr:
    for l in rand_arr:
        if k < l and k <= min_i_2:
            min_i_2 = k

print('два минимальных элемента', min_i, 'и', min_i_2)

