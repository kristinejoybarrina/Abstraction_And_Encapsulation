from pet import Pet

# Display output


# Let the user input their pet's name, type, and age
print ("Introduce your pet!\n")

# user interface
name = input(str("What's your pet's name: "))
animal_type = input(str("What's the type of your pet: "))
age = input(str("What's your pet's age: "))

# Create an instance of the class
pet1 = Pet(name, animal_type, age)

# Set the data from the user
pet1.set_name(name)
pet1.set_animal_type(animal_type)
pet1.set_age(age)

# Get the data
print ("\nPet's name: ", pet1.get_name())
print ("Type of pet: ", pet1.get_animal_type())
print ("Pet's age: ", pet1.get_age())