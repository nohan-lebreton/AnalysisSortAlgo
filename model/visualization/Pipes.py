from model.visualization.Pipe import Pipe

class Pipes:
    """
        Class representing a list of pipes.
    """
    def __init__(self):
        """
            Initializes an empty list of pipes.
        """
        self.__pipes : list = []

    def add(self, pipe : Pipe):
        """
            Adds a pipe to the list.

            Args:
                pipe (Pipe): The pipe to add to the list.
        """
        self.__pipes.append(pipe)

    def addAll(self, pipes):
        """
            Adds a list of pipes to the list.

            Args:
                pipes (Pipes): The list of pipes to add to the list.
        """
        for i in range(pipes.size()) :
            self.__pipes.append(pipes.get(i))

    def insert(self, index : int, pipe : Pipe):
        """
            Inserts a pipe at the given index in the list.

            Args:
                index (int): The index at which to insert the pipe.
                pipe (Pipe): The pipe to insert in the list.
        """
        self.__pipes.insert(index, pipe)

    def get(self, index : int) -> Pipe:
        """
            Returns the pipe at the given index in the list.

            Args:
                index (int): The index of the pipe to return.

            Returns:
                Pipe: The pipe at the given index in the list.
        """
        if index < len(self.__pipes) and self.__pipes[index] != None :
            return self.__pipes[index]
        return None

    def removeIndex(self, index : int) -> bool:
        """
            Removes the pipe at the given index in the list.

            Args:
                index (int): The index of the pipe to remove.

            Returns:
                bool: True if the pipe was removed successfully, False otherwise.
        """
        pipe = self.get(index)
        if pipe != None :
            self.__pipes.remove(pipe)
            return True
        return False

    def remove(self, pipe : Pipe) -> bool:
        """
            Removes the given pipe from the list.

            Args:
                pipe (Pipe): The pipe to remove from the list.

            Returns:
                bool: True if the pipe was removed successfully, False otherwise.
        """
        if pipe in self.__pipes:
            self.__pipes.remove(pipe)
            return True
        return False

    def clear(self):
        """
            Clears the list of pipes.
        """
        self.__pipes = []

        
    def contains(self, pipe : Pipe) -> bool:
        """
            Checks if a pipe is contained in the list

            Args:
                pipe (Pipe): The pipe to check from the list.

            Returns:
                bool: True if the pipe was checked successfully, False otherwise.
        """
        if pipe in self.__pipes:
            return True
        return False

        """
            Returns the index of the element in the list

            Args:
                value (int): The value of the pipe where we want to find its position in the list.

            Returns:
                int : True if the value is the same as the one passed in parameter, False otherwise.
        """
    def index(self, value) -> int:
        n = len(self.__pipes)
        for index in range(n):
            if (self.__pipes[index].getValue() == value):
                return index
        return None

    
    def size(self) -> int:
        """
            Returns an integer representing the size of the list.

            Returns:
                int: The integer representing the size of the list.
        """
        return len(self.__pipes)

    def swap(self, index1 : int, index2 : int):
        """
            Swaps the positions of two pipes at the specified indices.

            Args:
                index1 (int): The index of the first pipe.
                index2 (int): The index of the second pipe.
        """
        if (self.contains(self.get(index1)) != False or self.contains(self.get(index2)) != False):
            
            # Sauvegarde de la pos_x du premier élément
            tmp : int = self.__pipes[index1].getPos_x()

            # échange les pos_x
            self.__pipes[index1].setPos_x(self.__pipes[index2].getPos_x())
            self.__pipes[index2].setPos_x(tmp)

            # sauvegarde des pipes
            tmp1 : Pipe = self.get(index1)
            tmp2 : Pipe = self.get(index2)

            # on permute les deux pipes
            self.__pipes.remove(tmp1)
            self.__pipes.insert(index2, tmp1)
            self.__pipes.remove(tmp2)
            self.__pipes.insert(index1, tmp2)

    def __str__(self) -> str:
        """
            Returns a string representation of the Pipes object.

            Returns:
                str: The string representation of the Pipes object.
        """
        string : str = "["
        pipesSize : int = len(self.__pipes)
        for i in range(pipesSize):
            string += str(self.__pipes[i])
            if i < pipesSize - 1:
                string += ", "
        string += "]"
        return string
