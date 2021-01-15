items = [el for el in input().split(", ")]

command = input()

while not command == "Craft!":
    command = command.split(" - ")

    if command[0] == "Collect":
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Renew":
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
    else:
        sub_command = command[1].split(":")
        if sub_command[0] in items:
            index = items.index(sub_command[0])
            items.insert(index + 1, sub_command[1])

    command = input()

print(", ".join(items))