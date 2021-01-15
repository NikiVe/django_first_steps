def repeat(text, counter):
    result = text * counter
    return result


string = input()

n = int(input())
print(repeat(string, n))

# string = input()
# n = int(input())
#
#
# def repeat(text, counter):
#     result = ""
#     for i in range(n):
#         result += string
#     return result
#
#
# print(repeat(string, n))
