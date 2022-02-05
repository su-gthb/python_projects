#Practice Notebook: Methods and Classes
#The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are 
# the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors requested.

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        """Information about Current floor"""
        return "Current floor: {}".format(self.current)
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > 0:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= self.bottom and floor <= self.top:
            self.current = floor
        elif floor < 0:
            self.current = 0
        else:
            self.current = 10

elevator = Elevator(-1, 10, 0)