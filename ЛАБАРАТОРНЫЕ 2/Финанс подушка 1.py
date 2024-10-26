money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен
kol_mec = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
if kol_mec == 0:
    money_capital = money_capital + salary - spend
    kol_mec += 1
while money_capital >= 0:
    spend = spend + spend*increase
    money_capital = money_capital + salary - spend
    if money_capital < 0:
        break
    else:
        kol_mec += 1

















print("Количество месяцев, которое можно протянуть без долгов:", kol_mec)
