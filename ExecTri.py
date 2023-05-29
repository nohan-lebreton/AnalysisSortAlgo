from model.importLib.importAll import *

class ExecTri():
    def __init__(self,algo,entropy,length,seed=None,precision='1.0000',glist=None):
        
        if glist == None:
            g = Generator()
            temp = g.createFloatValuesListEntropy(entropy=entropy,length=length,seed=seed,precision=precision)
            for i in range(0,len(temp)):
                temp[i] = FloatCompare(temp[i]) 
            temp = MonitoredList(temp)
            self.glist = temp
        else:
            temp = glist
            for i in range(0,len(temp)):
                temp[i] = FloatCompare(temp[i]) 
            temp = MonitoredList(temp)
            self.glist = temp
        
        self.algo = algo
        self.slist = []
        self.sortstrat = globals()[self.algo](self.glist)

    def execSort(self):
        self.slist = Sort(self.sortstrat).executeStrategy()
        
    def computeGList(self,entropy,length,seed=None,precision='1.0000'):
        g = Generator()
        temp = g.createFloatValuesListEntropy(entropy=entropy,length=length,seed=seed,precision=precision)
        for i in range(0,len(temp)):
            temp[i] = FloatCompare(temp[i]) 
        temp = MonitoredList(temp)
        
        self.glist = temp
        self.sortstrat = globals()[self.algo](self.glist)
        
    def setGList(self,glist):
        temp = glist
        for i in range(0,len(temp)):
            temp[i] = FloatCompare(temp[i]) 
        temp = MonitoredList(temp)
        
        self.glist = temp
        self.sortstrat = globals()[self.algo](self.glist)
        
    def setAlgo(self,algo):
        self.algo = algo
        self.sortstrat = globals()[self.algo](self.glist)
        
    def getGList(self):
        return self.glist
        
    def getSList(self):
        return self.slist

    def getArrayAccesses(self):
        return self.sortstrat.getArrayAccesses()

    def getComparisons(self):
        return self.sortstrat.getComparisons()

    def getTime(self):
        return self.sortstrat.getTime()







"""
Array access
Comparaisons
Time
algo utilisé
liste de base
liste triée
"""

"""
algo utilisé
entropie
taille
seed
précision
"""