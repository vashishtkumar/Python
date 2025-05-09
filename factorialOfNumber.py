n=5
fact=1
for i in range(n+1):
    if(i ==0 ):
        print(f"The factorial of {i} =" ,fact)
        continue
    fact=i*fact
    print(f"The factorial of {i} =" ,fact)