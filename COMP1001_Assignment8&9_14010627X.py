"""
Brandon Lee
14010627X
COMP1001 Assignment 8-9
11-14-14
"""

from random import shuffle
import os

"""
getKey() PseudoCode
function definition:                 def genkey(length):
check if length is less than 1:         if(length<1):
if so raise value error:                   raise ValueError
otherwise:                              else:
create key:                                key = []
for loop from i to the length:             for i in range(length):
add i value to key:                             key.append(i)
shuffle key list:                          shuffle(key)
return key:                             return key
"""
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
"""
printkey() Pseudocode
function definition:               def printkey(key):
check if length of key is under 1:       if(len(key) < 1):
if so raise value error:                      raise ValueError
otherwise print plain/cyphertext:        else:
declare alphabet list:                        alphabet = ["a", ... ,"z"]
for each element in key:                      for i in range(len(key)):
print it:                                           print(key[i])
for each element in alphabet:                 for i in range(len(alphabet)):
print it:                                           print(alphabet[i])
"""
def printkey(key):
    if(len(key) < 1):
        raise ValueError("The key length is not valid")
    else:
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        print("Pos in CypherText: ", end="")
        for i in range(len(key)):
## Uncomment if printkey() is used before encrypt()
##            temp = key[i]
##            key[i] = alphabet[temp]
            print(key[i], end=" ")
            
        print("\nPos in PlainText:  ", end="")
        for i in range(len(alphabet)):
            print(alphabet[i], end=" ")
#----------------------------------------------------------------------------------------------------------------------------------------
"""
encrypt() Pesudocode
function definition:                                     def encrypt(plaintext, key):
if key length not 26:                                        if(len(key) != 26):
raise value error:                                               raise ValueError
otherwise:                                                   else:
create list from plaintext and convert to lowercase:             listPlainText = list(plaintext.lower())
declare alphabet:                                                alphabet = ["a", ... ,"z"]

Change key from numbers to alphabet letters..
*Note: No need to do this again in printkey() if done here*
for each value in key:                                          for i in range(len(key)):
store key value:                                                    temp = key[i]
redeclare key value with the stored key value in alphabet:          key[i] = alphabet[temp]

Change each character in string to new encrypted key value..
for each value in plaintext:                                    for i in range(len(plaintext)):
if character is in the alphabet:                                    if(listPlainText[i] in alphabet):
get the letter position in the alphabet:                            letterPos = alphabet.index(letterPlainText[i])
change the text to key position of the letter:                      listPlainText[i] = key[letterPos]

join all list values together:                                  plaintext = "".join(listPlainText)
return:                                                         return plaintext
"""
def encrypt(plaintext, key):
    if(len(key) != 26):
        raise ValueError("The key length is not 26")
    else:
        listPlainText = list( plaintext.lower() )
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        # Comment if printkey() is used before encrypt() 
        for i in range(len(key)):               #
            temp = key[i]                       #
            key[i] = alphabet[temp]             #
        
        for i in range(len(plaintext)):
            if(listPlainText[i] in alphabet):
                letterPos = alphabet.index(listPlainText[i])
                listPlainText[i] = key[letterPos]

        plaintext = "".join(listPlainText)
        return plaintext
#----------------------------------------------------------------------------------------------------------------------------------------
"""
decrypt() Pseudocode
function decleration:                               def decrypt(ciphertext, key):
if key length is not 26                                 if(len(key) != 26):
raise value error                                           raise ValueError
otherwise                                               else:
create list from ciphertext and convert to lowercase:       listCipherText = list( ciphertext.lower() )
declare alphabet                                            alphabet = ["a",... ,"z"]

for every value in ciphertext                               for i in range(len(ciphertext)):
if it's a letter                                                  if(listCipherText[i] in alphabet):
get the letter position in the key                                      letterPos = key.index(listCipherText[i])
change the key to alphabet position of the letter                       listCipherText[i] = alphabet[letterPos]
                
combine list                                                ciphertext = "".join(listCipherText)
return                                                      return ciphertext
"""
def decrypt(ciphertext, key):
    if(len(key) != 26):
        raise ValueError("The key length is not 26")
    else:
        listCipherText = list( ciphertext.lower() )
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        for i in range(len(ciphertext)):
            if(listCipherText[i] in alphabet):
                letterPos = key.index(listCipherText[i])
                listCipherText[i] = alphabet[letterPos]
                
        ciphertext = "".join(listCipherText)
        return ciphertext
#----------------------------------------------------------------------------------------------------------------------------------------
"""
getFile() Prototype
function definition:         def getFile():
Create while loop:                while(True):
Ask user for file name:                fileName = input("Please input a text file: ")
if file exists:                        if os.path.exists(fileName):
open the file                             fileHandler = open(fileName, "r+")
return the file name and handler          return (fileName, fileHandler)
otherwise                              else:
print error message and loop              print("File not found. Please re-enter a file name: ")
"""
def getFile():
    while(True):
        fileName = input("Please input a text file: ")
        if os.path.exists(fileName):
            fileHandler = open(fileName, "r+")
            return (fileName, fileHandler)
        else:
            print("File not found. Please re-enter a file name: ")
#----------------------------------------------------------------------------------------------------------------------------------------
"""
isSameFile() Pseudocode
function definition:    def isSameFile(file1, file2):
if both files exist:        if(os.path.exists(file1) and os.path.exists(file2)):
open both and read:              file1h = open(file1, "r")
                                 file2h = open(file2, "r")
        
read content:                     content1 = file1h.read()
                                  content2 = file2h.read()

change content to lowercase:      lower1 = content1.lower()
                                  lower2 = content2.lower()
        
if both contents are equal:       if(lower1 == lower2):
return true                             return True
otherwise false                   else:
                                        return False
if file not found           else:
raise ioerror                     raise IOError("The file(s) cannot be found")
"""
def isSameFile(file1, file2):
    if(os.path.exists(file1) and os.path.exists(file2)):
        file1h = open(file1, "r")
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
"""
test() Pseudocode
funciton definition:                             def test():
set working directory:                                os.chdir("C:\\")
create key:                                           key = genkey(26)
get user input for file:                              fileName, fileHandler = getFile()
create text file:                                     encryptFile = open("Encrypted_"+fileName+".txt", "w+")
begin try block:                                      try:
read from user inputted file:                               encryptContent = encrypt(fileHandler.read(), key)
print randomly generated key:                               printkey(key)
read encrypted file and write over:                         encryptFile.write(encryptContent)
begin except block:                                   except ValueError as errMsg:
print error message:                                        print(errMsg)
end program:                                                return
close file:                                           encryptFile.close()
reopen file:                                          encryptFile = open("Encrypted_"+fileName+".txt", "r+")
read encrypted content and write over:                encryptContent = encryptFile.read()
reclose file:                                         encryptFile.close()
create another text file for editing:                 decryptFile = open("Decrypted_"+fileName+".txt", "w+")
begin try block:                                      try:
decrypt content and create decrypted string:                decryptContent = decrypt(encryptContent, key)
write decrypted content onto decrypted content:             decryptFile.write(decryptContent)
begin except block:                                   except ValueError as errMsg:
print error:                                                print(errMsg)
end program:                                                return
begin try block:                                      try:
check if encryption/decryption work with isSameFile():      isSameFile(fileName, "Decrypted_"+fileName+".txt")
begin except block:                                   except IOError as errMsg:
print error:                                                print(errMsg)
end program:                                                return
print finish message:                                 print("Congrats, all done!")
"""
def test():
    os.chdir("C:\\")                                                                    # set working directory
    key = genkey(26)                                                                    # create key
    
    fileName, fileHandler = getFile()
    encryptFile = open("Encrypted_"+fileName+".txt", "w+")                              # w+ is for creating/reading/writing
    
    try:
        encryptContent = encrypt(fileHandler.read(), key)                               # Read from main file
        printkey(key)                                                                   # Print key
        encryptFile.write(encryptContent)                                               # read encrypted content and write over
    except ValueError as errMsg:
        print(errMsg)
        return

    encryptFile.close()                                                                 # Close and reopen file
    encryptFile = open("Encrypted_"+fileName+".txt", "r+")                              
    encryptContent = encryptFile.read()                                                 # Read file
    encryptFile.close()                                                                 # Reclose
        
    decryptFile = open("Decrypted_"+fileName+".txt", "w+")                              # Create another file                             
    
    try:
        decryptContent = decrypt(encryptContent, key)                                   # decrypt content and write string
        decryptFile.write(decryptContent)                                               # write decrypted content onto decrypted content
    except ValueError as errMsg:
        print(errMsg)
        return
        
    try:
        isSameFile(fileName, "Decrypted_"+fileName+".txt")
    except IOError as errMsg:
        print(errMsg)
        return
        
    print("\nCongrats, encryption and decryption work correctly")
#----------------------------------------------------------------------------------------------------------------------------------------
#If module is run as main module itself, run test
if __name__ == "__main__":
    test()
