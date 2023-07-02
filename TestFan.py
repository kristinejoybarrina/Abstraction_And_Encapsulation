from fan import Fan
import pyfiglet
from colorama import Style, Fore, Back

# Create Objects
fan1 = Fan (3, 1, 10, "yellow")
fan2 = Fan (2, 0, 5, "blue")

# Display output

fan_text = pyfiglet.figlet_format("Fan")
print (fan_text)

# Fan 1 Details
print ("\033[1mFan 1\n", Style.RESET_ALL)
print (Fore.RED + "\033[1mSpeed: ", Style.RESET_ALL, fan1.get_speed())
print (Fore.GREEN + "\033[1mRadius: ", Style.RESET_ALL, fan1.get_radius())
print (Fore.CYAN + "\033[1mColor: ", Style.RESET_ALL, fan1.get_color())
print (Fore.YELLOW + "\033[1mOn: ", Style.RESET_ALL, fan1.get_on())

# Fan 2 Details
print ("\n\033[1mFan 2\n", Style.RESET_ALL)
print (Fore.RED + "\033[1mSpeed: ", Style.RESET_ALL, fan2.get_speed())
print (Fore.GREEN + "\033[1mRadius: ", Style.RESET_ALL, fan2.get_radius())
print (Fore.CYAN + "\033[1mColor: ", Style.RESET_ALL, fan2.get_color())
print (Fore.YELLOW + "\033[1mOn: ", Style.RESET_ALL, fan2.get_on())
