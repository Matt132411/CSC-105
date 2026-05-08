#Author: Mathew Allin
#Assignment: Inter Planetary Weights

#Share what you like about this assignment?
#   I liked how it made me think about different ways I could expand on it. Honestly, it was a bit tough to stay within the assignment guidelines without wanting to add too much.

#Explain specifically how you used the Python formatting options to align the out out:
#   I used Python’s format function with "10.2f" so each weight takes up. 10 spaces and always shows 2 decimal places. This right-aligns the
#   numbers so they all line up in a clean column.

#Share Exactly three things you learned on this assignment:
#   1.) I learned IDLE shows which lines are incorrect before you can even run it.
#   2.) How to properly use float.
#   3.) How to remove a space between sNameMA and the printed text.

#Note: I couldn't fine a way to make the Weights line up perfectly like in the example.

#Input
sNameMA = input("What is your name: ")

fEarthWeightMA = float(input("What is your weight: "))

#Planets Gravity
#w = Weight
#g = Gravity

gMercuryMA = 0.38
gVenusMA = 0.91
gMoonMA = 0.165
gMarsMA = 0.38
gJupitarMA = 2.34
gSaturnMA = 0.93
gUranusMA = 0.92
gNeptuneMA = 1.12
gPlutoMA = 0.066


#Planet Weigths

wMercuryMA = fEarthWeightMA * gMercuryMA
wVenusMA = fEarthWeightMA * gVenusMA
wMoonMA = fEarthWeightMA * gMoonMA
wMarsMA = fEarthWeightMA * gMarsMA
wJupitarMA = fEarthWeightMA * gJupitarMA
wSaturnMA = fEarthWeightMA * gSaturnMA
wUranusMA = fEarthWeightMA * gUranusMA
wNeptuneMA = fEarthWeightMA * gNeptuneMA
wPlutoMA = fEarthWeightMA * gPlutoMA


print("\n" + sNameMA + "'s weight on each of our Solar System's planets is:\n")

print("Weight on Mercury:", format(wMercuryMA, "10.2f"))
print("Weight on Venus:", format(wVenusMA, "10.2f"))
print("Weight on the Moon:", format(wMoonMA, "10.2f"))
print("Weight on Mars:", format(wMarsMA, "10.2f"))
print("Weight on Jupitar:", format(wJupitarMA, "10.2f"))
print("Weight on Saturn:", format(wSaturnMA, "10.2f"))
print("Weight on Uranus:", format(wUranusMA, "10.2f"))
print("Weight on Neptune:", format(wNeptuneMA, "10.2f"))
print("Weight on Pluto:", format(wPlutoMA, "10.2f"))

input("\nPress Enter to close...")










