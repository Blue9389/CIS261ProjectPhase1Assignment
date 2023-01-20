#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked function
def GetHoursWorked():
    hoursWorked = float(input("Enter hours worked: "))
    return hoursWorked
#write the GetHourlyRate function
def GetHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

# write the GetTaxRate function
def GetTaxRate():
    taxRate = float(input("Enter Tax Rate:" ))
    return taxRate



def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    print(f"{hourlyRate:,.2f}"  f"{grosspay:,.2f}"  f"{taxRate:,.2%}"  f"{incometax:,.2f}"  f"{netpay:,.2f}")
    # taxrate needs to be formatted as percentage





    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total numbers of hours:  {TotHours} .2f")
    print(f"Total gross pay:  {TotGrossPay}, .2f")
    print(f"Total tax:  {TotTax}, .2f")
    print(f"Total net pay:  {TotNetPay}, .2f")
if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hoursWorked = GetHoursWorked()
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hourlyRate = GetHourlyRate()
        # write the code to assign to taxrate the return value from GetTaxRate
        taxRate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hoursWorked, hourlyRate, taxRate)
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        printinfo(empname, hoursWorked, hourlyRate, grosspay, taxRate, incometax, netpay)
        TotEmployees += 1 
        TotHours += hoursWorked
        # write the code to increment the other total variables with the appropriate values



    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)


