"""
Boat: The constructor for Boat must take a single argument denoting its maximum speed in knots. The class must be implemented to return a string based on the arg. for example, if boat is an object of class Boat with maximum speed of 82, then printing boat prints the following string "Boat with the maximum speed of 82 knots" without quotes.
class Boat:
"""
class Boat:
    def __init__(self, max_speed):
        """ takes single arg `max_speed`, and initializes an instance variable with the same time"""
        self.max_speed = max_speed
        
    def __str__(self):
        """  returnd a string that represents the object it uses an f-string to fformat the output string based on the instance variables `max_speed`"""
        return f"Boat with maximum speed of {self.max_speed} knots"
    
boat = Boat(int(input("Enter the max speed of the boat (in numbers ) : ")))
print(boat)