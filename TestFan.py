from fan import Fan

fan1 = Fan (3, "on", 10, "yellow")
fan2 = Fan (2, "off", 5, "blue")

print ("Fan 1 Details\n")
print ("Speed: ", fan1.get_speed())
print ("Radius: ", fan1.get_radius())
print ("On: ", fan1.get_on())
print ("Color: ", fan1.get_color())