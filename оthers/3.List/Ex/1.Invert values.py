# text = input()
text = input().split()

# integer[:] = [-1 * element for element in integer]
integer = [- int(el) for el in text]

print(integer)
