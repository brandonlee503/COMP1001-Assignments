#Brandon Lee
#14010627X
#Assignment 4
#10/8/14

#Pseudocode
#Function Definition:								def main():
#Prompt user for start and end numbers:			        			start, end = eval(input("prompt"))
#Prompt user for the row size and number of spaces:					rowSize, spaceNum = eval(input("prompt"))
#
#
#Declare a variable for number of spaces:						spaces = ""
#Declare a variable to store each time you need a newline:			        Increment = rowSize
#Create for loop for creating number of spaces between each number:			for i in range(spaceNum):
#Increment by one space:									spaces += " "
#Create for loop for incrementing the n value after each iteration or print:	        for i in range(endNum-startNum+1):
#Print variables:										print(startNum, end=spaces)
#Increment:											startNum += 1
#Check if a newline is needed after each iteration:						if i+1 == rowSize:
#Create new line:						                			print("")
#													rowSize += increment

def main():
	startNum, endNum = eval(input("Please enter a starting number and an ending number: "))
	rowSize, spaceNum = eval(input("Please enter the number of numbers printed on a row and the number of spaces per item: "))
	print("---")
	print("Your print-out of numbers", startNum, "-", endNum, "using", rowSize, "columns and", spaceNum, "spaces between numbers: ")
	spaces = ""
	rowSizeIncrement = rowSize
	for i in range(spaceNum):
		spaces += " "
	for i in range(endNum-startNum+1):
		print(startNum, end=spaces)
		startNum += 1
		if i+1 == rowSize:
			print("")
			rowSize += rowSizeIncrement

main()
