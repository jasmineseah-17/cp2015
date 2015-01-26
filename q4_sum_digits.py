
# Summing the digits in an integer

sum = 0
a = input("Please enter an integer between 0 to 1000: ")
x = list(a)
for item in x:
    sum = sum + int(item)
    continue
print(sum)

while True:
    try:
        answer = int(input("Please enter an integer between 0 to 1000: "))
        while not 0 < answer < 1000:
            answer = int(input("Sorry, please enter an integer between 0 to 1000: "))
        if 0 < answer < 1000:
            hundred = answer // 100
            ten = answer // 10 - hundred * 10
            one = answer % 10
            sum = hundred + ten + one
        break
    except ValueError:
        print("Sorry, please try again.")

print("Sum of digits is", sum)