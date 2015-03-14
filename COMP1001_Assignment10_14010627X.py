"""
Brandon Lee
14010627X
COMP1001 Assignment 10
11-28-14
"""

from random import shuffle
import os

class TextFile():
##    __init__() Pseudocode
##    function definition:    def __init__(self, name="", owner="")
##    set variables:              self.name = name
##                                self.owner = owner
##    add alphabet                self.alphabet = ["a", ... , "z"]
    def __init__(self, name = "", owner = ""):
        self.name = name
        self.owner = owner
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#----------------------------------------------------------------------------------------------------------------------------------------
##    getFile() Pseudocode
##    function definition:         def getFile():
##    Create while loop:                while(True):
##    Ask user for file name:                name = input("Please input a text file: ")
##    if file exists:                        if os.path.exists(name):
##    set file name in class                    self.name = name
##                                              return
##    otherwise                              else:
##    print error message and loop              print("File not found. Please re-enter a file name: ")
    def get_filename(self):
        while(True):
            name = input("Please input a text file for encryption: ")
            if os.path.exists(name):
                self.name = name
                return
            else:
                print("File not found. Please re-enter a file name: ")
#----------------------------------------------------------------------------------------------------------------------------------------
##    get_owner() Pseudocode
##    function definition:                def get_owner(self):
##    set owner variable to user input        self.owner = input("Prompt")
    def get_owner(self):
        self.owner = input("Please enter the name of the owner: ")
#----------------------------------------------------------------------------------------------------------------------------------------
##    retrieve_fileName() Pseudocode
##    function declaration:    def retrieve_fileName(self):
##    return name:                    return self.name
    def retrieve_fileName(self):
        return self.name
#----------------------------------------------------------------------------------------------------------------------------------------
##    retrieve_owner Pseudocode
##    function declaration:    def retrieve_owner(self):
##    return owner:                    return self.owner
    def retrieve_owner(self):
        return self.owner
#----------------------------------------------------------------------------------------------------------------------------------------
##    encrypt() Pesudocode
##    function definition:                                     def encrypt(self, key):
##    if key length not 26:                                        if(len(key) != 26):
##    raise value error:                                               raise ValueError
##    otherwise:                                                   else:
##    open file:                                                       fileHandler = open(self.retrieve_fileName(), "r+")
##    read file:                                                       fileContent = fileHandler.read()
##    make content into list for evaluation:                           listFileContent = list( fileContent.lower() )
##
##    Change each character in string to new encrypted key value..
##    for each value in plaintext:                                    for i in range(len(listFileContent)):
##    if character is in the alphabet:                                    if(listPlainText[i] in self.alphabet):
##    get the letter position in the alphabet:                            letterPos = self.alphabet.index(letterPlainText[i])
##    change the text to key position of the letter:                      listPlainText[i] = key[letterPos]
##
##    join all list values together:                                  plaintext = "".join(listPlainText)
##
##    Rewrite into new text file:                                     encryptedFile = open("Encrypted_"+self.retrieve_fileName() ,"w+")
##                                                                    encryptedFile.write(encryptedText)
##                                                                    encryptedFile.close()
##
##    Create new object:                                              encryptObj = TextFile("Encrypted_"+self.retrieve_fileName(), self.retrieve_owner() )
##    return:                                                         return encryptObj
    def encrypt(self, key):
        if(len(key) != 26):
            raise ValueError("The key length is not 26")
        else:
            fileHandler = open(self.retrieve_fileName(), "r+")
            fileContent = fileHandler.read()
            listFileContent = list( fileContent.lower() )

            # Comment if printkey() is used before encrypt() 
##            for i in range(len(key)):               #
##                temp = key[i]                       #
##                key[i] = alphabet[temp]             #

            for i in range(len(listFileContent)):
                if(listFileContent[i] in self.alphabet):
                    letterPos = self.alphabet.index(listFileContent[i])
                    listFileContent[i] = key[letterPos]

            encryptedText = "".join(listFileContent)

            #Rewrite into new text file
            encryptedFile = open("Encrypted_"+self.retrieve_fileName() ,"w+")
            encryptedFile.write(encryptedText)
            encryptedFile.close()

            #Create new object
            encryptObj = TextFile("Encrypted_"+self.retrieve_fileName(), self.retrieve_owner() )
            return encryptObj
#----------------------------------------------------------------------------------------------------------------------------------------
##    decrypt() Pseudocode
##    function decleration:                               def decrypt(self, key):
##    if key length is not 26                                 if(len(key) != 26):
##    raise value error                                           raise ValueError
##    otherwise                                               else:
##    Get file and read from it:                                  encryptedFile = open(self.retrieve_fileName(), "r")
##                                                                encyptedContent = encryptedFile.read()
##                                                                encryptedFile.close()
##    create list from ciphertext and convert to lowercase:       listCipherText = list( ciphertext.lower() )
##    for every value in ciphertext                               for i in range(len(ciphertext)):
##    if it's a letter                                                  if(listCipherText[i] in alphabet):
##    get the letter position in the key                                      letterPos = key.index(listCipherText[i])
##    change the key to alphabet position of the letter                       listCipherText[i] = self.alphabet[letterPos]                
##    combine list:                                               decryptedText = "".join(listCipherText)
##    Rewrite into new text file:                                 decryptedFile = open("Decrypted_"+self.retrieve_fileName(), "w+")
##                                                                decryptedFile.write(decryptedText)
##                                                                decryptedFile.close()
##    Create new object:                                          decryptObj = TextFile("Decrypted_"+self.retrieve_fileName(), self.retrieve_owner() )
##    return                                                      return decryptObj
    def decrypt(self, key):
        if(len(key) != 26):
            raise ValueError("The key length is not 26")
        else:
            #Get file and read from it
            encryptedFile = open(self.retrieve_fileName(), "r")
            encyptedContent = encryptedFile.read()
            encryptedFile.close()
            
            listFileContent = list( encyptedContent.lower() )

            for i in range(len(listFileContent)):
                if(listFileContent[i] in self.alphabet):
                    letterPos = key.index(listFileContent[i])
                    listFileContent[i] = self.alphabet[letterPos]
                    
            decryptedText = "".join(listFileContent)

            #Rewrite into new text file
            decryptedFile = open("Decrypted_"+self.retrieve_fileName(), "w+")
            decryptedFile.write(decryptedText)
            decryptedFile.close()

            #Create new object
            decryptObj = TextFile("Decrypted_"+self.retrieve_fileName(), self.retrieve_owner() )
            return decryptObj
#----------------------------------------------------------------------------------------------------------------------------------------
##    isSameFile() Pseudocode
##    function definition:    def isSameFile(self, file2):
##    if both files exist:        if(self.retrieve_fileName()) and os.path.exists(file2)):
##    open both and read:              file1h = open(file1, "r")
##                                     file2h = open(file2, "r")
##            
##    read content:                     content1 = file1h.read()
##                                      content2 = file2h.read()
##
##    change content to lowercase:      lower1 = content1.lower()
##                                      lower2 = content2.lower()
##            
##    if both contents are equal:       if(lower1 == lower2):
##    return true                             return True
##    otherwise false                   else:
##                                            return False
##    if file not found           else:
##    raise ioerror                     raise IOError("The file(s) cannot be found")
    def isSameFile(self, file2):
        if(os.path.exists(self.retrieve_fileName()) and os.path.exists(file2)):
                file1h = open(self.retrieve_fileName(), "r")
                file2h = open(file2, "r")
                
                content1 = file1h.read()
                content2 = file2h.read()

                lower1 = content1.lower()
                lower2 = content2.lower()
                
                if(lower1 == lower2):
                        return True
                else:
                        return False
        else:
                raise IOError("The file(s) cannot be found")
#----------------------------------------------------------------------------------------------------------------------------------------
##    getKey() PseudoCode
##    function definition:                 def genkey(length):
##    check if length is less than 1:         if(length<1):
##    if so raise value error:                   raise ValueError
##    otherwise:                              else:
##    create key:                                key = []
##    for loop from i to the length:             for i in range(length):
##    add i value to key:                             key.append(i)
##    shuffle key list:                          shuffle(key)
##    return key:                             return key
def genkey(length):
    if(length < 1):
        raise ValueError("The key length is not valid")
    else:
        key = []
        for i in range(length):
            key.append(i)
        shuffle(key)
        return key
#----------------------------------------------------------------------------------------------------------------------------------------
##    printkey() Pseudocode
##    function definition:               def printkey(key):
##    check if length of key is under 1:       if(len(key) < 1):
##    if so raise value error:                      raise ValueError
##    otherwise print plain/cyphertext:        else:
##    declare alphabet list:                        alphabet = ["a", ... ,"z"]
##    for each element in key:                      for i in range(len(key)):
##    print it:                                           print(key[i])
##    for each element in alphabet:                 for i in range(len(alphabet)):
##    print it:                                           print(alphabet[i])
def printkey(key):
    if(len(key) < 1):
        raise ValueError("The key length is not valid")
    else:
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        print("Pos in CypherText: ", end="")
        for i in range(len(key)):
## Uncomment if printkey() is used before encrypt()
            temp = key[i]               #
            key[i] = alphabet[temp]     #
            print(key[i], end=" ")
            
        print("\nPos in PlainText:  ", end="")
        for i in range(len(alphabet)):
            print(alphabet[i], end=" ")
#---------------------------------------------------------------------------------------------------------------------------------------
##    test() Pseudocode
##    funciton definition:                             def test():
##    set working directory:                                os.chdir("C:\\")
##    get file name:                                        testObj.get_filename()
##    get user name:                                        testObj.get_owner()
##    create key:                                           key = genkey(26)
##    print key:                                            printkey(key)
##    begin try block:                                      try:
##    create object                                               encryptObj = testObj.encrypt(key)
##    begin except block:                                   except ValueError as errMsg:
##    print error message:                                        print(errMsg)
##    end program:                                                return
##    begin try block:                                      try:
##    create object                                               decryptObj = encryptObj.decrypt(key)
##    begin except block:                                   except ValueError as errMsg:
##    print error:                                                print(errMsg)
##    end program:                                                return
##    begin try block:                                      try:
##    check if encryption/decryption work with isSameFile():      isSameFile("Decrypted_"+fileName+".txt")
##    begin except block:                                   except IOError as errMsg:
##    print error:                                                print(errMsg)
##    end program:                                                return
##    print finish message:                                 print("Congrats, all done!")
def test():
    os.chdir("C:\\")
    testObj = TextFile()
    
    #Get info
    testObj.get_filename()
    testObj.get_owner()
    
    #gen and print key
    key = genkey(26)
    printkey(key)

    try:
        encryptObj = testObj.encrypt(key)
    except ValueError as errMsg:
        print(errMsg)
        return

    try:
        decryptObj = encryptObj.decrypt(key)
    except ValueError as errMsg:
        print(errMsg)
        return

    try:
        testObj.isSameFile( decryptObj.retrieve_fileName() )
    except IOError as errMsg:
        print(errMsg) 
        return
    
    print("\nCongrats ", testObj.retrieve_owner(), ", encryption and decryption work correctly!", sep="")
#----------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    test()
