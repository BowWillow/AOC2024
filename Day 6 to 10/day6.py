'''
Day 6: 

input is <>
Part 1: <> Answer is <> Test input answer is <>

Part 2 <>.  Answer is <> Test input answer is <>

personal stats
<>
'''
from collections  import defaultdict
import copy

inputFile = '../Data/Day 6 Input.txt'
inputFile = '../Data/Day 6 InputTEMP.txt'



mapDict = defaultdict(lambda:' ')
mapWidth = 0; mapHeighth = 0

# routeList generated in pt1; used to find obstacle placement in pt2
routeList = list() # elements are location and direction
guardX = -1; guardY = -1; guardDir = (0,-1)
# save map, guard location and direction for pt2
savedMapDict = defaultdict(lambda:' ')
savedGuardX = -1; savedGuardY = -1; savedGuardDir = (0,-1)

def parseInput():
    global mapDict,mapWidth, mapHeighth, \
        guardX, guardY, guardDir, routeSet, \
        savedMapDict, savedGuardX, savedGuardY, savedGuardDir 

    for line in open(inputFile, 'r') :
        
        lineStart = 0
        carotRow = line.find('^')
        if carotRow != -1:
            guardX = carotRow; guardY = mapHeighth
            savedGuardX = guardX; savedGuardY = guardY
            savedGuardDir = guardDir
            mapDict[(carotRow,mapHeighth)] = 'X'
            routeList.append((guardX, guardY, guardDir))

        while lineStart != -1:
            lineStart = line.find('#',lineStart)
            if lineStart != -1:
                mapDict[(lineStart,mapHeighth)] = '#'
                lineStart += 1

        mapWidth = len(line); mapHeighth +=1
        savedMapDict = copy.deepcopy(mapDict)
    return


def takeStep(x, y, dir):


    dirX,dirY = dir
    return x+dirX,y+dirY


def guardTurn():
    global guardDir
    Yup = (0,-1);  Ydown = (0,1)
    Xright = (1,0); Xleft = (-1,0)
    if guardDir == Yup:
        guardDir =  Xright  ; return
    if guardDir == Xright:
        guardDir =  Ydown  ; return
    if guardDir == Ydown:
        guardDir =  Xleft  ; return
    if guardDir == Xleft:
        guardDir =  Yup  ; return


def doIt():
    global mapDict,mapWidth, mapHeighth, guardX, guardY, guardDir

    # pt 1 walk - obstacle - turn rinseAndRepeat
    onMap = True
    while onMap:
        # try a step
        newGuardX,newGuardY = takeStep(guardX, guardY, guardDir)
        # if off map stop
        if newGuardX < 0 or newGuardX >= mapWidth or \
        newGuardY < 0 or newGuardY >= mapHeighth:
            onMap = False
            continue
        # if obstacle change direction
        if mapDict[(newGuardX,newGuardY)] == '#':
            guardTurn()
        else:
            # commit step
            guardX = newGuardX; guardY = newGuardY
            mapDict[(newGuardX,newGuardY)] = 'X'
            routeList.append((guardX, guardY, guardDir))

    # count x values in mapDict
    pt1Count = 0
    for char in mapDict.values():
        if char == 'X':
            pt1Count += 1 

    # pt2 find obstacle placements

    pt2Count = 0
    # for each routeList item create obstacle and place in map
    for item in routeList:
    # unpack item 
        x,y,dir = item
    # initialize new map, guard location and direction
        mapDict = copy.deepcopy(savedMapDict)
        guardX = savedGuardX;  guardY = savedGuardY
        guardDir = savedGuardDir
   
    #    if can't create skip to next item
        x,y = takeStep(x,y,dir)
        if mapDict[(x,y)] == '#':
            continue
        else:
            mapDict[(x,y)] = '#'
    # walk -- recording route in routeSet. TODO
    # if guard leaves map -- not a good obstacle TODO
    # if route loop occurs -- good obstacle else continue TODO
        pass



    print(f'Part 1: {pt1Count}')
    print(f'Part 2: {pt2Count}')


def main():
    parseInput()
    doIt()
    return

main()
