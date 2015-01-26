
# Conversion from miles to kilometres

print("Miles", "Kilometers", "Kilometers", "Miles")

for item in range(1, 11):
    mile = item
    kilometer = 1.609 * mile
    kilometers = 15 + item * 5
    miles = kilometers / 1.609
    print(("{0:<5.0f} {1:<10.3f} {2:<10.0f} {3:<5.3f}").format(mile, kilometer, kilometers, miles))