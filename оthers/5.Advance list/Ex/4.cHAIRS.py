rooms = int(input())
total_free = 0
game_on = True

for room in range(1, rooms + 1):
    chairs = input().split()
    total_chairs = chairs[0].count("X")
    taken = int(chairs[1])
    free = total_chairs - taken
    if free < 0:
        print(f"{abs(free)} more chairs needed in room {room}")
        game_on = False
    else:
        total_free += free
    free = 0

if game_on:
    print(f"Game On, {total_free} free chairs left")