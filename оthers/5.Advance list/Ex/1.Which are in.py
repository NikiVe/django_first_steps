sub_string = input().split(", ")
strings = input().split(", ")

subs = [subs for subs in sub_string for string in strings if subs in string]

print(sorted(set(subs), key=subs.index))
