mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

while True:
    data = input().split()
    is_found = False
    for index in range(0, len(data), 2):
        quantity = int(data[index])
        item = data[index + 1].lower()

        if item in key_materials:
            key_materials[item] += quantity
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity

        for key, value in key_materials.items():
            if value >= 250:
                print(f"{mapper[key]} obtained!")
                key_materials[key] -= 250
                is_found = True
                break
        if is_found:
            break
    if is_found:
        break

ordered_key = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))

for k_item, k_quantity in ordered_key:
    print(f"{k_item}: {k_quantity}")

ordered_junk = sorted(junk.items(), key=lambda x: x[0])

for j_item, j_quantity in ordered_junk:
    print(f"{j_item}: {j_quantity}")
