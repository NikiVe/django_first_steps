card = input().split()
team_a = []
team_b = []
players_a = 0
players_b = 0
for cards in card:
    card_2 = cards.split("-")
    team = card_2[0]
    player = int(card_2[1])
    if team == "A":
        team_a.append(player)
    elif team == "B":
        team_b.append(player)

    players_a = 11 - len(set(team_a))
    players_b = 11 - len(set(team_b))
    if players_a < 7 or players_b < 7:
        print(f"Team A - {players_a}; Team B - {players_b}")
        print("Game was terminated")
        break
if players_a >= 7 and players_b >= 7:
    print(f"Team A - {players_a}; Team B - {players_b}")
