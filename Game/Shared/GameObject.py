
class GameObject:

    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_size(self):
        return self.__size

    def get_sprite(self):
        return self.__sprite

    def __intersectsY(self, other):
        other_position = other.getPosition()
        other_size = other.getSize()

        if self.__position[1] >= other_position[1] and self.__position[1] <= other_position[1] + other_size[1]:
            return 1
        if (self.__position[1] + self.__size[1]) > other_position[1] and (self.__position[1] + self.__size[1]) <= (other_position[1] + other_size[1]):
            return 1
        return 0

    def __intersectsX(self, other):
        other_position = other.getPosition()
        other_size = other.getSize()

        if self.__position[0] >= other_position[0] and self.__position[0] <= other_position[0] + other_size[0]:
            return 1
        if (self.__position[0] + self.__size[0]) > other_position[0] and (self.__position[0] + self.__size[0]) <= (other_position[0] + other_size[0]):
            return 1
        return 0

    def intersects(self, other):
        if self.__intersectsY(other) and self.__intersectsX(other):
            return 1
        return 0
