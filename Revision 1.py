#Indi Knighton
#30/11/2014
#Revision task 1


def integer():
    number_of_symbols = int(input("Please enter the amount of symbols you would like to be displayed: "))
    return number_of_symbols

def symbol():
    sign = str(input("Please enter the synbol you would like to be displayed: "))
    return sign

def OutputSymbols(number_of_symbols, sign):
    character_symbol = symbol()
    number_of_symbols = integer()
    print(character_symbol * number_of_symbols) 
    
print(OutputSymbols(number_of_symbols, sign))
