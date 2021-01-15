n = int(input())

pos = []
neg = []
even = []
odd = []

for num in range(n):
    cur_num = int(input())
    if cur_num < 0:
        neg.append(cur_num)
    else:
        pos.append(cur_num)
    if cur_num % 2 == 0:
        even.append(cur_num)
    else:
        odd.append(cur_num)

command = input()

if command == "positive":
    print(pos)
elif command == "negative":
    print(neg)
elif command == "odd":
    print(odd)
else:
    print(even)
