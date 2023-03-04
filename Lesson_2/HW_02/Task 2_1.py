# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input())
# count_reshka = 0
# for i in range(n):
#     v = int(input())
#     if v == 0:
#         count_reshka += 1
# print("Переворачиваем монетки:", count_reshka if count_reshka < n / 2 else n - count_reshka)

#или
n = int(input())
count = 0
for i in range(n):
    if int(input()):
        count += 1
print(min(count, n - count))