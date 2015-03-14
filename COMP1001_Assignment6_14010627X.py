"""
Brandon Lee
14010627X
Assignment 6

Pseudocode:

Import graphics file:               from graphics import *
Function definition:                def main():
Read file:                                 inputName = open("c:\config.txt","r")
Read input for window dimensions:          firstLine = inputName.readline()                                 #This reads the only first line of file 
                                           windowSize = [int(i) for i in firstLine.split() if i.isdigit()]  #Read string and seperate integer inputs into list  
Read user input for colors:                secondLine = inputname.readline()                                #This reads second line of the file
                                           colors = secondLine.split()                                      #Split the different colors into list
Create window:                             win = GraphWin("Name", windowSize[0], windowSize[1])             #Create window with user inputs
Set background color:                      win.setBackground("white")
Define center:                             center = Point(winSize[0]/2, winSize[1]/2)                       #Sets this to the exact center of window
Define Diameter:                           diameter = winSize[0]/2                                          #Set diameter to window size

Define circle:                             circleOne = Circle(center, diameter)
Fill circle with color:                    circleOne.setfill("set color depending on file")
Draw circle:                               circleOne.draw(win)

                                           ---Repeat this for the number of circles---

Define ring:                               ringOne.Circle(center, diameter-20)
Set ring outline color:                    ringOne.setOutline("color")
Draw ring:                                 ringOne.draw(window)

                                           ---Repeat this for the number of rings---
"""
from graphics import *

def main():
    #Read file
    inputFile = open("c:\\config.txt","r")

    #Get user input for window dimensions
    line1 = inputFile.readline()
    winSize = [int(i) for i in line1.split() if i.isdigit()]
    
    #Get user input for colors
    line2 = inputFile.readline()
    colors = line2.split()
    
    #Create window and draw content
    window = GraphWin("Target Board", winSize[0], winSize[1])
    window.setBackground("white")
    center = Point(winSize[0]/2,winSize[1]/2)
    diameter = winSize[0]/2

    #Draw Circles
    circle1 = Circle(center, diameter)
    circle1.setFill(colors[4])
    circle1.draw(window)

    circle2 = Circle(center, diameter-40)
    circle2.setFill(colors[3])
    circle2.draw(window)
    
    circle3 = Circle(center, diameter-80)
    circle3.setFill(colors[2])
    circle3.draw(window)

    circle4 = Circle(center, diameter-120)
    circle4.setFill(colors[1])
    circle4.draw(window)

    circle5 = Circle(center, diameter-160)
    circle5.setFill(colors[0])
    circle5.draw(window)

    #Draw Rings
    ring1 = Circle(center, diameter-20)
    ring1.draw(window)

    ring2 = Circle(center, diameter-60)
    ring2.setOutline("white")
    ring2.draw(window)

    ring3 = Circle(center, diameter-100)
    ring3.draw(window)

    ring4 = Circle(center, diameter-140)
    ring4.draw(window)    

    ring5 = Circle(center, diameter-180)
    ring5.draw(window)   

    inputFile.close()

    
main()
