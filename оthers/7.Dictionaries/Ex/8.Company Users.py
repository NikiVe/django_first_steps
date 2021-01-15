register = {}

while True:
    data = input()
    if data == "End":
        break
    else:
        company, id_e = data.split(" -> ")
        if company not in register:
            register[company] = []
        if id_e not in register[company]:
            register[company].append(id_e)

for company, ids_e in sorted(register.items(), key=lambda x: x[0]):
    print(company)
    for e in ids_e:
        print(f"-- {e}")

