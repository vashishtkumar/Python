def lines(file):
    found=False

    with open(file,"r") as f:
        content=f.readlines()

        for i in content:
            if "learning" in i:
                print("found at ", i.strip())
                found=True
                break
        if(not found):
            print("Not found")

lines("practice.txt")