happiness_factor = int(input())
people = list(map(lambda x: int(x) * happiness_factor, input().split()))

filtered = list(filter(lambda x: x >= (sum(people) / len(people)), people))

if len(filtered) >= len(people) / 2:
    print(f"{len(filtered)}/{len(people)}")
else:
    print(f"{len(filtered)}/{len(people)}")
