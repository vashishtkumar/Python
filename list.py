# A built-in data types that stores set of values
#It cna store elements of different types (integer, flaotm strings,float etc.)
#list is mutable


marks=[87, 64, 33, 95, 76]

student=["vashist", 25, "Male"]
print(student)
student[0]="Vashisht Kumar"
print(student)

print(len(student))  # return the size of typle

# Slicing
print(student[1:3])
print(student[-3:-1])
print(student[-1:-3:-1])
print(student)

#Some List Methods

list =[2,1,3]

list.append(4)
print(list)

list.sort() #To sort the list in ascending order
print(list)

list.sort(reverse=True) # To sort the lsit in descending order
print(list)

list.reverse()  #To revese the list
print(list)

list.insert(1,5) # To insert data idx,ele
print(list)

list.remove(5)  # Remove the first occurence of of that particilar element
print(list)

list.pop(0) # Removes the particular index
print(list)
