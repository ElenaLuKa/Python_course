# Список - это упорядоченный конечный набор элементов. 
# Давайте разбираться, по сути список - это тот же самый массив, 
# в котором можно хранить элементы любых типов данных

# list_1 = [] #создание пустого списка
# list_2 = list() #создание пустого списка


# В списках существует нумерация, которая начинается с 0, 
# что бы вывести первый элемент списка воспользуемся следующей конструкцией:

# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0]) # 7
# print(*list_1) # убирает квадратные скобки при выводе в терминал

# for i in list_1:

# print(len(list_1)) #выводит количество элементов в списке

# print(list_1[-1]) #при -1 список начинается с конца

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # позволяет добавить что нибудь к списку
# print(list_1)


# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) #удаляет последний элемент из списка
# print(list_1.pop(0)) #удаляет конкретный элемент из списка
# print(list_1.insert(2, 11)) #добавление элемента в нужную позицию, вначале номер позиции, потом вставляемый элемент

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                          # 1
# print(list_1[1])                          # 2
# print(list_1[len(list_1) - 1])            # 10
# print(list_1[-1])                         # 10
# print(list_1[-5])                         # 6
# print(list_1[:])                          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])                         # [1, 2]
# print(list_1[len(list_1) - 2:])           # [9, 10]
# print(list_1[2:9])                        # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:18])                       # []
# print(list_1[0:len(list_1):6])            # [1, 7]
# print(list_1[::6])                        # [1, 7]

# кортеж - это неизменяемый список. В случае защиты каких либо данных от изменений. 
# Кортеж занимает меньше места в памяти и работает быстрееб по сравнению со списками.

# t = () # создание пустого кортежа
# print(type(t))  #class <'tuple'>
# t = (1,)
# print(type(t)) 
# t = (1)         #class <'tuple'>
# print(type(t))  #class <'int'>
# t = (28, 9, 1990) 
# print(type(t))  #class <'tuple'>
# v = [1, 8, 9]
# print(v)
# print(type(v))  #class <'list'>
# v = tuple(v)
# print(v)
# print(type(v))

# a = 1
# b = 2
# a, b = 1, 2

# a,b,c = v
# print(a, b, c) #1 8 9

# t = (1, 2, 3, 5,)
# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t = [1, 2, 3, 5,]
# t[0] = 2

# словари - неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. 
# В словаре для определения элемента используется значение ключа(строка, число)

# d = {} - используются для создания словаря
# d = dict() - так же является словарем

# d['q'] = 'qwerty' # 'q' - ключ, 'qwerty' - значение
# print(d) #{'q': 'qwerty'}
# d['w'] = 'werty'
# print(d) #{'q': 'qwerty', 'w': 'werty'}
# print(d['q']) # qwerty

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# dictionary[895] = 98998
# print(dictionary)

# множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# одно множество может содержать значения любых типов. Если у Вас есть два множества, 
# Вы можете совершать над ними любые стандартные операции, например, объединение, пересечение и разность.

# colors = {'red', 'gren', 'blue'} #множество создается при помощи фигурных скобок
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# colors.clear() #{ }
# print(colors) #set()
# q = set()

# Операции со множествами в Python:

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} копирование
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение по уникальным значениям 
# i = a.intersection(b) # i = {8, 2, 5} пересечеиние
# dl = a.difference(b) # dl = {1, 3} разность а - в
# dr = b.difference(a) # dr = {13, 21} разность в - а
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13} 
# # сначала действие в скобках (пересечение а и в), потом слева направо объединяются по уникальным значениям а и в, 
# # и из полученного множества находим находится разность с пересечением в скобках

# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# Обобщение свойств встроенных коллекций:
# 1. Список: изменяется, индексируется, не уникален, создаем [] либо list()
# 2. Кортеж: не изменяется, индексируется, не уникален, создаем () либо tuple()
# 3. Строка: не изменяется, индексируется, не уникальна, создаем '' либо ""
# 4. Множество: изменяется, не индексируется, уникально, создаем {elm1, elm2} либо set()
# 5. Неизменное множество: не изменяется, не индексируется, уникально, создаем frosenset()
# 6. Словарь: элементы и значения изменяются, ключи не изменяются, не индексируются, элементы и ключи уникальны, значения нет, 
# создаем {} либо {key: value,} либо dict()

# У каждого языка программирования есть свои особенности и преимущества. 
# Одна из культовых фишек Python — list comprehension (редко переводится на русский, но можно
# использовать определение «генератора списка»). Comprehension легко читать, и их
# используют как начинающие, так и опытные разработчики. List comprehension — это
# упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
# if-else для определения того, что в итоге окажется в финальном списке.

# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable] #
# 1. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

# Мы с вами люди, а людям суждено ошибаться, даже при написании программного кода 🙂
# Давайте разберем с Вами самые частые ошибки в написании кода на Python.

# # 🔥Самые распространенные ошибки:
# # ○ SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second     # !!!!!
#     print(number_first)
# # Отсутствие :

# Профилирование и отладка
# IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
# # Отсутствие отступов
# ● TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя
# ● KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

# NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует
# ● ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения