class CommandLinePlotter:
    #Note： plotting only works between 1-10
    def Plan2D(x, y):
        for m in range(y[1] - y[0] + 1):
            print(y[1] - m, "|")
        print("   ", end = "")
        for i in range(x[1] - x[0] + 1):
            if i == x[1] - 1:
                print("——")
            else:
                print("——",end = "")
        print("   ", end = "")
        for i in range(x[1] - x[0] + 1):
            if i == x[1] - 1:
                print(x[0] + i)
            else:
                print(x[0] + i, end = " ")
     
    def Scatter2D(x, y = None):
        if y == None:
            y = []
            for i in range(len(x)):
                y.append(x[i])
            x = []
            for i in range(len(y)):
                x.append(i + 1)
                
        for m in range(max(y) - min(y) + 1):
            if max(y) - m in y:
                a = y.index(max(y) - m)
                print(max(y) - m, "|" + " " * (x[a] - min(x)) * 2 + "x")
            else:
                print(max(y) - m, "|")
        print("   ", end = "")
        
        for i in range(max(x) - min(x) + 1):
            if i == max(x) - min(x):
                print("——")
            else:
                print("——", end = "")
        print("   ", end = "")
        for i in range(max(x) - min(x) + 1):
            if i == max(x) - min(x):
                print(min(x) + i)
            else:
                print(min(x) + i, end = " ")

            
        
            


        
            
          
        