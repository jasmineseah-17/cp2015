
# Computing GCD

def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for d in range(1, smaller + 1):
        if(x % d == 0) and (y % d == 0):
            hcf = d
    return hcf

print("The gcd of", 24, "and", 16, "is", gcd(24, 16))
print("The gcd of", 255, "and", 25, "is", gcd(255, 25))