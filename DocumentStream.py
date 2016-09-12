class DocumentStream:
    def __init__(self):
        self.text = ''
        self.slist = []

    def readfile(self, filename):
        try:
            file = open(filename,'r')
        except Exception:
            filename = None
        self.text = file.read()
        file.close()
        
    def readWhole(self):
        charindex = -1
        strlist = ''
        for i in self.text:
            charindex += 1
            strlist += i
            if i in '!.?; ':
                if charindex == len(self.text) - 1:
                    self.slist.append(strlist)
                    break
                elif i == ' ':
                    if charindex == 0:
                        strlist = ''
                        continue
                    elif self.text[charindex + 1] != ' ' and self.text[charindex - 1] not in '!.?; ':
                        continue
                    elif self.text[charindex + 1] == ' ':
                        strlist = strlist[:-1]
                    elif self.text[charindex - 1] in '!.?;':
                        strlist = ''
                        continue
                self.slist.append(strlist)
                strlist = ''
        return self.slist

    def writeWhole(self):
        for i in self.slist:
            print(i)
                
 # def readfile()                   
                
        
        #"!", "?", ";", "  "


        