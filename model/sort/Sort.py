from model.sort.SortingStrategy import SortingStrategy

class Sort:
    """
        A class representing a sorting algorithm.

        This class takes a `SortingStrategy` object as a parameter and delegates the sorting algorithm to it.

    """
    def __init__(self, strategy : SortingStrategy):
        """
            Constructs a `Sort` object with the given `SortingStrategy`.

            Args:
                strategy: The `SortingStrategy` object to use for sorting.

        """
        self.strategy : SortingStrategy = strategy

    def setStrategy(self, strategy : SortingStrategy):
        """
            Sets the `SortingStrategy` object to use for sorting.

            Args:
                strategy: The `SortingStrategy` object to use for sorting.

        """
        self.strategy = strategy

    def executeStrategy(self) -> list:
        """
            Executes the sorting algorithm using the current `SortingStrategy`.

            Returns:
                The sorted list of elements.

        """
        return self.strategy.sort()

    def executeStrategyDrawing(self, window) -> list:
        """
            Executes the sorting algorithm for graphical elements using the current `SortingStrategy`.

            Args:
                window: The window to draw the sorted elements on.

            Returns:
                The sorted list of graphical elements.

        """
        return self.strategy.sortDrawing(window)