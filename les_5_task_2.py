'''Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
 представляется как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
  Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’,
  ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''
#асимптотика выйдет из моего решения та еще...но еще подумать уже не успеваю...
from collections import deque, Counter

first_num = deque(input('Введите первое шестнадцатиричное число: '))
second_num = deque(input('Введите второе шестнадцатиричное число: '))

print(first_num, second_num) #для удобства просмотра и проверки

#простите мне это безобразие, но у меня сдают нервы...)) совсем уже нет времени...можно ли иначе добавить appendleft
#несколько раз подряд?
if len(first_num) > len(second_num):  # Приравниваем длину чисел
    q = (len(first_num) - len(second_num))
    for i in range(q):
        second_num.appendleft('0')
else:
    q = (len(first_num) - len(second_num))
    for i in range(q):
        first_num.appendleft('0')

first_num.reverse()
second_num.reverse()

print(first_num, second_num) #для удобства просмотра и проверки

first_num = list(first_num)
second_num = list(second_num)

sum_num = deque([])
w = 0
for i, elem in enumerate(first_num):
    list_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    list_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    x = list_16.index(elem)
    elem = list_10[x]
    for k, ele in enumerate(second_num):
        m = list_16.index(ele)
        ele = list_10[m]
        per = int(elem + ele + w)
        w = 0
        if per < 16:
            per = list_16[per]
            sum_num.appendleft(per)
            second_num.pop(k)
            break
        else:
            per = per - 16
            per = list_16[per]
            w += 1
            sum_num.appendleft(per)
            second_num.pop(k)
            break

if w != 0:
    sum_num.appendleft(w)

sum_num = Counter(sum_num)

print(''.join(list(sum_num.elements())))

