data = input()
resources = {}

while not data == "stop":
    quantity = int(input())
    if data in resources:
        resources[data] += quantity
    else:
        resources[data] = quantity

    data = input()

for metal, quantity in resources.items():
    print(f"{metal} -> {quantity}")
