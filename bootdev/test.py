class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 and self.pos_x <= x_2) and (self.pos_y >= y_1 and self.pos_y <= y_2):
            return True
        return False

# class Dragon(Unit):
#     def __init__(self, name, pos_x, pos_y, fire_range):
#         super().__init__(name, pos_x, pos_y)
#         self.__fire_range = fire_range
    
#     def breathe_fire(self, x, y, units):
#         # bot_left 
#         x_1 = x-self.__fire_range
#         y_1 = y-self.__fire_range

#         # top_right 
#         x_2 = x+self.__fire_range
#         y_2 = x+self.__fire_range

#         units_hit = []
#         for unit in units:
#             if unit.in_area(x_1, y_1, x_2, y_2):
#                 units_hit.append(unit.name)
#         return units_hit

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_units = []
        for u in units:
            if u.in_area(x-self.__fire_range, y-self.__fire_range, x+self.__fire_range, y+self.__fire_range):
                hit_units.append(u.name)
        return hit_units
    
dragon = Dragon("Smaug", 6, 6, 2)
units = [
        Unit("Yvor", 1, 0),
        Unit("Nicholas", 0, 1),
        Unit("Eoin", 2, 0),
        Unit("Cian", 3, 3),
        Unit("Andrew", -1, 4),
        Unit("Baran", -6, 5),
        Unit("Carbry", 2, 1)
    ]
print(dragon.breathe_fire(1, 1, units))
