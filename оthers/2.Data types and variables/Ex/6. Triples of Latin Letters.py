n = int(input())

for i1 in range(0, n):
    for i2 in range(0, n):
        for i3 in range(0, n):
            print(f"{chr(97 + i1)}{chr(97 + i2)}{chr(97 + i3)}")

