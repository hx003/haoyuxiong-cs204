from DecisionTree import *
def prefixWalk(root, prevWalk = ''):
    if root == None:
        return prevWalk
    if root.children != None:
        prevWalk += str(root.key) + ' '
        print(root.key)
        for key, val in root.children.items():
            prevWalk += '--' + str(key) + ' '
            prevWalk = prefixWalk(val, prevWalk)
    prevWalk += str(root.key) + '   '
    return prevWalk

def postfixWalk(root, prevWalk = ''):
    if root == None:
        return prevWalk
    if root.children != None:
        for key, val in root.children.items():
            prefixWalk(val, prevWalk)
            prevWalk += str(key) + ' ' 
        prevWalk += str(root.key) + ' '
    return prevWalk

def writeFile(text, author):
    fileName = author + '.txt'
    file = open(fileName, 'w')
    file.write(text)
    file.close()

def test():

    attributes = ['Author', 'Name', 'Genre', 'Year', 'Topics']
    infolists = [['James Joyce', 'Ulyssess', 'Novel', 1922, 'Modernist Novel'],
                 ['James Joyce',	'AfterTheRace',	'Short Story', 1914, 'Realist Fiction'],
                 ['James Joyce', 'Araby', 'Short Story', 1914, 'Realist Fiction'],
                 ['James Joyce', 'Encounter', 'Short Story', 1914, 'Realist Fiction'],
                 ['James Joyce', 'Eveline'	,'Short Story', 1904, 'Realist Fiction'],
                 ['James Joyce', 'TheBoardingHouse', 'Short Story', 1914, 'Realist Fiction'],
                 ['Mark Twain', 'ConnecticutYankee', 'Novel', 1889, 'Science Fiction'],
                 ['Poe', 'CaskofAmontillado', 'Short Story', 1846, 'Horror'],
                 ['Poe', 'FallHouseOfUsher', 'Short Story', 1839, 'Horror'],
                 ['Poe', 'MasqueofTheRedDeath', 'Short Story', 1842, 'Horror'],
                 ['Poe', 'Raven', 'Short Story', 1845, 'Horror']]
    testlists = [[None, 'TwoGallants', 'Short Story', 1914,'Realist Fiction'],
         [None, 'Sisters', 'Short Story',1914, 'Realist Fiction'],
         [None, 'AnnalbelLee', 'Short Story',1849, 'Horror'],
         [None, 'ConnecticutYankee', 'Novel', 1889, 'Science Fiction']]

    infoTree = DecisionTree()
    aftereval = None
    while True:
        try:
            infoTree = DecisionTree()
            infoTree.train(infoTree.root, infolists, attributes)
            aftereval = infoTree.eval(testlists)

            break
        except Exception as e:
            e = str(e)
            for i in testlists:
                ind = 0
                for j in i:
                    j = str(j)
                    if j == e :
                        attributes[ind] = None
                        break
                    elif ind == len(i) -1:
                        break
                    ind += 1
        else:
            break

    print(attributes)

    text = 'Prefix Walk \n'
    text += prefixWalk(infoTree.root)
    text += '\nPostfix Walk \n'
    text += postfixWalk(infoTree.root)
    writeFile(text, 'author')

    print(aftereval)

    


                
    

a = ['Author', 'Name', 'Genre', 'Year', 'Topics']
b = [['James Joyce', 'Ulyssess', 'Novel', 1922, 'Modernist Novel'], ['James Joyce',	'AfterTheRace',	'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Araby', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Encounter', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Eveline'	,'Short Story', 1904, 'Realist Fiction'], ['James Joyce', 'TheBoardingHouse', 'Short Story', 1914, 'Realist Fiction'], ['Mark Twain', 'ConnecticutYankee', 'Novel', 1889, 'Science Fiction'], ['Poe', 'CaskofAmontillado', 'Short Story', 1846, 'Horror'], ['Poe', 'FallHouseOfUsher', 'Short Story', 1839, 'Horror'], ['Poe', 'MasqueofTheRedDeath', 'Short Story', 1842, 'Horror'], ['Poe', 'Raven', 'Short Story', 1845, 'Horror']]

if __name__ == '__main__':
    test()
