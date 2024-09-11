import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled: bool = False):
        self.__sides = self.check_sides(sides)
        self.__color = self.check_color(color)
        self.filled = filled

    def check_color(self, color):
        if len(color) == 3 and self.__is_valid_color(*color):
            return color
        return [255, 255, 255]

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        return all(isinstance(i, int) and i > 0 for i in sides) and len(sides) == self.sides_count

    def check_sides(self, sides):
        if self.__is_valid_sides(sides):
            return sides
        return [1] * self.sides_count

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(list(new_sides)):
            self.__sides = new_sides

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled: bool = False):
        super().__init__(color, sides=list(sides), filled=filled)

    def get_radius(self):
        return self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled: bool = False):
        super().__init__(color, sides=list(sides), filled=filled)

    def get_square(self):
        _p = sum(self.get_sides()) / 2
        return math.sqrt(_p * (_p - self.get_sides()[0]) * (_p - self.get_sides()[1]) * (_p - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides_, filled: bool = False):

        if len(list(sides_)) == 1:
            sides_ = list(sides_) * self.sides_count
        super().__init__(color=color, sides = list(sides_), filled=filled)


    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())