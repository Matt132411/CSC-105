# Author: Mathew Allin
# Assignment: Temp Convertor
# Reflection:
# Share what you liked about this assignment?
#   Seeing all the diffrent ways you can use, if/elif/else, also using the else/if in diffrent contexts. 
# Share waht you struggled with?
#   Printing the correct answer or using format. Took me quite a few tries to get it right.
# Explain How the if/else and if/elif/else works and how the differ.
# Which one did you code for this assignment?
#    Using all three was good to pick between F or C but also if someone enters an invalid choice in this case. Meaning it works well when there is more than two choices, if/else works well if there is only two.
# Share 3 things you learned on this assignment:
#   One thing I learned was how to properly use if/elif/else statements to control the flow of a program based on user input.
#   Another thing I learned was how to use float input and apply formulas to convert values from one unit to another.
#   Lastly, I learned how to format output so numbers display in a cleaner way, such as rounding to one decimal place.

#Input

print ("Mat's Tempeture Convertor")

fTempMA = float(input("Enter a temperature: "))
sScaleMA = input("Is the temperature Fahrenheit or Celsius, enter F or C: ")

if sScaleMA == "F" or sScaleMA == "f":
    if fTempMA > 212:
        print ("Temperature cannot be greater than 212")
    else:
        fCelsiusMA = (5.0 / 9) * (fTempMA - 32)
        print ("The Celsius is equivalent to", format(fCelsiusMA, ".1f"))

elif sScaleMA == "C" or sScaleMA == "c":
    if fTempMA > 100:
        print("Temperature cannot be greater than 100")
    else: fFahrenheitMA = ((9.0 / 5.0) * fTempMA) + 32
    print("The Fahrenheit equivalent is:", format(fFahrenheitMA, ".1f"))
else:
    print("You must enter a F or C")

input ("\nPress enter to close...")
