# python can be used to perform operations ona file (read & write data)
# Types of files:
# Text Types: .txt, .docx, .log etc
# Binary Files: .mp4, .mov, .jpeg, .png etc


# Open , Read and close file

f=open("sample.txt","r")
data = f.read()
print(data)
f.close()


f=open("sample.txt","w+")

data=f.write("Over rideen by vashisht")
print(data)
f.close()

f=open("sample.txt","r")
data=f.readline()
print(data)

data=f.readline()
print(data)

# with Syntax

with open("sample.txt","a+") as f:
    data=f.read()
    print(data)


# Deleting a File

import os
os.remove("sample.txt")