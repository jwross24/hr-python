students = []

# Input
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)

min_score = 101
second_min = 101

# Calculate the second-minimum score
for student in students:
    score = student[1]
    if min_score > score:
        min_score, second_min = score, min_score
    elif second_min > score > min_score:
        second_min = score

# Find the students with the second-minimum score
students_with_second_min = []
for student in students:
    if student[1] == second_min:
        students_with_second_min.append(student[0])

# Order those students alphabetically and print the list
students_with_second_min.sort()
[print(student) for student in students_with_second_min]
