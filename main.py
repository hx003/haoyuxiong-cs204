from Document import Document
from DocumentStream import DocumentStream
from Sentence import Sentence
from DocumentStreamError import DocumentStreamError
from CommandLinePlotter import CommandLinePlotter
from BasicStats import BasicStats

def main():
    filename = input('Please input a filename:    ')
    fileA = Document(filename)
    title = fileA.generateWhole()
    wordlist = []
    for i in range(len(fileA)):
        sen = Sentence(fileA[i])
        wordlist += sen.parseWords()
    
    
    worddict = BasicStats.createFreqMap(wordlist)
    n = input('Please input the number of top words:    ')

    topdict = BasicStats.topN(worddict,int(n))
    lista = [[],[]]
    for i in topdict:
        lista[0] += [i]
        lista[1] += [topdict[i]]
    graph = CommandLinePlotter.Scatter2D(lista[1],lista[0])
    
    
    
    
    
