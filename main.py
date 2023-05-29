from model.importLib.importAll import *

if __name__ == '__main__':
    
    g = Generator()

    ########################################################################################################

    # on peut afficher 600 pipes si l'interval = 0
    #gList = g.createIntegerValuesList(5,455,600)

    # on peut afficher 299 pipes si l'interval = 1 ((largeur de l'écran / 2) -1 ( le -1 c l'espace avant le premier élément))
    #gList = g.createIntegerValuesList(5,455,299)

    #gList = [200,320, 480, 360, 400]
    #gList = [200,300,400, 500]

    # La première barre n'est plus affichée car nous avons 
    # dépassé la résolution verticale d'1 pixel, 
    # donc l'afficheur va essayer de représenter la valeur 1 mais n'arrivera pas car on ne peut pas afficher 0.5 pixel.
    #gList = [1,8, 3, 2, 10,1,8, 3, 2, 10]

    #gList = [7, 5, 4, 1, 9, 3]
    #gList = [3,2,1, 15]
    #gList = [5, 2, 4, 1, 5, 7, 17, 2]
    #gList = [5, 2, 4, 1, 7]
    #gList = [18, 7, 8, 3, 39, 36, 45, 43, 22, 25, 21, 35, 30, 41, 27, 17, 50, 32, 47, 6, 12]
    #gList = g.createIntegerValuesList(1,1350,200)
    #gList = g.createIntegerValuesList(1,400,50)
    #gList = g.createIntegerValuesList(1,50,50)
    #gList = [7,1,11,5,14,13,6,4,16,3,9,15,2,12,8,10]
    #gList = [7,1,11,5,14]
    #gList = [6 ,2 ,3 ,1 ,5 ,4]
    #gList = [6,9,8,1,15,4,3,12,7,10,13,2,5,14,16,11]
    #gList = [6,9,8,1,15]
    #gList = [15,2,5,16,12,10,13,3,9,6,11,8,14,4,1,7]
    
    #gList = [177, 324, 287, 204, 346, 203, 138, 204, 37, 359, 22, 43, 164, 40, 51, 25, 41, 66, 141, 32, 323, 191, 275, 92, 4, 38, 351, 265, 353, 348, 69, 204, 141, 29, 173, 327, 114, 101, 116, 386, 148, 135, 19, 276, 99, 255, 274, 172, 281, 23]
    
    """
    gList = []
    for i in  range(1,5):
        gList.append(i)
    """
    
    """
    gList = []
    for i in reversed (range(1,41)):
        gList.append(i)
    """
    
    

    
    
    #gList = [15, 9, 2,1]
    #gList = [1, 2, 3,4]

    #gList = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    #gList= [1,2,3,4]
    #gList= [3,2,1,4] 

    #gList= [2,1, 4,3]
    #gList= [2,4,1,3]

            




    #gList = g.createIntegerValuesList(1,140,80)

    #gList = g.createFloatValuesListEntropy(0.5, 10)
    
    ##gList = [4, 2, 1, 3]
    ##gList = [4, 2, 3, 1]
    #gList = [2,3,4,1]


    gList = [2,1,4, 3]
    
    #gList = [0.0029, 0.0904, 0.0612, 0.0016, 0.0024, 0.0025, 0.0, 0.009, 0.0032, 0.0392]
    
    #gList = [4,7,3,5,1,6,8,2]
    
    for i in range(len(gList)):
        gList[i] = FloatCompare(float(gList[i]))
        
    gList = MonitoredList(gList)
    
    

    #gList = [4,3,2,1]

    #gList = []

    #gList = [4,2,7,1,3]

    ########################################################################################################

    # Instanciation des différents algos de tri
    ####################
    #SS = SelectionSort(gList)
    #SS = BubbleSort(gList)
    #SS = InsertionSort(gList)
    #SS = QuickSort(gList)
    #SS = MergeSort(gList)
    #SS = HeapSort(gList)
    #SS = CountingSort(gList)
    #SS = ShellSort(gList)
    #SS = GnomeSort(gList)
    #SS = PancakeSort(gList)
    #SS = CombSort(gList)
    SS = BogoSort(gList)



    # Instanciation de cette classe qui va permettre de lancer le tri
    sort = Sort(SS)



    choice = -1

    
    if choice == 2 :
        
        # Version sans affichage

        print("Liste de départ : ", gList)
        print("Stratégie " + SS.getName() + " : ", sort.executeStrategy())
        print("Comparaison : ", SS.getComparisons())
        print("Accès aux tableaux : ", SS.getArrayAccesses())

        print("Times : ", SS.getTime()," seconds")

    elif choice == -1 :

        test_runner = Run_tests()
        test_runner.display_tests()
   
    else:
    
        # Version avec affichage
        
        WIDTH = 600
        HEIGHT = 400
        TITLE = SS.getName()

        window = Window(WIDTH,HEIGHT, TITLE)

        print("Liste de départ : ", gList)
        print("Stratégie " + SS.getName() + " : ", sort.executeStrategyDrawing(window))
        
        window.run()
    
