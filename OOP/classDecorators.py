class Person:
    name="anonymous"

    # def __init__(self,name):
    #    #self.name=name
    #    #Person.name=name
    #     self.__class__.name=name

    # with Decorators
    @classmethod

    def changeName(cls,name):
        cls.name=name

P1=Person()
P1.changeName("Vashisht")
print(P1.name)
print(Person.name)   # Here it is also printing anonyms so for that

P2=Person()
print(P2.name)
P2.changeName("Beehyv")
print(Person.name)