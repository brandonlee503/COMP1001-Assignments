"""
Brandon Lee
14010627X
Assignment 5 
10/17/2014
"""

"""
Part 1 Pseudocode:
function def:                                                           def part1():
openfile a text file:                                                       infile = open("name", "w")
get user input for start/end numbers:                                       start,end = eval(input("Prompt"))
get user input for row size and number of spaces:                           row, numSpace = eval(input("Prompt"))
initilize for loop with range of the interval of numbers the user inputted: for i in range(end-start):
write starting from the starting number:                                         infile.write(str(start))
if row not filled up yet, add comma after number:                                if(row not filled): infile.write(",")
otherwise, add a new line since row is full:                                     else: infile.write("\n")
increment starting number:                                                  start += 1
return number of spaces user initally inputted:                             return(numSpace)
"""
def part1():
    infile = open("A5Write.txt", "w")

    startNum, endNum = eval(input("Please enter a starting number and an ending number: "))
    rowSize, spaceNum = eval(input("Please enter the number of numbers printed on a row and the number of spaces per item: "))
    
    for i in range(endNum-startNum+1):
        infile.write(str(startNum))
        if(((i+1) % rowSize) != 0):
            infile.write(",")
        else:
            infile.write("\n")   
        startNum += 1
        
    return (spaceNum)

"""
Part 2 Pseudocode:
define function:                          def part2():
create file to read from:                     outfile = open("filename", "r")
declare space string:                         spaces = ""
read the file:                                content = outfile.read()
determine how many spaces to add:             for i in range(numSpace): spaces += " "
create for loop for length of the string:     for i in range(len(content)):
if index has comma, print spaces:                if(content[i] == ","): print(spaces, end="")
else print the index:                            if(content[i] != ","): print(content[i], end="")
"""
def part2(spaceNum):
    outfile = open("A5Write.txt","r")
    spaces = ""
    
    content = outfile.read()
    
    for i in range(spaceNum):
        spaces += " "

    for i in range(len(content)):
        if(content[i] == ","):
            print(spaces, end="")
        if(content[i] != ","):
            print(content[i], end="")

def main():
    spaceNum = part1()
    part2(spaceNum)


main()
