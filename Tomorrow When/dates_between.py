from datetime import date

today = date.today()
day_end = date(2022, 3, 8)

# day_end =input("Day end: ", date.year, date.month, date.day)

days_between = day_end - today

print(f'Faltam {days_between.days} dias para o dia {day_end}')