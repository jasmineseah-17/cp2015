
# Converting milliseconds to hours, minutes, and seconds

def convert_ms(n):
    hour = n // 3600000
    x = n % 3600000
    min = x // 60000
    y = n % 60000
    sec = y // 1000
    print(str(hour) + ":" + str(min) + ":" + str(sec))

time = int(input("Enter milliseconds: "))
convert_ms(time)