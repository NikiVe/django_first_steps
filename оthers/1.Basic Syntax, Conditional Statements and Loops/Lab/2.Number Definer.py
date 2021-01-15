numb = float(input())
numb_type = ""

if numb == 0:
    print("zero")
elif numb > 0:
    numb_type = "positive"
elif numb < 0:
    numb_type = "negative"

if abs(numb) < 1 and numb != 0:
    print(f"small {numb_type}")
elif abs(numb) > 1000000:
    print(f"large {numb_type}")
else:
    print(numb_type)
