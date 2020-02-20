''' Задача 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n —
любое натуральное число.
 https://drive.google.com/file/d/1438WbHqqvjg82zNBQDGCbgvSSPM6Yi8X/view?usp=sharing'''

n = int(input('Введите n'))

n_1 = 0
for i in range(1, n+1):
   n_1 += i

n_2 = n * (n + 1) // 2

if n_1 == n_2:
   print('теорема доказана')
else:
   print('опять где-то накосячила')





