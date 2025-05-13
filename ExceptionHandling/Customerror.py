
class Ageerror(Exception):
    def __init__(self, message):
       super().__init__(message)

try:
    age=int(input("Enter your age"))
    if(age < 18 ):
     raise Ageerror("you are not eligible for voting")
    else:
       print("You are eligible to vote")
except Ageerror as e:
   print("Vashsiht this is age error",e)