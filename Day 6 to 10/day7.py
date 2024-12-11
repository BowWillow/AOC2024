'''
Day 7: Bridge Repair

input is lines like 7290: 6 8 6 15
Part 1: Each line is an equation. The test value appears before the colon; 
determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are evaluated left-to-right. Numbers cannot be rearranged.
There are two operators: add (+) and multiply (*).

Determine which equations could possibly be true. What is the sum of the test value result?

Answer is 538191549061 Test input answer is 3749

Part 2 same as pt1 with added operator 'cat' which concatenates the two operators (base 10).  
Answer is 34612812972206 Test input answer is 11387

personal stats
 7   01:20:33   9554      0       >24h  65308      0
'''
import copy

inputFile = '../Data/Day 7 Input.txt'
inputFile = '../Data/Day 7 InputTEMP.txt'
inputFile = '../Data/Day 7 Input.txt'

equationList = list()

def parseInput():
    global equationList

    for line in open(inputFile, 'r') :
        lineList = line.strip('\n').split(' ')
        itemList = list()
        # first item (the test value) ends in a colon which we do not want
        itemList.append(int(lineList[0][0:-1]))
        for numStr in lineList[1:]:
            itemList.append(int(numStr))
        equationList.append(itemList)


def testEquationPt1(equation,numOperands,opIndex):
    # convert opindex to bit pattern
    binOpIndex = f'{opIndex:050b}'
    bitPattern = binOpIndex[-(numOperands):]
    partial = equation[1]
    for i in range (0,numOperands):
        if bitPattern[i] == '0': # add
            partial += equation[i+2]
        else: # mult
            partial *= equation[i+2]

    return partial == equation[0]


def convertToTrinary(num,length):
    # reverse a string "Hello World" [::-1]
    outStr = ''
    for i in range(length):
        # build string in reverse order
        outStr += str(num%3)
        num //= 3
    # reverse the string to the correct order
    outStr = outStr[::-1]
    return outStr

def testEquationPt2(equation,numOperands,opIndex):
    # convert opindex to base 3 string
    tripOpIndex = convertToTrinary(opIndex,numOperands)
    tripPattern = tripOpIndex
    if tripPattern.find('2') == -1: # if no cat
        return False

    partial = equation[1]
    # process each operand
    for i in range (0,numOperands):
        if tripPattern[i] == '0': # add
            partial += equation[i+2]
        elif tripPattern[i] == '1': # mult
            partial *= equation[i+2]
        else: # concatenate
            partial = int(str(partial)+str(equation[i+2]))

    return partial == equation[0]


def doIt():
    global equationList

    pt1Total = 0; pt2Total = 0
    # for each equation
    for equation in equationList:
        # do pt 1
        # generate each combination of operands (base 2)
        # num of operands = len - 2
        numOperands = len(equation) - 2
        for i in range(2**numOperands):
        # test
            resultFlag = testEquationPt1(equation,numOperands,i)
        # if success, sum into total (both pts are good)
            if resultFlag:
                pt1Total += equation[0]
                pt2Total += equation[0]
                break
        # do pt2
        # generate each combination of operands (base 3)
        # num of operands = len - 2  
        # if found in pt1 skip
        if not resultFlag:
            numOperands = len(equation) - 2
            for i in range(3**numOperands):
            # test      
                resultFlag = testEquationPt2(equation,numOperands,i)
            # if success, sum into pt2 total 
                if resultFlag:
                    pt2Total += equation[0]
                    break



    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
