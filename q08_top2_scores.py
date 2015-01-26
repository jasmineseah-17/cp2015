
# Finding the two highest scores

number = int(input("Enter number of students: "))
names = []
scores = []
for student in range(1, number + 1):
    name = input("Student's name:")
    names.append(name)
    score = int(input("Student's score:"))
    scores.append(score)
print(names, scores)

for x in range(0,2):
    count = 0
    highest = 0
    for x in scores:
        if x > highest:
            highest = x
        count += 1
    print("The highest score is", highest, "held by", names[count-1])
    names.pop(count-1)
    scores.pop(count-1)


#print(names[count-1])
#print(x)
#print(names[count2])




