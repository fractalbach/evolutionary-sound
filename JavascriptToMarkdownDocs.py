

# Javascript to MarkDown


BASE_URL = 'https://github.com/fractalbach/evolutionary-sound/docs/'

INPUT_FILE_LIST = [
    'soundCheck'
]



BEGUN = False
INBLOCK = False


# build the Index File for the documentation.

def makeTitle (title):
    return '# Documentation - ' + title + ' - Evolutionary Sound Project \n\n'

# Table of Contents - 

DOCS_TOC = str()

for name in INPUT_FILE_LIST:
    link = '[' + name + '](' + BASE_URL + name +'.html' + ')'
    DOCS_TOC += '* ' + link + '\n'


# Creation of the Index Document

def buildIndexDocument (toWrite) :
    with open( 'docs/index.md', 'w') as newFile:
        newFile.write(toWrite)


# Combine the Main Title with the TOC for the index page

buildIndexDocument(makeTitle('Overview') + DOCS_TOC)


# Builds one of the documentation files, one for each js file.

def buildDocument(inputFile_name):

    newFile_string = str()

    newFile_string += makeTitle(inputFile_name) + DOCS_TOC



    with open('js/' + inputFile_name + '.js') as inputFile:
        inputFile_data = list(inputFile)



    for line in inputFile_data:
        newFile_string += switchSequence(line)

    if INBLOCK: newFile_string += '\n~~~\n'

    with open( 'docs/' + inputFile_name + '.md', "w") as newFile:
        newFile.write(newFile_string)



def switchSequence(line):

    global BEGUN
    global INBLOCK
    
    if not BEGUN:
        if (line[:9] == "/*BEGIN*/"): BEGUN = True
        return ''
    
    first2 = line[:2]

    if first2 == '//':
        if INBLOCK:
            INBLOCK = False
            return "~~~\n\n" + line[2:].strip() + '\n'
        else: 
            return line[2:].strip() + '\n'

    if first2 == '/*': return '' 

    if INBLOCK: 
        if first2 == '\n': return ''
        return line
    else:
        if first2 == '\n': return '\n'
        INBLOCK = True
        return '~~~ javascript \n' + line






for inputFile_name in INPUT_FILE_LIST:
    buildDocument(inputFile_name)
