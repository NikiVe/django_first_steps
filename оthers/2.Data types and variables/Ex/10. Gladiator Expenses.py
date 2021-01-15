lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = 0
sword = 0
shield = 0
armor = 0

for battle in range(1, lost_battles + 1):
    if battle % 2 == 0:
        helmet += 1
    if battle % 3 == 0:
        sword += 1
        if battle % 2 == 0:
            shield += 1
            if shield % 2 == 0 and not shield == 0:
                armor += 1

total = helmet * helmet_price + sword * sword_price + shield * shield_price + armor * armor_price

print(f"Gladiator expenses: {total:.2f} aureus")
