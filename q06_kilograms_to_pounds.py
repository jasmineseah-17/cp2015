
# Conversion from kilograms to pounds

print("Kilograms", "Pounds")
for item in range(1, 11):
    kilogram = item
    pound = 2.2 * kilogram
    #print(kilogram, pound)
    print(("{0:<10.0f} {1:<10.1f}").format(kilogram, pound))