
# Reverse the digits in an integer recursively

def reverse_int(n):
    x = int(str(n)[::-1]) # Cheat way of reversing by reading from end
    return x

print(reverse_int(int(input("Enter integer: "))))