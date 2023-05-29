from numpy.random import default_rng
from model.generator.Gen_entropy import gen_entropy as ge

class Generator:
    """
    Class containing multiple ways of generating lists with some element of randomness.
    """

    def createIntegerValuesList(self, lower : int, upper : int, length : int, seed : int = None) -> list :
        """
        Generates a list of specified length of random integers over a fixed interval.
        If no seed is specified, it defaults to None, meaning it uses a seed given by the OS.

        Args:
            lower (int): Lower bound of the interval.
            upper (int): Upper bound of the interval.
            length (int): Length of the generated list.
            seed (int, optional): Seed used in the PRNG. Defaults to None.

        Returns:
            list: List of random integer values.
        """
        rng = default_rng(seed=seed)
        valuesList : list = []
        for i in range(length):
            valuesList.append(rng.integers(lower, upper))
        return valuesList

    def createIntegerValuesListRange(self, lower : int, upper : int, seed : int = None) -> list :
        """
        Generates a shuffled list of integers going from one number to the other.
        The length of the list will be (upper-lower)+1.
        If no seed is specified, it defaults to None, meaning it uses a seed given by the OS.

        Args:
            lower (int): Lower bound of the interval.
            upper (int): Upper bound of the interval.
            seed (int, optional): Seed used in the PRNG. Defaults to None.

        Returns:
            list: Shuffled list of integers.
        """
        rng = default_rng(seed=seed)
        valuesList : list = []
        for i in range(lower, upper + 1):
            valuesList.append(i)
        rng.shuffle(valuesList)
        return valuesList

    def createFloatValuesListEntropy(self, entropy : float, length : int, precision : str = '1.0000', seed : int = None) -> list:
        """
        Generates a list of specified length of random floats, the list being of the specified entropy.
        The floats will have the same number of fractional digits as the precision parameter.

        In the event of a math domain error, try adding more zeros to the precision parameter.
        
        If no seed is specified, it defaults to None, meaning it uses a seed given by the OS.

        Args:
            entropy (float): Entropy of the generated list.
            length (int): Length of the generated list.
            precision (str, optional): Defines the number of fractional digits used in the algorithm and in the resulting floats. Defaults to '1.0000'.
            seed (int, optional): Seed used in the PRNG. Defaults to None.

        Returns:
            list: List of floats of a certain entropy.
        """
        return ge(entropy,length,precision,seed)
