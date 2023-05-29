
from model.observer.AbstractListenableModel import AbstractListenableModel


class MonitoredList(list, AbstractListenableModel):
    """
        A subclass of list that implements the AbstractListenableModel interface and monitors access to the list elements.
    """
    def __init__(self, data):
        """
            Initializes the list with the given data and initializes the AbstractListenableModel superclass.
        """

        list.__init__(self, data)
        AbstractListenableModel.__init__(self)

        self.__data = data
        self.__access_count = 0

    def __getitem__(self, key):
        """
            Overrides the __getitem__ method of list to fire events before and after getting an item from the list.
            arg :
                key (int) : element at the index will be deleted
            return :
                used parent class methods
        """
        super()._fireSetColor(key)
        self.__access_count += 1
        super()._fireArrayAccesses()
        super()._fireResetColor(key)
        return super().__getitem__(key)
            

    def __setitem__(self, key, value):
        """
            Overrides the __setitem__ method of list to fire events before and after setting an item in the list.
            arg :
                key (int) : element at the index will be deleted
            return :
                used parent class methods
        """
        super()._fireSetColor(key)
        self.__access_count += 1
        super()._fireArrayAccesses()
        super()._fireResetColor(key)
        return super().__setitem__(key, value)
    
    
    def __delitem__(self, key):
        """
            Overrides the __delitem__ method of list to fire events before and after deleting an item from the list.
            arg :
                key (int) : element at the index will be deleted
            return :
                used parent class methods
        """
        super()._fireSetColor(key)
        self.__access_count += 1
        super()._fireArrayAccesses()
        super()._fireResetColor(key)
        return super().__delitem__(key)


    def getArrayAccesses(self):
        """
            Returns the number of times an item in the list has been accessed.
            return :
                (int) : number of array accesses
        """
        return self.__access_count
        
    
    def getCompareCount(self):
        """
            Returns the number of times a comparison was made on the list items.
            return :
                compareCount (int) : number of comparison
        """
        compareCount = 0
        for floatC in self.__data:
            compareCount += floatC.getCompareCount()
        return compareCount

    # PipeFactory accesses list items, so it increments the array access count
    # what we don't want, so we reset the counter to zero
    def clearCounts(self):
        """
            Clears the array access count and comparison count.
        """
        self.__access_count -= 1
        for i in range(1, len(self.__data)):
            self.__access_count -= 1
            self.__data[i].resetCompareCount()

    def clearCompareCount(self,startIndex=1):
        """
            Clears the comparison count for all items in the list starting from the specified index.
            arg:
                startIndex : the index of the beginning
        """
        for i in range(startIndex, len(self.__data)):
            self.__data[i].resetCompareCount()

    
    def clearArrayAccesses(self):
        """
            Clears the array access count for all items in the list.
        """
        self.__access_count -= len(self.__data)