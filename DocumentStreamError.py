class DocumentStreamError:
    def existFileName(filename):
        '''
        check if the file exist a filename or if the file exists
        if an error do occur, return "Error Found"
        if not, return "Pass"        
        '''
        try:
            file = open(filename,'r')
        except Exception:
            return "Error Found"
        else:
            return "Pass"
        