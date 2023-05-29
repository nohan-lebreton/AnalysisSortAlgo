import os
 

 
def algoListFiles(listeAlgos):
    """
        function collecting the name of all the algorithm in 'model/sort/sortAlgo'
        and put them in the tkinter listBox "listeAlgos"
        'if' checks if the extension of the file
        last lane removes ".py" from the name 
    Args:
        listeAlgos : A tkinter listBox
    """

    path = 'model/sort/sortAlgo'

    files = os.listdir(path)
    for name in files:
        if name[len(name)-3: len(name)+1] == ".py" :    
            listeAlgos.insert(1, name[0:len(name)-3])   
            

    
