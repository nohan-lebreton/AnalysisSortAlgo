from abc import ABC, abstractmethod
from model.observer.ModelListener import ModelListener

# This module defines an abstract base class for a listenable model.
class AbstractListenableModel(ABC):
    # Initializes an instance of the AbstractListenableModel class.
    def __init__(self):
        self._listeners : list = []

    # Adds a ModelListener object to the list of listeners.
    def addListener(self, listener : ModelListener):
        if listener not in self._listeners:
            self._listeners.append(listener)

    # Removes a ModelListener object from the list of listeners.
    def removeListener(self, listener : ModelListener):
        self._listeners.remove(listener) 

    # Calls the 'setColor' method on all the ModelListener objects in the list of listeners.
    def _fireSetColor(self, index1 : int, index2 : int = None):
        for listener in self._listeners:
            listener.setColor(self, index1, index2)

    # Calls the 'resetColor' method on all the ModelListener objects in the list of listeners.
    def _fireResetColor(self, index1 : int, index2 : int = None):
        for listener in self._listeners:
            listener.resetColor(self, index1, index2)

    # Calls the 'swap' method on all the ModelListener objects in the list of listeners.
    def _fireSwap(self, index1 : int, index2 : int):
        for listener in self._listeners:
            listener.swap(self, index1, index2)

    # Calls the 'comparisons' method on all the ModelListener objects in the list of listeners.
    def _fireComparisons(self):
        for listener in self._listeners:
            listener.comparisons(self)

    # Calls the 'arrayAccesses' method on all the ModelListener objects in the list of listeners.
    def _fireArrayAccesses(self):
        for listener in self._listeners:
            listener.arrayAccesses(self)

    # Calls the 'time' method on all the ModelListener objects in the list of listeners.
    def _fireTime(self):
        for listener in self._listeners:
            listener.time(self)
