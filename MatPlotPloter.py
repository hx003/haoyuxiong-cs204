import matplotlib.pyplot as plt
import numpy as np

class MatPlotPloter:
    def __init__(self):
        """
        keep track of the figure number so that graphs won't be printed on the same figure
        """
        self.figure = 1

    def scatterPlot(self, X, Y):
        """
        do a scatter plot with two lists x and y
        """
        plt.figure(self.figure)
        self.figure += 1
        xt = [X[i][0] for i in range(len(X))]
        yt = [X[i][1] for i in range(len(X))]
        xe = [Y[i][0] for i in range(len(Y))]
        ye = [Y[i][1] for i in range(len(Y))]
        trainX = plt.scatter(xt, yt, s = 100, c = 'r', alpha = 0.5)
        evalY = plt.scatter(xe, ye, s = 100, c = 'g', alpha = 0.5)
        plt.legend((trainX, evalY),('Training Data', 'Eval Data'))
        plt.show()

    def barGraph(self, x, y):
        """
        a horizontal bar graph just like in command line plotter
        takes in two lists x and y
        """
        plt.figure(self.figure)
        self.figure += 1
        plt.barh(y, x)
        plt.show()

    def barGraphfortop(self, x, y, book = 'None Given'):
        '''
        a bar graph to show the words and its frequency
        '''
        y_pos = np.arange(len(x))
        plt.barh(y_pos, y, height = 0.5-(4/(len(y_pos)+2)),align='center', alpha=0.2)
        plt.yticks(y_pos, x)
        plt.xlabel('Frequency')
        plt.title(book.upper()+ " - most frequent used words")
        plt.show()
