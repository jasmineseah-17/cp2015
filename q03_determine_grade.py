
# Determining grade

score = int(input("Enter score:"))

if 0 <= score <= 34:
    grade = "U"
    print(grade)
elif 35 <= score <= 44:
    grade = "S"
elif 45 <= score <= 49:
    grade = "E"
elif 50 <= score <= 54:
    grade = "D"
elif 55 <= score <= 59:
    grade = "C"
elif 60 <= score <= 69:
    grade = "B"
elif 70 <= score <= 100:
    grade = "A"
else:
    print("Invalid! Score must be within 0 - 100.")

