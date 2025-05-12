class Car:
    color="black"
    
    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stopped")

class TATA(Car):
       name="TATA PUNCH"

class Punch(TATA):
    def __init__(self):
        self.model="Adventure S"

car1=Punch()
car1.start()
print(car1.name)
print(car1.model)