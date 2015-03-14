#Brandon Lee
#ID: 14010627X
#9/26/14

#Question 1 Pseudocode:
#function definition:													def main():
#prompt user input for first name:											firstName = input("String Prompt")
#prompt user input for last time:											lastName = input("String Prompt")
#combine both inputs into a single string:									fullName = firstName + lastName
#initialize variable to store length of string:								stringLength = len(fullName)
#create for loop and use initialized variable for range:					for i in range(0,stringLength):
#print the string:																print(fullName[0:i+1])
#create another for loop for going backwards, same concept as before:		for i in range(stringLength-1,0,-1)
#print the string:																print(fullName[0:j])

def test1():
	firstN = input("Please enter your first name: ")
	lastN = input("Please enter your last name: ")
	fullName = firstN + " " + lastN
	strlen = len(fullName)
	for i in range(0,strlen):
		print(fullName[0:i+1])
	for j in range(strlen-1,0,-1):
		print(fullName[0:j])


#Question 2 Pseudocode:
#import math library:														import math
#function definition:														def main():
#prompt user to enter positive n value:											n = eval(input("String Prompt"))
#initialize variable to store total value as for loop iterates:					totalValue = 0
#print value of e and labels:													print("Value of e = ", math.e, "Round:     The approximated e: ")
#create for loop with range of user input:										for i in range(n)
#initialize variable to store factorial of current round:						factorialVariable = math.factorial(i)
#increment total value by adding its self with (1/current value factorial):		totalValue = totalValue + (1/factorialValue)
#print round number and the total value:										print(i, totalValue)

import math

 def test2():
	n = eval(input("Enter positive n value: "))
	totalVal = 0
	print("The value of e is:", math.e)
	print("Round:     The approximated e: ")
	for i in range(n):
		factVar = math.factorial(i) #0 factorial = 1
		totalVal = totalVal + (1/factVar)
		print(i+1, "        ", totalVal)