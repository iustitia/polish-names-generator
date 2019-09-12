import random
from names import gen_names

students = []

for student in gen_names(350, formatted=False):
    grades = [random.randint(2, 5) for grade in range(6)]
    students.append([student[0], random.randint(200000, 500000), grades])

for s in students:
    print('{:15s} | {} | {}'.format(s[0], s[1], s[2]))

input('Press any key to start calculations')
print('run')

for s in students:
    grades_sum = sum(s[2])
    grades_count = len(s[2])
    avg = grades_sum/grades_count

    print('{:15s} | {} | {}'.format(s[0], s[1], avg))
