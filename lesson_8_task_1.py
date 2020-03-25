'''1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
 Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")'''

''' я уже представила как Вы зажмуриваетесь, глядя на мое дз... често, было сложно, но я пыталась... я понимаю, что это много времени и 
памяти - просто даже незнаю, что еще придумать(((( как думаете, из меня может получится нормальный специалист? ребята в чате хорошо
решают
в любом случае курс мне много дал и понравился,спасибо!)) понимаю намного больше чем мой 0, хоть и решаю как сапожник..
вторую задачку порешаю потом для себя, боюсь от html отстать'''

import hashlib

def my_func(animals):
    len_anim = len(animals)
    count_ = 0
    size_for_letter_ahead = 1

    for i in range(len(animals)):
        for j in range(len(animals)):
            if i == j and hashlib.sha1(animals[i].encode('utf-8')).hexdigest() == hashlib.sha1(animals[j].encode('utf-8')).hexdigest():
                count_ += 1                                                    # когда i и j  совпадают, считаю отдельные буквы

            while size_for_letter_ahead < len_anim - 1:                        # цикл работает только с первой буквой
                if hashlib.sha1(animals[i:i + size_for_letter_ahead].encode('utf-8')).hexdigest() == hashlib.sha1(
                    animals[j:j + size_for_letter_ahead].encode('utf-8')).hexdigest():
                    count_ += 1
                    size_for_letter_ahead += 1
            if i != 0 and i == j:                                              #далее до конца считаю подстроки, уменьшая каждый раз на i
                size = 1
                while size < (len_anim - i):
                    if hashlib.sha1(animals[i:i + size].encode('utf-8')).hexdigest() == hashlib.sha1(
                            animals[j:j + size].encode('utf-8')).hexdigest():
                        count_ += 1
                        size += 1
    return count_

print(my_func('кошка'))