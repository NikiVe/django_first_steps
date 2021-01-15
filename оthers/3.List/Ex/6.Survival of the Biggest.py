integer = input().split()
n = int(input())

integer = [int(el) for el in integer]

for i in range(n):
    integer.remove(min(integer))

print(integer)
