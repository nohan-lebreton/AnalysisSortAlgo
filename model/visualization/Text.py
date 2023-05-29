import pygame
from pygame.locals import *

from model.visualization.Color import Color

class Text:
    """
        This class represents a piece of text that can be displayed on the screen using the Pygame library. It allows the user to customize the text's content, font, size, position, color, and other properties.
    """
    def __init__(self, text, text2, pos_x, pos_y, size):
        """
            Initializes the Text object with the given properties.
        """
        self.__text = text
        self.__text2 = text2
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__fontFamily = "monospace"
        self.__size = size
        self.__color = Color.GREEN

        self.__textSurface = None
        self.__textRect = None

        self.__init()



    def __init(self):
        """
            Initializes the Text object's Pygame surface and rect attributes.
        """

        font = pygame.font.SysFont(self.__fontFamily ,self.__size)
        self.__textSurface = font.render (self.__text + self.__text2, True , self.__color)
        self.__textRect = self.__textSurface.get_rect()

        rectX, rectY, rectWidth, rectHeight = self.__textRect
    
        self.__textRect.update((self.__pos_x, self.__pos_y),(rectWidth, rectHeight))




    def getText(self) -> str:
        """
            Returns the main text content.
        """
        return self.__text

    def setText(self, newText : str):
        """
            Sets the main text content to the given string and updates the Pygame surface and rect.
        """
        self.__text = newText
        self.__init()

    def getText2(self) -> str:
        """
            Returns the additional text content.
        """
        return self.__text2

    def setText2(self, newText : str):
        """
            Sets the additional text content to the given string and updates the Pygame surface and rect.
        """
        self.__text2 = newText
        self.__init()

    def getPos_x(self) -> int:
        """
            Returns the x-coordinate of the text's top-left corner.
        """
        return self.__pos_x

    def setPos_x(self, newPos_x : int):
        """
            Sets the x-coordinate of the text's top-left corner to the given value and updates the Pygame surface and rect.
        """
        self.__pos_x = newPos_x
        self.__init()

    def getPos_y(self) -> int:
        """
            Returns the y-coordinate of the text's top-left corner.
        """
        return self.__pos_y

    def setPos_y(self, newPos_y : int):
        """
            Sets the y-coordinate of the text's top-left corner to the given value and updates the Pygame surface and rect.
        """
        self.__pos_y = newPos_y
        self.__init()

    def getFontFamily(self) -> str:
        """
            Returns the name of the font family used for the text.
        """
        return self.__fontFamily

    def setFontFamily(self, newFontFamily : str):
        """
            Sets the name of the font family to use for the text and updates the Pygame surface and rect.
        """
        self.__fontFamily = newFontFamily
        self.__init()

    def getSize(self) -> int:
        """
            Returns the font size used for the text.
        """
        return self.__size

    def setSize(self, newSize : int):
        """
            Sets the font size to use for the text and updates the Pygame surface and rect.
        """
        self.__size = newSize
        self.__init()

    def getColor(self) -> Color:
        """
            Returns the color used for the text.
        """
        return self.__color

    def setColor(self, newColor : Color):
        """
            Sets the color to use for the text and updates the Pygame surface and rect.
        """
        self.__color = newColor
        self.__init()

    def getTextSurface(self) -> pygame.Surface:
        """
            Returns the Pygame surface that contains the rendered text.
        """
        return self.__textSurface

    def setTextSurface(self, newTextSurface : pygame.Surface):
        """
            Sets the Pygame surface that contains the rendered text and updates the Text object's attributes.
        """
        self.__textSurface = newTextSurface
        self.__init()

    def getTextRect(self) -> pygame.Rect:
        """
            Returns the rectangle that defines the position and size of the rendered text.
        """
        return self.__textRect

    def setTextRect(self, newTextRect : pygame.Rect):
        """
            Sets the rectangle that defines the position and size of the rendered text and updates the Text object's attributes.
        """
        self.__textRect = newTextRect
        self.__init()