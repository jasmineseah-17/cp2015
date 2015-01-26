
# Computing the volume of a cylinder

import math
#radius, length = input("Please enter radius and length:")

radius = int(input("Please enter radius in cm: "))
length = int(input("Please enter length in cm: "))

area = round(radius * radius * math.pi, 5)
volume = round(area * length, 0)
volume1 = int(volume)
print(volume1, "cm3")