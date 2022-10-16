salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
total_delta = 0 # общая сумма ухода в минус за все месяцы


for i in range(1, months+1):
    delta = salary - spend   # на сколько в месяц уходим в минус
    spend *= 1.03
    total_delta += delta

need_money = -total_delta


print(round(need_money))

