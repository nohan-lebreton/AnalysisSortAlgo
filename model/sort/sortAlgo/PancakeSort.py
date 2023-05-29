import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing


class PancakeSort(SortingStrategy, AbstractListenableModel):
    """
        PancakeSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Given an unsorted array, the task is to sort the given array. You are allowed to do only following operation on array. 
            - flip(arr, i): Reverse array from 0 to i 
    """
    def __init__(self, tab : list):
        """
            Constructor for PancakeSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "PancakeSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0


    def __flip(self, arr, i):
        """
            Reverses arr[0..i]

            Args:
                arr : represents an array
                i : represents the index where the path will stop
        """
        start = 0
        while start < i:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            super()._fireSwap(start, i)
            start += 1
            i -= 1


    def __findMax(self, arr, n):
        """
            Returns index of the maximum, element in arr[0..n-1]

            Args:
                arr : represents an array
                n : represents the size of the array
        """
        mi = 0
        for i in range(0,n):
            if arr[i] > arr[mi]:
                mi = i
        return mi


    def __pancakeSort(self, window=None):
        """
            The main algorithm for Pancake sort.

            Args:
                window (Pg): A Pygame window object to display the sorting process (optional).
        """
        
        start_time = time.time()

        if window != None:
            # Instantiate the PipeDrawing class to display pipes on the screen
            PipeDrawing(window, self, self.__tab)
            self.__tab.clearCounts()

        # Useful if we want to run the sorting algorithm multiple times to avoid biased results
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

        curr_size = len(self.__tab)
        while curr_size > 1:
            mi = self.__findMax(self.__tab, curr_size)
            if mi != curr_size-1:
                self.__flip(self.__tab, mi)
                self.__flip(self.__tab, curr_size-1)

            curr_size -= 1

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
        self.__pancakeSort()
        return self.__tab


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__pancakeSort(window)
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