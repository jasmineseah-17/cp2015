
# Payroll

name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
payrate = int(input("Enter hourly pay rate:"))
cpfratein = int(input("Enter CPF contribution rate (%): "))

gross = round(abs(int(hours * payrate)), 2)
cpfrateout = round(abs(int(cpfratein * gross)), 2)
net = round(int(gross - cpfrateout),2)

print("Payroll statement for: " + name + "\nNumber of hours worked in week: " + str(hours) + "\nHourly pay rate: $" +
      "\nGross pay = $" + str(gross) + "\nCPF contribution at 20% = $" + str(cpfrateout) + "\nNet pay = $" + net)
