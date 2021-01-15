budget = float(input())
flour_price = float(input())
colored_eggs = 0
eggs_price = 0.75 * flour_price
milk_price = (1.25 * flour_price) / 4
cozonac_price = eggs_price + flour_price + milk_price
cozonacs = 0
while budget >= cozonac_price:
    budget -= cozonac_price
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs - 2

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")






