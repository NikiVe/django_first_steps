def palindrome(a):
    pal = a.split(", ")
    for el in pal:
        el2 = el[::-1]
        if el == el2:
            print("True")
        else:
            print("False")


int_string = input()
palindrome(int_string)

