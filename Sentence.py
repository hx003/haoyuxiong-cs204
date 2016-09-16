class Sentence:

    def __init__(self, sen):
        self.wordcount = 0
        self.charcount = 0
        self.sen = sen
        self.puncutaion = sen[-1]

        
    def parseWords(self):


        wordlist = self.sen[:-1].split()
        self.wordcount = len(wordlist)
        return wordlist

    def parseChar(self):
        charlist = [i for i in self.sen]
        self.charcount = len(charcount)
        return charlist
                
