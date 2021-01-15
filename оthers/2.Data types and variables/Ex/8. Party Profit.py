party = int(input())
days = int(input())
coin = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        party -= 2
    if day % 15 == 0:
        party += 5
    coin += 50 - (party * 2)
    if day % 3 == 0:
        coin -= party * 3
    if day % 5 == 0:
        coin += party * 20
        if day % 3 == 0:
            coin -= party * 2
print(f"{party} companions received {int(coin / party)} coins each.")
     
    
