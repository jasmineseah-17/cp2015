
# Prime number
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            break
    a.append(n)

a = []
for prime in range(1, 1001):
    is_prime(prime)

for x in a:
    print(a[0:10])
    del a[0:10]
print(a)
