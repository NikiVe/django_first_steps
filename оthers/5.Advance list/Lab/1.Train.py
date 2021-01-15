wagons = int(input())
train = [0] * wagons

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    else:
        result = train[int(command[1])] - int(command[2])
        train[int(command[1])] = result

    command = input()

print(train)

