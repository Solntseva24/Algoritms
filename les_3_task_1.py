'''не забывайте придираться)) Задача1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
 каждому из чисел в диапазоне от 2 до 9.
 Помучила я конечно эту задачку...хоть с виду казалась самой простой. оставлю закоменченными свои попытки '''

num_range = list(range(2, 100))
num_range_2 = list(range(2, 10))

n_1 = 0
n_2 = 0
n_3 = 0
n_4 = 0
n_5 = 0
n_6 = 0
n_7 = 0
n_8 = 0

for a in num_range:

    for i in num_range_2:
        if a%i == 0:
            if i == num_range_2[0]:
                n_1 += 1
            if i == num_range_2[1]:
                n_2 += 1
            if i == num_range_2[2]:
                n_3 += 1
            if i == num_range_2[3]:
                n_4 += 1
            if i == num_range_2[4]:
                n_5 += 1
            if i == num_range_2[5]:
                n_6 += 1
            if i == num_range_2[6]:
                n_7 += 1
            if i == num_range_2[7]:
                n_8 += 1

print((num_range_2[0], '-', n_1))
print((num_range_2[1], '-', n_2))
print((num_range_2[2], '-', n_3))
print((num_range_2[3], '-', n_4))
print((num_range_2[4], '-', n_5))
print((num_range_2[5], '-', n_6))
print((num_range_2[6], '-', n_7))
print((num_range_2[7], '-', n_8))

#a = 0
#while a < len(n_1):
#    print(a+2, '-', n_1[a])
#    a =+ 1
#count = []
#for num_range in num_range_2:
#   if num_range % num_range_2 == 0:
#        i = 0
#        count[i] =+ 1
#        print(num_range_2[i], '-', count[])
#        i =+ 1

#new_list_1 = []
#for a in num_range:
 #   for i in num_range_2:
  #      if a % i == 0:
   #         new_list_1.append()
    #        print(num_range_2[0], new_list_1.count())

            #print(num_range_2, '-', new_list.count(a))
#print(new_list)
#x = 0
#while x < len(new_list):
#    print(x + 2, '-', new_list[a])
 #   x =+ 1а
