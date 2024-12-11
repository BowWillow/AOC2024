'''
Day 11: 

input is line of stones with a number written on each.
Part 1: Each round, change each stone as follows:
  - If the stone has 0, replace with the number 1.
  - If the stone has even number of digits, replace with two stones. 
    The left half of the digits on the new left stone, and the right 
    half of the digits on the new right stone. (drop leading zeroes)
  - else replace with the old stone's number multiplied by 2024 
how many stones after 25 rounds
Answer is 186203 Test input answer is 55312

Part 2 same as part 1 but 75 times.  
Answer is 221291560078593 Test input answer is not given

Notes
did pt1 brute force but doesn't scale for pt2, so changed to dict.
AS other AOCer said "part 1 I used a list to represent the stones as is. 
  for part 2 i rewrote the solution using defaultdict[number on stone] = count. 
  this reduces the number of entries from rougly 10^15 to 4000."

personal stats
 11   00:31:33   7495      0   09:30:40  23260      0
'''
from collections import defaultdict

inputFile = '../Data/Day 11 Input.txt'
inputFile = '../Data/Day 11 InputTEMP.txt'
inputFile = '../Data/Day 11 Input.txt'


stoneDict = defaultdict(int)

def parseInput():
    global stoneDict

    fd = open(inputFile, 'r') 
    for numStr in fd.readline().strip('\n').split(' '):
        stoneDict[int(numStr)] += 1
    return

# newStoneNum returns one or two numbers for stones.
# In all cases we put them in a list.  Picked this technique up 
# from a Reddit post
def newStoneNums(stoneNum):
    if stoneNum == 0:
        return [1]
    else:
        stoneStr = str(stoneNum)
        if len(stoneStr)%2 == 0:
            return [int(stoneStr[0:len(stoneStr)//2]), \
            int(stoneStr[len(stoneStr)//2:])]
        else:
            return [stoneNum*2024]


def doIt():
    global stoneDict

    #pt1 & pt2
    for i in range(75):
        newDict = defaultdict(int)

        for (stoneNum,stoneQty) in stoneDict.items():
            # get new stone number(s) and add qty to newDict
            for item in newStoneNums(stoneNum):
                newDict[item] += stoneQty
        stoneDict = newDict
        if i == 24: # pt1 completed
            print(f'Part 1: {sum(stoneDict.values())}')
    
    print(f'Part 2: {sum(stoneDict.values())}')


def main():
    parseInput()
    doIt()
    return

main()
