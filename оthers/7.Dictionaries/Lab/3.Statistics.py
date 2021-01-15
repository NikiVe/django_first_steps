command = input()
products = {}

while not command == "statistics":
    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key in products:
        products[key] += value
    else:
        products[key] = value

    command = input()

print("Products in stock:")
for x, y in products.items():
    print(f"- {x}: {y}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
