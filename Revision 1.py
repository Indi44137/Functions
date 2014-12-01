#Indi Knighton
#30/11/2014
#Revision task 1

import math

symbol = str(input("Please enter a symbol here: "))
integer = int(input("Please enter the amount of times you would like the symbol to be displayed:" ))
    
def outputsymbols():
    for count in range(1):
        answer = integer * symbol
        print(answer) 
    
outputsymbols()
