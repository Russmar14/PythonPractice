
#this file creates three functions, one to write a file, one 
#to append (write to the end) and a third to read the string
#contents of the file
def writeToFile(filename, text):
    with open(filename,'w') as fileObj:
        fileObj.write(text)
    return fileObj


def appendToFile(filename,text):
    with open(filename,'a') as fileObj:
        fileObj.write(text)
    return fileObj


def readFromFile(filename):
    with open(filename) as fileObj:
        contents = fileObj.read()
    return contents

#use and then check functions
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'