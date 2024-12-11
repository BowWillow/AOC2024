'''
Day 5: 

input is lines like:
47|53
75,47,61,53,29
The first section specifies the page ordering rules
second section specifies page numbers

Part 1: Determine which updates are in the correct order. 
Sum up the middle page number from the correctly-ordered updates. 
Answer is 6505 Test input answer is 143

Part 2 For each of the incorrectly-ordered updates, use the page 
ordering rules to put the page numbers in the right order.
Sum up the middle page numbers after correctly ordering those updates.
Answer is 6897 Test input answer is 123

NOTE:
Could have used python's sort and  compare function; the code would 
have been a bit more concise but probably lower performance.

personal stats
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  5   01:05:30  11451      0   02:25:19  13406      0
'''
from collections import defaultdict
import copy

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
            pageList.append([]) #add list of page numbers
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
            # if out of order
            if not printList[j] in orderDict[thisUpdatePage]:
                return i,j
    return -1,-1  # must be in order

def pt2process(updateList):
    global orderDict

    # deep copy updateList
    workingList = copy.deepcopy(updateList)
    while True:
        # search for out of order
        failureI,failureJ = searchToTheRight(workingList)
        if failureI == -1: # no failure found
            return int(workingList[len(workingList)//2])
        # move current page to the right
        else: # failure index points to the bad pages
        # place bad page in front of i
            newList = []
            newList.extend(workingList[0:failureI]) # copy front of list
            newList.append(workingList[failureJ])   # append [j]
            workingList.pop(failureJ)               # and delete it
            newList.append(workingList[failureI])   # append [i]
            newList.extend(workingList[failureI+1:]) # copy rest of list
            workingList = copy.deepcopy(newList)


def doIt():
    global pageList, orderDict

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
