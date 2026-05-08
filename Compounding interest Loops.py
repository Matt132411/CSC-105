#Author: Mathew Allin
#Assignment: Compounding Interest Loops

#Reflection:
#Share What you liked about this assignment?
#   I liked learning how loops can be used to repeat calculations over time. No matter how many months you can keep going
#Share what you struggled with?
#   I struggled with alignments of the code alot for this one.
#Explain the common and diffrence of Python while and for loops.
#   While loops run until a condition is false, for loops run a set number of times.
#Which type of loops did you use for this assignment did you use and why?
#   I used both while and for loops because one is better for counting and one for unknown loops.
#How many loops in total did you code?
#   3 Loops in Total.
#Share Three things you learned on this assignment:
#   How to properly make a loop
#   Knowing how much alignements matter the deeper into coding I go.
#   Diffrence between for a while loops.

#Input

while True:
    try:
        DepositMA = float(input("Enter Deposit: "))
        if DepositMA <= 0:
            print("Input must be a positive number.")
        else:
            break
    except:
            print("Input must be a numeric Value")

while True:
    try:
        RateMA = float(input("Enter Interest Rate Percent: "))
        if RateMA <= 0:
            print("Input must be a positive number.")
        else:
            break
    except:
        print("Input must be a numeric value.")

while True:
    try:
        MonthsMA = int(input("Enter Number of Months: "))
        if MonthsMA <= 0:
            print("Input must be a positive number.")
        else:
            break
    except:
        print("Input must be a numeric value.")

while True:
    try:
        GoalMA = float(input("Enter Goal Amount: "))
        if GoalMA < 0:
            print("Goal cannot be a negative.")
        else:
            break
    except:
        print("Input must be a numeric value.")

    
MonthlyRateMA = (RateMA / 100) / 12

BalanceMA = DepositMA

for MonthMA in range(1, MonthsMA + 1):
    InterestMA = BalanceMA * MonthlyRateMA
    BalanceMA = BalanceMA + InterestMA

    print("Month:", MonthMA,
          "Account Balance: $", format(BalanceMA, ",.2f"))

if GoalMA > 0:
    SavingsMA = DepositMA
    CounterMA = 0

    while SavingsMA < GoalMA:
        SavingsMA = SavingsMA + (SavingsMA * MonthlyRateMA)
        CounterMA += 1

    print("\nMonths to reach goal:",
          format(CounterMA, ","))
        

input("\nPress Enter to close...")
