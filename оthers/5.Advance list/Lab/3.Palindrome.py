string = input().split()
key = input()

palindromes = [word for word in string if word == word[::-1]]
counter = palindromes.count(key)

print(palindromes)
print(f"Found palindrome {counter} times")
