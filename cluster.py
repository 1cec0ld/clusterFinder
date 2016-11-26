#import shitake mushrooms
import math
import random
import turtle
import time

#global constants
#How many points to have total
totalPoints = 50
#range of x locations possible of -x to x
xRange = [-100,100]
#range of y locations possible of -y to y
yRange = [-100,100]
#number of points per cluster
clusterSize = 5


#functions are good
def createRandomPoints(count, x, y):
    points = []
    for i in range(count):
        xcoord = random.randint(x[0],x[1])
        ycoord = random.randint(y[0],y[1])
        newPoint = [xcoord,ycoord]
        points.append(newPoint)
    return points
def displayPoints(pts):
    turtle.penup()
    for eachPoint in pts:
        turtle.goto(eachPoint[0],eachPoint[1])
        turtle.color("Blue")
        turtle.dot(5)
def getCluster(pts,size):
    minSum = 0
    results = []
    t = []
    theSum = 0
    #initialize a base minimum, using the distance from first few points to the first point
    for i in range(min(size,len(pts))):
        minSum = minSum + (pts[0][0]-pts[i][0])**2 + (pts[0][1]-pts[i][1])**2
        results.append(pts[i])
    for j in range(len(pts)):
        t = []
        for k in range(len(pts)):
            distval = (pts[j][0]-pts[k][0])**2 + (pts[j][1]-pts[k][1])**2
            t.append({'pt':pts[k],'dist':distval})
        t.sort(key=lambda obj: obj['dist'])
        theSum = 0
        for m in range(min(size,len(pts))):
            theSum = theSum + t[m]['dist']
        if theSum < minSum:
            minSum = theSum
            results = []
            for i in range(min(size,len(pts))):
                results.append(t[i]['pt'])
    print "Cluster distance: ",math.sqrt(minSum)
    return results
def drawCluster(points):
    turtle.tracer(1)
    turtle.color("#%06X" % random.randint(0x0, 0xFFFFFF))
    for eachPoint in points:
        turtle.penup()
        turtle.goto(points[0][0],points[0][1])
        turtle.dot(5)
        turtle.pendown()
        turtle.goto(eachPoint[0],eachPoint[1])
        turtle.dot(5)
        
def resetScreen():
    turtle.clearscreen()
    turtle.title("Cluster Finder")
    turtle.hideturtle()
    #turtle.speed(0)
    turtle.tracer(10)
    print "---------------------------------------------"

if __name__ == '__main__':
    while True:
        resetScreen()
        #create a random spray of points, within constraints
        randomPoints = createRandomPoints(totalPoints,xRange,yRange)
        #plot them on turtle view
        displayPoints(randomPoints)
        #while there are still unused points
        while len(randomPoints) > 0:
            #use my algorithm to determine which points are best-cluster
            clusterPoints = getCluster(randomPoints,clusterSize)
            #use turtle to visually link them
            drawCluster(clusterPoints)
            #remove each one from the list of unused points
            for eachPoint in clusterPoints:
                randomPoints.remove(eachPoint)
        time.sleep(1)
    turtle.done()
