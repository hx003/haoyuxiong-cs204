from tkinter import *
from os import *
from os.path import *
from Document import *
from DocumentStream import *
from Sentence import *
from DecisionTree import *
from BasicStats import *
from TextFilter import *
from MatPlotPloter import *
from SKPCA import *
from SKTree import *

class GUI:
    fileName = []
    fileObj = []
    filters = [] #[[filters]]
    charInfo = [] #['Author','Genre','Year','Topic']
    attr = ['None']
    DT = DecisionTree()
    DTSK = SKTree()
    def __init__(self, root):
        '''
        Initialize the first interface that gives a line of instruction that tells the user to
        go to the upload
        '''
        self.root = root
        self.uploadB = Button(text = 'Upload', command = upLoadF)
        self.chrInfoB = Button(text = 'Characteristic Info', command = charInfoF)
        self.textFiltersB = Button(text = 'Text Filters', command = textFiltersF)
        self.statsB = Button(text = 'Statistics', command = statsF)
        self.predictB = Button(text = 'Predictions', command = predictF)
        self.uploadB.grid(row = 0, column = 0)
        self.chrInfoB.grid(row = 0, column = 1)
        self.textFiltersB.grid(row = 0, column = 2)
        self.statsB.grid(row = 0, column = 3)
        self.predictB.grid(row = 0, column = 4)
        welcome = Label(root, text = 'Welcome!\nPlease press upload button to upload the file.')
        welcome.grid(columnspan = 5)
    def forget(self, row = 1):
        '''
        This method clears the frame with the inputted row number, if not inputted, use default v
        value of 1
        '''
        for label in root.grid_slaves():
            if int(label.grid_info()["row"]) >= row:
                label.grid_forget()
    def validate(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_filename = ''
            return True
        try:
            self.entered_filename = new_text
            return True
        except ValueError:
            return False

class textFiltersF(GUI):
    def __init__(self):
        '''
        This function inherits from the GUI class and constructs the interface frames for
        textfilters, which contains three frames that leads to three frames doing separate works
        The three frames are the fileframe filterframe and a state frame that tells whether the
        filters are being applied
        '''
        super().__init__(root)
        self.forget()
        self.variables = []
        self.fileFrame = LabelFrame(root, text = 'Files')
        self.files()
        self.fileFrame.grid(row = 2, column = 0, columnspan = 2, sticky = W+E+N+S)
        self.filterframe = LabelFrame(root, text = 'Text Filters, Check to Apply')
        self.filters()
        self.filterframe.grid(row = 2, column = 2, columnspan = 2,sticky = N)
        self.stateFrame = LabelFrame(root, text = 'State')
        self.state()
        self.stateFrame.grid(row = 2,column = 4, columnspan = 1, sticky = W+E+N+S)
        if GUI.fileObj == []:
            for thefile in GUI.fileName:
                GUI.fileObj.append(Document(thefile))
            for D in GUI.fileObj:
                D.generateWhole()
        elif len(GUI.fileObj) != len(GUI.fileName):
            lengthD = len(GUI.fileName) - len(GUI.fileObj)
            for i in range(lengthD)[::-1]:
                GUI.fileObj.append(Document(GUI.fileName[-(1 + i)]))
                GUI.fileObj[-1].generateWhole()
    def filters(self):
        '''
        This method allows the user to check the filters they want to apply on the files they
        selected and then there is a button that enable them to execute with clicking
        '''
        self.varnws = IntVar()
        self.varnc = IntVar()
        self.varsnc = IntVar()
        self.varsn = IntVar()
        self.varfw = IntVar()
        self.filters = ['NWS','NC','SNC','SN','FW']
        nws = Checkbutton(self.filterframe, text = 'Normalize White Space',variable = self.varnws, onvalue = 1, offvalue = 0)
        nc = Checkbutton(self.filterframe, text = 'Normalize Cases',variable = self.varnc, onvalue = 1, offvalue = 0)
        snc = Checkbutton(self.filterframe, text = 'Strip Null Characters',variable = self.varsnc, onvalue = 1, offvalue = 0)
        sn = Checkbutton(self.filterframe, text = 'Strip Numbers',variable = self.varsn, onvalue = 1, offvalue = 0)
        fw = Checkbutton(self.filterframe, text = 'Filter Words',variable = self.varfw, onvalue = 1, offvalue = 0)
        ap = Button(self.filterframe, text = 'Apply filters',command = lambda: self.applyfilters(self.variables,[self.varnws, self.varnc, self.varsnc, self.varsn, self.varfw]))
        nws.grid(sticky = 'W')
        nc.grid(sticky = 'W')
        snc.grid(sticky = 'W')
        sn.grid(sticky = 'W')
        fw.grid(sticky = 'W')
        ap.grid(sticky = 'E')
    def state(self):
        '''
        This method allows the user to see whether the filters are applied by giving the variable string
        that changes according to the application of filters

        '''
        self.sti_text = StringVar()
        self.sti = "Haven't applied anything"
        self.sti_text.set(self.sti)
        stil = Label(self.stateFrame, textvariable = self.sti_text)
        stil.grid(columnspan= 2 , sticky = W+E+N+S)
    def files(self):

        '''
        This method prints out the filename that was inputed and gives the user the choice
        to check them if they want to apply the filters on it.

        '''
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(self.fileFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            self.variables.append(var)
        if GUI.fileName == []:
            welcome = Label(self.fileFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid()
    def applyfilters(self, variables, filterscs):
        '''
        This method applies the filters to the files by taking in the two list, one of which contains
        the files checked to apply, the other one contains the filters checked to apply, and this
        method will change the state string accordingly
        '''
        if GUI.fileObj == []:
            for thefile in GUI.fileName:
                GUI.fileObj.append(Document(thefile))
            for D in GUI.fileObj:
                D.generateWhole()
        elif len(GUI.fileObj) != len(GUI.fileName):
            lengthD = len(GUI.fileName) - len(GUI.fileObj)
            for i in range(lengthD)[::-1]:
                GUI.fileObj.append(Document(GUI.fileName[-(1 + i)]))
                GUI.fileObj[-1].generateWhole()
        empty = True
        for i in range(len(variables)):
            if variables[i].get() == 1:
                dofil = TextFilter(GUI.fileObj[i])
                dofil.apply([self.filters[j] for j in range(len(filterscs)) if filterscs[j].get() == 1], GUI.fileObj[i])
                empty = False
        if empty == True:
            self.sti= 'Nothing applied'
        else:
            self.sti= 'Successfully applied'
        self.sti_text.set(self.sti)

class predictF(GUI):
    def __init__(self):
        '''
        This method creates the frame and the construction for prediction
        It inherits from the GUI class
        There are two buttons that enables the user to choice which kind of decision method
        they want to use
        And it also leads to the dtF method which constructs the train, evaluate frame
        '''
        super().__init__(root)
        self.forget()
        self.treevar = StringVar()
        self.treevar.set('None')
        self.treef = LabelFrame(self.root, text = 'Select Tree')

        DTB = Radiobutton(text="ID3", variable=self.treevar, value='ID3')
        SKTB  = Radiobutton( text  = 'SKtree', variable= self.treevar, value = 'SKT')
        pcaB = Button(text = 'PCA', command = self.pcaF)

        DTB.grid(row = 1, rowspan = 1,column = 0, columnspan = 2, sticky = W)
        SKTB.grid( row = 1, rowspan =1, column = 2, columnspan = 2, sticky = W)
        pcaB.grid(row = 1, column = 5, columnspan = 1, sticky = W)
        self.dtF()
    #decision tree
    def dtF(self):
        '''
        This method creates the buttons for train and evaluate, and call the trainF funtion defaultly
        , which calls to the frame of train
        '''
        self.forget(2)
        trainB = Button(text = 'Train', command = self.trainF)
        evaluationB = Button(text = 'Evaluation', command = self.evaluationF)
        trainB.grid(row = 3, column = 0, columnspan = 1, sticky = W+E+S+N)
        evaluationB.grid(row = 4, column = 0, columnspan = 1, sticky = W+E+S+N)
        self.trainF()
    def trainF(self):
        '''
        This method creates the train frame which belongs to the ID3 method
        '''
        labelframe1 = LabelFrame(self.root, text = 'Train with desired infos')
        labelframe1.grid(row = 3, rowspan = 100, column = 1, columnspan = 9, sticky = W+E+N+S)
        self.labelframe1of1 = LabelFrame(self.root, labelframe1, text = 'Select classifier')
        self.labelframe1of1.grid(row = 4, rowspan = 4, column = 1, columnspan = 2, sticky =N)
        self.labelframe2of1 = LabelFrame(self.root, labelframe1, text = 'Select the files')
        self.labelframe2of1.grid(row = 4, rowspan = 100 , column = 3, columnspan = 5, sticky = W+N+S+E)
        labelframe3of1 = LabelFrame(self.root, labelframe1, text = 'State')
        labelframe3of1.grid(row =5,  column = 8, sticky = W+E+N+S)
        self.sfiles = []
        self.filesi()
        self.var = StringVar()
        self.var.set('None')
        self.selection= StringVar()
        self.selection_text = "You selected:\n" + str(self.var.get())
        self.selection.set(self.selection_text)

        R1 = Radiobutton(self.labelframe1of1, text="Genre", variable=self.var, value='Genre',command=self.sel)
        R1.grid(sticky = W)
        R2 = Radiobutton(self.labelframe1of1, text="Year", variable=self.var, value='Year',command=self.sel)
        R2.grid(sticky = W)
        R3 = Radiobutton(self.labelframe1of1, text="Topic", variable=self.var, value='Topic',command=self.sel)
        R3.grid(sticky = W)
        R4 = Radiobutton(self.labelframe1of1, text="Author", variable=self.var, value='Author',command=self.sel)
        R4.grid(sticky = W)
        self.svar = StringVar()
        self.svar_text = "Haven't\ntrained"
        self.svar.set(self.svar_text)

        label  = Label(self.labelframe1of1, textvariable = self.selection)
        label.grid(sticky = W+E)
        statelabel = Label(labelframe3of1, textvariable = self.svar)
        applyB = Button(text = 'Apply', command = lambda: self.apply(self.var.get(), self.sfiles, self.treevar.get()))



        applyB.grid(row = 4, column = 8, columnspan = 1, sticky = W+E+N+S)

        statelabel.grid()
    def filesi(self):
        '''
        This method enables the user to check the file they want to train the program with
        The method creates n check button for n files checked
        '''
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(self.labelframe2of1, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            self.sfiles.append(var)
    def apply(self, classifier, files, tree):
        '''
        This method train the program with selected files and classifier
        This method will check which classifer was selected and then creates the two dimensional list
        and the one dimensional list accordingly
        The method will check the availability, if not, the program will returns with nothing
        '''

        if classifier == 'None':
            return
        if tree == 'None':
            tree = 'ID3'



        self.attr = ['Author','Genre','Year','Topic']
        indexc = self.attr.index(classifier)
        self.odlist = [classifier]
        self.tdlist = [[i[indexc]] for i in GUI.charInfo]
        if self.tdlist != []:


            for i in range(len(self.attr)):
                if self.attr[i] != classifier:
                    self.odlist += [self.attr[i]]
                    for j in range(len(self.tdlist)):
                        self.tdlist[j]+= [GUI.charInfo[j][i]]

            if tree == 'ID3':
                GUI.DT.train(GUI.DT.root, self.tdlist, self.odlist)
            elif tree == 'SKT':
                GUI.DTSK.train(self.tdlist, self.odlist, 10)


        if GUI.DT.root != None or GUI.DTSK.tree != None:
            self.svar_text = 'trained'
        else:
            self.svar_text = "Haven't\ntrained"
        self.svar.set(self.svar_text)
    def sel(self):
        '''
        This method updates the selection text which tells the user which classifier they chose
        '''
        self.selection_text = "You selected:\n" + str(self.var.get())
        self.selection.set(self.selection_text)

    def setk(self):
        '''
        This method takes in the one dimensional list and put which known information the
        user should input
        '''
        if self.svar.get() != 'trained':
            self.odlist = ['Author','Genre','Year','Topic']
        self.firstk.set(self.odlist[1])
        self.secondk.set(self.odlist[2])
        self.thirdk.set(self.odlist[3])

    def evaluationF(self):
        '''
        This method sets up the frame and the structure for evalutaion
        It has a big frame containing the input frame for known information and a button for predict
        and a button for adding the information
        The entries will input the information that can help decide what the unknown information is
        '''
        self.twolist = []
        self.labelframe2 = LabelFrame(self.root, text = 'Evaluate with part of the informations')
        self.labelframe2.grid(row = 3, rowspan = 100, column = 1, columnspan = 100, sticky = W+E+N+S)
        self.firstk = StringVar()
        self.secondk = StringVar()
        self.thirdk = StringVar()
        self.setk()
        self.entered_1 = ''
        self.entered_2 = ''
        self.entered_3 = ''
        inputframe1 = LabelFrame(self.labelframe2, text = 'Input known infos')
        inputframe1.grid(row = 4, rowspan = 4, column = 2, columnspan = 4, sticky = W+N+E+S)
        vcmdf = self.root.register(self.validate1)
        vcmds = self.root.register(self.validate2)
        vcmdt = self.root.register(self.validate3)
        labelf = Label(inputframe1, textvariable = self.firstk)
        labelf.grid(row = 5, column = 2, columnspan = 1)
        labels = Label(inputframe1, textvariable = self.secondk)
        labels.grid(row =6, column = 2, columnspan = 1)
        labelt = Label(inputframe1, textvariable = self.thirdk)
        labelt.grid(row = 7, column = 2, columnspan = 1)
        entryf = Entry(inputframe1, validate="key", validatecommand=(vcmdf, '%P'))
        entryf.grid(row = 5, column = 3, columnspan = 2, sticky = W)
        entrys = Entry(inputframe1, validate="key", validatecommand=(vcmds, '%P'))
        entrys.grid(row = 6, column = 3, columnspan = 2, sticky = W)
        entryt = Entry(inputframe1, validate="key", validatecommand=(vcmdt, '%P'))
        entryt.grid(row = 7, column = 3, columnspan = 2, sticky = W)
        infoaddB = Button(inputframe1, text = 'Add', command = lambda: self.add(self.entered_1, self.entered_2, self.entered_3))
        infoaddB.grid(row = 8, column = 2, columnspan = 1, sticky = N)
        self.inputedframe1 = LabelFrame(self.labelframe2, text = 'Inputed known info')
        self.inputedframe1.grid(row = 9, rowspan = 100, column = 2, columnspan = 4, sticky = W+N+E+S)
        predictionB = Button(self.labelframe2, text = 'Predict', command = self.predict)
        predictionB.grid(row = 4, column = 8, columnspan = 4, sticky = N+W+E)
        self.predictionframe = LabelFrame(self.labelframe2, text = 'Prediction')
        self.predictionframe.grid(row = 5, column = 6, columnspan = 80, sticky = W)
    def validate1(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_1 = ''
            return True
        try:
            self.entered_1 = new_text
            return True
        except ValueError:
            return False


    def validate3(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_3 = ''
            return True
        try:
            self.entered_3 = new_text
            return True
        except ValueError:
            return False
    def validate2(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_2 = ''
            return True
        try:
            self.entered_2 = new_text
            return True
        except ValueError:
            return False
    def predict(self):
        '''
        this method prints out the prediction outcome after evaluation
        '''
        tree = self.treevar.get()
        if tree == 'None':
            tree = 'ID3'

        if tree == 'ID3':
            self.twolist = GUI.DT.eval(self.twolist)
            labelist2= []
            for i in range(len(self.twolist)):
                labelist2+= [Label(self.predictionframe, text = 'Info-'+str(i) +' - '
                                   + str(self.twolist[i][0]) + '('+self.odlist[0]+')')]
                labelist2[i].grid(column = 6, columnspan = 2, sticky= W)
        elif tree == 'SKT':
            labelist2 = []
            listA = GUI.DTSK.eval(self.twolist)
            for i in range(len(listA)):
                labelist2 += [Label(self.predictionframe, text = str(listA[i])+'('+str(self.odlist[0])+')')]
                labelist2[i].grid(column = 6, columnspan = 2, sticky = W)
    def add(self, f, s,t):
        '''
        This method add the information to the list that we want to evaluate
        and it will check the eligibility
        '''


        if f!= '' and s!= '' and t!= '':
            self.twolist += [[None, f, s, t]]
        if self.twolist != []:

            self.labelist = []
            for i in range(len(self.twolist)):
                self.labelist+=[Label(self.inputedframe1, text = 'Info-'+str(i) + ': \n        ' +
                      self.odlist[1] + ': ' + str(self.twolist[i][1]) + ' '+ self.odlist[2] +
                      ': ' + str(self.twolist[i][2]) + ' ' + self.odlist[3] + ': ' + str(self.twolist[i][3]))]
                self.labelist[i].grid(column = 3, columnspan = 4, sticky = W)
    #pca
    def pcaF(self):
        #this frame calles sub functionalities of PCA
        self.forget(2)
        self.nF()
        self.selectF()
        self.buttonF()
    def nF(self):
        '''
        this frame contains an entry box for user to input the number of words for analysis
        '''
        nframe = LabelFrame(self.root)
        nframe.grid(row = 3, column = 0, columnspan = 2, sticky = E+W+S+N)
        nL = Label(nframe, text = 'Please enter N for PCA')
        vcmd = self.root.register(self.validate)
        self.nE = Entry(nframe, validate="key", validatecommand=(vcmd, '%P'))
        nL.grid()
        self.nE.grid()
    def selectF(self):
        '''
        this frame let user to select uploaded files to evaluate or train
        '''
        selectframe = LabelFrame(self.root, text = 'Please select files')
        selectframe.grid(row = 3, column = 2, columnspan = 2, sticky = E+W+S+N)
        self.variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(selectframe, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            self.variables.append(var)
    def buttonF(self):
        '''
        this frame contains the Evaluate and Train button and the status entry at the right
        '''
        Button(text = 'Train', command = self.pcaTrain).grid(row = 3, column = 5, columnspan = 1, sticky = E+W+S+N)
        Button(text = 'Evaluation', command = self.pcaEval).grid(row = 4, column = 5, columnspan = 1, sticky = E+W+S+N)
        Label(text = 'Status\nNothing has been done yet').grid(row = 5, column = 5)
    def pcaTrain(self):
        '''
        this function calls SKPCA to train self.pca
        '''
        tlnames = []
        tlobjs = []
        for i in range(len(self.variables)):
            if self.variables[i].get() == 1:
                tlnames.append(GUI.fileName[i])
                tlobjs.append(GUI.fileObj[i])
        self.n = int(self.nE.get())
        self.pca = SKPCA()
        self.pca.train(tlnames, tlobjs, self.n)
        self.forget(4)
        Label(text = 'Status\nTrained').grid(row = 5, column = 5)
    def pcaEval(self):
        '''
        this function evaluate the given files
        plot the scatter plot of transformed data
        and update the result below the buttons toward the right
        '''
        evnames = []
        evobjs = []
        for i in range(len(self.variables)):
            if self.variables[i].get() == 1:
                evnames.append(GUI.fileName[i])
                evobjs.append(GUI.fileObj[i])
        (result, X, Y) = self.pca.evaluation(evnames, evobjs)
        self.forget(4)
        Label(text = 'Result in order').grid(row = 5, column = 5)
        index = [GUI.fileName.index(item) for item in result]
        for i in index:
            Label(text = GUI.charInfo[i][0]).grid(row = 6, column = 5)
        MatPlotPloter().scatterPlot(X, Y)

class charInfoF(GUI):
    def __init__(self):
        '''
        this is a frame for Characteristic infos
        it contains 4 subframes, author, genre, year, and topics
        user inputs will be displayed as a table toward the right
        '''
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root, text = 'Characteristic Info')
        labelframe.grid(columnspan = 100)
        authorB = Button(text = 'Author', command = self.authorF)
        genreB = Button(text = 'Genre', command = self.genreF)
        yearB = Button(text = 'Year', command = self.yearF)
        topicsB = Button(text = 'Topics', command = self.topicsF)
        authorB.grid(row = 1, column = 0)
        genreB.grid(row = 1, column = 1)
        yearB.grid(row = 1, column = 2)
        topicsB.grid(row = 1, column = 3)
        if GUI.charInfo == []:
            for i in range(len(GUI.fileName)):
                GUI.charInfo.append([None, None, None, None])
        elif len(GUI.charInfo) != len(GUI.fileName):
            for i in range(len(GUI.fileName) - len(GUI.charInfo)):
                GUI.charInfo.append([None, None, None, None])
        self.authorF()
        self.printInputs()
    def printInputs(self):
        #user inputs will be displayed as a table toward the right
        inputframe = LabelFrame(self.root, text = 'Inputs')
        inputframe.grid(row = 2, column = 2, sticky = W+E+N+S, columnspan = 3)
        Label(inputframe, text = ' ').grid(row = 2, column = 3)
        Label(inputframe, text = 'Author'). grid(row = 2, column = 4)
        Label(inputframe, text = 'Genre').grid(row = 2, column = 5)
        Label(inputframe, text = 'Year').grid(row = 2, column = 6)
        Label(inputframe, text = 'Topics').grid(row = 2, column = 7)
        for i in range(len(GUI.charInfo)):
            Label(inputframe, text = GUI.fileName[i]).grid(row = i + 3, column = 3)
            for m in range(4):
                Label(inputframe, text = GUI.charInfo[i][m]).grid(row = i + 3, column = 4 + m)
    def authorF(self):
        #enable user to select document and add information of author
        self.forget(2)
        self.printInputs()
        authorFrame = LabelFrame(self.root, text = 'Author')
        authorFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(authorFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(authorFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        authorL = Label(authorFrame, text = 'Please enter the author.')
        author = Entry(authorFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(authorFrame, text = 'Add', command = lambda: self.getResult(variables, author))
        authorL.grid()
        author.grid()
        upB.grid()
    def genreF(self):
        #enable user to select document and add information of genre
        self.forget(2)
        self.printInputs()
        genreFrame = LabelFrame(self.root, text = 'Genre')
        genreFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(genreFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(genreFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        genreL = Label(genreFrame, text = 'Please enter the genre.')
        genre = Entry(genreFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(genreFrame, text = 'Add', command = lambda: self.getResult(variables, genre, 1))
        genreL.grid()
        genre.grid()
        upB.grid()
    def yearF(self):
        ##enable user to select document and add information of year
        self.forget(2)
        self.printInputs()
        yearFrame = LabelFrame(self.root, text = 'Year')
        yearFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(yearFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(yearFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        yearL = Label(yearFrame, text = 'Please enter the year.')
        year = Entry(yearFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(yearFrame, text = 'Add', command = lambda: self.getResult(variables, year, 2))
        yearL.grid()
        year.grid()
        upB.grid()
    def topicsF(self):
        self.forget(2)
        self.printInputs()
        topicsFrame = LabelFrame(self.root, text = 'Topics')
        topicsFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(topicsFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(topicsFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        topicsL = Label(topicsFrame, text = 'Please enter the year.')
        topics = Entry(topicsFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(topicsFrame, text = 'Add', command = lambda: self.getResult(variables, topics, 3))
        topicsL.grid()
        topics.grid()
        upB.grid()
    def getResult(self, variables, info, infoType = 0):
        #update GUI.charInfo
        if GUI.charInfo == []:
            for i in range(len(GUI.fileName)):
                GUI.charInfo.append([None, None, None, None])
        elif len(GUI.charInfo) != len(GUI.fileName):
            for i in range(len(GUI.fileName) - len(GUI.charInfo)):
                GUI.charInfo.append([None, None, None, None])
        for i in range(len(variables)):
            if variables[i].get() == 1:
                GUI.charInfo[i][infoType] = info.get()
        self.printInputs()

class statsF(GUI):
    def __init__(self):
        '''
        this frame contains three subframes
        Display Stats, topN and bottomN
        '''
        super().__init__(root)
        self.forget()
        topNB = Button(text = 'TopN', command = self.topNF)
        bottomNB = Button(text = 'BottomN', command = self.bottomNF)
        printStatsB = Button(text = 'Display Statistics', command = self.printStatsF)
        printStatsB.grid(row = 1, column = 0)
        topNB.grid(row = 1, column = 1)
        bottomNB.grid(row = 1, column = 2)
        self.printStatsF()
    def printStatsF(self):
        '''
        print statistics in ['author', 'genre', 'year', 'topics', 'word count', 'line count', 'char count']
        as a table
        '''
        self.forget(2)
        statsframe = LabelFrame(self.root)
        statsframe.grid(columnspan = 5, sticky = E+W+S+N)
        attr = ['author', 'genre', 'year', 'topics', 'word count', 'line count', 'char count']
        Label(statsframe, text = ' ').grid(row = 2, column = 1)
        for i in range(len(GUI.fileName)):
            Label(statsframe, text = GUI.fileName[i]).grid(row = 2, column = i + 2)
        for i in range(len(attr)):
            Label(statsframe, text = attr[i]).grid(row = i + 3, column = 1)
            if i >= 0  and i <= 3:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.charInfo[m][i]).grid(row = i + 3, column = m + 2)
            elif i == 4:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].getWordCount()).grid(row = i + 3, column = m + 2)
            elif i == 5:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].getLineCount()).grid(row = i + 3, column = m + 2)
            elif i == 6:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].getCharCount()).grid(row = i + 3, column = m + 2)
    def topNF(self):
        #this frame will let user to enter N for topN
        self.forget(2)
        topNframe = LabelFrame(self.root, text = 'TopN')
        topNframe.grid(columnspan = 5, sticky = E+W+S+N)
        nL = Label(topNframe, text = 'Please enter N for TopN')
        vcmd = self.root.register(self.validate)
        n = Entry(topNframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(topNframe, text = 'Enter', command = lambda: self.getResultTop(n))
        nL.grid()
        n.grid()
        upB.grid()
    def bottomNF(self):
        #this frame will let user to enter N for bottomN
        self.forget(2)
        bottomNframe = LabelFrame(self.root, text = 'BottomN')
        bottomNframe.grid(columnspan = 5, sticky = E+W+S+N)
        nL = Label(bottomNframe, text = 'Please enter N for BottomN')
        vcmd = self.root.register(self.validate)
        n = Entry(bottomNframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(bottomNframe, text = 'Enter', command = lambda: self.getResultBottom(n))
        nL.grid()
        n.grid()
        upB.grid()
    def getResultTop(self, n):
        #this frame will generate topN graph for every uploaded document
        self.N = int(n.get())
        for m in range(len(GUI.fileObj)):
            worddict = BasicStats.createFreqMap(GUI.fileObj[m].wordlist)
            [maxlistn, maxlists, minlistn, minlists] = BasicStats.HTopNBottomN(worddict, self.N)
            MatPlotPloter().barGraphfortop(maxlists[1:], maxlistn[1:], GUI.fileName[m])
    def getResultBottom(self, n):
        #this frame will generate bottomN graph for every uploaded document
        self.N = int(n.get())
        for m in range(len(GUI.fileObj)):
            worddict = BasicStats.createFreqMap(GUI.fileObj[m].wordlist)
            [maxlistn, maxlists, minlistn, minlists] = BasicStats.HTopNBottomN(worddict, self.N)
            MatPlotPloter().barGraphfortop(minlists[1:], minlistn[1:], GUI.fileName[m])

class upLoadF(GUI):
    def __init__(self):
        '''
        this frame let users to upload and remove files and keep track of them
        '''
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root)
        labelframe.grid(rowspan = 5, column = 0, columnspan = 2, sticky = N)
        fileNameL = Label(labelframe, text = 'Please enter the file name.')
        vcmd = self.root.register(self.validate)
        fileName = Entry(labelframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(labelframe, text = 'Upload', command = lambda: self.getResult(fileName))
        removeB = Button(labelframe, text = 'Remove', command = lambda: self.removeResult(fileName))
        fileNameL.grid(row=1,column = 0, columnspan = 2)
        fileName.grid(row=2,column = 0 ,columnspan = 2)
        upB.grid(row = 3,sticky = W+E)
        removeB.grid(row = 4, sticky = W+E)
        self.printFileNames()
    def printFileNames(self):
        #this will print out all uploaded file on the right
        self.forget(2)
        Label(self.root, text = 'Uploaded Files').grid(row = 1, column = 2, columnspan = 3, sticky = N)
        rown = 2
        for item in GUI.fileName:
            Label(self.root, text = item).grid(row= rown, column = 2, columnspan = 3, sticky = N)
            rown+= 1
    def getResult(self, fileName):
        #this is a helper function to get the filenames
        GUI.fileName.append(fileName.get())
        self.printFileNames()
    def removeResult(self, fileName):
        #this will remove entered filenames
        index = GUI.fileName.index(fileName.get())
        GUI.fileName.pop(index)
        if GUI.filters != []:
            GUI.filters.pop(index)
        if GUI.charInfo != []:
            GUI.charInfo.pop(index)
        if GUI.fileObj != []:
            GUI.fileObj.pop(index)
        self.printFileNames()




root = Tk()
gui = GUI(root)
root.mainloop()
