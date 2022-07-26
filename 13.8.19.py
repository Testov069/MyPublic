price = [0, 990, 1390]
percent = 0.9
ticket = int(input('Введите количество билетов: '))
age = [int(input('Введите возраст участника конференции: ')) for i in range(1, ticket+1)]
count_1 = 0
count_2 = 0
count_3 = 0

for i in age:
    if 0 < i < 18:
        count_1 += 1
    elif 18 < i < 25:
        count_2 += 1
    elif i > 25:
        count_3 += 1

value_1 = count_1*price[0]
value_2 = count_2*price[1]
value_3 = count_3*price[2]

if ticket > 3:
    value_ = (value_1 + value_2 + value_3)*percent
else:
    value_ = (value_1 + value_2 + value_3)

print('Сумма к оплате: ', int(value_))
