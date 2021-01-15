operator_inp = input()
n1 = int(input())
n2 = int(input())


def calc(num1, num2, operator):
    res = None
    if operator == "multiply":
        res = num1 * num2
    elif operator == "divide":
        res = num1 / num2
    elif operator == "add":
        res = num1 + num2
    elif operator == "subtract":
        res = num1 - num2
    return res


result = calc(operator_inp, n1, n2)
print(f"{result:.0f}")