#Brandon Lee
#ID: 14010627X
#9/17/2014
#COMP1001
#Assignment 1

#PSEUDOCODE
#function definition:                                                         def main()
#prompt user to input n value:                                                    n = eval(input("string"))
#create for loop with a range of the user input:                                  for i in range(n)
#create another variable to store the number of spaces as the for loop runs:          i = storeSpaces
#create for loop nested within the previous for loop                                  for j in range(storeSpaces)
#with a range of the newly created variable:                              
#print a single space within the nested for loop:                                         print(" ")
#lastly, on outer for loop print the number of cycles that the for loop has       print(i)
#been through according to the user imputed value:


def main():
	n = eval(input("Please input a positive integer: "))
	for i in range(n):
		spaces = i
		for j in range(spaces):
			print(" ", end="")
		print("i=",i+1)	