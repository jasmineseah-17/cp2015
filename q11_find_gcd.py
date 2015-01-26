
# Computing the greatest common divisor

def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for d in range(1, smaller + 1):
        if(x % d == 0) and (y % d == 0):
            hcf = d
    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The gcd of", num1, "and", num2, "is", gcd(num1, num2))