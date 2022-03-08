studentName = input("Enter student's name:")
studentBirthday = input("Enter student's birthday:")
studentClassNum = input("Enter student's class num:")

courses = ['math', 'English', 'physics']
grades = {}

sum = 0
for course in courses:
    grades[course] = input("Enter student's " + course + " grade:")
    while not grades[course].isdigit():
        grades[course] = input("input isn't a number. Enter a valid grade:")
    grades[course] = float(grades[course])
    sum += grades[course]

avg = sum / len(courses)
avg = round(avg, 2)
print(studentName + "'s average is: " + str(avg))
