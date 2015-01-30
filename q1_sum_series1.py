
# Summing series

def sum_series1(i):
    total = 0
    for x in range(1, i + 1):
        if x == i + 1:
            return total
        else:
            total = round(total + 1/x, 4)
    return total

num = int(input("Enter number: "))
print(sum_series1(num))

