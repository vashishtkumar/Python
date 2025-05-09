def check(n):
    str=""
    if(n%2==0):
        str="EVEN"
    else:
        str="ODD"
    return str

num=int(input("ENter your NUmber = ", ))

print(check(num))