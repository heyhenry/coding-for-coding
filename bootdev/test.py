class Rectangle:
    def overlaps(self, rect):
        if self.get_left_x() <= rect.get_left_x():
            return True
        elif self.get_right_x() >= rect.get_right_x():
            return True
        elif self.get_top_y() >= rect.get_top_y():
            return True
        elif self.get_bottom_y() <= rect.get_bottom_y():
            return True
        return False


    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # bottom 
    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    # top
    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    # top
    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    # bottom
    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"

reccy = Rectangle(1,1,2,2)
rectangle = Rectangle(2,2,3,3)

print(rectangle.overlaps(reccy)) # should be true