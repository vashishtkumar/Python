# Write a Program to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

num1=["abc",2,3,2,"abc"]

lis1=["abc",1,"abc"]

num1_copy=num1.copy()
num1_copy.reverse()
flag=False

for i in range(len(lis1)):
    if(num1[i]!=num1_copy[i]):
        print("It is not plaindrome")
        flag=True
        break
if(not flag):
    print("It is plaindrome")


