def prefixWalk(root, prevWalk):
    if root == None:
        return prevWalk
    prevWalk += root.key + ' '
    for key, val in root.children.items():
        prefixWalk(val)

def postfixWalk(root, prevWalk):
    if root == None:
        return prevWalk
    for key, val in root.children.items():
        prefixWalk(val)
    prevWalk += root.key + ' '

def writeFile(text, author):
    fileName = author + '.txt'
    file = open(fileName, 'w')
    file.write(text)
    file.close()

