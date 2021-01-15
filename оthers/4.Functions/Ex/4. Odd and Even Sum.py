def odd_even_sum(num):
    odd = 0
    even = 0
    for (el) in num:
        n = int(el)
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print(f"Odd sum = {odd}, Even sum = {even}")


number = input()
odd_even_sum(number)