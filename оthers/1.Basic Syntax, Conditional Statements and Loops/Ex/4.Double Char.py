text = input()

result = ""
for i in range(len(text)):
    result += text[i] + text[i]
print(result)

new_string = ''
for letter in text:
    new_string += letter * 2
print(new_string)