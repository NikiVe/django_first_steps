houses = [int(hearts) for hearts in input().split("@")]
command = input()
position = 0

while not command == "Love!":
    move = [int(jump) for jump in command.split() if jump.isdigit()]
    jump = move[0] + position
    if jump >= len(houses):
        jump = 0
    if houses[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
    else:
        houses[jump] -= 2
        if houses[jump] == 0:
            print(f"Place {jump} has Valentine's day.")

    position = jump
    command = input()

print(f"Cupid's last position was {position}.")
if sum(houses) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - houses.count(0)} places.")






