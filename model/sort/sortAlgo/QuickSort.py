import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing


class QuickSort(SortingStrategy, AbstractListenableModel):
    """
        QuickSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        QuickSortLike Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 
            - Always pick the first element as a pivot.
            - Always pick the last element as a pivot (implemented below)
            - Pick a random element as a pivot.
            - Pick median as the pivot.
    """
    def __init__(self, tab : list):
        """
            Constructor for QuickSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "QuickSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0
        

        
    # Fonction de partitionnement du tableau, le pivot est le dernier élément
    def __partition(self, l, start, end):
        """
            This method used to partition the list around the pivot, which is set to the last element of the list in this implementation
            
            args :
                l : array
                start : the index of the first item in the list
                end : the index of the last item in the list

            return :
                int : index of j
        """
        piv = l[end]
        j = start
        for i in range(start,end):
            if l[i] <= piv:
                l[i], l[j] = l[j], l[i]
                super()._fireSwap(i, j)
                j += 1
                
        l[j], l[end] = l[end], l[j]
        super()._fireSwap(j, end)

        return j


    # Algo récursif
    def __quickS(self, l, start=0, end=None):
        """
            This methode is the recursive function that sorts the sublists..

            args :
                l : array
                start : the index of the first item in the list
                end : the index of the last item in the list

        """
        if end == None:
            end = len(l)-1

        if end > start:
            pivot = self.__partition(l, start, end)
            self.__quickS(l, start, pivot-1)
            self.__quickS(l, pivot+1, end)
            
            
    def __quickSort(self, window=None):
        """
            The main algorithm for Quick sort.

            Args:
                window (Pg): A Pygame window object to display the sorting process (optional).

            Returns:
                list: The sorted list.
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
        
        self.__quickS(self.__tab)

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
        self.__quickSort()
        return self.__tab


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__quickSort(window)
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