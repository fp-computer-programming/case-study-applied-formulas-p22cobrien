# Author: CMOB 10/12/2021

p = input("What is the initial investment amount? ")
r = float(input("What is the annual interest rate as a percent? "))
t = input("What is the amount of time in years that the money is invested? ")
n = float(12)
r /= 100

a = float(p) * (1 + (float(r) / n)) ** (n * float(t))

print(a)
