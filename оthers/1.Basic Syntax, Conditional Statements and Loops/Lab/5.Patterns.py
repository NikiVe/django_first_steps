n = int(input())
symbol = "*"

for i in range(1, n + 1):
    print(symbol*i)
for i2 in range(n - 1, 0, -1):
    print(symbol * i2)

