import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing


class GnomeSort(SortingStrategy, AbstractListenableModel):
    """
        GnomeSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Gnome Sort also called Stupid sort is based on the concept of a Garden Gnome sorting his flower pots. A garden gnome sorts the flower pots by the following method :  
         - He looks at the flower pot next to him and the previous one; if they are in the right order he steps one pot forward, otherwise he swaps them and steps one pot backwards.
         - If there is no previous pot (he is at the starting of the pot line), he steps forwards; if there is no pot next to him (he is at the end of the pot line), he is done.
    """
    def __init__(self, tab : list):
        """
            Constructor for GnomeSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "GnomeSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

    def __gnomeSort(self, window=None):
        """
            The main algorithm for Gnome sort.

            Args:
                window (Pg): A Pygame window object to display the sorting process (optional).
        """

        start_time = time.time()

        if window != None:
            # Instantiate the PipeDrawing class to display pipes on the screen
            PipeDrawing(window, self, self.__tab)
            self.__tab.clearCounts()

        # Useful if we want to run the sorting algorithm multiple times to avoid biased results
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

        index = 0
        while index < len(self.__tab):
            if index == 0:
                index = index + 1
            if self.__tab[index] >= self.__tab[index - 1]:
                index = index + 1
            else:
                self.__tab[index], self.__tab[index-1] = self.__tab[index-1], self.__tab[index]
                
                super()._fireSwap(index, index-1)

                index = index - 1

        

        end_time = time.time()

        self.__time = end_time - start_time

        self.__comparisons = self.__tab.getCompareCount()
        self.__arrayAccesses = self.__tab.getArrayAccesses()
         
        super()._fireTime()



    def sort(self) -> list:
        """
            Sort function without displaying the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__gnomeSort()
        return self.__tab


    # algo avec affichage
    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__gnomeSort(window)
        return self.__tab



    def getTab(self) -> list:
        """
            Getter for the sorted list.

            Returns:
            list: The sorted list.
        """
        return self.__tab

    def getName(self):
        """
            Getter for the name of the sorting algorithm.

            Returns:
                str: The name of the sorting algorithm.
        """
        return self.__name

    def getComparisons(self):
        """
            Getter for the number of comparison from the sorting algorithm.

            Returns:
                int: The number of comparison from the sorting algorithm.
        """
        return self.__comparisons
        
    def getArrayAccesses(self):
        """
            Getter for the number of array accesses from the sorting algorithm.

            Returns:
                int: The number of array accesses from the sorting algorithm.
        """
        return self.__arrayAccesses

    def getTime(self):
        """
            Getter for the time it took for the sorting algorithm to complete.

            Returns:
                float: The time it took for the sorting algorithm to complete.
        """
        return self.__time