# Functions in python are piece of code or block of statements that perform a specific task.

def sum(a,b):
    return a+b

print(sum(10,20))

# Default Parameter


def sum1(a,b=90):     # but can't do this def sum1(b=10,a)
    return a+b

print(sum1(8))

