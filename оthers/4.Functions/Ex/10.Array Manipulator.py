list_str = input().split()
list_int = [int(el) for el in list_str]
command_inp = input()

while not command_inp == "end":
    command = command_inp.split()
    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(list_int):
            rev_list = list_int[index:] + list_int[:index]
        else:
            print("Invalid index")
    elif command[0] == "max":
        if command[1] == "even":
            max_even = [el for el in list_int if el % 2 == 0]
            if len(max_even) > 0:
                a = max(max_even)
                print(list_int.index(a, -1))
            else:
                print("No matches")
        else:
            max_odd = [el for el in list_int if not el % 2 == 0]
            if len(max_odd) > 0:
                a = max(max_odd)
                print(list_int.index(a, -1))
            else:
                print("No matches")
    elif command[0] == "min":
        if command[1] == "even":
            min_even = [el for el in list_int if el % 2 == 0]
            if len(min_even) > 0:
                a = min(min_even)
                print(list_int.index(a, -1))
            else:
                print("No matches")
        else:
            min_odd = [el for el in list_int if not el % 2 == 0]
            if len(min_odd) > 0:
                a = min(min_odd)
                print(list_int.index(a, -1))
            else:
                print("No matches")


    elif command[0] == "first":
        pass
    elif command[0] == "last":
        pass
