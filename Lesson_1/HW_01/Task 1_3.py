#  Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#  Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#  Вам требуется написать программу, которая проверяет счастливость билета.

# n = int(input('Введите номер билета: '))
# s1 = 0
# s2 = 0
# while n > 1000:
#     k = n % 10
#     s1+= k
#     n //= 10
# while n > 0:
#     k = n % 10
#     s2 += k
#     n //= 10
# if s1 == s2:
#     print('Поздравляю! Билет счастливый')
# else:
#     print('К сожалению в этот раз Вам не повезло, ничего, в другой раз обязательно повезет')

# или решение от преподавателя

# способ при помощи индексов

# ticket_num = input()
# sum_first = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
# sum_last = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])
# print(f"The ticket is lucky: {sum_first == sum_last}")

# способ без использования индексов

ticket_number = int(input())

sum_first = 0
sum_last = 0
while ticket_number:
    digit = ticket_number % 10
    if ticket_number > 999:
        sum_first += digit
    else:
        sum_last += digit
    ticket_number //= 10
print(f"The ticket is lucky: {sum_first == sum_last}")




