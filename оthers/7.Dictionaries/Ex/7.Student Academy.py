n = int(input())
average_grades = {}

for data in range(n):
    name = input()
    grade = float(input())
    if name not in average_grades:
        average_grades[name] = [grade]
    else:
        average_grades[name] += [grade]

filtered = {}

for key in average_grades:
    av_grade = sum(average_grades[key]) / len(average_grades[key])
    if av_grade >= 4.50:
        filtered[key] = av_grade

for student, average in sorted(filtered.items(), key=lambda x: x[1],reverse=True):
    print(f"{student} -> {average:.2f}")
