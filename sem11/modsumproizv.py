import sys
def calc(oper, *s):
    nums = [int(arg) for arg in s]
    res = 1
    if oper == "sum":
        res = sum(nums)
    elif oper == "proizv":
        for i in nums:
            res *= i
    else:
        print("Неправильная операция!!!")
        sys.exit(1)
    return res 
if __name__ == "__main__":
    # Получаем аргументы командной строки
    operation = sys.argv[1]
    args = sys.argv[2:]

    # Вызываем функцию calculate с переданными аргументами
    result = calc(operation, *args)

    # Выводим результат на экран
    print(f"Результат: {result}")
