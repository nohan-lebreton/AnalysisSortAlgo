from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    """
        An abstract base class representing a sorting strategy.

        This class defines two abstract methods `sort` and `sortDrawing`, which must be implemented by any concrete
        sorting strategy classes that inherit from it.

    """

    @abstractmethod
    def sort(self):
        """
            Sorts a collection of elements according to the chosen sorting strategy.
            This method must be implemented by any concrete sorting strategy classes that inherit from this class.
        """
        pass

    @abstractmethod
    def sortDrawing(self, window):
        """
            Sorts a collection of graphical elements according to the chosen sorting strategy.
            This method must be implemented by any concrete sorting strategy classes that inherit from this class.
            Args:
                window: The window to draw the sorted elements on.
        """
        pass