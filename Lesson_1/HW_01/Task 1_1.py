# Найдите сумму цифр трехзначного числа.

# n = int(input("Введите число: "))
# s = 0
# while n > 0:
#     k = n % 10
#     s += k
#     n //= 10
# print('Сумма цифр в числе равна', s)

# или решение от преподавателя

num = int(input())
num_sum = 0

while num:
    num_sum += num%10
    num //= 10
print(num_sum)