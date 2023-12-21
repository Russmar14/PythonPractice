#http://inventwithpython.com/pythongently/exercise7/
#
def printASCIITable():
    for number in range(32,127):
        ascii = chr(number)

        print(f"{number} {ascii}")

printASCIITable()
