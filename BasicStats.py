from Document import Document
from Sentence import Sentence
from DocumentStream import DocumentStream



class BasicStats:

    @staticmethod
    def createFreqMap(wlist):
        b = wlist
        adict = {}
        for word in b:
            if word.lower() in adict:
                adict[word.lower()] += 1
            elif word.lower() not in adict and word != '':
                adict[word.lower()] = 1
        
            
        return adict
    @staticmethod
    def maxl(kdict):
        b = 0
        s = ''
        for i in kdict:
            if kdict[i] > b:
                b = kdict[i]
                s = i
        return s
                
                
        
    def topN(self, bdict, n):
        cdict = {}
        for i in range(n):

            cdict[self.maxl(bdict)] = bdict[self.maxl(bdict)]
            bdict[self.maxl(bdict)] = 1
        return cdict
        
    
    
    
