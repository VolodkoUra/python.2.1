"""
Создать функцию calc(a, b, operation). Описание входных параметров:
1. Первое число
2. Второе число
3. Действие над ними:
   1) + Сложить
   2) - Вычесть
   3) * Умножить
   4) / Разделить
   5) В остальных случаях функция должна возвращать "Операция не поддерживается"""


def calc(a=1, b=1, operation=""):
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    operation = input("Введите код операции: ")
    if operation == "+":
        result = a + b
        print("Результат {}".format(result))
    elif operation == "-":
        result = a - b
        print("Результат {}".format(result))
    elif operation == "*":
        result = a * b
        print("Результат {}".format(result))
    elif operation == "/":
        if b != 0:
            result = a / b
            print("Результат {}".format(result))
        else:
            print("Деление на ноль")
    else:
        print("Операция не поддерживается")


if __name__ == '__main__':
    calc()
