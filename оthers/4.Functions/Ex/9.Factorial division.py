def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num1 = int(input())
num2 = int(input())

res = factorial(num1) / factorial(num2)
print(f"{res:.2f}")
