'''
Day 1: Historian Hysteria

input is lines with two numbers (left and right) like '87501   76559'
Part 1: 
Pair up the smallest number in left list with smallest number in right list, 
then the second-smallest, and so on.

Within each pair, figure out how far apart the two numbers are.
To find the total distance between the left list and the right list, 
add up the distances between all of the pairs you found.

Answer is 936063 


Part 2 
This time, you'll need to figure out exactly how often each number from left list 
appears in right list. Calculate a total similarity score by adding up each number 
in the left list after multiplying it by the number of times that number appears in 
the right list.

Answer is 23150395

'''
from collections import defaultdict

inputFile = '../Data/Day 1 InputTEMP.txt' 
inputFile = '../Data/Day 1 Input.txt'

leftList = list(); rightList = list()

def parseInput():
    global leftList, rightList 

    for line in open(inputFile, 'r') :
        lineList = line.strip('\n').split(' ')
        # save first and last element
        leftList.append(int(lineList[0]) )
        rightList.append(int(lineList[-1]) )

def doIt():
    global leftList, rightList 

    # sum abs of each item pair
    leftList.sort(); rightList.sort()
    pt1Total = 0
    for left,right in zip(leftList, rightList):
        pt1Total += abs(left-right)

    # put right list into dict (value is # of times in list)
    # for each left list item tot+=rightDict[item]*item
    rightDict = defaultdict(lambda:0)
    for right in rightList:
        rightDict[right]+=1
    pt2Total = 0
    for left in leftList:
        pt2Total += left*rightDict[left]

    print(f'Part 1: {pt1Total}')
    print(f'Part 2: {pt2Total}')


def main():
    parseInput()
    doIt()
    return

main()
