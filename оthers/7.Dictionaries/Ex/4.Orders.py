# dict_price = {}
# dict_quantity = {}
#
# data = input()
#
# while not data == "buy":
#     product, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product not in dict_price:
#         dict_price[product] = price
#         dict_quantity[product] = quantity
#     else:
#         dict_price[product] = price
#         dict_quantity[product] += quantity
#
#     data = input()
#
# for key in dict_quantity:
#     total = dict_quantity[key] * dict_price[key]
#     print(f"{key} -> {total:.2f}")


products = {}
data = input()

while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity

    data = input()

for key in products:
    total = products[key]['price'] * products[key]['quantity']
    print(f"{key} -> {total:.2f}")
