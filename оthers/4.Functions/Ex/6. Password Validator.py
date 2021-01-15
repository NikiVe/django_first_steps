def pas_validator(password_valid):
    digits = 0
    is_valid = True

    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for el in password:
        if not (48 <= ord(el) <= 57 or 65 <= ord(el) <= 90 or 97 <= ord(el) <= 122):
            print("Password must consist only of letters and digits")
            is_valid = False
            break

    for el in password:
        if 48 <= ord(el) <= 57:
            digits += 1

    if digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
pas_validator(password)
