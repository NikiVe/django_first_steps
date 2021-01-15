import math

numbers = [int(numb) for numb in input().split(", ")]
groups = math.ceil(max(numbers) / 10)
low = 1

for group in range(1, groups + 1):
    cur_group = [numb for numb in numbers if (low <= numb <= 10 * group)]
    print(f"Group of {group * 10}'s: {cur_group}")
    low += 10
