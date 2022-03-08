names = []
name = input("Enter a student's name: ")
while name != "=":
    names.append(name)
    name = input("Enter a student's name: ")

# print(names)
for name in names:
    print(name)
