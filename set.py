# Set is the collection of unordered items
# Each element in the set must be unique and immutable
# It can not store dictionary and list

nums={1,2,3,4,}
set2 ={1,2,2,2,"Vashisht"}

null_set=set()

print(nums)
print(set2)


# Set Methods

set1=set()

set1.add(10)  # To add an element in set
set1.add(89)
set1.add(45)
print(set1)

set1.remove(89) # To remove an element from set
print(set1)

set1.pop() # To remove an random element from an set
print(set1)

set1.clear() # To cear data from set
print(set1)

set1={1,2,3,4,10,6}
set2={1,2,4,90,35}

print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))