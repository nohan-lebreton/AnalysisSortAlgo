from controller.TKActions import TKActions
from controller.GraphActions import GraphActions
from controller.algoListFiles import algoListFiles

from ExecTri import ExecTri

from tkinter import *

import tkinter as tk
import os
import sys                  
sys.path.insert(0,"..")


import re



if __name__ == '__main__':
  """
  Class containing the code that creates the interface 
  """

  fenetre = tk.Tk()
  fenetre.geometry("600x900")
  fenetre['bg']='white'
  fenetre.title("Fenetre de paramétrage")

  tkactions = TKActions()
  graphactions = GraphActions()


  # - - - - - - - - - - - - - - - - - - - #
  # - - - - - - - - - -Frames- - - - - - - - - - #
  # - - - - - - - - - - - - - - - - - - - #

  # - - - - frame HAUT  - - - - #
  
  firstFrame = LabelFrame(fenetre, text="Paramètres", padx=10, pady=10)
  firstFrame.pack(side=TOP, fill='both', expand='yes')


  # - - - - frame MILIEU - - - - #
  secondFrame = LabelFrame(fenetre, text="Algorithmes", padx=10, pady=10)
  secondFrame.pack(side=TOP, fill='both', expand='yes')

  # - - - - frame BAS - - - - #
  bottomFrame = Frame(fenetre, borderwidth=2)
  bottomFrame.pack(side = BOTTOM, padx=5, pady=5)


  bottomFrameSimu = LabelFrame(bottomFrame, text="Simuler", padx=10, pady=10)
  bottomFrameSimu.pack(side=RIGHT, fill='both', expand='yes')

  bottomFrameGraph = LabelFrame(bottomFrame, text="Graphiques", padx=10, pady=10)
  bottomFrameGraph.pack(side=LEFT, fill='both', expand='yes')







  # - - - - - - - - - - - - - - - - - - - #
  # - - - - - -  Création des widgets - - - - - - - #
  # - - - - - - - - - - - - - - - - - - - #

  

  """
  the differents inputs boxes and their variable
  """
  global listLengthInput
  listLengthLabel = Label(firstFrame, text='* Taille de la liste')
  listLengthInput = Entry(firstFrame)

  global entropyInput
  entropyLabel = Label(firstFrame, text='* Entropie')
  entropyInput = Entry(firstFrame)

  global seedInput
  seedLabel = Label(firstFrame, text='Seed')
  seedInput = Entry(firstFrame)

  global precisionInput
  precisionLabel = Label(firstFrame, text='Precision')
  precisionInput = Entry(firstFrame)

  global nameGraphTimeInput
  nameGraphTimeLabel = Label(firstFrame, text='Nom du fichier dans lequel enregistrer le graphique du temps')
  nameGraphTimeInput = Entry(firstFrame)

  global nameGraphCompaInput
  nameGraphCompaLabel = Label(firstFrame, text='Nom du fichier dans lequel enregistrer le graphique des comparaisons')
  nameGraphCompaInput = Entry(firstFrame)

  global nameGraphAccessesInput
  nameGraphAccessesLabel = Label(firstFrame, text='Nom du fichier dans lequel enregistrer le graphie des accès')
  nameGraphAccessesInput = Entry(firstFrame
  )
  global multiAlgo_variable
  multiAlgo_variable = IntVar()





  """
  get all the algorithm and put their name in the list
  """
  global listeAlgos
  listeAlgos = Listbox(secondFrame, selectmode = 'multiple')
  
  algoListFiles(listeAlgos)               


  
      












  ####################
  """
    The differents variable links to the checkbuttons
  """
  global var_cbTime, var_cbCompa, var_cbAccesses, var_cbSaveDisplay, var_cbSave
  var_cbTime = IntVar()
  var_cbCompa = IntVar()
  var_cbAccesses = IntVar()
  var_cbSaveDisplay = IntVar()      #save and display
  var_cbSave = IntVar()             #only save


    
  global getGraphButton

  def getGraphButton():
    """
      getGraphButton()
      Collec the different values of var_... variable and put them in a returned list
    """ 
    checkButtonList = [var_cbTime.get(), var_cbCompa.get(), var_cbAccesses.get(), var_cbSaveDisplay.get(), var_cbSave.get()]
    return checkButtonList
  
  """
    The differents checkbuttons are created here
  """

  cb_timeGraph = tk.Checkbutton(bottomFrameGraph, text='Afficher le graphique du temps', variable=var_cbTime, onvalue = 1, offvalue = 0)
  cb_comparisonsGraph = tk.Checkbutton(bottomFrameGraph, text='Afficher le graphique des comparaisons', variable=var_cbCompa, onvalue = 1, offvalue = 0 )
  cb_accessesGraph = tk.Checkbutton(bottomFrameGraph, text='Afficher le graphique des accès tableau', variable=var_cbAccesses, onvalue = 1, offvalue = 0)
  cb_saveGraphsDisplay = tk.Checkbutton(bottomFrameGraph, text='Sauvegarder ET afficher', variable=var_cbSaveDisplay, onvalue = 1, offvalue = 0)
  cb_saveGraphs = tk.Checkbutton(bottomFrameGraph, text='Sauvegarder SANS afficher', variable=var_cbSave, onvalue = 1, offvalue = 0)
  ####################

  """
    collect the differents inputs and acts according to these variables
  """

  global inputCollecter
  def inputCollecter():
    """
    inputCollector()
    
    call the differents fonctions related to the execution of the algorithms and the creation of the graphs, collect also the differents inputs and chosen algorithms
    """
    listeAlgoslist = []
    notAnAlgoOptions = [listLengthInput.get(), entropyInput.get(), seedInput.get(), precisionInput.get()]

    for i in listeAlgos.curselection():
      listeAlgoslist.append(listeAlgos.get(i))

    timeList, compaList, accessesList = tkactions.multipleAlgorithm(listeAlgoslist, notAnAlgoOptions)
    graphactions.graphDisplay(getGraphButton(), listeAlgoslist, nameGraphTimeInput.get(), nameGraphCompaInput.get(),nameGraphAccessesInput.get(), timeList, compaList, accessesList)

  





 
  """
    "Lancer la simulation" button, call inputCollector
  """
  
  simulationButton = Button(bottomFrameSimu,text="Lancer la simulation", command=lambda:inputCollecter())



















  listLengthLabel.pack()
  listLengthInput.pack()

  entropyLabel.pack()
  entropyInput.pack()

  seedLabel.pack()
  seedInput.pack()

  precisionLabel.pack()
  precisionInput.pack()

  nameGraphTimeLabel.pack()
  nameGraphTimeInput.pack()

  nameGraphCompaLabel.pack()
  nameGraphCompaInput.pack()

  nameGraphAccessesLabel.pack()
  nameGraphAccessesInput.pack()

  listeAlgos.pack()
  simulationButton.pack()

  cb_timeGraph.pack()
  cb_comparisonsGraph.pack()
  cb_accessesGraph.pack()
  cb_saveGraphsDisplay.pack()
  cb_saveGraphs.pack()



  fenetre.mainloop()
