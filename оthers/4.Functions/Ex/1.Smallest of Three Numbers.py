def smallest_numb(a, b, c):
    if b > a < c:
        return a
    elif a > b < c:
        return b
    if b > c < a:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_numb(num1, num2, num3))