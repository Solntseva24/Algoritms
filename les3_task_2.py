'''Задача 2. Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить
  значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого
   массива стоят четные числа.'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

arr_1 = []
count_arr = -1
for i in arr:
    count_arr += 1
    if i % 2 == 0:
        arr_1.append(count_arr)


print(arr_1)
