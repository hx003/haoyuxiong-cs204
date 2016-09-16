from Document import Document
from Sentence import Sentence
from DocumentStream import DocumentStream
from copy import deepcopy


class BasicStats:

    @staticmethod
    def createFreqMap(wlist):
        '''
        create a frequency map of a list of words by using dictionary
        if word already in dictionary, frequency + 1
        else create another tag if the words is not empty
        '''
        '''
        O will be length of the wlist = n
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
        helper function of topN
        find the key with the largest value in a dictionary
        '''
        b = 0
        s = ''
        for i in kdict:
            if kdict[i] > b:
                b = kdict[i]
                s = i
        return s
                
                
    def topN(bdict, n):
        '''
        input a dictionary and the inquired number n for analysis,
        analyze the dictionary, find the n words of highest frequency 
        returns the dictionary of top n word and its frequency         
        '''
        '''
        O will be length of bdict times n = m * n
        '''
        cdict = {}
        ddict = deepcopy(bdict)
        for i in range(n):

            cdict[BasicStats.maxl(ddict)] = ddict[BasicStats.maxl(ddict)]
            ddict[BasicStats.maxl(ddict)] = 1
        return cdict
        
    def minl(kdict):
        '''
        helper function of topN
        find the key with the largest value in a dictionary
        '''
        b = 0
        s = ''
        for i in kdict:
            if kdict[i] < b:
                b = kdict[i]
                s = i
        return s
                
                
    def BottomN(bdict, n):
        '''
        input a dictionary and the inquired number n for analysis,
        analyze the dictionary, find the n words of highest frequency 
        returns the dictionary of top n word and its frequency         
        '''
        '''
        O will be length of bdict times n = m * n
        if we want to put bottomn and topn together and have a faster runtime, 
        we can use the state method.
        '''
        cdict = {}
        ddict = deepcopy(bdict)
        for i in range(n):

            cdict[BasicStats.minl(ddict)] = ddict[BasicStats.minl(ddict)]
            ddict[BasicStats.minl(ddict)] = 1
        return cdict
        
    
    
