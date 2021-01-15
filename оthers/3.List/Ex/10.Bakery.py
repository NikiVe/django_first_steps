events_list = input().split("|")
energy = 100
coins = 100
is_bankrupt = False

for turn in range(len(events_list)):
    event = events_list[turn].split("-")
    event_value = int(event[1])
    if event[0] == "rest":
        if energy == 100:
            print("You gained 0 energy.")
        else:
            energy += event_value
            if energy > 100:
                event_value = energy - 100
                energy = 100
            print(f"You gained {event_value} energy.")
        print(f"Current energy: {energy}.")
    elif event[0] == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= event_value
        if coins > 0:
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            is_bankrupt = True
            break

if not is_bankrupt:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
