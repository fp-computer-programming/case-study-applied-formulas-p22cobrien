# Author: CMOB 10/12/2021

x_1 = input("what is the 1st x coordinate? ")
y_1 = input("what is the 1st y coordinate? ")
x_2 = input("what is the 2nd x coordinate? ")
y_2 = input("what is the 2nd y coordinate? ")

distance = ((((float(x_2) - float(x_1)) ** 2) + ((float(y_2) - float(y_1)) ** 2)) ** 0.5)

print("the distance between the two points is " + str(distance))
