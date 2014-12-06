#Indi Knighton
#6/12/2014
#Development 1

hours = int(input("Please enter the amount of hours: "))
minutes = int(input("Please enter the amount of minutes here: "))
seconds = int(input("Please enter the amount of seconds here: "))

def calculate_seconds(hours, minutes, seconds):
    hours = minutes * 60
    minutes = seconds * 60
    total_seconds = hours + minutes + seconds
    print(total_seconds)
    return total_seconds

calculate_seconds(hours, minutes, seconds)
