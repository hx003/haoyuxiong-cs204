class DocumentStreamError:
    def existFileName(filename):
        try:
            file = open(filename,'r')
        except Exception:
            return "Error Found"
        else:
            return "Pass"
        