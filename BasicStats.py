from Document import Document
from Sentence import Sentence
from DocumentStream import DocumentStream
from copy import deepcopy
from sllist import *

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
    def slinkFreq(wlist):
        b = wlist
        allist = sllist()
        for word in b:
            a = allist.head

            while True:
                if a == None:
                    
                    allist.head = ListNode([word,1])
                    break
                elif a.next == None:
                    if a.data[0] == word:
                        a.data[1] += 1
                    else:
                        a.next = ListNode([word,1])
                    break
                elif a.data[0] == word:
                    a.data[1] += 1
                    break
                a = a.next
            
                
        return allist

        
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

    def TopN(sslist, n):
        a = sllist()
        b = sslist.head
        small = 0
        if b == None:
            return a
        while b.next != None:
            k = a.head
            if a.size < n:
                if k == None:
                    a.head = ListNode(b.data)
                    small = b.data[1]
                    
                elif a.size == 1:
                    if b.data[1] > small:
                        a.head = ListNode(b.data)
                        a.head.next = k
                    else:
                        a.head.next = ListNode(b.data)
                        small = a.head.next[1]
                    
                else:                   
                    while k.next != None and k.next.data[1] > b.data[1]:
                        k = k.next
                    nextnode = k.next
                    if nextnode == 0:
                        small = b.data[1]
                    k.next = ListNode(b.data)
                    k.next.next = nextnode
                a.size += 1
            else:
                if b.data[1] > small:
                    k = a.head
                    c = None
                    n = None
                    p = None
                    while k.next != None:
                        if k.next.data[1] < b.data[1]:
                            c = k
                            n = k.next
                        p = k
                        k = k.next
                    c.next = ListNode(b.data)
                    c.next.next = n
                    p.next = None
                    small = p.data[1]
            b = b.next
        return a
                                               
                
                 
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
        
    
    
