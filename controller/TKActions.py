import os
from ExecTri import ExecTri


class TKActions :
    """
    TKActions 

    This class looks how many algorithm have been chosen by the user then call these algorithms
    """

    def __init__(self):
        pass


    def multipleAlgorithm(self, listeAlgoslist, notAnAlgoOptions):
        """
        multipleAlgorithm(self, listeAlgoslist, notAnAlgoOptions)

        Execute the chosen algorithms

        Parameters:
        - listeAlgoslist: list
            list with the different algorithm chosen by the user in the list
        -notAnAlgoOptions: list
            list with all the value given by the user in the inputs
        """
        timeList = []
        compaList = []
        accessesList = []

        for i in range(len(listeAlgoslist)):
            time, compa, accesses = self.__simpleAlgorithm_(listeAlgoslist[i], notAnAlgoOptions[0],notAnAlgoOptions[1], notAnAlgoOptions[2], notAnAlgoOptions[3]) #listLength, entropy, seed, precision
            timeList.append(time)
            compaList.append(compa)
            accessesList.append(accesses)

        return timeList, compaList, accessesList

    def __simpleAlgorithm_(self, chosenAlgo, listLength, entropy, seed, precision):
        """
        __simpleAlgorithm_(self, chosenAlgo, listLength, entropy, seed, precision)

        Based on what options has been chosen, execute the algorithm

        Parameters:
        - chosenAlgo: string
            Chosen algorithm
        - listLength: int
            Size of the generated list, which the algorithm is applied on, chosen by the user
        - entropy: float
            Chosen entropy, applied to the generated list
        - seed: integer
            Chosen seed, applied on the generated list
        - precision: float
            Chosen precision, applied on the generated list        
        """
        print( chosenAlgo +","+ listLength +","+ entropy+"," + seed +"," + precision)
        timeList = []
        compaList = []
        accessesList = []

        if ((seed != "") and (precision != "")): 
            ex = ExecTri(str(chosenAlgo), float(entropy), int(listLength), int(seed), float(precision))
            ex.execSort()
            print("Liste de départ : ", ex.getGList())
            print("Stratégie " + chosenAlgo + " : ", ex.getSList())
            print("Comparaison : ", ex.getComparisons())
            print("Accès au tableau : ", ex.getArrayAccesses())
            print("Temps : ", ex.getTime(), " secondes")  
            return ex.getTime(), ex.getComparisons(), ex.getArrayAccesses()                  

        if ((seed != "") and (precision == "")):
            ex = ExecTri(str(chosenAlgo), float(entropy), int(listLength), int(seed))
            ex.execSort()
            print("Liste de départ : ", ex.getGList())
            print("Stratégie " + chosenAlgo + " : ", ex.getSList())
            print("Comparaison : ", ex.getComparisons())
            print("Accès au tableau : ", ex.getArrayAccesses())
            print("Temps : ", ex.getTime(), " secondes")  
            return ex.getTime(), ex.getComparisons(), ex.getArrayAccesses()             
 
        if ((seed == "") and (precision != "")):
            ex = ExecTri(str(chosenAlgo), float(entropy), int(listLength), float(precision))
            ex.execSort()
            print("Liste de départ : ", ex.getGList())
            print("Stratégie " + chosenAlgo + " : ", ex.getSList())
            print("Comparaison : ", ex.getComparisons())
            print("Accès au tableau : ", ex.getArrayAccesses())
            print("Temps : ", ex.getTime(), " secondes")  
            return ex.getTime(), ex.getComparisons(), ex.getArrayAccesses()              

        if ((seed == "") and (precision == "")):
            ex = ExecTri(str(chosenAlgo), float(entropy), int(listLength))
            ex.execSort()
            print("Liste de départ : ", ex.getGList())
            print("Stratégie " + chosenAlgo + " : ", ex.getSList())
            print("Comparaison : ", ex.getComparisons())
            print("Accès au tableau : ", ex.getArrayAccesses())
            print("Temps : ", ex.getTime(), " secondes")  
            return ex.getTime(), ex.getComparisons(), ex.getArrayAccesses()                


