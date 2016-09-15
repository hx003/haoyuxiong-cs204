import DocumentStream
from DocumentStream import DocumentStream
class Document:

    def __init__(self,filename = ''):
        '''
        initiate variables
        '''
        self._Slist = []
        self.filename = filename
        self.id = 0
        self.wordcount = 0
        self.linecount = 0
        self.charcount = 0
        
    def __getitem__(self):
        '''
        getter for variable in self
        '''
        pass

    def__setitem__(self):
        '''
        setter for variable in self
        '''
        pass

    def generateWhole(self):
        '''
        using text read from DocumentStream
        return the title information
        '''
        a = DocumentStream()
        Slist = a.readWhole(self.filename)
        firstsen = Slist[0]
        fircopy = firstsen
        loc = 0
        firstlineword = []
        title = 'untitled'
        fircopy = fircopy.replace('"',' ')
        fircopy = fircopy.replace('-',' ')
        for i in fircopy:
            if i == '\n':
                i.replace('\n', ' ')               
                firstlineword += fircopy[0:loc].split()
                break
            loc += 1
        print(firstlineword)
        if False not in [k[0].isupper() for k in firstlineword]:
            title = firstsen[0:loc]
        return title
        '''
        filename = title
        fileout = open(filename,'wt',encoding = 'UTF-8')
        fileout.write(firstsen[loc:])
        for i in Slist[1:]:
            fileout.write(i)
        fileout.close
        '''


    def getWordCount(self):
        '''
        count how many words are there in a file by splitting with space
        '''
        a = DocumentStream()
        a.readfile(self.filename)
        text = a.text
        self.wordcount = len(text.split())
        return self.wordcount
        
        
        
        
    
    def getLineCount(self):
        '''
        count number of lines identified by "\n"
        '''
        a = DocumentStream()
        a.readfile(self.filename)
        text = a.text
        self.linecount = text.count('\n')
        return self.linecount
    
        
        

    
    
    

