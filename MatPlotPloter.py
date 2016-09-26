import matplotlib.pyplot as plt
import numpy as np

class MatPlotPloter:
    def __init__(self):
        self.figure = 1
        
    def scatterPlot(self, x, y):
        plt.figure(self.figure)
        self.figure += 1
        colors = np.random.rand(len(y))
        size = [10 * np.pi * i ** 2 for i in y]
        plt.scatter(x, y, s = size, c = colors, alpha = 0.5)
        plt.show()
        
    def barGraph(self, x, y):
        plt.figure(self.figure)
        self.figure += 1
        plt.barh(y, x)
        plt.show()
