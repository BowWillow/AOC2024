'''
Day 5: 

input is <>
Part 1: <> Answer is 6505 Test input answer is 143

Part 2 <>.  Answer is 6897 Test input answer is 123


personal stats
<>
'''
from collections import defaultdict
import copy


inputFile = '../Data/Day 5 Input.txt'
inputFile = '../Data/Day 5 InputTEMP.txt'
inputFile = '../Data/Day 5 Input.txt'

orderDict = defaultdict(list)

pageList = list()

def parseInput():
    global pageList, orderDict

    for line in open(inputFile, 'r') :
        if line.find('|') != -1:
            orderDict[line[0:2]].append(line[3:5]) 
        elif line.find(',') != -1:
            pageList.append([])
            i = 0
            while i < len(line):
                pageList[len(pageList)-1].append(line[i:i+2])
                i += 3

def searchToTheRight(printList):
    #     for each item in print list
    for i in range(len(printList)):
        thisUpdatePage = printList[i]
    #     account for all pages to the right
        for j in range(i+1,len(printList)):
            if not printList[j] in orderDict[thisUpdatePage]:
                return i,j
    return -1,-1

def pt2process(updateList):
    global orderDict

    # deep copy updateList
    workingList = copy.deepcopy(updateList)
    while True:
        # search for out of order
        failureI,failureJ = searchToTheRight(workingList)
        if failureI == -1:
            return int(workingList[len(workingList)//2])
        # move current page to the right
        else: # failure index points to the bad page
        # place bad page in front of i
            newList = []
            newList.extend(workingList[0:failureI]) # copy front of kist
            newList.append(workingList[failureJ])   # append [j]
            workingList.pop(failureJ)               # and delete it
            newList.append(workingList[failureI])   # append [i]
            newList.extend(workingList[failureI+1:]) # copy rest of list
            workingList = copy.deepcopy(newList)



def doIt():
    global pageList, orderDict

    # for each pagelist
    pt1Total = 0; pt2Total = 0
    for updateList in pageList:
    # pt1 check
        inOrderFlag = True if searchToTheRight(updateList) == (-1,-1) else False

        if inOrderFlag:
            pt1Total += int(updateList[len(updateList)//2])
        else:
    # process pt 2
            pt2Total += pt2process(updateList)




    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
