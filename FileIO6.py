import sys

def parseNumber(numstr):
    num = float(numstr)
    print("Parsed succesfully, got", num)
    return num


numstr = input("Enter a number:")

try:
    num = parseNumber(numstr)
    print("You entered: ",num)

except ValueError as err:
    print("Incorrect value entered", numstr,"Message:", err)