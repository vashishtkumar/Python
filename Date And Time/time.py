import time as t

print(t.time()) # time since epoch that 1st jan 1970

#t.sleep(9) stops execution of program for t seconds

print(t.localtime())

print("Readable time: ",t.asctime(t.localtime()))

print(t.strftime("%d-%B-%Y"),t.localtime())