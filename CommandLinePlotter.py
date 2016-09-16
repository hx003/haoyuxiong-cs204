import math
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
        print(digitX)
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
     
    def Scatter2D(x, y = None):
        '''
        assume two lists are sorted with same length
        if only one list is given, it will be used as y-axis
        x-axis will be 1 to length of the list
        print axis and plot the points indicated by "x"
        must be number lists
        '''
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
        for m in range(max(y) - min(y) + 1):
            if max(y) - m in y:
                a = y.index(max(y) - m)
                print(str(max(y) - m) + "\t" + "|" + " " * (x[a] - min(x)) * (digitX + 1) + "x")
            else:
                print(str(max(y) - m) + "\t" + "|")
                
        print("\t ", end = "")
        
        for i in range(max(x) - min(x) + 1):
            if i == max(x) - min(x):
                print("—" * (digitX + 1))
            else:
                print("—" * (digitX + 1), end = "")
                
        print("\t ", end = "")
            
        for i in range(max(x) - min(x) + 1):
            b = math.ceil(math.log(min(x) + i, 10))
            if min(x) + i == 10 ** b:
                b += 1
            if i == max(x) - min(x):
                print(min(x) + i)
            else:
                print(str(min(x) + i) + " " * (digitX - b + 1), end = "")

            
        
            


        
            
          
        
