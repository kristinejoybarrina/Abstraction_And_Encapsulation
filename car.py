# Kristine Joy Barrina  # BSCPE 1-5
# Abstraction and Encapsulation
# July 1, 2023

class Car:
    def __init__(self, year_model, make, speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
        
    def accelerate (self):
        speed = self.__speed + 5 
        return speed
    
    def brake (self):
        speed = self.__speed - 5
        return speed
    
    def get_speed (self):
        speed = self.__speed
        return speed
    
car1 = Car(2020, "ewan", 60)

print (car1.accelerate())
print (car1.brake())
print (car1.get_speed())