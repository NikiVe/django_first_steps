num1 = int(input())
num2 = int(input())
numb = 0
for n in range(num2 + 1):
    if n % num1 == 0 and n <= num2:
        numb = n
print(numb)