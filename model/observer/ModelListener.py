from abc import ABC, abstractmethod


# This module defines an abstract base class ModelListener which represents a listener for observing and responding to events in a data model.
class ModelListener(ABC):

    @abstractmethod
    # An abstract method that sets the color of an element in the data model. The source parameter represents the source of the event, and index1 and index2 represent the indices of the elements being colored.
    def setColor(self, source, index1 : int, index2 : int):
        pass

    @abstractmethod
    # An abstract method that resets the color of an element in the data model. The source parameter represents the source of the event, and index1 and index2 represent the indices of the elements being reset.
    def resetColor(self, source, index1 : int, index2 : int):
        pass

    @abstractmethod
    # An abstract method that swaps the positions of two elements in the data model. The source parameter represents the source of the event, and index1 and index2 represent the indices of the elements being swapped.
    def swap(self, source, index1 : int, index2 : int):
        pass


    @abstractmethod
    # An abstract method that records a comparison operation in the data model. The source parameter represents the source of the event.
    def comparisons(self, source):
        pass

    @abstractmethod
    # An abstract method that records an array access operation in the data model. The source parameter represents the source of the event.
    def arrayAccesses(self, source):
        pass

    @abstractmethod
    # An abstract method that records a time operation in the data model. The source parameter represents the source of the event.
    def time(self, source):
        pass
