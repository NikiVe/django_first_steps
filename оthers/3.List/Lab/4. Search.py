n = int(input())
code_word = input()
text_list = []
code_list = []

for text in range(n):
    cur_text = input()
    text_list.append(cur_text)
    if code_word in cur_text:
        code_list.append(cur_text)

print(text_list)
print(code_list)
