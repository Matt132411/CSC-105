#Author: Mathew Allin
# Assignment: Real Estate and Lists
#Reflection:
# I liked that this assignment helped me better understand how lists work
# and how to use loops and functions together.
#
# I struggled most with the input validation and making sure the loops
# repeated correctly when bad data was entered.
#
# A list is a variable that can store multiple values in one place.
# Lists work by allowing you to add, remove, sort, and access values
# using positions called indexes.
#
# A list could be used in a previous project to store quiz scores or
# store multiple usernames entered by the user.

#Input

def getFloatInput(strPromptMA):

    while True:

        try:
            fltValueMA = float(input(strPromptMA))

            if fltValueMA <= 0:
                print("Value must be greater than zero.")
            else:
                return fltValueMA

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def getMedian(lstValuesMA):

    intCountMA = len(lstValuesMA)
    intMiddleMA = intCountMA // 2

    if intCountMA % 2 == 1:
        return lstValuesMA[intMiddleMA]

    else:
        return (lstValuesMA[intMiddleMA] +
                lstValuesMA[intMiddleMA - 1]) / 2


lstSalesMA = []

while True:

    fltSalesPriceMA = getFloatInput(
        "Enter property sales value: "
    )

    lstSalesMA.append(fltSalesPriceMA)

    strAgainMA = input(
        "Enter another value Y or N: "
    )

    while strAgainMA.upper() not in ["Y", "N"]:
        strAgainMA = input(
            "Please enter Y or N: "
        )

    if strAgainMA.upper() == "N":
        break


lstSalesMA.sort()

print("\nSales Values:")

for fltSaleMA in lstSalesMA:
    print(f"${fltSaleMA:,.2f}")


fltMinMA = min(lstSalesMA)
fltMaxMA = max(lstSalesMA)
fltTotalMA = sum(lstSalesMA)
fltAverageMA = fltTotalMA / len(lstSalesMA)
fltMedianMA = getMedian(lstSalesMA)
fltCommissionMA = fltTotalMA * 0.03


print("\nStatistics")

print(f"Minimum: ${fltMinMA:,.2f}")
print(f"Maximum: ${fltMaxMA:,.2f}")
print(f"Total: ${fltTotalMA:,.2f}")
print(f"Average: ${fltAverageMA:,.2f}")
print(f"Median: ${fltMedianMA:,.2f}")
print(f"Commission: ${fltCommissionMA:,.2f}")

input("\nPress Enter to close...")
