import DocumentStream

from DocumentStream import DocumentStream


class Document:

    
    
    def __init__(self,filename = ''):
        self._Slist = []
        self.filename = filename
        self.id = 0
        self.wordcount = 0
        self.linecount = 0
        self.charcount = 0
        
        

        
    @property
    def Slist(self):
        pass

    @Slist.setter
    def Slist(self):
        pass

    def generateWhole(self):
        
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
        a = DocumentStream()
        a.readfile(self.filename)
        text = a.text
        self.wordcount = len(text.split())
        return self.wordcount
        
        
        
        
    
    def getLineCount(self):
        a = DocumentStream()
        a.readfile(self.filename)
        text = a.text
        self.linecount = text.count('\n')
        
        return self.linecount
    
        
        

    
    
    

