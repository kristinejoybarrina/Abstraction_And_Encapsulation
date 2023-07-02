# Kristine Joy Barrina  # BSCPE 1-5
# Abstraction and Encapsulation
# July 1, 2023

# Pseudocode

# Create class
class Pet:

# Create constructor with attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

# Create methods
    def set_name (self, name):
        self.__name = name
        return self.__name
    
    def set_animal_type (self, animal_type):
        self.__animal_type = animal_type
        return self.__animal_type
    
    def set_age (self, age):
        self.__age = age
        return self.__animal_type
    
    def get_name (self):
        return self.__name
    
    def get_animal_type (self):
        return self.__animal_type
    
    def get_age (self):
        return self.__age

# Display output
