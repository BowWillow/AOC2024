'''
Day 4: Ceres Search

input is letters in a grid
Part 1: How many times does XMAS appear? Answer is 2613 Test input answer is 18

Part 2 How many times does two MAS in the shape of an X appear?  
Answer is 1905 Test input answer is 9


personal stats
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  4   00:47:51   9012      0   01:15:50   9313      0

NOTE:
part 1 is very brute force.  A more clever approach would be to just check downward
and then rotate the grid 45 degrees and sum up the eight results.  One could 
probably use a dict to implement
'''

inputFile = '../Data/Day 4 Input.txt'
inputFile = '../Data/Day 4 InputTEMP.txt'
inputFile = '../Data/Day 4 Input.txt'

# a list of strings
L = list()

def parseInput():
    global L

    for line in open(inputFile, 'r') :
        L.append(line.strip('\n'))


def cntPt1(testWord):
    result = 1 if testWord == 'MAS' else 0
    return result

    
def cntPt2(word1,word2):
    if (word1 == 'MS' or word1 == 'SM') and \
       (word2== 'MS' or word2 == 'SM'):
        return 1
    else:
        return 0


def doIt():
    global L

    pt1XmasCnt = 0
    for row in range(len(L)):
        for col in range(len(L[row])):
    # search for 'X'
            if L[row][col] != 'X':
                continue
    # brute force chck all 8 directions
            # up
            if row >= 3:
                testWord = L[row-1][col] + L[row-2][col] + L[row-3][col]
                pt1XmasCnt += cntPt1(testWord)
            # down
            if row <= len(L)-4:
                testWord = L[row+1][col] + L[row+2][col] + L[row+3][col]
                pt1XmasCnt += cntPt1(testWord)
            # right
            if col <= len(L[row])-4:
                testWord = L[row][col+1] + L[row][col+2] + L[row][col+3]
                pt1XmasCnt += cntPt1(testWord)
            # left
            if col >= 3:
                testWord = L[row][col-1] + L[row][col-2] + L[row][col-3]
                pt1XmasCnt += cntPt1(testWord)
            # up-left
            if row >= 3 and col >= 3:
                testWord = L[row-1][col-1] + L[row-2][col-2] + L[row-3][col-3]
                pt1XmasCnt += cntPt1(testWord)
            # up-right
            if row >= 3 and (col <= len(L[row])-4):
                testWord = L[row-1][col+1] + L[row-2][col+2] + L[row-3][col+3]
                pt1XmasCnt += cntPt1(testWord)
            # down-left
            if (row <= len(L)-4) and col >= 3:
                testWord = L[row+1][col-1] + L[row+2][col-2] + L[row+3][col-3]
                pt1XmasCnt += cntPt1(testWord)
            # down-right
            if (row <= len(L)-4) and (col <= len(L[row])-4):
                testWord = L[row+1][col+1] + L[row+2][col+2] + L[row+3][col+3]
                pt1XmasCnt += cntPt1(testWord)

    # part 2
    # look for 'A'; if found check the cross items for MAS 
    pt2XmasCnt = 0
    for row in range(1,len(L)-1):
        for col in range(1,len(L[row])-1):
    # search for 'A'
            if L[row][col] == 'A':
                #diag - see if both are 'MS' or 'SM'
                word1 = L[row-1][col-1] + L[row+1][col+1]
                word2 = L[row-1][col+1] + L[row+1][col-1]
                pt2XmasCnt += cntPt2(word1,word2)

    print(f'Part 1: {pt1XmasCnt}')
    print(f'Part 2: {pt2XmasCnt}')


def main():
    parseInput()
    doIt()
    return

main()
