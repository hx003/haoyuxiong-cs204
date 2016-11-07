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

'''
['Author', 'Genre', 'Year', 'Topics']
[['James Joyce', 'Novel', 1922, 'Modernist Novel'], ['James Joyce', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Short Story', 1904, 'Realist Fiction'], ['James Joyce', 'Short Story', 1914, 'Realist Fiction'], ['Mark Twain', 'Novel', 1889, 'Science Fiction'], ['Poe', 'Short Story', 1846, 'Horror'], ['Poe', 'Short Story', 1839, 'Horror'], ['Poe', 'Short Story', 1842, 'Horror'], ['Poe', 'Short Story', 1845, 'Horror']]
'''
