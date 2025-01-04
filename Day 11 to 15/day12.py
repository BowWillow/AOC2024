'''
Day 12: Garden Groups 

input is lots of letters
Part 1: Find perimeter and area per problem statement 
Answer is 1546338 Test input answer is 1930

Part 2 change perimeter calculation per problem statement.  
Answer is 978590 Test input answer is 1206

personal stats
<>

'''
from collections import deque

inputFile = '../Data/Day 12 Input.txt'
inputFile = '../Data/Day 12 InputTEMP.txt'
inputFile = '../Data/Day 12 Input.txt'

plotList = list() # list of lists
# A-Z crops, "x" harvested, "." clear area

pt2PerimeterSet = set() # (x,y,dir)

thisPlotLocSet = set() # set of (x,y) tuples

def parseInput():
    global plotList

    firstTimeFlag = True
    for line in open(inputFile, 'r') :
        line = line.strip('\n')
        if firstTimeFlag:
            borderLine = "."*(len(line)+2)
            plotList.append(list(borderLine))
            firstTimeFlag = False  
        plotList.append(list("."+line+"."))
    plotList.append(list(borderLine))


def findFullPlot(startX,startY, cropType):
    global plotList, thisPlotLocSet

    plotQueue = deque( ) # create queue with starting plot
    plotQueue.append((startX, startY))
    # do til queue is empty
    while len(plotQueue) != 0:
        thisX,thisY = plotQueue.popleft() #  take item
        if plotList[thisY][thisX] == cropType:
            #  mark as harvested 'x'
            thisPlotLocSet.add((thisX,thisY))
            plotList[thisY][thisX] = 'x'
    
            #  add neighbors to queue
            if plotList[thisY-1][thisX] == cropType:
                plotQueue.append((thisX,thisY-1))
            if plotList[thisY+1][thisX] == cropType:
                plotQueue.append((thisX,thisY+1))
            if plotList[thisY][thisX-1] == cropType:
                plotQueue.append((thisX-1,thisY))
            if plotList[thisY][thisX+1] == cropType:
                plotQueue.append((thisX+1,thisY))
    return


# build pt1 perimeter and gather data for pt2
def pt1CalcPerimeter():
    global plotList, thisPlotLocSet, pt2PerimeterSet

    perimeter = 0
    # for xy in set
    for (x,y) in thisPlotLocSet:
        if plotList[y-1][x] != 'x':
            perimeter += 1
            pt2PerimeterSet.add( (x,y,'N')  )
        if plotList[y+1][x] != 'x':
            perimeter += 1
            pt2PerimeterSet.add( (x,y,'S')  )
        if plotList[y][x-1] != 'x':
            perimeter += 1
            pt2PerimeterSet.add( (x,y,'W')  )
        if plotList[y][x+1] != 'x':      
            perimeter += 1
            pt2PerimeterSet.add( (x,y,'E')  )

    return perimeter

def pt2calcPerimeter():
    global pt2PerimeterSet

    sideCount = 0

    while len(pt2PerimeterSet) > 0:
        (x,y,dir) = pt2PerimeterSet.pop()
        sideCount += 1
        if dir == 'N' or dir == 'S':
            incX = 1; incY = 0
        if dir == 'E' or dir == 'W':
            incX = 0; incY = 1  
    # check up / left
        tmp = 1
        doneFlag = False
        while not doneFlag:
            if (x-(tmp*incX),y-(tmp*incY),dir) in pt2PerimeterSet:
                pt2PerimeterSet.remove((x-(tmp*incX),y-(tmp*incY),dir))
                tmp += 1
            else:
                doneFlag = True
    # check down / right
        tmp = 1
        doneFlag = False
        while not doneFlag:
            if (x+(tmp*incX),y+(tmp*incY),dir) in pt2PerimeterSet:
                pt2PerimeterSet.remove((x+(tmp*incX),y+(tmp*incY),dir))
                tmp += 1
            else:
                doneFlag = True
    return sideCount

def clearLand():
    global plotList, thisPlotLocSet

    for (x,y) in thisPlotLocSet:
        plotList[y][x] = '.'
    thisPlotLocSet.clear()
    pt2PerimeterSet.clear()
    return


def doIt():
    global plotList, thisPlotLocSet

    pt1Total = 0; pt2Total = 0
    # pt1

    # take next available plot
    for nextY in range (1,len(plotList)-1):
        for nextX in range(1,len(plotList[0])-1):
            if plotList[nextY][nextX] != '.':
                cropType = plotList[nextY][nextX]
                # create queue of all adjacent
                findFullPlot(nextX,nextY, cropType) # thisPlotLocSet contains all locs
                # add the cost of this plot
                pt1Total += len(thisPlotLocSet) * pt1CalcPerimeter()
                pt2Total += len(thisPlotLocSet) * pt2calcPerimeter()
                # clear the land
                clearLand()

    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
