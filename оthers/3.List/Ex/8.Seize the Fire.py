fires_inp = input().split("#")
water_inp = int(input())
water_ceil = []

for tokens in fires_inp:
    fire_ceil = tokens.split(" = ")
    fire_power = int(fire_ceil[1])
    if fire_ceil[0] == "High" and 81 <= fire_power <= 125:
        if water_inp >= fire_power:
            water_inp -= fire_power
            water_ceil.append(fire_power)
    elif fire_ceil[0] == "Medium" and 51 <= fire_power <= 80:
        if water_inp >= fire_power:
            water_inp -= fire_power
            water_ceil.append(fire_power)
    elif fire_ceil[0] == "Low" and 1 <= fire_power <= 50:
        if water_inp >= fire_power:
            water_inp -= fire_power
            water_ceil.append(fire_power)

total_fire = sum(water_ceil)
print("Cells:")
for el in water_ceil:
    print(f"- {el}")
print(f"Effort: {(total_fire * 0.25):.2f}")
print(f"Total Fire: {total_fire}")