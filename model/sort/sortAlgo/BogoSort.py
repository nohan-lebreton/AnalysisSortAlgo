import time, random

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing



class BogoSort(SortingStrategy, AbstractListenableModel):
    """
        BogoSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is a particularly ineffective algorithm one person can ever imagine. It is based on generate and test paradigm. The algorithm successively generates permutations of its input until it finds one that is sorted.(Wiki) For example, if bogosort is used to sort a deck of cards, it would consist of checking if the deck were in order, and if it were not, one would throw the deck into the air, pick the cards up at random, and repeat the process until the deck is sorted.
    """
    def __init__(self, tab : list):
        """
            Constructor for BogoSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "BogoSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

    def __is_sorted(self, tab):
        """
            Helper function to check if a list is sorted.

            Args:
                tab (list): The list to be checked.

            Returns:
                bool: True if the list is sorted, False otherwise.
        """
        n = len(tab)
        for i in range(0, n-1):
            if (tab[i] > tab[i+1]):
                return False
        return True

    def __shuffle(self, tab):
        """
            Helper function to shuffle a list.

            Args:
                tab (list): The list to be shuffled.
        """
        n = len(tab)
        for i in range(0, n):
            r = random.randint(0, n-1)
            tab[i], tab[r] = tab[r], tab[i]
            super()._fireSwap(i, r)


    def __bogoSort(self, window=None):
        """
            The main algorithm for Bogo sort.

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
        while (self.__is_sorted(self.__tab) == False):
            self.__shuffle(self.__tab)

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
        self.__bogoSort()
        return self.__tab


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__bogoSort(window)
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