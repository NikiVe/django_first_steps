n_lines = int(input())
result = 0

for char in range(n_lines):
    character = input()
    result += ord(character)
print(f"The sum equals: {result}")
