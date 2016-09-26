import math
import os
import random
class CommandLinePlotter:
    def Plan2D(x, y):
        '''
        input two lists x and y
        which contains the [min, max] of the axis
        plot the axis out
        '''
        digitX = math.ceil(math.log(x[1], 10))
        if x[1] == 10 ** digitX:
            digitX += 1
  
        for m in range(y[1] - y[0] + 1):
            print(str(y[1] - m) + "\t" + "|")
        print("\t ", end = "")
        for i in range(x[1] - x[0] + 1):
            if i == x[1] - 1:
                print("—" * (digitX + 1))
            else:
                print("—" * (digitX + 1), end = "")
        print("\t ", end = "")
        for i in range(x[1] - x[0] + 1):
            a = math.ceil(math.log(i + x[0], 10))
            if i + x[0] == 10 ** a:
                a += 1
            if i == x[1] - 1:
                print(x[0] + i)
            else:
                print(str(x[0] + i) + " " * (digitX - a + 1), end = "" )
     
    def Scatter2D(x, y = None, label = ''):
        '''
        assume two lists are sorted with same length
        if only one list is given, it will be used as y-axis
        x-axis will be 1 to length of the list
        print axis and plot the points indicated by "x"
        must be number lists
        if list y is given, label must be given at the same time
        '''
        (columns, lines) = os.get_terminal_size()
        
        # exchange x and y when only one list is given
        if y == None:
            y = []
            for i in range(len(x)):
                y.append(x[i])
            x = []
            for i in range(len(y)):
                x.append(i + 1)

        digitX = math.ceil(math.log(max(x), 10))  
        if max(x) == 10 ** digitX:
            digitX += 1
                
        # scaling
        ysf = math.ceil((max(y) - min(y)) / (lines - 3)) # y scaling factor
        xsf = math.ceil((max(x) - min(x)) / (columns - 6) * (digitX + 2) )# x scaling factor
        y1 = []
        x1 = []
        for i in y:
            y1.append(round(i / ysf))
        for i in x:
            x1.append(round(i / xsf))
        # plotting
        
        """
        print(y)
        print(y1)
        print(ysf)
        print(lines)
        print()
        print(x)
        print(x1)
        print(xsf)
        print(columns)
        print()
        """
        
        print(label)
        
        for m in range(max(y1) - min(y1) + 1):
            if max(y1) - m in y1:
                a = y1.index(max(y1) - m)
                print(str(y1[a] * ysf) + "\t" + "|" + " " * (x1[a] - min(x1)) * (digitX + 1) + "x")
            else:
                print(str(int(max(y) - m * ysf)) + "\t" + "|")
                
        print("\t ", end = "")
        
        for i in range(max(x1) - min(x1) + 1):
            print("—" * (digitX + 1), end = "")
            
        print()                    
        print("\t ", end = "")
            
        for i in range(max(x1) - min(x1) + 1):
            b = math.ceil(math.log(min(x) + i * xsf, 10))
            if min(x) + i == 10 ** b:
                b += 1
            if i == 0:
                print(str(math.ceil(min(x) + i * xsf)), end = "")
            else:
                print(" " * (digitX - b + 1) + str(math.ceil(min(x) + i * xsf)), end = "")
            
        print()

    def barGraph(x, y = None, label = ''):
        '''
        assume two lists are sorted with same length
        if only one list is given, it will be used as y-axis
        x-axis will be 1 to length of the list
        print axis and plot the points indicated by "x"
        must be number lists
        if list y is given, label must be given at the same time
        '''
        (columns, lines) = os.get_terminal_size()
        
        # exchange x and y when only one list is given
        if y == None:
            y = []
            for i in range(len(x)):
                y.append(x[i])
            x = []
            for i in range(len(y)):
                x.append(i + 1)

        digitX = math.ceil(math.log(max(x), 10))  
        if max(x) == 10 ** digitX:
            digitX += 1
                
        # scaling
        ysf = math.ceil((max(y) - min(y)) / (lines - 3)) # y scaling factor
        xsf = math.ceil((max(x) - min(x)) / (columns - 6) * (digitX + 2) )# x scaling factor
        y1 = []
        x1 = []
        for i in y:
            y1.append(int(i / ysf))
        for i in x:
            x1.append(int(i / xsf))
        # plotting
        """
        print(y)
        print(y1)
        print(ysf)
        print(lines)
        print()
        print(x)
        print(x1)
        print(xsf)
        print(columns)
        print()
        """
        
        print(label)
        
        # plotting

        for m in range(max(y1) - min(y1) + 1):
            legend = chr(random.choice(range(33, 128)))
            if max(y1) - m in y1:
                a = y1.index(max(y1) - m)
                print(str(y1[a] * ysf) + "\t" + "|" + legend * (x1[a] - min(x1)) * (digitX + 1) + legend)
            else:
                print(str(int(max(y) - m * ysf)) + "\t" + "|")
                    
        print("\t ", end = "")
        
        for i in range(max(x1) - min(x1) + 1):
            print("—" * (digitX + 1), end = "")
            
        print()                    
        print("\t ", end = "")
            
        for i in range(max(x1) - min(x1) + 1):
            b = math.ceil(math.log(min(x) + i * xsf, 10))
            if min(x) + i == 10 ** b:
                b += 1
            if i == 0:
                print(str(math.ceil(min(x) + i * xsf)), end = "")
            else:
                print(" " * (digitX - b + 1) + str(math.ceil(min(x) + i * xsf)), end = "")
            
        print()

"""
def main():
    CommandLinePlotter.Scatter2D([1000, 250, 30],[20,80,150],'m/s')
    CommandLinePlotter.barGraph([1000, 250, 30],[20,80,150],'m/s')

if __name__ == '__main__':
    main()
"""
            
          
        
