from car import Car
from colorama import Fore, Back, Style
import pyfiglet

# Create object
car1 = Car(2020, "Chevrolet")
  
text_car = pyfiglet.figlet_format("CAR SPEED", font = "slant"  )
print(text_car)

# Call acceleration method 5 times then display current speed
for i in range (5):
    car1.accelerate()
    print (Fore.RED + "\033[1mThe current speed is", car1.get_speed())

# Call brake method 5 times then display current speed
for i in range (5):
    car1.brake()
    print (Fore.RED + "\033[1mThe current speed is", car1.get_speed(), Style.RESET_ALL)