#Instructions:
#How to run file: python3 LeapYearWithoutError.py


# Checks if year (user's input) is a leap year. 
def checkifLeapYear(userInput):
    if(userInput % 4 == 0):
        if(userInput % 100 == 0):
             if(userInput % 400 == 0):
                 return True;
             else: 
                 return False;
        else: 
           return True;
    else: 
        return False;

userInput = input("Enter a year: ");
if (checkifLeapYear(int(userInput))):
   print(int(userInput), "is a leap year.");
else: 
   print(int(userInput), "is not a leap year.");
