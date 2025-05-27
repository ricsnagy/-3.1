num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Ділити на 0 не можна!")#
    else:
        result = num1 / num2
        print( result)