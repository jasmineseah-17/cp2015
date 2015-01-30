
# Summing series

def m_series(i):
    total = 0
    for x in range(1, i + 1):
        frac = x / (x + 1)
        total = float(total + frac)
        print("{0:<10} {1:<10.4f}".format(x, total))

print("{0:<10} {1:<10}".format("i", "m(i)"))

m_series(20)
