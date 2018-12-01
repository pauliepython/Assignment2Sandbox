import sys

def parseNumber(numstr):
    num = float(numstr)
    print("Parsed succesfully, got", num)
    return num


numstr = input("Enter a number:")

try:
    num = parseNumber(numstr)
    print("You entered: ",num)

except (EOFError, ValueError) as err:
    print("Error:", err)
