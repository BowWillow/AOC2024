'''
Day 13: Claw Contraption

input is lines like
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

Part 1: simulate the claw machine Answer is 35082 Test input answer is 480

Part 2 simulate the claw machine with a large offset.  Answer is 82570698600470 

'''
import re

inputFile = '../Data/Day 13 InputTEMP.txt'
inputFile = '../Data/Day 13 Input.txt'

clawMachineList = list()

def parseInput():
    global clawMachineList

    doneFlag = False
    fd = open(inputFile, 'r') 
    while not doneFlag:
        tmpLine = ''
        line = fd.readline().strip()
        if line == '':
            doneFlag = True
            continue
        tmpLine += line
        line = fd.readline().strip()
        tmpLine += line
        line = fd.readline().strip()
        tmpLine += line
        line = fd.readline().strip()
        numList = re.findall(r'[0-9]+', tmpLine)
        intList = [int(x) for x in numList]
        clawMachineList.append(intList )

def calcMachine(clawMachine,addFactor):

    aX = clawMachine[0]; aY = clawMachine[1]
    bX = clawMachine[2]; bY = clawMachine[3]
    pX = clawMachine[4] + addFactor; pY = clawMachine[5] + addFactor
    
    D = aX * bY - aY * bX
    a = (pX * bY - pY * bX) // D
    b = (aX * pY - aY * pX) // D
    if (aX*a + bX*b != pX) or (aY*a + bY*b != pY):
        thisCost = 0
    else:
        thisCost = a*3 + b
    return thisCost


def doIt():
    global tmpList
    
    pt1Cost = 0; pt2Cost = 0
    for item in clawMachineList:

        thisCost = calcMachine(item,0)        
        pt1Cost += thisCost

    for item in clawMachineList:

        thisCost = calcMachine(item,10000000000000)        
        pt2Cost += thisCost

    print(f'Part 1: {pt1Cost}')
    print(f'Part 2: {pt2Cost}')


def main():
    parseInput()
    doIt()
    return

main()
