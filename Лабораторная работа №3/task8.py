money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
total_delta = 0   # разница между заpплатой и тратами суммарно за все месяцы

while money_capital > -total_delta:
    delta = salary - spend  # разница между зарплатой и тратами
    spend *= increase + 1
    total_delta += delta
    month += 1

month -= 1 #тк первый месяц не считается, это как бы 0
print(month)
