word = input()

# reverse_word = word[::-1]
# print(reverse_word)

# print(word[::-1])

for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")
