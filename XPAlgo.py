from ExecTri import ExecTri
import math
import json
import os
from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
from model.generator.Generator import Generator
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import numpy as np

def writeListJSON(filepath,li):
    print("Writing list to JSON...")
    with open(filepath, "w") as fp:
        json.dump(li, fp)
        print("Done writing list to JSON !")

def readListJSON(filepath):
    with open(filepath, 'rb') as fp:
        n_list = json.load(fp)
        return n_list

def makeGListFiles(algo, seed):
    glist_fd_path = "GLists"
    dirpath = os.path.join(os.path.dirname(__file__),glist_fd_path)
    os.makedirs(dirpath, exist_ok=True)
    
    g=Generator()
    
    entlist = []
    for i in range(1,21):
        entlist.append(((i*5)*math.log(10000,2))/100)
    
    for i in range(0,20):
        for j in range(10):
            try:
                glist = g.createFloatValuesListEntropy(entropy=float(D(entlist[i]).quantize(D('1.0000000'),rounding=ROUND_DOWN)),length=10000,seed=seed,precision='1.0000000')
            except:
                print(i, " glist attempt failed !")
            else:
                filepath = "GListSeed" + str(seed) + "Ent" + str(i) + ".json"
                writeListJSON(os.path.join(dirpath,filepath), glist)
                break
        
    
    

def xpAlgo(algo,seed):
    timelist = []
    arrlist = []
    complist = []
    entlist = []
    
    for i in range(0,20):
        entlist.append(i)
        
    glist_fd_path = "GLists"
    dirpath = os.path.join(os.path.dirname(__file__),glist_fd_path)
    filepath = "GListSeed" + str(seed) + "Ent" + str(0) + ".json"
    
    glist = readListJSON(os.path.join(dirpath,filepath))
    
    ex = ExecTri(algo=algo,entropy=None,length=None,glist=glist)
    ex.execSort()
    timelist.append(ex.getTime())
    arrlist.append(ex.getArrayAccesses())
    complist.append(ex.getComparisons())
    
    for i in range(1,20):
        filepath = "GListSeed" + str(seed) + "Ent" + str(i) + ".json"
        print(filepath)
        glist = readListJSON(os.path.join(dirpath,filepath))
        ex.setGList(glist)
        
        for j in range(10):
            try:
                ex.execSort()
            except:
                print(j, " sort attempt failed for ", i, " batch !")
            else:
                break
        print(i, " sort batch done.")
        timelist.append(ex.getTime())
        arrlist.append(ex.getArrayAccesses())
        complist.append(ex.getComparisons())
        
    print(timelist)
    print(arrlist)
    print(complist)
        
    algo_fd_path = algo + "XP"
    dirpath = os.path.join(os.path.dirname(__file__),algo_fd_path)
    os.makedirs(dirpath, exist_ok=True)
    
    filepath = "Time" + algo + ".json"
    writeListJSON(os.path.join(dirpath,filepath), timelist)
    filepath = "Access" + algo + ".json"
    writeListJSON(os.path.join(dirpath,filepath), arrlist)
    filepath = "Comparisons" + algo + ".json"
    writeListJSON(os.path.join(dirpath,filepath), complist)
    
    x = range(5,105,5)
    
    fig = plt.figure()
    ax = plt.axes()

    fig, ax = plt.subplots()
    ax.plot(x, timelist, color="b", marker='.', linestyle='solid', markersize=12)

    title = "Execution time of " + algo
    ax.set(xlabel='Entropy (%)', ylabel='Time (s)', title=title)

    ftitle = "GraphTime" + algo + ".png"
    plt.savefig(os.path.join(dirpath,ftitle))
    
    
    fig, ax = plt.subplots()
    ax.plot(x, arrlist, color="g", marker='.', linestyle='solid', markersize=12)

    title = "Number of array accesses of " + algo
    ax.set(xlabel='Entropy (%)', ylabel='Array accesses', title=title)

    ftitle = "GraphAccesses" + algo + ".png"
    plt.savefig(os.path.join(dirpath,ftitle))
    
    
    fig, ax = plt.subplots()
    ax.plot(x, complist, color="r", marker='.', linestyle='solid', markersize=12)

    title = "Number of comparisons of " + algo
    ax.set(xlabel='Entropy (%)', ylabel='Comparisons', title=title)

    ftitle = "GraphComparisons" + algo + ".png"
    plt.savefig(os.path.join(dirpath,ftitle))

xpAlgo('GnomeSort', 999999)