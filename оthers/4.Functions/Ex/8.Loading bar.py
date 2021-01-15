def load_bar(num):
    num_in = num // 10
    bar = ["."] * 10
    for i in range(num_in):
        bar.insert(i, "%")
        del bar[-1]
    bar_j = "".join(bar)
    if num_in < 10:
        print(f"{num}% [{bar_j}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


number = int(input())
load_bar(number)
