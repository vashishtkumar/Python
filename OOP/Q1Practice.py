class Marks:
    def __init__(self,java,python,javascript):
        self.java=java
        self.python=python
        self.javascript=javascript

    def avg(self):
        return (self.java+self.python+self.javascript)/3
    
m1=Marks(90,90,90)

print(int(m1.avg()))