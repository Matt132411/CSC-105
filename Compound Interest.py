#Author: Mathew Allin
#Assignment: Compound Interest
# Reflection:
# What I liked about this assignment:
# I liked that it made me think about how math formulas can
# actually be used inside a Python program.
#
# What I struggled with:
# The formatting of the final number and making sure the
# currency output matched the example exactly.
#
# Why we needed () in the formula:
# The parentheses make sure Python calculates parts of the
# formula in the correct order before finishing the rest
# of the equation.
#
# Top 3 things I learned:
# 1. How to take user input and convert it to floats
# 2. How to apply a math formula inside a program
# 3. How to format numbers as currency with commas and decimals


#Input

fPrincipalMA = float(input("Enter the starting principal: "))
fRateMA = float(input("Enter the annual interest rate: "))
iCompoundMA = int(input("How many times per year is the interest compounded? "))
iYearsMA = int(input("For how many years will the account earn interest? "))

fRateMA = fRateMA / 100

fFutureValueMA = fPrincipalMA * (1 + (fRateMA / iCompoundMA)) ** (iCompoundMA * iYearsMA)

print("At the end of {} years you will have ${:,.2f}" .format(iYearsMA, fFutureValueMA))   

input("\nPress Enter to close...")
