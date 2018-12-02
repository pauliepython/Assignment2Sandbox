#This python script checks a numbers.txt file for a number
#If there's more than one number, spaces etc. it will read the first number and state the file is malformed
#Otherwise it will simply read the number, and state that no exceptions were found

try:
    numberfile = open("numbers.txt", "r")
    numbers = []
    for numstr in numberfile:
        number = float(numstr)
        numbers.append(number)
        print("Read: ", number)
except ValueError:
    print("Malformed file");
else:
    print ("No Exceptions found");

#This is used to ensure the file is closed after script is executed
finally:
    if numberfile:
        numberfile.close()