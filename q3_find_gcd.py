
# Computing greatest common divisor using recursion

def gcd(i, j):
    if min(i, j) == 0:
        return max(i, j)
    else:
        return gcd(min(i, j), abs(i % j))

print(gcd(24, 16))
print(gcd(255, 25))

