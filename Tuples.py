# A built in data types that let us create immutable sequences of values.
#it is immutable
#tup[0]=90 This is not alowed
tup =(87, 4, 33, 95, 76)

print(tup)

# some important points to remember

tup1=(0,6)
print(type(tup1))

tup1=(3,5)
print(tup1)

tup3=()
print(type(tup3))

tup4=(1)  # it will treat this as normal integer and float value is there it will treat this like that
print(type(tup4))

tup5=(1,)
print(type(tup5))


# Tuple Methods

tup=(2,1,3,1)

print(tup.index(1)) # return the first occurence

print(tup.count(1)) # return the number of counts

