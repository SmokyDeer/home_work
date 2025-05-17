def find_max(num1:int, num2:int) -> None:
    print("Максимальное число:", max(num1, num2))

find_max(10, 5)

def difference(num1:int, num2:int) -> None:
    numdifference = abs(num1 - num2)

    if numdifference == 135:
        print('yes')
    else:
        print('no')


difference(200, 65)
difference(100, 10)

def get_season(num_month: int) -> None:
    if num_month in [12, 1, 2]:
        print('зима')
    elif num_month in [3, 4, 5]:
        print('весна')
    elif num_month in [6, 7, 8]:
        print('лето')
    elif num_month in [9, 10, 11]:
        print('зима')

get_season(5)

def num_10(num1: int, num2: int, num3: int) -> None:
    if num1 > 10 and num2 > 10 and num3 > 10:
        print('yes')
    else:
        print('no')

num_10(15, 17, 20)
num_10(4, 10, 9)

def positive_num(num_list: list[int]) -> None:
    num_count = 0
    for num in num_list:
        if num > 0:
            num_count += 1
    print('Количество позитивных чисел = ', num_count)

positive_num([1, -5, 0, 5])

def days(years: int, months: int) -> None:
    total_months = years * 12 + months
    total_days = total_months * 29
    print("За", years, "лет и", months, "месяцев количество дней составляет:", total_days)

days(5, 7)
days(0, 9)