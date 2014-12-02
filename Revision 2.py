#Indi Knighton
#02/12/2014
#Revision 2

import math

def test_function():
    invalid = True
    while invalid:
        number = int(input("Please enter an odd number here: "))
        if number > 31 or number < 0:
            print("You have entered an invalid number! Please try again!")
        elif number % 2 != 0:
            print("You have entered a valid number!")
            invalid = False
        else:
            print("You have entered an invalid number! Please try again!")
    return number
def print_pyramid():
    number = test_function()
    while number != -1:
        pyramid = number * "*"
        print("{0:^31}".format(pyramid,number))
        number = number - 2
              
print_pyramid()
