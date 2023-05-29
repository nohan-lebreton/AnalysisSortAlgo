
import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing



class SelectionSort(SortingStrategy, AbstractListenableModel):
    """
        SelectionSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted portion. This process is repeated for the remaining unsorted portion of the list until the entire list is sorted.
    """
    def __init__(self, tab : list):
        """
            Constructor for SelectionSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "SelectionSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0


    def __selectionSort(self, window=None):

        """
            The main algorithm for Selection sort.

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

        n : int = len(self.__tab)

        # there is no point in traversing the last element because if we do we will count the permutation of this element and itself
        for i in range(n-1):
            min_idx : int = i
            
            for j in range(i+1, n):
                # replace the old min element with the new one
                if self.__tab[min_idx] > self.__tab[j]:
                    min_idx = j

            # permutation of the 2 elements of the classic list
            self.__tab[i], self.__tab[min_idx] = self.__tab[min_idx], self.__tab[i]

            # ditto in the list of pipes
            super()._fireSwap(i, min_idx)

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
        self.__selectionSort()
        return self.__tab


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__selectionSort(window)
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