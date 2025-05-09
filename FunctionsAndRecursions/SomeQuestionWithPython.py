# write a program to print the length of alist (list is the parameter)

def length(list1):
    return len(list1)

list11=[10,29,45,89]
print(length(list11))


# write a program to print the elements of alist in a single ine (list is the parameter)

def Print(list1):
    for i in list1:
        print(i)

Print(list11)
print(" END ")

# write a program to find the factorial of a number

def fac(n):
    factt=1
    if(n==1):
        return factt
    
    for i in range(1,n+1):
        factt=factt*i
    return factt

print(fac(5))

# write a program to convert USD to INR

def convert(n):
    return 83*n

print(f"Rupees is = {convert(5)} Rs")
