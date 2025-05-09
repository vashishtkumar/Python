# Write a program to count "A" in following tuples

tup=("A","B","C","D","B","A","D","A","C")

print(tup.count("A"))

list=[]

for i in range(len(tup)):
    list.append(tup[i])

list.sort()

for i in range (len(tup)):
    print(list[i])