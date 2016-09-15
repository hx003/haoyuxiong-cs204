from Document import Document
from Sentence import Sentence
from DocumentStream import DocumentStream

class BasicStats:
    @staticmethod
    def createFreqMap(wlist):
        '''
        create a frequency map of a list of words by using dictionary
        if word already in dictionary, frequency + 1
        else create another tag if the words is not empty
        '''
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
        '''
        helper function for topN
        '''
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
        
    
    
    
