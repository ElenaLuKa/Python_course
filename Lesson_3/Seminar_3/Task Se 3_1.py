#Списки и словари

#1. Дан список чисел. Определите сколько в нем встречается разных чисел

list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

counter = int(input())
numbers = []
for i in range(counter):
    numbers.append(int(input()))
print(numbers)
num_values = len(set(numbers))
print(num_values)