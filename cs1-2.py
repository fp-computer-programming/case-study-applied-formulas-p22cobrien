# Author: CMOB 10/12/2021

p = input("What is the initial investment amount? ")
r = input("What is the annual interest rate as a percent? ")
t = input("What is the amount of time in years that the money is invested? ")

r = float(r) / 100

a = float(p) * (1 + (float(r) / 12)) ** (12 * float(t))

print("your account's value is now $" + str(a))
