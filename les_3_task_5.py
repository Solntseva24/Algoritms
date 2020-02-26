'''задача 5. В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве. Примечание к задаче:
  пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.'''

import random

SIZE = 10
MIN_ITEM = -20
MAX_ITEM = 10
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(arr)
max_i = MIN_ITEM
for i in arr:
    for z in arr:
        if i < 0 and i > z and i > max_i:
            max_i = i
            ind_arr = arr.index(i)

print('минимальное отрицательное число', max_i, 'его индекс', ind_arr)