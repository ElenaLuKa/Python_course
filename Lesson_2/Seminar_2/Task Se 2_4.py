# 4. Иван Васильевич пришел на рынок и решил купить
# два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза

n = int(input())
num_max = 0
num_min = 1000

for i in range(n):
    massa = int(input())
    if massa <= num_min:
        num_min = massa
    if massa >= num_max:
        num_max = massa
print(num_max, num_min)

# range - это формирование последовательностей

# n = list(range(0, 9)) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(n)

# n = list(range(0, 9, 2)) #[0, 2, 4, 6, 8]
# print(n)

# for i in range(1, 21, 2):
#     print (i, end = " ")
