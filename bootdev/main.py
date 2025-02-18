class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def in_area(self, x_1, y_1, x_2, y_2):
        # direct boolean response in lieu of a if statement to determine 
        return (self.pos_x >= x_1 and self.pos_x <= x_2) and (self.pos_y >= y_1 and self.pos_y <= y_2)
    
class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        # used list comprehension in lieu of traditional for loop 
        # reason: faster computation, noticeable for larger calculations due to less function calling (i.e. no need to call append())
        return [unit for unit in units if unit.in_area(x-self.__fire_range, y-self.__fire_range, x+self.__fire_range, y+self.__fire_range)]
        
