
# Displaying matrix of 0s and 1s
import random

a = []
def print_matrix(n):
    for item in range(1, n + 1):
        for num in range(1, n + 1):
            a.append(random.randint(0, 1))
        print(a[0:n + 1])
        del a[0:n + 1]

x = int(input("Enter number: "))
print_matrix(x)