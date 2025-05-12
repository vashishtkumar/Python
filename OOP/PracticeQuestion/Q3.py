class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2):
        if(self.price>o2.price):
           return True
        else:
            return False


o1=Order("biscuit",900)

o2=Order("bread",1000)

print(o1>o2)