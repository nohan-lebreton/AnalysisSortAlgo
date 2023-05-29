import sys
sys.path.append('../')


sys.path.append('model/sort/sortAlgo')

from model.importLib.importAll import *
from ExecTri import ExecTri


import argparse

import subprocess
import os

g = Generator()
"""
     python3 TERM.py -a Algorithm -n listLength -e entropy -s seed(optional) -p precision(optional)
     example :
     python3 TERM.py -a BubbleSort -n 10 -e 0.83 -s 123 > test.txt   
     > overwrite the file    >> write at the end of the file
"""
parser = argparse.ArgumentParser()

#Algorithm
parser.add_argument("-a", "--algorithm", type=str, help="Algorithm you want to apply", required=True)
#list length
parser.add_argument("-n", "--lengthlist", type=int, help="Length of the list you want the algorithm to be applied to", required=True)
#entropy
parser.add_argument("-e", "--entropy", type=float, help="Entropy applied to the list", required=True)
#seed
parser.add_argument("-s", "--seed", type=int, help="Seed you want to apply to the list")
#precision
parser.add_argument("-p", "--precision", type=str, help="Precision applied to the entropy")

args = parser.parse_args()

"""
    the first line looks if the algorithm exist in the folder containing the different algorithm
    then, the others "if" are looking at the differents inputs given and execute the algorithm according to those variables
    because if no seed is given, her value is "", not empty
"""
if os.path.exists("model/sort/sortAlgo/" + args.algorithm + ".py"):
    if ((args.seed != None) and (args.precision != None)):
        ex = ExecTri(algo=args.algorithm, entropy=args.entropy, length=args.lengthlist, precision=str(args.precision), seed=args.seed)
        ex.execSort()
        print("Liste de départ : ", ex.getGList())
        print("Stratégie " + args.algorithm + " : ", ex.getSList())
        print("Comparaison : ", ex.getComparisons())
        print("Accès au tableau : ", ex.getArrayAccesses())
        print("Temps : ", ex.getTime(), " secondes") 

    
    if (args.precision != None and args.seed == None) :
        ex = ExecTri(algo=args.algorithm, entropy=args.entropy, length=args.lengthlist, precision=str(args.precision))
        ex.execSort()
        print("Liste de départ : ", ex.getGList())
        print("Stratégie " + args.algorithm + " : ", ex.getSList())
        print("Comparaison : ", ex.getComparisons())
        print("Accès au tableau : ", ex.getArrayAccesses())
        print("Temps : ", ex.getTime(), " secondes")       
        
        
    if (args.seed != None and args.precision == None) :      
        ex = ExecTri(algo=args.algorithm, entropy=args.entropy, length=args.lengthlist, seed=args.seed)
        ex.execSort()
        print("Liste de départ : ", ex.getGList())
        print("Stratégie " + args.algorithm + " : ", ex.getSList())
        print("Comparaison : ", ex.getComparisons())
        print("Accès au tableau : ", ex.getArrayAccesses())
        print("Temps : ", ex.getTime(), " secondes")     
        
        
    if (args.seed == None and args.precision == None):
        ex = ExecTri(algo=args.algorithm, entropy=args.entropy, length=args.lengthlist)
        ex.execSort()
        print("Liste de départ : ", ex.getGList())
        print("Stratégie " + args.algorithm + " : ", ex.getSList())
        print("Comparaison : ", ex.getComparisons())
        print("Accès au tableau : ", ex.getArrayAccesses())
        print("Temps : ", ex.getTime(), " secondes")       
        
                

