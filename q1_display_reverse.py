
# Displaying an integer inversed

def reverse(n):
    total = ""
    while n > 0:
        a = n % 10
        n//= 10
        total+= str(a)
    return total

x = int(input("Enter number: "))
print(reverse(x))
