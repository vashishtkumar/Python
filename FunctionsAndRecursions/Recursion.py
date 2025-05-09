# A function callling itSelf repeatidly
# it have one base case to stop

# Write a program to print a number from 1 to n through recursion

def Print(n):
    if(n<=0):
        return
    Print(n-1)
    print(n)

Print(100)