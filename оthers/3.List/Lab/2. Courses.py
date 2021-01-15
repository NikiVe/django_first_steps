n = int(input())
courses_l = []

for courses in range(n):
    cur_course = input()
    courses_l += cur_course.split(",")

print(courses_l)

