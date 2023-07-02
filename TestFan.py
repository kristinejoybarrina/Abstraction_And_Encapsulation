from fan import Fan

# Create Objects
fan1 = Fan (3, "on", 10, "yellow")
fan2 = Fan (2, "off", 5, "blue")

# Display output

# Fan 1 Details
print ("Fan 1\n")
print ("Speed: ", fan1.get_speed())
print ("Radius: ", fan1.get_radius())
print ("On: ", fan1.get_on())
print ("Color: ", fan1.get_color())

# Fan 2 Details
print ("\nFan 2\n")
print ("Speed: ", fan2.get_speed())
print ("Radius: ", fan2.get_radius())
print ("On: ", fan2.get_on())
print ("Color: ", fan2.get_color())