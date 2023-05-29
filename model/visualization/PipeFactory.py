import math
from model.visualization.Pipe import Pipe
from model.visualization.Pipes import Pipes
from view.visualization.Window import Window
from model.visualization.Color import Color

class PipeFactory:
    """
        Create an empty or filled list of pipes based on the provided data.
    """

    def __init__(self, window : Window):
        self.__window : Window = window
        self.__space : int = 0

        # The location used to display information will have a height of 1/5 of the screen, but the width remains the same.
        self.__locationViewData = self.__window.getHeight() // 5

    def __createPipe(self, value : int, pos_x : int, pos_y : int, width : int, height : int, color : tuple) -> Pipe:
        """
            Create a single pipe.
        """
        return Pipe(value, pos_x, pos_y, width, height, color)


    def createPipes(self, valuesList : list) -> Pipes:
        """
            Create a list of pipes.
        """

        nbPipes : int = len(valuesList)

        """
        # si l'espace est trop grand et que chaque courbe n'est pas entouré de son espace(la 1ère courbe possède un espace avant, les autres par contre possède un espace après) alors c impossible.
        if ((self.__window.getWidth() - (nbPipes * self.__space) - self.__space) < self.__space):
            print("Impossible")
        """

        max_number : int = max(valuesList)

        pipes : Pipes = Pipes()

        color = Color()
        colors : list = color.gradient_rgb_spectrum(self.__window.getHeight())

        pos_x : int = self.__space
        pos_y : int = 0

        for i in range(nbPipes):

            listValue : int = valuesList[i]
            pipeWidth : int = (self.__window.getWidth() - (nbPipes * self.__space) - self.__space) // nbPipes

            # le -1 permet d'afficher les éléments qui ont pour valeur 0
            pipeHeight : int = math.floor((listValue / max_number) * (self.__window.getHeight() - self.__locationViewData)) + 1 

            pos_y = self.__window.getHeight() - pipeHeight

            pipes.add(self.__createPipe(listValue, pos_x, pos_y, pipeWidth, pipeHeight, colors[pipeHeight - 1]))
            
            pos_x += pipeWidth + self.__space

        return pipes

    def getSpace(self) -> int:
        """
            Returns the assigned space between two elements.
            return :
                (int) : The assigned space.
        """
        return self.__space

    def setSpace(self, newSpace : int):
        """
            Modifies the assigned space between two elements.
            arg : 
                newSpace (int) : The new assigned space.
        """
        self.__space = newSpace

    def getLocationViewData(self) -> int:
        """
            Returns the location view data.
            return :
                (int) : the location view data.
        """
        return self.__locationViewData

    def setLocationViewData(self, newLocationViewData : int):
        """
            Modifies the location view data.
            arg : 
                newLocationViewData (int) : the location view data.
        """
        self.__locationViewData = newLocationViewData