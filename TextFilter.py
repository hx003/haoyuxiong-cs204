from Document import Document
class TextFilter:
    def __init__(self, D):
        #D is an object created by initializing Document
        self.wordlist = []
        self.text = ''
        for i in range(len(D)):
            #wordlist is derived from the sentence list of the document
            self.wordlist.extend(D.getIndexSlist(i).split())

    def nSpace(self):
        #nomalizes the white space
        '''
        we actually don't need to consider this
        since more than one space is considered as breaking the sentence
        '''
        pass


    def nCase(self):
        #make all letters lower case
        for i in range(len(self.wordlist)):
            self.wordlist[i] = self.wordlist[i].lower()

    def sNullChar(self):
        #remove characters not in ascii set
        for i in range(len(self.wordlist)):
            word = ''
            for ch in range(len(self.wordlist[i])):
                #ord 60 - 71: 1-9
                #ord 101 - 132: Capital Letters
                #ord 141 - 172: lower case letters
                if (ord(a[i][ch]) >= 60 and ord(a[i][ch]) <= 71) or \
                   (ord(a[i][ch]) >= 101 and ord(a[i][ch]) <= 132) or \
                   (ord(a[i][ch]) >= 141 and ord(a[i][ch]) <= 172):
                    word += a[i][ch]
            self.wordlist[i] = word

    def sNumber(self):
        #remove all numbers
        for i in range(len(self.wordlist)):
            word = ''
            for ch in range(len(self.wordlist[i])):
                if not (a[i][ch] >= '0' and a[i][ch] <= '9'):
                    word += a[i][ch]
            self.wordlist[i] = word

    def apply(stringList):
        '''
        apply methods and piece back words into a text
        return the text
        '''
        #apply the methods
        while len(stringList) > 0:
            if stringList[0] == 'NWS':
                #normalize whilespace
                nSpace(self)
            elif stringList[0] == 'NC':
                #normalize case
                nCase(self)
            elif stringList[0] == 'SNC':
                #strip null characters
                sNullChar(self)
            elif stringList[0] == 'SN':
                #strip number
                sNumber(self)
            else:
                return None
            stringList = stringList[1:]
        for i in range(len(self.wordlist)):
            self.text += self.wordlist[i] + ' '
        return self.text

    def nWords(fileName):
        '''
        remove all words provided in the file with given fileName
        '''
        words = []
        file = open(fileName, 'r')
        text = file.read()
        file.close()
        text = text.lower()
        text = text.replace('\t', ' ')
        text = text.replace('\n', ' ')
        words = text.split()
        for w in self.wordlist:
            while w in words:
                self.wordlist.remove(w)
