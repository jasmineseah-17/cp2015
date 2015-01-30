
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
    print("{0:<5} {1:<5} {2:<5} {3:<5} {4:<5} {5:<5} {6:<5} {7:<5} {8:<5} {9:<5}"
    .format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
    del a[0:10]
    count += 1
    if count == 100:
        break
