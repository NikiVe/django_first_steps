def char_range(a, b):
    a = ord(a)
    b = ord(b)
    for i in range(a + 1, b):
        print(f"{chr(i)}", end=" ")


a = input()
b = input()
char_range(a, b)
