# L.McIntyre 2025
# Wanted to make an art piece for an artistic math person, and needed a guide for the lines.

# Program Usage: Create a program that draws a series of geomtric circles
# with a common center in increasing radius, in order of the fibonacci sequence.
# Optional: With lines connecting the pieces at a given angle

# Done in Python. Using turtle.


# Function to fill an array with the numbers of the fibnoccai sequences
# to be used in an arithemtic drawing

from turtle import *
import random
from time import perf_counter as sleep

def fibFill(arraySize):
    arrayName = [1,1]
    while len(arrayName)<arraySize:
        arrayName.append(arrayName[len(arrayName)-1]+arrayName[len(arrayName)-2])
    return arrayName


# Function to draw the circles.
# Upper Range indicates how large the circles whould get.
# With an option to connect them at a defined angle
def interlockingCircles(upperRange, xCoord, yCoord, angle=None, modifier=10 ):
    angleDirection = angle
    fibs=fibFill(50)
    fibs=fibs[1:] #Remove the duplicate  'one' in the sequence.
    
    #Using i as the radius. Interate through the sequence until upper limit is reached
    for i in fibs:
        if i<upperRange:
            #move so (x,y) is the continuously center of the half circles
            up()
            bk(i*modifier)
            right(90)
            
            #draw half circle
            down()
            circle(i*modifier,-180)

            currentHeading=heading() #captured to make sure the segments are drawn in the correct location
            #optional connecting lines
            
            if(angle != None):
                #check if the connecting segment will be drawn
                if(fibs[fibs.index(i)+3] < upperRange):
                    up()
                    circle(i*modifier,angle)
                    setheading(angleDirection) #point heading parallel to intended angle
                    down()
                    forward((fibs[fibs.index(i)+3]-i)*modifier)
                    setheading(currentHeading) #Return the heading to the previous location
                    angleDirection+=90
                

            #return to conter
            teleport(xCoord,yCoord)

#Set the angle of the line between the circles from the center. 
#Modifiying to work from where it ends! 
def logicTester(angle,distance):
    up()
    teleport(0,0)
    home() #makes heading pointed to the right
    fd(distance) #moves to edge of circle
    left(90)
    circle(distance, angle)
    left(angle-heading()) #point to angle degrees
    down()
    forward(fib[fib.index(distance)+3]-distance)
    print(fib[fib.index(distance)+3]-distance)



#Intended Use
ht()
interlockingCircles(20,0,0,57,5)

sleep(5)

#Other Examples
up()
home()
clear()
colors=['red','blue','black','purple','navy']
for x in range(5):
    angle=random.randrange(1,360)
    size = random.uniform(5,13)
    color(random.choice(colors))
    interlockingCircles(50,0,0,angle,size)
    

mainloop()

    
