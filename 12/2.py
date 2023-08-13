print(" *** Rank score ***")

lst = input("Enter ID and Score end with ID : ").split()

target = lst[len(lst) - 1]

lst.pop()

print(lst)

print(target)

students = {}

for i in range(0,len(lst) - 1,2):
    students[str(lst[i])] = float(lst[i + 1])

items = list(students.items())

n = len(items)
for i in range(n - 1):
    for j in range(n - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print(students)

cnt = 0

for i in students:
    if i == target:
        print(cnt + 1)
    else:
        cnt += 1


    

# print(lst)