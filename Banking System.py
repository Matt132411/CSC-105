#Author: Mathew Allin
#Assignment: Capstone Project
#Reflection:
# Share what you struggled with?
#   I liked that this assignment brought together a lot of the Python skills from class.
# Explain in your own 100-150 words what you learned this semester and how each of you previous coding assignments helped to prepare you to code this project?
#   I learned how Python Programming and how diffrent coding concepts work together to create a working program. I learned how to use variables, loops, functions, lists, string formatting 
#   And espicailly learned how to handle errors, alot of them. Earlier assignments helped prepare me for this final project because each one focused on a skill that was later combined into 
#   the banking system. Smaller programs taught me how to handle user input, validate data, repeat actions with loops, and organize code into functions. Overall, this semseter and project
#   helped me understand how all the concepts connect together to build a larger and better program. I think it will also help me have a better understanding of other programing languages like
#   Powershell, and Java which I use frecently at work. 


#Input

def PromptForInput(message):
    while True:
        try:
            amount = float(input(message))
            if amount > 0:
                return amount
            else:
                print("Enter a number that is > 0")
        except:
            print("Enter a valid number")


def Deposit(balanceMA, historyMA):
    amountMA = PromptForInput("Enter deposit amount: ")
    balanceMA = balanceMA + amountMA
    historyMA.append(["Deposit", amountMA])
    print(f"Deposit successful! New balance: $ {balanceMA:,.2f}")
    return balanceMA


def Withdraw(balanceMA, historyMA):
    amountMA = PromptForInput("Enter withdrawal amount: ")

    if amountMA > balanceMA:
        print("Insufficient funds.")
    else:
        balanceMA = balanceMA - amountMA
        historyMA.append(["Withdraw", amountMA])
        print(f"Withdrawal successful! New balance: $ {balanceMA:,.2f}")

    return balanceMA


def CheckBalance(balanceMA):
    print(f"Your current balance is: $ {balanceMA:,.2f}")


def TransactionHistory(historyMA):
    print("Transaction History:")
    print("+--------------------------------------+")
    
    if len(historyMA) == 0:
        print("| No transactions yet.                 |")
    else:
        for transactionMA in historyMA:
            print(f"| {transactionMA[0]:<15} $ {transactionMA[1]:>15,.2f} |")
    
    print("+--------------------------------------+")


def InterestApplication(balanceMA, historyMA):
    if balanceMA == 0:
        print("Balance is 0, so no interest will be calculated.")
    else:
        rateMA = PromptForInput("Enter interest rate: ")
        interestMA = balanceMA * (rateMA / 100 / 12)
        balanceMA = balanceMA + interestMA
        historyMA.append(["Interest", interestMA])
        print(f"Interest applied: {interestMA:,.2f}! New balance: $ {balanceMA:,.2f}")

    return balanceMA


def ProduceStatement(historyMA):
    fileMA = open("maBankStatements.txt", "w")

    fileMA.write("Bank Statement\n")
    fileMA.write("==============================\n")

    if len(historyMA) == 0:
        fileMA.write("No transactions.\n")
    else:
        for transactionMA in historyMA:
            fileMA.write(f"{transactionMA[0]:<15} $ {transactionMA[1]:>15,.2f}\n")

    fileMA.close()


def main():
    balanceMA = 0
    historyMA = []

    while True:
        print()
        print("Welcome to Mathew Allin's Python Mini Banking System")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Calculate and Apply Interest")
        print("6. Exit")

        choiceMA = input("Choose an option (1-6): ")

        if choiceMA == "1":
            balanceMA = Deposit(balanceMA, historyMA)
        elif choiceMA == "2":
            balanceMA = Withdraw(balanceMA, historyMA)
        elif choiceMA == "3":
            CheckBalance(balanceMA)
        elif choiceMA == "4":
            TransactionHistory(historyMA)
        elif choiceMA == "5":
            balanceMA = InterestApplication(balanceMA, historyMA)
        elif choiceMA == "6":
            ProduceStatement(historyMA)
            print("Thank you! You're using Mathew's Banking System and Statement Generated. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


main()


