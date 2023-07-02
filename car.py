# Kristine Joy Barrina  # BSCPE 1-5
# Abstraction and Encapsulation
# July 1, 2023

# Create a class
class Car:
    
    # Create a constructor
    def __init__(self, year_model, make, speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    
    # Create methods
    def accelerate (self):
        self.__speed += 5
        return self.__speed
        
    def brake (self):
        self.__speed -= 5
        return self.__speed
    
    def get_speed (self):
        return self.__speed
    
    