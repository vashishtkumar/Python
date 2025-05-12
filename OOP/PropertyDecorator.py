class Student:

    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem

    @property
    def Percentage(self):
        return str((self.phy+self.math+self.chem)/3)+" % "
    

s1=Student(90,90,90)

print(s1.Percentage)
s1.math=68
print(s1.Percentage)
              