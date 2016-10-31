
from copy import deepcopy
import math

class DTNode:

    def __init__(self, key = None):
        self.key = key
        self.children = None

class DecisionTree:

    def __init__(self, root = None):
        self.root = root

    @staticmethod
    def train(root, tdlist, odlist, maxd = None):
        ctdlist = deepcopy(tdlist)
        codlist = deepcopy(odlist)
        classifier = odlist[0]
        classifierd = DecisionTree.catagorizediff(ctdlist, 0)
        igc = DecisionTree.igcaculate(classifierd)[0]


        if maxd == None:
            pass
        else:
            if maxd == 0:
                return 
        igdict = {}
        iginfo = {}
        for i in range(1,len(codlist)):
            if codlist[i] != None:
                iginfo[codlist[i]] = {}
                igdict[codlist[i]] = 0
                for j in ctdlist:
                    if j[i] != None:
                        if j[i] not in iginfo[codlist[i]]:
                            iginfo[codlist[i]][j[i]] = [j[0]]
                        elif j[i] in iginfo[codlist[i]]:
                            iginfo[codlist[i]][j[i]] += [j[0]]

                for k in iginfo[codlist[i]]:
                    iginfo[codlist[i]][k] = DecisionTree.igcaculate(DecisionTree.catagorizediff(iginfo[codlist[i]][k]))
                    
                    igdict[codlist[i]] -= (iginfo[codlist[i]][k][1]/len(codlist))*iginfo[codlist[i]][k][0]
                igdict[codlist[i]] = igc + igdict[codlist[i]]


        maxc = None
        maxcn = 0
        if igdict == {} and iginfo == {}:
            return None
        for l in igdict:
            if igdict[l] >= maxcn:
                maxcn = igdict[l]
                maxc = l
        childrendict = {}

        g = odlist.index(maxc)
        for h in iginfo[maxc]:
            if iginfo[maxc][h][2] == None:
                ctdlist = deepcopy(tdlist)
                codlist = deepcopy(odlist)
                for u in iginfo[maxc]:
                    if u!= h:
                        for o in ctdlist:
                            if o[g] == u:
                                o = None
                codlist[g] = None
                childrendict[h] = DecisionTree.train(DTNode(h),ctdlist, codlist)
            else:
                childrendict[h] = iginfo[maxc][h][2]                                                  
        if root == None:
            root = DTNode(maxc)
            root.children = childrendict
        else:
            root.children = childrendict
            return root
        
                        
                        
            
        
    @staticmethod
    def catagorizediff(tdlist, columnnum = None):
        ddiff = {}
        for i in tdlist:
            if columnnum != None:
                attr = i[columnnum]
            else:
                attr = i
            
            if attr in ddiff:
                ddiff[attr] += 1
            else:
                ddiff[attr] = 1
        print(ddiff)
        return ddiff

       
    
    def igcaculate(diction):
        total = 0
        for i in diction:
            total += diction[i]
        ig = 0
        g = None
        for j in diction:
            if diction[j] > 0:
                ig -= (diction[j]/total)*math.log(diction[j]/total, 2)
                g = j
        if ig != 0.0:
            g = None
        print(ig, total, g)
        return ig, total, g
    


    def eval(self, tdlist):
        pass
        
        


