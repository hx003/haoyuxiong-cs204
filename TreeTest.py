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
['Author', 'Name', 'Genre', 'Year', 'Topics']
[['James Joyce', 'Ulyssess', 'Novel', 1922, 'Modernist Novel'], ['James Joyce',	'AfterTheRace',	'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Araby', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Encounter', 'Short Story', 1914, 'Realist Fiction'], ['James Joyce', 'Eveline	Short Story', 1904, 'Realist Fiction'], ['James Joyce', 'TheBoardingHouse', 'Short Story', 1914, 'Realist Fiction'], ['Mark Twain', 'ConnecticutYankee', 'Novel', 1889, 'Science Fiction'], ['Poe', 'CaskofAmontillado', 'Short Story', 1846, 'Horror'], ['Poe', 'FallHouseOfUsher', 'Short Story', 1839, 'Horror'], ['Poe', 'MasqueofTheRedDeath', 'Short Story', 1842, 'Horror'], ['Poe', 'Raven', 'Short Story', 1845, 'Horror']]
'''
