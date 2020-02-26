'''Задача4. Определить, какое число в массиве встречается чаще всего.
еще один велосипед,
 стыдно, но только на этой задаче  научилась худо-бедно пользоваться дебагером...))'''
import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 8

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = 0
max_num = 0
count_num = 0
for i in array:
    count_num = 0
    for k in array:
        if i == k:
            count_num += 1
        if count_num > max_num:
            num = i
            max_num = count_num



print('чаще всего встречается ', num, 'в количестве ', max_num)
