class Sentence:

    def __init__(self, sen):
        '''
        initiate variables
        punctuation is the last letter in the element
        sen is the list of sentence created by DocumentStream
        '''
        self.wordcount = 0
        self.charcount = 0
        self.punctuation = self.sen[-1]
        self.sen = sen
        
    def parseWords(self):
        '''
        create a list of words
        '''
        wordlist = self.sen[-1].split()
        self.wordcount = len(wordcount)
        return wordlist

    def parseChar(self):
        '''
        create a list of characters
        '''
        charlist = [i for i in self.sen]
        self.charcount = len(charcount)
        return charlist
                
