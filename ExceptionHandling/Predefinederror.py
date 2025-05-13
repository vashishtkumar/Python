a=10
b=20

try:
    print(a/b)
    k=int(input("Enter a Number "))
    print(k)

except ZeroDivisionError as e:
    print("you can't divide a number by 0",e)

except ValueError as e:
    print("An Value error has occured ",e)

except Exception as e:
    print("AN error has occured that is" ,e)

finally:
    print("Everything done")