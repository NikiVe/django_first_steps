import sys
n_snowballs = int(input())
max_value = - sys.maxsize - 1
snow = 0
time = 0
quality = 0

for snowball in range(1, 1 + n_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_snow / snowball_time) ** snowball_quality
    if value > max_value:
        max_value = int(value)
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality

print(f"{snow} : {time} = {max_value} ({quality})")


