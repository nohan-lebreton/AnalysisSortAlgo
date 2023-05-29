
import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing

class HeapSort(SortingStrategy, AbstractListenableModel):
    """
        HeapSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.
    """
    def __init__(self, tab : list):
        super().__init__()
        """
            Constructor for HeapSort.

            Args:
                tab (list): The list to be sorted.
        """
        self.__name = "HeapSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0


    def __heapify(self, tab, n, i):
        """
        Function to build a heap.

        Args:
            tab (list): The list to be sorted.
            n (int): Number of elements in the heap.
            i (int): Index of the root node.
        """

        # Initialize the largest as the root
        maxVal = i 
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child of root exists and is greater than root
        if left < n and tab[left] > tab[maxVal]:
            maxVal = left

        # Check if the right child of the root exists and is greater than the root
        if right < n and tab[right] > tab[maxVal]:
            maxVal = right

        # Change the root if necessary
        if maxVal != i:
            tab[i], tab[maxVal] = tab[maxVal], tab[i]
            super()._fireSwap(i, maxVal)
            self.__heapify(tab, n, maxVal)



    def __heapSort(self, window=None):
        """
            The main algorithm for Heap sort.

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

        n = len(self.__tab)

        # Build the max heap
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify(self.__tab, n, i)

        # Extract elements from the max-heap one by one
        for i in range(n - 1, 0, -1):
            # Swap max item with last item
            self.__tab[0], self.__tab[i] = self.__tab[i], self.__tab[0] 
            super()._fireSwap(0, i) 

            # Call heapify for the root element
            self.__heapify(self.__tab, i, 0)  

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
        self.__heapSort()
        return self.__tab
    
    

    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__heapSort(window)
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