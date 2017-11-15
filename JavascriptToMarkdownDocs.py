

# Javascript to MarkDown



INPUT_FILE_LIST = [
    'soundCheck'
]


BEGUN = False
INBLOCK = False



def buildDocument(inputFile_name):

    with open('js/' + inputFile_name + '.js') as inputFile:
        inputFile_data = list(inputFile)

    newFile_string = str()


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
