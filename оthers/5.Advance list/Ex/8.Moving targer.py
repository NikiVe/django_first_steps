targets = [int(target) for target in input().split()]
command = input()

while not command == "End":
    command = command.split()
    if command[0] == "Shoot":
        index = int(command[1])
        if 0 <= index < len(targets):
            power = int(command[2])
            targets[index] -= power
            if targets[index] <= 0:
                del targets[index]
    elif command[0] == "Add":
        index = int(command[1])
        if 0 <= index < len(targets):
            add_points = int(command[2])
            targets.insert(index, add_points)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if 0 <= (index - radius) and (index + radius) < len(targets):
            del targets[(index - radius):(index + radius) + 1]
        else:
            print("Strike missed!")

    command = input()

print("|".join(map(str, targets)))

