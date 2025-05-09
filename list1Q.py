#   Write a program to take input three name and sort them 

list=[]

for i in range(3):
    list.append(input("Enter the " +str(i)+" name "))

list.sort()

for i in range(3):
    print(list[i])