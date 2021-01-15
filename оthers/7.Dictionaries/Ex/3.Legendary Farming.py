materials = [m.lower() for m in input().split()]
dictionary = {}

for i in range(0, len(materials), 2):
    material = materials[i + 1]
    quantity = int(materials[i])
    if material in dictionary:
        dictionary[material] += quantity
    else:
        dictionary[material] = quantity

    if material == "shards":
        if dictionary["shards"] >= 250:
            print("Shadowmourne obtained!")
            dictionary["shards"] -= 250
            print(f"shards: {dictionary['shards']}")
            del dictionary["shards"]
            break
    elif material == "fragments":
        if dictionary["fragments"] >= 250:
            print("Valanyr obtained!")
            dictionary["fragments"] -= 250
            print(f"fragments: {dictionary['fragments']}")
            del dictionary["fragments"]
            break
    elif material == "motes":
        if dictionary["motes"] >= 250:
            print("Dragonwrath  obtained!")
            dictionary["fragments"] -= 250
            print(f"motes: {dictionary['motes']}")
            del dictionary["motes"]
            break

print(dictionary)
