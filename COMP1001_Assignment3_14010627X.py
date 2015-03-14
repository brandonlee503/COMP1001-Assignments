#Brandon Lee
#ID: 14010627X
#10/1/14

#Assignment 3 Pseudocode
#function definition:											def main():
#prompt user for line of text:										textInput = input("String Prompt")	
#prompt user for a key value:										keyInput = eval(input("String Prompt")
#declare string for a cipher:										cipherString = ""
#initialize for loop with range of the size of user text string:	for i in textInput:
#initialize variable for the new ciphered:								newCipher = (ord(i)+keyInput)%126
#check if characters were encrypted correctly:							if(newCipher<32):
#																			newCipher+=31
#print encrypted text:												print("String" + cipher)


import sys

def main():
	userText = input("Please input a text (only English letters) to be encrypted: ")
	userKey = eval(input("Please enter a key (from 1 to 25): "))
	cipher = ""
	for i in userText:
		yam = (ord(i)+userKey)%126
		if(yam < 32):
			yam+=31
		cipher += chr(yam)
	print("The encrypted message is: " + cipher)

main()
