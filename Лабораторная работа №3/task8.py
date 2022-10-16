money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = salary - spend  # разница между заpплатой и тратами в месяц
total_delta = 0   # разница между заpплатой и тратами суммарно за все месяцы

while money_capital > -total_delta:
    delta = salary - spend  # разница между зарплатой и тратами
    spend *= 1.05
    total_delta += delta
    month += 1

print(month-1)
