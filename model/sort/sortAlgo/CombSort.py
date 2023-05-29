
import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing



class CombSort(SortingStrategy, AbstractListenableModel):
    """
        CombSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using a gap of the size of more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion count with one swap and performs better than Bubble Sort.
    """
    def __init__(self, tab : list):
        """
            Constructor for CombSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "CombSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

    def __getNextGap(self, gap):
        """
            Calculates the next gap to be used in the comb sort algorithm.

            Args:
                gap (int): The previous gap value.

            Returns:
                The next gap value.
        """
        gap = (gap * 10)//13
        if gap < 1:
            return 1
        return gap


    def __combSort(self, window=None):
        """
            The main algorithm for Comb sort.

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
  
        gap = n

        swapped = True
    
        while gap !=1 or swapped == 1:

            gap = self.__getNextGap(gap)

            swapped = False

            for i in range(0, n-gap):
                if self.__tab[i] > self.__tab[i + gap]:
                    self.__tab[i], self.__tab[i + gap]=self.__tab[i + gap], self.__tab[i]
                    super()._fireSwap(i, i + gap)
                    swapped = True

        
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
        self.__combSort()
        return self.__tab


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__combSort(window)
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