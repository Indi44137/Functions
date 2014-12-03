#Indi Knighton
#03/12/2014
#Revision task 3

number1 = int(input("Please enter a number here: "))
number2 = int(input("Please enter a number here: "))

def sort(number1, number2):
    if number1 > number2:
        print("{0}, {1}".format(number2, number1))
    else:
        print("{0}, {1}".format(number1, number2))

sort(number1, number2)
              
