#Indi Knighton
#6/12/2014
#Revision 4

import math

temperature = int(input("Please enter the teperature in fahrenheit: "))

def convert_to_celsius(temperature):
    fahrenheit = temperature
    celsius = (fahrenheit - 32) * (5/9)
    print(celsius)
    return celsius

convert_to_celsius(temperature)

