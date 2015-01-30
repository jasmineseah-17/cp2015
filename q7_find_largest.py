
# Finding the largest number in an array

def find_largest(alist):
    alist.sort()
    return alist[-1]

a = [5, 1, 8, 7, 2]
print(find_largest(a))


