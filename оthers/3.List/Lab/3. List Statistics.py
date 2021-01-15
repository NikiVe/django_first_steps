n = int(input())

positive = []
negative = []

for numb in range(n):
    cur_numb = int(input())
    if cur_numb < 0:
        negative.append(cur_numb)
    else:
        positive.append(cur_numb)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")
