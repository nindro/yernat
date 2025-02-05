#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:
#`C = (5 / 9) * (F – 32)`
def conv(F):
    C = (5 / 9) * (F - 32)
    print(C)
F = int(input())
conv(F)
#RESULT
# F = 32
# C = 0.0