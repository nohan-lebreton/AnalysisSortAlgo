import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing



class BubbleSort(SortingStrategy, AbstractListenableModel):
    """
        BubbleSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
    """
    def __init__(self, tab : list):
        """
            Constructor for BubbleSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "BubbleSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0


    def __bubbleSort(self, window=None):
        """
            Helper function to perform the BubbleSort algorithm.

            Args:
                window (Pg): A Pygame window object to display the sorting process (optional).
        """
        
        start_time = time.time()

        if window != None:
            # on instancie la classe qui permet d'afficher des pipes à l'écran
            PipeDrawing(window, self, self.__tab)
            self.__tab.clearCounts()

        # utile si on souhaite lancer plusieurs fois le tri, pour ne pas avoir un résultat faussé
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

        n : int = len(self.__tab)

        for i in range(n-1):

            for j in range(n-i-1):

                if self.__tab[j] > self.__tab[j+1]:
                    self.__tab[j], self.__tab[j+1] = self.__tab[j+1], self.__tab[j]
                    super()._fireSwap(j, j+1)

        end_time = time.time()

        self.__time = end_time - start_time

        self.__comparisons = self.__tab.getCompareCount()
        self.__arrayAccesses = self.__tab.getArrayAccesses()
         
        # idem pour le temps
        super()._fireTime()



    def sort(self) -> list:
        """
            Sort function without displaying the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__bubbleSort()
        return self.__tab
    


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__bubbleSort(window)
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