# Complete the unit's in_area method and the dragon's breathe_fire method.

# in_area
# This method has four parameters, x_1, y_1, x_2, and y_2.
# The coordinates x_1 and y_1 represent the bottom-left corner of the rectangle, while x_2 and y_2 represent the top-right corner.

# To determine if a unit is within or on the boundary of this rectangle, use the unit's position coordinates pos_x and pos_y.
# If the unit's position falls inside or on the edge of the rectangle, the method returns True. Otherwise, it returns False.

# breathe_fire
# This method causes the dragon to breathe a swath of fire in the target area.
# The target area is centered at (x,y). The area stretches for __fire_range in both directions inclusively.

# For each unit in the units list, append that unit to a list if the unit is within the blast. Return the list of units hit by the blast.


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2) -> bool:
        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        x_2 = x + self.__fire_range
        y_2 = y + self.__fire_range
        x_1 = x - self.__fire_range
        y_1 = y - self.__fire_range
        unit_hits = []
        for unit in units:
            is_hit = unit.in_area(x_1, y_1, x_2, y_2)
            if is_hit:
                unit_hits.append(unit)
        return unit_hits
