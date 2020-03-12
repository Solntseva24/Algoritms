'''Задача 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
 принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
  алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
 улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо исключить/заменить
 команды print и input в анализируемом коде.'''
# 1   2    3     4    5    6    7    8    9    10
#  11     12     13    14     15    16

''' Спасибо за подсказку i = n * 20 -  я долго голову ломала, пробовала и удалять и добавлять элементы'''
import timeit
import cProfile

def sieve_func(n):
    m = n * 20
    sieve = [i for i in range(m)]
    sieve[1] = 0
    for i in range(2, m):
        if sieve[i] != 0:
            j = i + i
            while j < m:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    z = res[n-1]

    return f'Решето Эратосфена выглядит как - {sieve} \n Список натулальных чисел - {res}\n искомое простое число {z}'

print(sieve_func(15))

print(timeit.timeit('sieve_func(10)', number=100, globals=globals()))  # 0.009638389999999997
print(timeit.timeit('sieve_func(20)', number=100, globals=globals()))  # 0.020337765
print(timeit.timeit('sieve_func(30)', number=100, globals=globals()))  # 0.031107827999999997
print(timeit.timeit('sieve_func(40)', number=100, globals=globals()))  # 0.04133914100000001
print(timeit.timeit('sieve_func(100)', number=100, globals=globals()))  # 0.10834211700000002
print(timeit.timeit('sieve_func(200)', number=100, globals=globals()))  # 0.225556613
print(timeit.timeit('sieve_func(300)', number=100, globals=globals()))  # 0.34930912099999994

cProfile.run('sieve_func(10)')  #  1    0.000    0.000    0.000    0.000 les_4_task_2.py:30(sieve_func)
cProfile.run('sieve_func(20)')  # 1    0.000    0.000    0.000    0.000 les_4_task_2.py:30(sieve_func)
cProfile.run('sieve_func(100)')  #  1    0.001    0.001    0.001    0.001 les_4_task_2.py:30(sieve_func)
cProfile.run('sieve_func(200)')  #1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
cProfile.run('sieve_func(1000)') # 1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}


def prime_func(k):
    prime = []
    for i in range(2, k * 20):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    num = prime[k-1]

    return f'{prime},\n {num}'

print(prime_func(35))

print(timeit.timeit('prime_func(10)', number=100, globals=globals()))  # 0.037138799000000056
print(timeit.timeit('prime_func(20)', number=100, globals=globals()))  # 0.11511994000000003
print(timeit.timeit('prime_func(30)', number=100, globals=globals()))  # 0.24417836800000003
print(timeit.timeit('prime_func(40)', number=100, globals=globals()))  # 0.4147153320000001
print(timeit.timeit('prime_func(100)', number=100, globals=globals()))  # 2.4978933889999997
#print(timeit.timeit('prime_func(200)', number=100, globals=globals()))  # 9.364340635000001
#print(timeit.timeit('prime_func(300)', number=100, globals=globals()))  # 20.395588849000003

cProfile.run('prime_func(10)')  #1    0.000    0.000    0.000    0.000 les_4_task_2.py:63(prime_func)
cProfile.run('prime_func(20)') #    1    0.001    0.001    0.001    0.001 les_4_task_2.py:63(prime_func)
cProfile.run('prime_func(100)') #    1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
cProfile.run('prime_func(200)') #1    0.000    0.000    0.093    0.093 {built-in method builtins.exec}
cProfile.run('prime_func(1000)') # 1    0.000    0.000    2.040    2.040 {built-in method builtins.exec}

'''Вывод - с помощью решета Эратосфена решать быстрее. Сложность у него линейная. По результату работы профайлера видно,
 что основное время занимает построение диапазона - в зависимости от введенного n.
 Мое решение поиска простых чисел во второй задаче смахивает на первое, но работает дольше, за счет двойного перебора.
 По-другому не придумала, как решить. сложность квадратичная. последние проверки с timeit  закомментила, т.к. долго висят,
  результаты оставила. профайлер так же показывает, что большее время занимает построение диапазона, в зависимости от введенного
  аргумента'''