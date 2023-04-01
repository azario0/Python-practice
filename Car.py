""" Implement Car class:
Car: the constructor for car must take two arg. the first of them is its maximum speed, and the second is a string that denotes the units in which speed . Given: either "km/h" or "mph". The class must be implemented to return a string  based on the args. For example, if car is an object of class Car with maximum speed 120, and the unit is "km/h", then print _car_ prints the following string: "Car with the maximum speed of 120 km/h", without quotes. if the max speed is 94 and the know is "mph", then printing prints in the following string: "Car with maximum speed of 94 mph", without  quotes.
"""
class Car:
    def __init__(self, max_speed, units):
        """ takes two args, `max_speed` and `units`, and initializes instance variables with same names"""
        self.max_speed = max_speed
        self.units = units
        
    def __str__(self): 
        """ returns a string that represents the object. It uses an  f-string to format the output string string based on the instance variables `max_speed` and `units`"""
        return f"Car with  maximum speed of {self.max_speed} {self.units}"

car = Car(int(input()), "km/h")
print(car)
car_1 = Car(int(input()), "mph")
print(car_1)