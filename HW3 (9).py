def Roman_Numerals_func(numeral):
    if numeral == "I":
        number = 1
    elif numeral == "II":
        number = 2
    elif numeral == "III":
        number = 3
    elif numeral == "IV":
        number = 4
    else:
        number = 5
    return number
numeral = input("Enter a Roman Numeral between I-V: ")
print ("Your Roman numeral is: {0}".format(str(numeral))) 
print ("Your Number is: {0}".format(str(Roman_Numerals_func(numeral))))
