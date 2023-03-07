# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

from random import randint
list = []
for i in range(int(input("Введите количество элементов в списке: "))):
    list.append(int(randint(-20, 20)))
print(list)
x = int(input("Введите число: "))
k = list[0]
for i in range(len(list)):
    if (abs(list[i] - x) < abs(k - x) and list[i] < x) or list[i] == x:
        k = list[i]
print(k)