from model.visualization.Pipe import Pipe
from model.visualization.Pipes import Pipes
from model.visualization.PipeFactory import PipeFactory
from view.visualization.Window import Window
from model.observer.ModelListener import ModelListener
from model.observer.AbstractListenableModel import AbstractListenableModel

from model.sort.MonitoredList import MonitoredList
from model.sort.FloatCompare import FloatCompare




import pygame
from pygame.locals import *

from model.visualization.Color import Color
from model.visualization.Text import Text


class PipeDrawing(ModelListener):
    """
        This class draws pipes on the screen.
    """
    def __init__(self, window : Window, algorithme : AbstractListenableModel, mList : MonitoredList, pipeDisplayMode = False):
        self.__window : Window = window
        self.__algorithme : AbstractListenableModel = algorithme
        self.__mList = mList

        # allows you to choose whether you want a display one by one or all at once
        # default display all at once
        self.__pipeDisplayMode = pipeDisplayMode

        self.__algorithme.addListener(self)

        self.__pipes : Pipes = None
        self.__color : tuple = Color.GRAY

        # the attributes display in the location of important information, of type Text initialized to None
        self.__comparisons = None
        self.__arrayAccesses = None
        self.__time = None
        self.__delay = None
        self.__nbDelay = None

        # initialization of the delay to use within the class
        self.__waitingDelay = 80
        self.__nbWaitingDelay = 0

        self.__initDrawPipes()



    # Drawing methods
    
    
    def __initDrawPipes(self):
        """
            draw all pipes.
        """

        pf = PipeFactory(self.__window)

        # we erase a part of the screen where we display the important information (comparisons, ...) in case if there are any previous artifacts
        self.__window.erasePartScreen(0, 0, self.__window.getWidth(), pf.getLocationViewData())

        # comparison, access to arrays, time, delay between each transition
        nbItemsScreen = 5
        itemSize = (pf.getLocationViewData() // nbItemsScreen) 

        self.__comparisons = Text("Comparisons : ", str(self.__mList.getCompareCount()), 0, 0, itemSize)

        self.__arrayAccesses = Text("Array Accesses : ", str(self.__mList.getArrayAccesses()), 0, self.__comparisons.getPos_y() + self.__comparisons.getSize(), itemSize)

        self.__time = Text("Time : ", str(self.__algorithme.getTime()) + " seconds", 0, self.__arrayAccesses.getPos_y() + self.__arrayAccesses.getSize(), itemSize)
        self.__delay = Text("Delay : ", "", 0, self.__time.getPos_y() + self.__time.getSize(), itemSize)
        self.__nbDelay = Text("NB Delay : ", "", 0, self.__delay.getPos_y() + self.__delay.getSize(), itemSize)


        

        # we display the nb of comparison
        self.__drawText(self.__comparisons)

        # we display the number of accesses to the arrays
        self.__drawText(self.__arrayAccesses)

        # display the execution time
        self.__drawText(self.__time)
        
        # displays the delay
        self.__delay.setText2(str(self.__waitingDelay) + " ms")
        self.__drawText(self.__delay)

        # displays the number of delay 
        self.__nbDelay.setText2(str(self.__nbWaitingDelay))
        self.__drawText(self.__nbDelay)

        # Creation of the pipes
        self.__pipes = pf.createPipes(self.__mList)

        if self.__pipeDisplayMode == False:
            # here we draw the pipes on the screen
            for i in range(self.__pipes.size()):
                self.__drawPipe(self.__pipes.get(i))
            self.__window.drawUpdate()

        else:
            # here we draw the pipes one by one on the screen
            for i in range(self.__pipes.size()):
                copyColor = self.__window.getColor()
                self.__window.setColor(Color.BLACK)

                # We erase the old pipe displayed on the screen, the -1 allows to display the elements which have a value of 0
                recEraseOldPipe = self.__window.erasePartScreen(self.__pipes.get(i).getPos_x(), pf.getLocationViewData() -1 , self.__pipes.get(i).getWidth(), self.__window.getHeight() - pf.getLocationViewData())
                self.__window.drawUpdate(recEraseOldPipe)
                
                self.__nbDelayDraw(str(self.__nbWaitingDelay))
                
                pygame.event.pump()
                pygame.time.delay(self.__waitingDelay)

                self.__nbWaitingDelay += 1
                self.__nbDelayDraw(str(self.__nbWaitingDelay))


                # we display the new pipe
                self.__window.setColor(copyColor)
                self.__window.drawUpdate(self.__drawPipe(self.__pipes.get(i)))

                pygame.event.pump()
                pygame.time.delay(self.__waitingDelay)

                self.__nbWaitingDelay += 1
                self.__nbDelayDraw(str(self.__nbWaitingDelay))
                



        self.__mList.addListener(self)

        # we add an observer to each object contained in the list to watch for their changes
        for floatC in self.__mList:
            floatC.addListener(self)

        
        self.__nbDelayDraw(str(self.__nbWaitingDelay))
        
        pygame.event.pump()
        pygame.time.delay(self.__waitingDelay)

        self.__nbWaitingDelay += 1
        self.__nbDelayDraw(str(self.__nbWaitingDelay))


    def removeListeners(self):
        """
            Remove the listeners
        """
        self.__algorithme.removeListener(self)
        self.__mList.removeListener(self)

        for floatC in self.__mList:
            floatC.removeListener(self)


    def __drawPipe(self, pipe : Pipe) -> pygame.Rect:
        """
            draw a pipe.
        """
        return pygame.draw.rect(self.__window.getScreen(), pipe.getColor(), (pipe.getPos_x(), pipe.getPos_y(), pipe.getWidth(), pipe.getHeight()))
        

    def __drawPipes(self, mList : list):
        """
            draw all the pipes according to a list of numbers.
        """
        for i in range(len(mList)):
            self.__window.drawUpdate(self.__drawPipe(mList[i]))

    def __drawText(self, text : Text):
        """
            draws on the screen the important data (comparison, ...)
        """        
        self.__window.getScreen().blit(text.getTextSurface(), text.getTextRect())
        self.__window.drawUpdate(text.getTextRect())


    def __eraseText(self, text : Text):
        """
            erase text from the screen
        """
        text.getTextSurface().fill(Color.BLACK)
        self.__window.getScreen().blit(text.getTextSurface(), text.getTextRect())
        self.__window.drawUpdate(text.getTextRect())



    # Method launched by the observers

    # Auxiliary method The color is modified according to the self.__color attribute
    def __setColorWithoutDelay(self, source, index1 : int, index2):
        
        pipes : list = [self.__pipes.get(index1)]
        pipes[0].setColor(self.__color)

        if (index2 != None):
            pipes.append(self.__pipes.get(index2))
            pipes[1].setColor(self.__color)

        self.__drawPipes(pipes)


    def setColor(self, source, index1 : int, index2):
        """
            The color is modified according to the self.__color attribute 
        """
        
        # displays the delay with the value of the delay of the others
        self.__delayDraw(str(self.__waitingDelay) + " ms")

        self.__setColorWithoutDelay(source, index1, index2)
        
        pygame.event.pump()
        pygame.time.delay(self.__waitingDelay)

        self.__nbWaitingDelay += 1
        self.__nbDelayDraw(str(self.__nbWaitingDelay))
 

    def __resetColorWithoutDelay(self, source, index1 : int, index2 : int):
        """
            Auxiliary method we reset thanks to the base color saved in an attribute that does not move.
        """
        pipes : list = [self.__pipes.get(index1)]
        pipes[0].setColor(pipes[0].getCOLOR())

        if (index2 != None):
            pipes.append(self.__pipes.get(index2))
            pipes[1].setColor(pipes[1].getCOLOR())

        self.__drawPipes(pipes)



    def resetColor(self, source, index1 : int, index2 : int):
        """
            we reset thanks to the base color saved in an attribute that does not move.
        """
        # displays the delay with the value of the delay of the others
        self.__delayDraw(str(self.__waitingDelay) + " ms")

        self.__resetColorWithoutDelay(source, index1, index2)
        
        pygame.event.pump()
        pygame.time.delay(self.__waitingDelay)

        self.__nbWaitingDelay += 1
        self.__nbDelayDraw(str(self.__nbWaitingDelay))



    def swap(self, source, index1 : int, index2 : int):
        """
            permutation of two elements
        """
        if index2 != index1 :

            # displays the delay with the value of the swap delay
            self.__delayDraw(str(self.__waitingDelay) + " ms")
            
            # here we make a backup of the selection color, to be able to restore it later
            copyColor : tuple = self.__color
            self.__color = Color.WHITE

            # change the color
            self.__setColorWithoutDelay(source, index1, index2)
            
            pygame.event.pump()
            pygame.time.delay(self.__waitingDelay)

            self.__nbWaitingDelay += 1
            self.__nbDelayDraw(str(self.__nbWaitingDelay))

            self.__color = Color.BLACK

            # change the color
            self.__setColorWithoutDelay(source, index1, index2)
            
            pygame.event.pump()
            pygame.time.delay(self.__waitingDelay)

            self.__nbWaitingDelay += 1
            self.__nbDelayDraw(str(self.__nbWaitingDelay))

            self.__pipes.swap(index1, index2)

            self.__color = Color.WHITE

            # change the color
            self.__setColorWithoutDelay(source, index1, index2)
            
            pygame.event.pump()
            pygame.time.delay(self.__waitingDelay)

            self.__nbWaitingDelay += 1
            self.__nbDelayDraw(str(self.__nbWaitingDelay))

            pipes : list = [self.__pipes.get(index1), self.__pipes.get(index2)]

            self.__drawPipes(pipes)

            # reset the color
            self.__resetColorWithoutDelay(source, index1, index2)
            
            pygame.event.pump()
            pygame.time.delay(self.__waitingDelay)

            self.__nbWaitingDelay += 1
            self.__nbDelayDraw(str(self.__nbWaitingDelay))

            self.__color = copyColor 

 

    def comparisons(self, source):
        """
            display of the number of comparison when several pipes are selected, a listener of the model notifies this class to carry out the change.
        """
        
        # Erase old text
        self.__eraseText(self.__comparisons)

        # modify the text
        self.__comparisons.setText2(str(self.__mList.getCompareCount()))

        # we display the new text => number of comparison
        self.__drawText(self.__comparisons)


    def arrayAccesses(self, source):
        """
            display of the number of accesses to the arrays when an access or a modification is made, a listener of the model warns this class to make the change.
        """

        # Erase old text
        self.__eraseText(self.__arrayAccesses)

        # modify the text 
        self.__arrayAccesses.setText2(str(self.__mList.getArrayAccesses()))
        
        # we display the new text => number of array accessess
        self.__drawText(self.__arrayAccesses)



    def time(self, source):
        """
            display the execution time, a model listener notifies this class to make the change.
        """
        
        # Erase old text 
        self.__eraseText(self.__time)

        # modify the text
        self.__time.setText2(str(self.__algorithme.getTime()) + " seconds")

        # we display the new text => execution time
        self.__drawText(self.__time)


    def __delayDraw(self, delay : str):
        """
            display of the delay between each transition
        """
        # Erase old text 
        self.__eraseText(self.__delay)

        # modify the text
        self.__delay.setText2(delay)

        # we display the new text => the delay between each transition
        self.__drawText(self.__delay)
        

    def __nbDelayDraw(self, nbDelay : str):
        """
            display of the number of delay
        """
        # Erase old text 
        self.__eraseText(self.__nbDelay)

        # modify the text
        self.__nbDelay.setText2(nbDelay)

        # we display the new text => the delay between each transition
        self.__drawText(self.__nbDelay)