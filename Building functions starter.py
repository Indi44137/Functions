#Indi Knighton
#18/11/2014
#Building functions

def calculate_basic_pay(hours, pay):
    total_pay = hours * pay
    return total_pay

def calculate_overtime_pay(hours, pay):
    overtime_pay = (hours-40) * (pay*1.5)
    basic_pay = 40 * pay
    total_pay = basic_pay + overtime_pay
    return total_pay

def calculate_total_pay(hours, pay):
    if hours <=40:
        total_pay = calculate_basic_pay(hours, pay)
    else:
        total_pay =  calculate_overtime_pay(hours, pay)
    return total_pay

def work_details():
    hours = int(input("Please enter how much hours you work weekly: "))
    pay = float(input("Please enter how much you get payed hourly: "))
    return hours, pay

def calculate_pay(hours, pay):
    hours, pay = work_details()
    total_pay = calculate_total_pay(hours, pay)
    return total_pay

def display_total_pay(total_pay):
    total_pay = calculate_pay(hours, pay)
    return total_pay

#main program
hours, pay = work_details()
total_pay = calculate_total_pay(hours, pay)
print(total_pay)



