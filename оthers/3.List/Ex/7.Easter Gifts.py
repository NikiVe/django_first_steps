gifts = input().split()
command = input()

while not command == "No Money":
    tokens = command.split()
    if tokens[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == tokens[1]:
                gifts[i] = "None"
    elif tokens[0] == "Required":
        if 0 <= int(tokens[2]) < len(gifts):
            gifts[int(tokens[2])] = tokens[1]
    elif tokens[0] == "JustInCase":
        gifts[-1] = tokens[-1]

    command = input()

gifts = [el for el in gifts if not el == "None"]
print(*gifts)

# result = []
# for gift in gifts:
#     if not gift == "None":
#         result.append(gift)
# print(*result)


