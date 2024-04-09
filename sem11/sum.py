#Написать программу, которая запускается из консоли и считает сумму переданных в неё чисел
import sys
oper = sys.argv[1]
s = sys.argv[2:]
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
print(f"Результат: {oper}={res}")