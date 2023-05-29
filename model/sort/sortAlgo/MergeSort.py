import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing



class MergeSort(SortingStrategy, AbstractListenableModel):
    """
        MergeSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
    """
    def __init__(self, tab : list):
        """
            Constructor for MergeSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "MergeSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0
    

    def __merge(self, l, start, mid, end):
        """
            This method is a helper function for the merge sort algorithm. It merges two sub-lists together.
            
            args :
                l : array
                start : the index of the first item in the list
                mid : the middle index of the array
                end : the index of the last item in the list
        """
        left = []
        for i in range(start, mid):
            left.append(l[i])

        right = []
        for i in range(mid, end):
            right.append(l[i])

        i = 0
        j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1

            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
        
    def __mergeSort(self, window=None):
        """
            The main algorithm for Merge sort.

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
        if (n == 0 or n == 1):
            end_time = time.time()
            self.__time = end_time - start_time
            self.__comparisons = self.__tab.getCompareCount()
            self.__arrayAccesses = self.__tab.getArrayAccesses()
            return  self.__tab
        
        pas = 1
        
        while pas < n:
            for start in range(0, n - pas, 2 * pas):
                mid = start + pas
                end = min(start + 2 * pas, n)

                self.__merge(self.__tab, start, mid, end)
                
                if window != None:
                    # be careful, do not forget to remove the old earpiece that has become useless
                    pipeD.removeListeners()

                    # replace the old class with the new one
                    pipeD = PipeDrawing(window, self, self.__tab, True)
                    self.__tab.clearCounts()

            pas *= 2
            

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
        self.__mergeSort()
        return self.__tab



    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__mergeSort(window)
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