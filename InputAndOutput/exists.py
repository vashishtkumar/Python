def exists(path):
    with open(path,"r") as f:
        content=f.read()
        if "learnings" in content:
           print("Yes")
        else:
            print("no")

exists("practice.txt")