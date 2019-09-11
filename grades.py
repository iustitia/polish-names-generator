import random
from names import gen_names

students = []

for student in gen_names(350, formatted=False):
    grades = [random.randint(2, 5) for grade in range(6)]
    students.append([student[0], random.randint(200000, 500000), grades])

for s in students:
    print('{} | {} | {}'.format(s[0], s[1], s[2]))

input('Press any key to start calculations')

print('run')

for s in students:
    avg = sum(s[2])/len(s[2])
    print(s[0], avg)
