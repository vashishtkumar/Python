def Print(list1,i):
    if(i==len(list1)):
        return
    print(list1[i])
    i+=1
    Print(list1,i)

Print([2,4,7,90,34],0)