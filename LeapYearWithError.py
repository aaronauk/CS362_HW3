#Instructions:
#How to run file: python3 LeapYearWithError.py


# Checks if user's input is an integer. 
def checkIfInteger():
  user_input = "";
  while user_input.isdigit() == False:
    user_input = input("Enter a year: ");
    if(user_input.isdigit() == True):
      return int(user_input);
    else: 
      print("Your input is not a integer.");

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


userInput = checkIfInteger();
if(checkifLeapYear(userInput)):
    print(userInput, "is a leap year.");
else:
    print(userInput, "is not a leap year.");
