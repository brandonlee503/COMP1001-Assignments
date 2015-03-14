#Brandon Lee
#14010627X
#10/31/14
#Assignment 7

"""
countLetters() - Pseudocode
Import libraries:                                                                  import os
function definition:                                                               def countLetters(fileName, fileContent):
create list with all letters of alphabet:                                                alphaList = ["A", ... , "Z"]
convert all letters in string into upper case as this program is case insensitive:       upperCase = fileContent.upper()
create list to store number of letters:                                                  alphaNum = []
fill each element in list with respective number of characters:                          for i in range( length of alphaList ):
                                                                                                alphaNum.extend([upperCase.count(alphaList[i])])
return statement:                                                                        return alphaNum
"""

import os

def countLetters(string):
    #Declared here again because of assignment's parameter restrictions
    alphaList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    upperString = string.upper() 
    alphaNum = []
    
    #This appends to list the number of letters for each letter
    for i in range(len(alphaList)):
        alphaNum.extend([upperString.count(alphaList[i])]) 

    return alphaNum

"""
getFile() - Pseudocode
function definition:                                def getFile():
set working directory:                                  os.chdir("working directory")
create while loop:                                      while(True):
ask for user input:                                          userInput = input("Prompt")
check if file exists:                                        if os.path.exists(userInput):
if so, open with UTF-8 encoding:                                    inputFile = open(userInput, encoding="utf8") #to prevent errors from reading the encoded text doc
read content:                                                       content = inputFile.read()
return name of file and content                                     return (userInput, content)
if incorrect input, print error message and loop:            else: print("error message")
"""         

def getFile():
    os.chdir("C:\\") #set working directory
    while(True):
        userInput = input("Please input a text file: ")  #Note: file should be in the same folder in order to be recognizable
        if os.path.exists(userInput):
            inputFile = open(userInput, encoding="utf8") #Encoding set to read files with UTF-8 encoding
            content = inputFile.read()                            
            return (userInput, content)
        else:
            print("File not found. Please re-enter a file name: ")

"""
main() - Pseudocode
function definition:                                                                def main():
create list with all letters of alphabet:                                                 alphaList = ["A", ... , "Z"]  #for printing purposes
define userInput string and content string to be obtained from getFile() function:        userInput, data = getFile()
call countLetters() function with the previous variables:                                 countLetters(data)

print title with file name:                                                              print("sample title", fileName)
print number of letters in entire file:                                                  print("sample title", sum(alphaNum)) 
print table title:                                                                       print("sample title")
create for loop to print table values:                                                   for i in range( length of alphaList ):
print letter:                                                                                   print(alphaList[i], end="")
print total number of that letter:                                                              print(alphaNum[i], end="")
for loop to print out spaces:                                                            for j in range( number of spaces - number of digits in alphaNum ):
                                                                                                print(" ", end="")
print letter frequency:                                                                  if(check if dividing by zero):
                                                                                                print( number of letter / total number of letters ) * 100
if dividing by zero, print N/A                                                           else: print("N/A") 

""" 
def main():
    alphaList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    uInput, data = getFile()
    alphaNum = countLetters(data)
    
    print("The statistics of the alphabets in", uInput , "are: \n")
    print("The total number of alphabets is:", sum(alphaNum), "\n")
    print("Alphabet  Frequency in number    Frequency in %")
    for i in range(len(alphaList)):
        print("  ", alphaList[i], end="")
        print("            ", alphaNum[i], end="")
        for j in range(19 - len(str(alphaNum[i]))):
            print(" ", end="")
        if (alphaNum[i] != 0):
            freq = alphaNum[i]/sum(alphaNum) * 100
            print( "{0:.4f}".format(freq) ) #Format to 4 decimal places
        else:
            print("N/A")

main()
