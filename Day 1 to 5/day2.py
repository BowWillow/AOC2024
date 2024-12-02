'''
Day 2: Red-Nosed Reports

input is space seperated list of numbers like '75 76 77 80 82 85 84'

a report is safe if both of the following are true:
  - The levels are either all increasing or all decreasing.
  - Any two adjacent levels differ by at least one and at most three.

Part 1: how many safe reports are there Answer is 479 Test input answer is 2

Part 2 if removing a single level from an unsafe report would make it safe, 
the report instead counts as safe. 
Answer is 531 Test input answer is 4

personal stats
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  2   00:33:49  10294      0   11:05:14  51067      0
'''

inputFile = '../Data/Day 2 InputTEMP.txt'
inputFile = '../Data/Day 2 Input.txt'

tempList = list()

def parseInput():
    global tempList

    for line in open(inputFile, 'r') :
        lineList = line.strip('\n').split(' ')
        numList = []
        for itemStr in lineList:
            numList.append(int(itemStr))

        tempList.append(numList )

# safe test checks if safe conditions are met
def safeTest(numList):
    i = 0; safe = True
    # if list is decreasing we flip the sign to simplify the compares
    if numList[0] > numList[1]:
        numList = [-x for x in numList]
    while i < len(numList)-1:
        if numList[i] >= numList[i+1] or \
        numList[i]+4 <= numList[i+1]:
            safe = False
        i += 1
    return safe


def doIt():
    global tempList

    pt1Total = 0; pt2Total = 0
    # Part 1
    for numList in tempList:
        # if numList[0] == 45:
        #     print('GOTCHA')
        # if numList[0] > numList[1]:
        #     numList = [-x for x in numList]
        safe = safeTest(numList)          
        if safe:
            pt1Total += 1
    
    # Part 2
    # if pt1 ws safe, so will be pt2
    # if not safe retry dropping each element if any are safe treeat it as safe
        if safe:
            pt2Total += 1
            continue

        # for each shorter list
        for dropItem in range(len(numList)):
            # create new deep copy list to avoid corrupting numList
            tmpList = []; tmpList.extend(numList)
            del(tmpList[dropItem])
            safe = safeTest(tmpList)
        #   check; if safe -- incr pt2Total and break
            if safe:
                pt2Total += 1
                break                    


    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
