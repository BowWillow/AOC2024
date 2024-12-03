'''
Day 3:  Mull It Over

input is series of strings containing
mul(X,Y), don't(), do() and garbage

Part 1: multiply some numbers; like mul(X,Y), 
where X and Y are each 1-3 digit numbers.
Find the sum of the results of the multiplications.
Answer is 173517243 Test input answer is 161

Part 2 Same as part 1 except ignore all data betweeen 
don't() and the next do(). 
Answer is 100450138 Test input answer is 48

personal stats
3   01:05:07  16005      0   09:48:38  53724      0

'''
import re

inputFile = '../Data/Day 3 Input.txt'
inputFile = '../Data/Day 3 InputTEMP.txt'
inputFile = '../Data/Day 3 Input.txt'

inputStr = str()
pt2InputStr = str()

def parseInput():
    global inputStr

    inputstr= ''
    # input contains multiple lines! (with NLs)
    for line in open(inputFile, 'r') :
        inputStr += line.strip('\n')
    

# createPt2Data goes through the input removing data between
# don't() and do()
def createPt2Data():
    global inputStr, pt2InputStr

    startDataIndex=0
    while startDataIndex < len(inputStr):
        # find don't() and move substring
        startDontIndex = inputStr.find("don't()",startDataIndex)
        # handle end of data
        if startDontIndex == -1:
            startDontIndex = len(inputStr)
        else:
            startDontIndex += 7
        pt2InputStr += inputStr[startDataIndex:startDontIndex]
        # find do()
        startDataIndex = inputStr.find("do()",startDontIndex)
        # handle end of data
        if startDataIndex == -1:
            break
        else:
            startDataIndex += 4
    return

# mul returns the product of its operands (used with eval)
def mul(a,b):
    return a*b

def doIt():
    global inputStr, pt2InputStr

    pt1Total = 0; pt2Total = 0
    matchPattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"

    # process pt1

    # use regex to extract mul strings
    mulList = re.findall(matchPattern, inputStr)

    # sum up the product of the ops in mulList
    for item in mulList:
        pt1Total += eval( item )

    # build pt2 list -- take orig list and delete stuff
    # between don't() and do()
    createPt2Data()

    # process pt2

    # use regex to extract mul strings
    mulList = re.findall(matchPattern, pt2InputStr)

    # sum up the product of the ops in mulList
    for item in mulList:
        pt2Total += eval( item )


    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
