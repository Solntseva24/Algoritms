''' Задача 3. Сформировать из введенного числа обратное по порядку входящих
в него цифр и вывести на экран. Например, если введено число 3486,
 надо вывести 6843.
 https://drive.google.com/file/d/1438WbHqqvjg82zNBQDGCbgvSSPM6Yi8X/view?usp=sharing'''

z = int(input('Введите число: '))

def num(z):

    m = z % 10
    z = int(z / 10)

    if z > 0:
        return f'{m}{num(z)}'
    else:
        return f'{m}'

print(num(z))

