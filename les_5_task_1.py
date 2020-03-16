'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
 предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
  предприятий, чья прибыль выше среднего и ниже среднего.'''
#думаю не самая лучшая реализация))
from collections import Counter

enterprise_count = int(input('Введите количество предприятий'))
enterprises = []
for i in range(enterprise_count):
    name = input('введите название предприятия:')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('введите квартальные прибыли через пробел: ').split(' '))
    enterprise = {
        'name': name,
        'profit_year': profit_q1 + profit_q2 + profit_q3 + profit_q4
    }
    enterprises.append(enterprise)

print(enterprises)

c = Counter()
for d in enterprises:
    c.update(d)
middle = c['profit_year'] / enterprise_count
print(c)
print(middle)

for i in enterprises:
    above_m = []
    below_m = []
    if i['profit_year'] >= middle:
        name = i['name']
        profit_year = i['profit_year']
        above_middle = {
            'name': name,
            'profit_year': profit_year
        }
        above_m.append(above_middle)
        print(f'Прибыль выше среднего: {above_m}', sep='\n')

    if i['profit_year'] < middle:
        name = i['name']
        profit_year = i['profit_year']
        below_middle = {
            'name': name,
            'profit_year': profit_year
        }
        below_m.append(below_middle)
        print(f'Прибыль ниже среднего: {below_m}', sep='\n')

# Закомментировала то как помучила defaultdict
'''enterprise_count = int(input('Введите количество предприятий'))
enterprises = defaultdict(list)
for key, values in enterprises:
    if len(enterprises) <= enterprise_count:
        key = input('Введите название предприятия :')
        enterprises.append(key)
        if values < 4:
            values_app = input(f'введите прибыль за {values} квартал поочередно: ')
            enterprises[key].append(values_app)
print(enterprises)'''

'''enterprise_count = int(input('Введите количество предприятий'))
enterprises = []

for i in range(enterprise_count):
    name = input('введите название предприятия:')
    enterprise = {
        'name': name,
    }
    profit = defaultdict(list)
    for name, profit_q in enterprises:
        k = 0
        if k <= 4:
            profit_q = input(f'введите прибыль за {k} квартал поочередно: ')
            profit[name].append(profit_q)
            k += 1

enterprises.append(enterprise)

print(enterprises)'''







