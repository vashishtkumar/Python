str1="Hello Vashisht"
str2='Helo Vashisht2'
str3="""Hello Vashisht3"""
str4="Hello vashisht's brother"

print(str1+"\n"+str2+"\n"+str3+"\t"+str4)


# concationation

str5="Vashisht"
str6="Kumar"

print(str5+str6)

#Length of a string

str7=str5+str6

print(len(str7))

## slicing

str8="Hello Vashisht is learning python"

print(str8[5],str8[1])

print(str8[1:3])
print(str8[:4])
print(str8[5:])
print(str8[-5:-1])
print(str8[-2:-5])

#string[start:stop:step]

# Some String Functions

str9="i am Coder"

print(str9.find("Coder"))  # returns the 1st index of matching
print(str9.endswith("er"))
print(str9.capitalize())
print(str9.count("e"))
print(str9.replace("am","AMM"))

first=input("Enter the first good name ")

print(len(first))

str10="Hello America $ is the largest value in this world . India is competing against $ but see what will happens in future as  is very Strong"

print(str10.find("$"),str10.count("$"))

# TO print the Ascii Value of 

a="A"
print(ord(a))

b=97
print(chr(b))


# String is immutable that it cannot be changed
# Means that you can access but you can't change that
