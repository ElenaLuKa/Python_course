# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

from random import randint
list = []
for i in range(int(input("Введите количество элементов в списке: "))):
    list.append(int(randint(0, 100)))
print(list)
x = int(input("Введите число: "))
print(f"Число {x} встречается {sum([list[i] == x for i in range(len(list))])}")


#или решение от преподавателя:
   
# from random import choices

# num = int(input())
# list_nums = choices(range(num * 2), k = num)
# print(list_nums)
# result = list_nums.count(int(input()))
# print(result)

#или решение от преподавателя:

# list_nums = [int(input()) for _ in range(int(input()))]
# print(list_nums.count(int(input())))