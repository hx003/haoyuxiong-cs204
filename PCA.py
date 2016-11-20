from Document import Document
from BasicStats import BasicStats
class PCA:
    def __init__(self, LoDM, n):
        #LoDM for list of document names
        #n is the number of words considered
        self.processedList = [[None] + LoDM]
        self.wordlist = BasicStats.topN(BasicStats.createFreqMap(Document(LoDM[0]).wordlist), n)
        self.dictList = []
        for item in LoDM:
            self.dictList.append(BasicStats.topN(BasicStats.createFreqMap(Document(item).wordlist), len(BasicStats.createFreqMap(Document(item).wordlist))))
        self.wordCount = []
        for item in dictList:
            count = 0
            for i in item:
                count += item[i]
            self.wordCount.append(count)
        for w in self.wordlist:
            listofProb = []
            for i in range(len(dictList)):
                if w in dictList[i]:
                    listofProb.append(item[w]/self.wordCount[i])
                else:
                    listofProb.append(0)
            self.processedList.append([w].extend(listofProb))
        return self.processedList
