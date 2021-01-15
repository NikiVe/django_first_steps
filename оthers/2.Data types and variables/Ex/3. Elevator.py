people = int(input())
capacity = int(input())

course = (people // capacity)
if not people % capacity == 0:
    course += 1

print(course)
