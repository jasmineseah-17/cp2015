
#Finding the number of uppercase letters in a string

def find_num_uppercase(str):
    total = 0
    for letter in str:
        if letter.isupper():
            total = total + 1
        else:
            total = total
    return total

print(find_num_uppercase("Good MorniNG!"))