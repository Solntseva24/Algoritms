'''Задание1. Найти сумму и произведение цифр трехзначного числа,
 которое вводит пользователь.
  https://drive.google.com/file/d/1YlUtqLMn-ZPQXjRHXaQ0omqdbkv3rtnn/view?usp=sharing'''

abc = int(input('Введите целое трехзначное число: '))
a = int(abc / 100)
b = int((abc - (100*a)) / 10)
c = int(abc - (a*100) - (b * 10))

s = a + b + c
p = a * b * c

print('Сумма трехзначного числа равна: ', s, 'Произведение равно : ', p)

''' задание 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
https://drive.google.com/file/d/1YlUtqLMn-ZPQXjRHXaQ0omqdbkv3rtnn/view?usp=sharing'''

n = int(input('Введите номер буквы английского алфавита: '))

alphabet = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l = alphabet[n]
print(l)


'''Задание 8: Определить, является ли год, который ввел пользователь,
 високосным или не високосным.
 https://drive.google.com/file/d/1YlUtqLMn-ZPQXjRHXaQ0omqdbkv3rtnn/view?usp=sharing'''

year = int(input('Введите год: '))
if year % 4 != 0:
    print('не високосный год')
elif year % 100 == 0:
    if year % 400 != 0:
        print('не високосный год')
    else:
        print('високосный год')
else:
    print('високосный год')

'''Задание 9. Вводятся три разных числа. Найти,
 какое из них является средним (больше одного, но меньше другого).
 https://drive.google.com/file/d/1YlUtqLMn-ZPQXjRHXaQ0omqdbkv3rtnn/view?usp=sharing'''

print('Введите три разных целых числа')
d = int(input('Первое число: '))
e = int(input('Второе число: '))
f = int(input('Третье число: '))

if e < d < f or f < d < e:
    print('Среднее число равно ', d)
elif d < e < f or f < e < d:
    print('Среднее число равно ', e)
else:
    print('Среднее число равно ', f)



