from car import Car

# Create object
car1 = Car(2020, "Chevrolet")

# Call acceleration method 5 times then display current speed
for i in range (5):
    car1.accelerate()
    print ("The current speed is", car1.get_speed())
    
# Call brake method 5 times then display current speed
for i in range (5):
    car1.brake()
    print ("The current speed is", car1.get_speed())