class Complex:
    def __init__(self,real,imag):
        self.imag=imag
        self.real=real

    def showNumber(self):
        print(f"{self.real}i {self.imag}j")

    def __add__(self,c2):
        newImag=self.imag+c2.imag
        newReal=self.real+c2.real
        return Complex(newReal,newImag)


c1=Complex(9,8)
c1.showNumber()

c2=Complex(7,5)
c2.showNumber()

# c3=c1.add(c2)
# c3.showNumber()

c3=c1+c2
c3.showNumber()