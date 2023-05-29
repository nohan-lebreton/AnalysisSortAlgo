from model.observer.AbstractListenableModel import AbstractListenableModel

class FloatCompare(float, AbstractListenableModel):
    """
        Class representing a floating point number with additional functionality for counting comparisons.
        Inherits from the float class and the AbstractListenableModel class.
    """
    def __new__(cls, value):
        """
            Creates a new FloatCompare object with a given float value.

            param :
                value (float) : The float value to initialize.
            return :
                A new FloatCompare object.
        """
        cls.__compare_count = 0
        return super().__new__(cls, value)

    def __init__(self, value):
        """
            Creates a new FloatCompare object with a given float value.

            param :
                value (float) : The float value to initialize.
        """
        AbstractListenableModel.__init__(self)
        float.__init__(value)
        self.__value = value

    def __eq__(self, other):
        """
            Compares this FloatCompare object to another FloatCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (FloatCompare) : The FloatCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__eq__(other)

    def __lt__(self, other):
        """
            Compares this FloatCompare object to another FloatCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (FloatCompare) : The FloatCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__lt__(other)

    def __le__(self, other):
        """
            Compares this FloatCompare object to another FloatCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (FloatCompare) : The FloatCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__le__(other)

    def __gt__(self, other):
        """
            Compares this FloatCompare object to another FloatCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (FloatCompare) : The FloatCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__gt__(other)

    def __ge__(self, other):
        """
            Compares this FloatCompare object to another FloatCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (FloatCompare) : The FloatCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__ge__(other)

    def __ne__(self, other):
        """
            Compares this FloatCompare object to another FloatCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (FloatCompare) : The FloatCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__ne__(other)
    
    def getCompareCount(self):
        """
            Returns the number of times a comparison has been made with this FloatCompare object.
            return 
                (int) : The number of comparisons performed.
        """
        return self.__compare_count
    
    def resetCompareCount(self):
        """
            Resets the comparison counter for this FloatCompare object.
        """
        self.__compare_count -= 1

    def getValue(self):
        """
            Returns the float value stored in this FloatCompare object.

            return:
                (float) : The stored float value.
        """
        return self.__value