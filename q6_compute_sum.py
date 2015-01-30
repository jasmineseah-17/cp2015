
# Summing the digits in an integer using recursion

def sum_digits(n):
    a = []
    for num in n:
        a.append(int(num))
    return sum(a)

print(sum_digits("234"))