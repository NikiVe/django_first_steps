# integers = [int(el) for el in input().split()]
# integers.reverse()
# string = [str(el) for el in integers]
# print("".join(string))

numbers = input().split()
numbers.sort(reverse=True)
print(''.join(numbers))