


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f'{self.__width:.2f} cm'

    @property #methods
    def height(self):
        return f'{self.__height:.2f} cm'

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print('Width must be greater than 0')

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print('Height must be greater than 0')

rectangle = Rectangle(20, 30)
print(rectangle.width)
print(rectangle.height)
rectangle.height = 56.56