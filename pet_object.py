from pet import Pet
import pyfiglet
from colorama import Back, Style, Fore

# Display output


# Let the user input their pet's name, type, and age

pet_text = pyfiglet.figlet_format("Pet", font = "bulbhead" )
print(pet_text)

print (Fore.GREEN + "Tell", Fore.BLUE + "me", Fore.YELLOW + "about", Fore.RED + "your", Fore.MAGENTA + "pet!\n")

# user interface
name = input(str(Fore.CYAN + "\033[1mWhat's your pet's name: " + Style.RESET_ALL))
animal_type = input(str(Fore.CYAN + "\033[1mWhat's the type of your pet: " + Style.RESET_ALL))
age = input(str(Fore.CYAN + "\033[1mWhat's your pet's age: " + Style.RESET_ALL))

# Create an instance of the class
pet1 = Pet(name, animal_type, age)

# Set the data from the user
pet1.set_name(name)
pet1.set_animal_type(animal_type)
pet1.set_age(age)

# Get the data
print (Fore.GREEN + "\n\033[1mPet's name: ", pet1.get_name())
print (Fore.YELLOW + "\033[1mType of pet: ", pet1.get_animal_type())
print (Fore.MAGENTA + "\033[1mPet's age: ", pet1.get_age(), Style.RESET_ALL)