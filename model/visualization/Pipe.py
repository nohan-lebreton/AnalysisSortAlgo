from model.visualization.Color import Color

class Pipe:
    """
        Represents a Pipe object with value, position, width, height, and color.
    """
    def __init__(self, value : int, pos_x : int, pos_y : int, width : int, height : int, color : tuple):
        """
            Initializes a Pipe object with a value, position, width, height, and color.
        """
        self.__value : int = value
        self.__pos_x : int = pos_x
        self.__pos_y : int = pos_y
        self.__width : int = width
        self.__height : int = height
        self.__color : tuple = color

        # Couleur de base
        self.__COLOR : tuple = color
        
    # Getters & Setters

    def getValue(self) -> int:
        """
            Returns the value of the Pipe.

            return : 
                (int) : the value of the Pipe.
        """
        return self.__value

    def setValue(self, newValue : int):
        """
            Modifies the value of the Pipe.
            arg :
                newValue (int) : he new value of the Pipe
        """
        self.__value = newValue

    def getPos_x(self) -> int:
        """
            Returns the horizontal position of the Pipe.
            return: 
                (int) : The horizontal position of the Pipe.
        """
        return self.__pos_x

    def setPos_x(self, newPos_x : int):
        """
            Modifies the horizontal position of the Pipe.
            arg : 
                newPos_x (int) : The new horizontal position of the Pipe.
        """
        self.__pos_x = newPos_x


    def getPos_y(self) -> int:
        """
            Returns the vertical position of the Pipe.
            return :
                (int) : The vertical position of the Pipe.
        """
        return self.__pos_y

    def setPos_y(self, newPos_y : int):
        """
            Modifies the vertical position of the Pipe.
            arg : 
                newPos_y (int) : The new vertical position of the Pipe.
        """
        self.__pos_y = newPos_y


    def getWidth(self) -> int:
        """
            Returns the width of the Pipe.
            return :
                (int) : The width of the Pipe.
        """
        return self.__width

    def setWidth(self, newWidth : int):
        """
            Modifies the width of the Pipe.
            arg : 
                newWidth (int) : The new width of the Pipe.
        """
        self.__width = newWidth


    def getHeight(self) -> int:
        """
            Returns the height of the Pipe.
            return :
                (int) : The height of the Pipe.
        """
        return self.__height

    def setHeight(self, newHeight : int):
        """
            Modifies the height of the Pipe.
            arg : 
                newHeight (int) : The new height of the Pipe.
        """
        self.__height = newHeight


    def getColor(self) -> tuple:
        """
            Returns the color of the Pipe.
            return :
                (int) : The color of the Pipe.
        """
        return self.__color

    def setColor(self, newColor : tuple):
        """
            Modifies the color of the Pipe.
            arg : 
                newColor (int) : The new color of the Pipe.
        """
        self.__color = newColor

    def getCOLOR(self) -> tuple:
        """
            Returns the base color of the Pipe.
            return :
                (int) : The base color of the Pipe.
        """
        return self.__COLOR

    def setCOLOR(self, newColor):
        """
            Modifies the base color of the Pipe.
            arg : 
                newColor (int) : The new base color of the Pipe.
        """
        self.__COLOR = newColor


    def __str__(self) -> str:
        """
            Returns a string representation of the Pipe.
        """
        return "Pipe n°{}".format(self.__value)