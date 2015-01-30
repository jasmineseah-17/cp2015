
# Summing series

def sum_series2(i):
    total = 0
    for x in range(1, i + 1):
        if x == i + 1:
            return total
        else:
            total = round(total + x/(2*x + 1), 4)
    return total

num = int(input("Enter number: "))
print(sum_series2(num))
