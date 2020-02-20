'''  Задача 2.  Посчитать четные и нечетные цифры
 введенного натурального числа. Например, если введено число 34560, в нем 3 четные
  цифры (4, 6 и 0) и 2 нечетные (3 и 5)..
  https://drive.google.com/file/d/1438WbHqqvjg82zNBQDGCbgvSSPM6Yi8X/view?usp=sharing'''


x = int(input('Введите число'))

ev = 0
od = 0

while x > 0:
    if x % 2 == 0:
        ev += 1
    else:
        od += 1
    x = int(x / 10)

print('четных чисел', ev, 'нечетных чисел', od)
