class CommandLinePlotter:
    def Plan2D(x, y):
        for m in range(y[1] - y[0]):
            print(y[1] - m, "|")
            print(" ", "|")
        print("   ", end = "")
        for i in range(x[1] - x[0]):
            print("--",end = "")
        print("")
        print("    ", end = "")
        for i in range(x[1] - x[0]):
            print(x[0] + i + 1, end = " ")
        print("")
     
    def Scatter2D(x, y = None):
        if y == None:
            y = []
            for i in range(len(x)):
                y.append(x[i])
            x = []
            for i in range(len(y)):
                x.append(i + 1)
        
            
          
        