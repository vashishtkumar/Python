class Car:
    color="black"
    
    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stopped")

class TATA(Car):
    def __init__(self):
       self.name="TATA PUNCH"

car1=TATA()
car1.start()
print(car1.name)