#Списки и словари

#1. Дан список чисел. Определите сколько в нем встречается разных чисел

#list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

# counter = int(input())
# numbers = []
# for i in range(counter):
#     numbers.append(int(input()))
# print(numbers)
# num_values = len(set(numbers))
# print(num_values)

# 2. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# listik = [1, 2, 3, 4, 5]
# k = int(input('Input number: '))
# for i in range(k):
#     listik.insert(0, listik.pop())

# print(listik)


# 3. Напишите программу для печати всех уникальных значений в словарей

# list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII": " S007 "}]  

# print(set([list(i.values())[0].strip() for i in list_dict]))
#strip() -  удаляет пробелы и слева и справа

# 4. Дан список, состоящий из целых чисел. 
# Напишите программу, которая подсчитывает количество элементов массива, 
# больших предыдущего(элемента с предыдущим номером)

# list_nums = [0, -1, 5, 2, 3]
# print(sum([list_nums[i] > list_nums[i-1] for i in range(1, len(list_nums))]))
# в таком варианте записи сначала идет условие, потом цикл. 

# "1 2      3".split()   ['1', '2', '3'] убирает пробелы

# " ".join(["Name", "Surname"])    'Name Surname' объединяет в строку (работает только со строковыми значениями)
# " & ".join(["Name", "Surname"])    'Name & Surname' объединяет в строку (работает только со строковыми значениями)
# "\n".join(["Name", "Surname"])    'Name\nSurname' объединяет в строку (работает только со строковыми значениями)
# m = "\n".join(["Name", "Surname"])    Name Surname объединяет в строку (работает только со строковыми значениями)

# "сЕрГеЙ сЕрГеЙ".title() Сергей Сергей - это для слова
# "сЕрГеЙ сЕрГеЙ".capitalize() Сергей сергей - это для предложения

# .upper() -поднимает в верхний регистр
# .lower()

# "gipopotampo".count("po")
# "gipopotampo".replace("po", " ").count.('pa')