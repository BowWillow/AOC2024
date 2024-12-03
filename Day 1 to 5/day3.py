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

NOTES
TODO A better solution is to use regex

'''

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
        tmpStr = line.strip('\n')
        inputStr += tmpStr

def findNum(scanStr,i,delim):
 
    tempNum = 0
    if scanStr[i].isdigit():
        tempNum = int(scanStr[i])
    else:
        return (i,-1)
    i += 1
    if scanStr[i].isdigit():
        tempNum = tempNum*10 + int(scanStr[i]) 
    elif scanStr[i] == delim:
        return (i+1,tempNum)
    else:
        return (i,-1)
    i += 1
    if scanStr[i].isdigit():
        tempNum = tempNum*10 + int(scanStr[i]) 
    elif scanStr[i] == delim:
        return (i+1,tempNum)
    else:
        return (i,-1)
    i += 1
    if scanStr[i] == delim:
        return (i+1,tempNum)
    return (i,-1)
    
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


def doIt():
    global inputStr, pt2InputStr


    # pt1 scan for valid instruction
    # multiply and accumulate
    pt1Total = 0; pt2Total = 0
    operand1 = 0; operand2 = 0

    # process pt1
    i=0; 
    while (1):
        j = inputStr.find('mul(',i)
        if j == -1:
            #done
            break
        else:
            i = j+4
        # find number
        i,operand1 = findNum(inputStr,i,',')
        if operand1 == -1:
            continue
        i,operand2 = findNum(inputStr,i,')')
        if operand2 == -1:
            continue
        pt1Total += operand1 * operand2

    # build pt2 list -- take orig list and delete stuff
    # between don't() and do()
    createPt2Data()

    # process pt2
    # TODO SHOULD COMBINE PT1 and PT2 PROCESSING INTO A FUNCTION
    i=0; 
    while (1):
        j = pt2InputStr.find('mul(',i)
        if j == -1:
            #done
            break
        else:
            i = j+4
        # find number
        i,operand1 = findNum(pt2InputStr,i,',')
        if operand1 == -1:
            continue
        i,operand2 = findNum(pt2InputStr,i,')')
        if operand2 == -1:
            continue
        pt2Total += operand1 * operand2
    

    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
