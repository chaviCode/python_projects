min = 9223372036854775807  # Maximum integer

for i in range(0, 3):
    num = input("Enter a number: ")
    while not num.isdigit():
        num = input("Not number! Enter a number: ")
    num = int(num)

    if num < min:
        min = num

print("Minimum number is: " + str(min))
