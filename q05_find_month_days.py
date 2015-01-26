
# Finding the number of days in a month

leapdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nonleapdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

year = int(input("Enter year: "))
month = int(input("Enter month (in integer form): "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(monthname[month - 1], year, "has", leapdays[month - 1], "days.")
else:
    print(monthname[month - 1], year, "has", nonleapdays[month - 1], "days.")