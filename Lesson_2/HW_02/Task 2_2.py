# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# S = int(input())
# P = int(input())
# for x in range(1, P):
#     D = S ** 2 - 4 * P
#     y = S - x
#     if D >= 0 and S == x + y and P == x * y:
#         print(x, y)

# или решение от преподавателя

s = int(input("Sum of numbers: "))
p = int(input("The product of numbers: "))
answer = "I didn't guess."
d = s ** 2 - 4 * p
if d >= 0:
    x_1 = (s + d ** 0.5) // 2
    x_2 = (s - d ** 0.5) // 2
    if x_1 * x_2 == p:
        answer = f"{x_1}, {x_2}"
print(answer)