# Javascript to MarkDown

print ( '='*70 + '\n' + '   Documentation Makeshifter!\n' + '='*70 )
print ( '\n Now Building Markdown Files... \n')
print ( '-' * 70)


BASE_URL = 'https://fractalbach.github.io/evolutionary-sound/docs/'

INPUT_FILE_LIST = [
    'soundCheck',
    'GraphRepresentEquation'
]



BEGUN = False
INBLOCK = False


# build the Index File for the documentation.

def makeTitle (title):
    text = '# Documentation - ' + title + ' \n\n'
    text += 'Welcome to the Documentation of the *Evolutionary Sound* project!  Each javascript file was converted into a markdown file in the github repository.  For each of those, there is a separate HTML page and PDF, which can be found here.\n\n'
    return text

# Table of Contents
DOCS_TOC = '## Documentation Navigation: \n\nDocumentation HTML Page | PDF \n-|- \n'

# Adds Links to the Table of Contents
for name in INPUT_FILE_LIST:
    link = '[' + name + '](' + BASE_URL + name +'.html' + ')'
    link += ' |  [PDF](' + BASE_URL + 'pdf/' + name + '.pdf' + ')'
    DOCS_TOC += link + '\n'
    




# Creation of the Index Document
def buildIndexDocument (toWrite) :
    with open( 'docs/index.md', 'w') as newFile:
        newFile.write(toWrite)


# Combine the Main Title with the TOC for the index page

buildIndexDocument(makeTitle('Navigate') + DOCS_TOC)


# Builds one of the documentation files, one for each js file.

def buildDocument(inputFile_name):

    newFile_string = str()

    # newFile_string += makeTitle(inputFile_name) + DOCS_TOC

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





# Calls Functions to Build Individual Documents.

for inputFile_name in INPUT_FILE_LIST:
    print ( 'Building ' + inputFile_name + '.md ...\n')
    buildDocument(inputFile_name)


print ('=' * 70 +'\n')
print ( 'Now Building TEX and PDF Files...')
print ('=' * 70 +'\n')

# Building PDF Documents from the pages using pandoc and pdflatex

# Create .TEX file using pandoc
from subprocess import call

for name in INPUT_FILE_LIST:
    print ('\n' + '-' * 70 +'\n')
    print ('Now Building ' + name + '.tex and .pdf ...')
    print ('-' * 70 +'\n')

    call([
        "pandoc", 
        "docs/" + name + ".md",
        "-s", 
        "-S", 
        "-o", 
        "docs/tex/" + name + ".tex", 
        # "--highlight-style=monochrome",
        "--template=docs/tex/templates/templateDraft.tex"
    ])

    # Create .pdf file using pdflatex
    call([
        "pdflatex", 
        "docs/tex/" + name + ".tex", 
        "-output-directory=docs/pdf", 
        "-aux-directory=docs/tex/temp"
    ])
 


print ('=' * 70 +'\n')
print ( 'Documentation Build Complete !!')
print ('=' * 70 +'\n')

input("\nPress Enter to Exit...")

