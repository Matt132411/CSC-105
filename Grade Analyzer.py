#Author: Mathew Allin
#Assignment: Grade Analyzer
#Reflection:
#   Share what you liked about this assignment?
#       I liked that this assignment helped me practice using if/elif/else statements
#       and showed how to work with multiple test scores in one program.
#   Share What you struggled with?
#       I struggled most with figuring out how to drop the lowest grade
#       without using min() or lists.
#   Share how you figured out to the drop the lowest grade and how many if statements
#       I figured it out by comparing each test score with the others
#       and then averaging the three remaining scores.
#   Share 3 things you learned on this assignment:
#       1.) How to validate user input with if statements.
#       2.) How to assign a letter grade using an if/elif/else chain.
#       3.) Using the SystemExit Code, while also adding "Press enter to close", so it does not close right away.

#Input

strNameMA = input("Name of the person we are calculating the grades for: ")

intTest1MA = int(input("Test 1: "))
intTest2MA = int(input("Test 2: "))
intTest3MA = int(input("Test 3: "))
intTest4MA = int(input("Test 4: "))

strDropLowestMA = input("Do you wish to drop the lowest grade Y or N? ")

if intTest1MA < 0 or intTest2MA < 0 or intTest3MA < 0 or intTest4MA < 0:
    print("Test Score must be greater than 0.")
    input("\nPress Enter to close...")
    raise SystemExit

if strDropLowestMA != "Y" and strDropLowestMA != "N":
    
    print("Enter Y or N to drop the Lowest Grade. Enter Y or N to Drop the Lowest Grade.")
    input("\nPress Enter to close...")
    raise SystemExit

if strDropLowestMA == "Y":
    if intTest1MA <= intTest2MA and intTest1MA <= intTest3MA and intTest1MA <= intTest4MA:
        fltAverageMA = (intTest2MA + intTest3MA + intTest4MA) / 3
    elif intTest2MA <= intTest1MA and intTest2MA <= intTest3MA and intTest2MA <= intTest4MA:
        fltAverageMA = (intTest1MA + intTest3MA + intTest4MA) / 3
    elif intTest3MA <= intTest1MA and intTest3MA <= intTest2MA and intTest3MA <= intTest4MA:
        fltAverageMA = (intTest1MA + intTest2MA + intTest4MA) / 3
    else:
        fltAverageMA = (intTest1MA + intTest2MA + intTest3MA) / 3
else:
    fltAverageMA = (intTest1MA + intTest2MA + intTest3MA + intTest4MA) / 4

if fltAverageMA >= 97.0:
    strLetterGradeMA = "A+"
elif fltAverageMA >= 94.0:
    strLetterGradeMA = "A"
elif fltAverageMA >= 90.0:
    strLetterGradeMA = "A-"
elif fltAverageMA >= 87.0:
    strLetterGradeMA = "B+"
elif fltAverageMA >= 84.0:
    strLetterGradeMA = "B"
elif fltAverageMA >= 80.0:
    strLetterGradeMA = "B-"
elif fltAverageMA >= 77.0:
    strLetterGradeMA = "C+"
elif fltAverageMA >= 74.0:
    strLetterGradeMA = "C"
elif fltAverageMA >= 70.0:
    strLetterGradeMA = "C-"
elif fltAverageMA >= 67.0:
    strLetterGradeMA = "D+"
elif fltAverageMA >= 64.0:
    strLetterGradeMA = "D"
elif fltAverageMA >= 60.0:
    strLetterGradeMA = "D-"
else:
    strLetterGradeMA = "F"

# Output
print("Name:", strNameMA)
print("Test average is:", format(fltAverageMA, ".1f"))
print("Letter Grade for the test is:", strLetterGradeMA)

input("\nPress Enter to close...")
    

    

