#Indi Knighton
#18/11/2014
#Building functions

def calculate_basic_pay(hours, pay):
    basic_pay = hours * pay
    return basic_pay

def calculate_overtime_pay(hours, pay):
    overtime_pay = (hours-40) * (pay*1.5)
    basic_pay = 40 * pay
    total_pay = basic_pay + total_overtime
    return total_pay

def calculate_total_pay(hours, pay):
    if hours <=40:
        total_pay = calculate_basic_pay(hours, pay)
    else:
        total_pay =  calculate_overtime_pay(hours, pay)
        return total_pay

def work_detailshours(hours, pay):
    hours = float(input("Please enter how much hours you work weekly: "))
    pay = float(input("Please enter how much you get payed hourl: "))
    return hours, pay



#main program
total = calculate_basic_pay + calculate_overtime_pay 
print(total)
