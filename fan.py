# Kristine Joy Barrina  # BSCPE 1-5
# Abstraction and Encapsulation
# July 1, 2023

# Pseudocode

# Create a class
class Fan:

# Create 3 constants
    SLOW = 1
    MEDIUM = 2
    FAN = 3

# Create constructor
    def __init__(self, speed = "SLOW", on= "False", radius= 5, color="blue"):
        self.__speed = int(speed)
        self.__on = bool(on)
        self.__radius = float(radius)
        self.__color = str(color)

# Create methods (getters and setters)
    def set_speed (self, speed):
        self.__speed = speed
        return self.__speed
        
    def set_on (self, on):
        self.__on = on
        return self.__on
        
    def set_radius (self, radius):
        self.__radius = radius
        return self.__radius
        
    def set_color (self, color):
        self.__color = color
        return self.__color
        
    def get_speed (self):
        return self.__speed
        
    def get_on (self):
        return self.__on
        
    def get_radius (self):
        return self.__radius
        
    def get_color (self):
        return self.__color
    

        

# Create objects
# Display output

