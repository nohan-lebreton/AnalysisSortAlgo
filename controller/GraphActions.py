import matplotlib.pyplot as plt


class GraphActions: 
    """
    Class managing the differents graphs created with the tkinter interface
    """

    
    def graphDisplay(self, checkButtonList, listeAlgoslist, nameTime, nameCompa, nameAccesses, timeList, compaList, accessesList):
        """
        graphDisplay(self, checkButtonList, listeAlgoslist, nameTime, nameCompa, nameAccesses, timeList, compaList, accessesList)

        Look what button is checked, according to that, calls timeGraph_, compaGraph_ and/or accessesGraph_

        Parameters:
        - checkButtonList: list
            list with the different values return by the checkButtons. 1 = checked, 0 = unchecked
        - listeAlgoslist: list
            list with the different algorithm chosen by the user in the list
        - nameTime: string
            name given by the user in the file name input ( time graph )
        - nameCompa: string
            name given by the user in the file name input ( comparisons graph )
        - nameAccesses: string
            name given by the user in the file name input ( accesses graph )
        - timeList: list
            times taken by the algorithm(s) to sort the list
        - compaList: list
            number of comparisons taken by the algorithm(s) to sort the list
        - accessesList: list
            number of array accesses taken by the algorithm(s) to sort the list
        
        More details :
        - checkButtonList[0]:
            "Afficher le graphique du temps" checkButton value
        - checkButtonList[1]:
            "Afficher le graphique des comparaisons" checkButton value
        - checkButtonList[2]:
            "Afficher le graphique des accès tableau" checkButton value
        - checkButtonList[3]:
            "Sauvegarder ET afficher" checkButton value
        - checkButtonList[4]:
            "Sauvegarder SANS afficher" checkButton value

        """
        if (nameTime == ""):
            nameTime = "Time"
        if (nameCompa == ""):
            nameCompa = "Comparisons"
        if (nameAccesses == ""):
            nameAccesses = "Accesses"

            #Looks if the checkbox "Sauvegarder SANS afficher" is checked
        if checkButtonList[4]:     
            if checkButtonList[0]:   
                self.timeGraph_(listeAlgoslist, timeList) 
                plt.savefig(nameTime + '.png')
            if checkButtonList[1]:
                self.compaGraph_(listeAlgoslist, compaList)
                plt.savefig(nameCompa + '.png')
            if checkButtonList[2]:
                self.accessesGraph_(listeAlgoslist, accessesList)
                plt.savefig(nameAccesses + '.png')

            
            #Looks if the checkbox "Sauvegarder SANS afficher" is NOT checked
        if checkButtonList[4] == 0: 
            if checkButtonList[0]:   
                self.timeGraph_(listeAlgoslist, timeList) 
                if checkButtonList[3]:
                    plt.savefig(nameTime + '.png')
                    
            
            if checkButtonList[1]:
                self.compaGraph_(listeAlgoslist, compaList)
                if checkButtonList[3]:
                    plt.savefig(nameCompa + '.png')

            if checkButtonList[2]:
                self.accessesGraph_(listeAlgoslist, accessesList)
                if checkButtonList[3]:
                    plt.savefig(nameAccesses + '.png')                         
            
            plt.show()





    
    def timeGraph_(self, listeAlgoslist, timeList):
        """
        timeGraph_(self, listeAlgoslist, timeList)
        
        Use matplotlib to create the graphs of the different times taken of the algorithms

        Parameters:
        - listeAlgoslist:
            list with the different algorithm chosen by the user in the list   
        - timeList: list
            times taken by the algorithm(s) to sort the list                 
        """
        x = []
        y = []
        plt.figure("Time")
        for i in listeAlgoslist:
            x.append(i)
        
        for i in timeList:
            y.append(i)

        plt.bar(x, y)



    def compaGraph_(self, listeAlgoslist, compaList):
        """
        compaGraph_(self, listeAlgoslist, compaList)
        
        Use matplotlib to create the graphs of the different times taken of the algorithms

        Parameters:
        - listeAlgoslist:
            list with the different algorithm chosen by the user in the list   
        - compaList: list
             number of comparisons taken by the algorithm(s) to sort the list                 
        """        
        x = []
        y = []
        plt.figure("Comparisons") 
        for i in listeAlgoslist:
            x.append(i)
        
        for i in compaList:
            y.append(i)

        plt.bar(x, y)



    def accessesGraph_(self, listeAlgoslist, accessesList):
        """
        accessesGraph_(self, listeAlgoslist, accessesList)
        
        Use matplotlib to create the graphs of the different times taken of the algorithms

        Parameters:
        - listeAlgoslist:
            list with the different algorithm chosen by the user in the list   
        - accessesList: list
            number of array accesses taken by the algorithm(s) to sort the list                     
        """        
        x = []
        y = []
        plt.figure("Accesses")
        for i in listeAlgoslist:
            x.append(i)
        for i in accessesList:
            y.append(i)
        plt.bar(x,y)

