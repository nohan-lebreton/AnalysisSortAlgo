import pygame, sys
from pygame.locals import *

from model.visualization.Color import Color

# Classe qui initialise une fenêtre Pygame.
class Window :
    """
        A class that initializes a Pygame window.
    """
    def __init__(self, width : int, height : int, title : str):
        """
            Initializes the Pygame window with the given width, height, and title.
        """
        pygame.init()
        self.__width : int = width
        self.__height : int = height
        self.__title : str = title
        self.__screen : pygame.Surface = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.__color : tuple = Color.BLACK

    def run(self):
        """
            Runs the main Pygame event loop for the window.
        """
        running : bool = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        self.__quit()


    def __quit(self):
        """
            Closes the window and cleans up Pygame resources.
        """
        pygame.quit()
        sys.exit()


    
    def drawUpdate(self, rect : pygame.Rect = None):
        """
            Updates the display with any new elements drawn on the screen.
        """
        if rect == None:
            pygame.display.update()
        else:
            pygame.display.update(rect)




    def resetScreen(self):
        """
            Completely clears the window.
        """
        self.__screen.fill(self.__color)

    def erasePartScreen(self, pos_x, pos_y, width, height):
        """
            Erases a rectangular section of the window.
        """
        return pygame.draw.rect(self.__screen, self.__color, (pos_x, pos_y, width, height))

    # Getters & Setters

    def getWidth(self) -> int:
        """
            Returns the width of the window.
        """
        return self.__width

    def setWidth(self, newWidth : int):
        """
            Sets the width of the window to a new value.
        """
        self.__width = newWidth

    def getHeight(self) -> int:
        """
            Returns the height of the window.
        """
        return self.__height

    def setHeight(self, newHeight : int):
        """
            Sets the height of the window to a new value.
        """
        self.__height = newHeight

    def getTitle(self) -> str:
        """
            Returns the title of the window.
        """
        return self.__title 

    def setTitle(self, newTitle : str):
        """
            Sets the title of the window to a new value.
        """
        self.__title = newTitle

    def getScreen(self) -> pygame.Surface:
        """
            Returns the surface object representing the window.
        """
        return self.__screen

    def getColor(self) -> tuple:
        """
            Returns the background color of the window.
        """
        return self.__color

    def setColor(self, newColor : tuple):
        """
            Sets the background color of the window to a new value.
        """
        self.__color = newColor