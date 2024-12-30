'''
Day 10: Hoof It

input is array of altitudes
Part 1: find hiking trails; count number of peaks accessible from all trail heads.
 Answer is 574 Test input answer is 36

Part 2 same but count routes.  Answer is 1238 Test input answer is 81


'''
from collections import defaultdict

inputFile = '../Data/Day 10 InputTEMP.txt'
inputFile = '../Data/Day 10 Input.txt'

mapList = list()

def parseInput():
    global mapList

    #read input and convert to numbers bounding the outsides with -5
    firstTime = True
    for line in open(inputFile, 'r') :
        line = line.strip('\n')
        if firstTime:
            mapList.append([-5]*(len(line)+2))
            firstTime = False
        tempList = [-5] + [int(x) for x in line] + [-5]
        mapList.append(tempList)
    mapList.append([-5]*len(mapList[0]))



def findNext(currentSet, z:int): # z is level to look for
    global mapList

    resultSet = set()
    for (x,y)  in currentSet:
        for (xTest,yTest) in [(x-1,y),(x+1,y), \
                              (x,y-1),(x,y+1)]:
                if mapList[yTest][xTest] == z:
                    resultSet.add( (xTest,yTest) )
    return resultSet


def doIt():
    global mapList

    pt1Total = 0; pt2Total = 0
    thTuple = (-1,-1)
    countDict = defaultdict(int)

    # pt1
    for yCand in range(1,len(mapList)):
        for xCand in range(1,len(mapList[1])):
            # at each trailhead:
            if mapList[yCand][xCand] == 0:
                thTuple = (xCand,yCand)
                currentSet = { (xCand,yCand) }
                for z in range(1,10):
                    currentSet = findNext(currentSet, z)
                # at this point currentSet contains all accessible peaks
                pt1Total += len(currentSet)

    # pt2
                # for each peak node 
                for (xPeak,yPeak) in currentSet:

                    # start countDict with peakTuple
                    countDict.clear(); countDict[ (xPeak,yPeak) ] = 1
                    currentLevel = 9; newLevel = currentLevel - 1
                    nodeStackList = [(xPeak,yPeak)] # peakTuple
                    onTrailSet = set()
                    while currentLevel > 0:
                        for (x,y) in nodeStackList:   
                            #     for four newLoc based on item
                            for (xTest,yTest) in [(x-1,y),(x+1,y), \
                                                (x,y-1),(x,y+1)]:
                                if mapList[yTest][xTest] == newLevel:
                                    onTrailSet.add( (xTest,yTest) ) 
                                    countDict[ (xTest,yTest) ] += countDict[(x,y)]

                        if currentLevel != 1: 
                            nodeStackList = list(onTrailSet)                    
                            currentLevel -= 1; newLevel = currentLevel - 1
                            onTrailSet.clear()
                        else:   # at the trailhead
                            currentLevel = 0
                            pt2Total += countDict[thTuple]

    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
