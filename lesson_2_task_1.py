'''пожалуйста придирайтесь!)) и я буду рада справедливым (не завышенным) оценкам (вдруг жалко станет)) ),
 для понимания уровня своей безнадежности ))
 хотелось бы сделать больше задач, но слишкрм долго я сними вожусь и только вечером...
 Задача 1.  Написать программу, которая будет складывать, вычитать, умножать или делить
 два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа
 не завершается, а запрашивает новые данные для вычислений. Завершение программы должно
 выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
 знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак
 операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел
  его в качестве делителя.
  https://drive.google.com/file/d/1438WbHqqvjg82zNBQDGCbgvSSPM6Yi8X/view?usp=sharing'''

while True:
    print('Введите 2 числа')

    while True:
        e = int(input("Первое число"))
        f = int(input("Второе число"))
        if f == 0:
            print('на 0 делить нельзя')
        else:
            break
    k = input("Введите действие '+', '-', '/', '*'. Для выхода нажмите '0'")
    if k != '0':
        if k == '+':
            sum = e + f
            print(sum)
        elif k == '-':
            sb = e - f
            print(sb)
        elif k == '/':
            div = e / f
            print(div)
        elif k == '*':
            pr = e * f
            print(pr)
        else:
           print('Введен неверный символ, попробуйте еще раз')
    else:
        print('выход выполнен')
        break

