# Найдите сумму цифр трехзначного числа.

n = int(input("Введите число: "))
s = 0
while n > 0:
    k = n % 10
    s += k
    n //= 10
print('Сумма цифр в числе равна', s)