string = input()

text = {}

for char in string:
    text[char] = string.count(char)

for key, value in text.items():
    if not key == " ":
        print(f"{key} -> {value}")
