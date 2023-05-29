import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing


class ShellSort(SortingStrategy, AbstractListenableModel): 
    """
        ShellSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Shell sort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of ShellSort is to allow the exchange of far items. In Shell sort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element are sorted.
    """  
    def __init__(self, tab : list):
        """
            Constructor for ShellSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "ShellSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

    def __shellSort(self, window=None):
        """
            The main algorithm for Shell sort.

            Args:
                window (Pg): A Pygame window object to display the sorting process (optional).
        """

        start_time = time.time()

        if window != None:
            # Instantiate the PipeDrawing class to display pipes on the screen
            pipeD = PipeDrawing(window, self, self.__tab)
            self.__tab.clearCounts()
        
        # Useful if we want to run the sorting algorithm multiple times to avoid biased results
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

        n = len(self.__tab)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = self.__tab[i]
                j = i
                while j >= gap and self.__tab[j - gap] > temp:
                    self.__tab[j] = self.__tab[j - gap]
                    j -= gap    

                self.__tab[j] = temp
                
                if window != None:
                    # be careful, don't forget to delete the old listener that has become useless
                    pipeD.removeListeners()

                    # replace the old class with the new one
                    pipeD = PipeDrawing(window, self, self.__tab, True)
                    self.__tab.clearCounts()
                
            gap = gap // 2

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
        self.__shellSort()
        return self.__tab
        
    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__shellSort(window)
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