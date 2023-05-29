
import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing


class InsertionSort(SortingStrategy, AbstractListenableModel):
    """
        InsertionSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
    """
    def __init__(self, tab):
        """
            Constructor for InsertionSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "InsertionSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0


    def __insertionSort(self, window=None):
        """
            The main algorithm for Insertion sort.

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
        
        n = len(self.__tab)

        for i in range(1, n):
            key = self.__tab[i]
            j = i - 1

            while j >= 0 and self.__tab[j] > key :
                self.__tab[j], self.__tab[j+1] = self.__tab[j+1], self.__tab[j]
                super()._fireSwap(j, j+1)
                j = j - 1           

        end_time = time.time()

        self.__time = end_time - start_time

        self.__comparisons = self.__tab.getCompareCount()
        self.__arrayAccesses = self.__tab.getArrayAccesses()

        super()._fireTime()



    def sort(self):
        """
            Sort function without displaying the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__insertionSort()
        return self.__tab

    
    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__insertionSort(window)
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