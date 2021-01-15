def calc(drink, quantity):
    price = None
    if drink == "coffee":
        price = quantity * 1.50
    elif drink == "water":
        price = quantity * 1.00
    elif drink == "coke":
        price = quantity * 1.40
    elif drink == "snacks":
        price = quantity * 2.00

    return print(f"{price:.2f}")


order = input()
quantity_inp = int(input())
calc(order, quantity_inp)
