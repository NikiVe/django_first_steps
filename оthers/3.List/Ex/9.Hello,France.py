items = input().split("|")
budget = float(input())
new_prices = []
price = 0
for command in items:
    cur_command = command.split("->")
    item_cost = float(cur_command[1])
    if cur_command[0] == "Clothes":
        if budget >= item_cost <= 50.00:
            budget -= item_cost
            price += item_cost
            item_cost *= 1.40
            new_prices.append(item_cost)
    elif cur_command[0] == "Shoes":
        if budget >= item_cost <= 35.00:
            budget -= item_cost
            price += item_cost
            item_cost *= 1.40
            new_prices.append(item_cost)
    else:
        if budget >= item_cost <= 20.50:
            budget -= item_cost
            price += item_cost
            item_cost *= 1.40
            new_prices.append(item_cost)

profits = sum(new_prices) - price
# new_prices = [round(el, 2) for el in new_prices]
# print(*new_prices)
for el in new_prices:
    print(f"{el:.2f} ", end='')

print()
print(f"Profit: {profits:.2f}")

if (sum(new_prices) + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
