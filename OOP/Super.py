# Super is used to access the methods of their Parent class

class Car:
    color="black"

    def __init__(self,type):
       self.type=type

    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stopped")

class TATA(Car):
    def __init__(self,type):
       self.name="TATA PUNCH"
       super().start()
       super().__init__(type)


car1=TATA("diesel")
print(car1.name)
print(car1.type)