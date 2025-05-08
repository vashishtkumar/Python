a=int(input("Enter the first Number"))
b=int(input("Enter the second Number"))
c=int(input("Enter the Third Number"))

if(a>b):
    if(a>c):
        print("The Greatest Number is = ",a)
elif(b>a):
    if(b>c):
        print("The Greatest Number is = ",b)
else:
    print("The greates Number is = ", c)
