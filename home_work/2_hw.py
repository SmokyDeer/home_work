def task_1() -> None: # Добавляем аннотацию возвращаемого типа -> None, который означает "отсутствие значения"
    a = 30
    b = 99.99
    c = "Alice"
    d = ['milk', 'bread', 'egg']
    f = True

    print(a, 'относится к типу', type(a))
    print(b, 'относится к типу', type(b))
    print(c, 'относится к типу', type(c))
    print(d, 'относится к типу', type(d))
    print(f, 'относится к типу', type(f))

task_1() #вызов функции

def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
task_2() #вызов функции

# Это числа Фибоначчи

def task_3(number: int) -> int:
    square = number ** 2
    return square

print('Квадрат числа 5 = ', task_3(5))