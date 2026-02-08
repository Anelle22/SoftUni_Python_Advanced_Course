number_of_students = int(input())
student_record = {}

for i in range(number_of_students):
    name, grade = input().split()
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(grade)

sum_of_value = 0
for key, value in student_record.items():
    for item in value:
        sum_of_value = sum_of_value + float(item)
    average = sum_of_value / len(value)
    print(f'{key} -> {" ".join(map(str, value))} (avg: {average:.2f})')
    sum_of_value = 0


