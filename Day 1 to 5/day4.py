'''
Day 4: Ceres Search

input is <>
Part 1: <> Answer is 2613 Test input answer is 18

Part 2 <>.  Answer is 1905 Test input answer is 9


personal stats
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  4   00:47:51   9012      0   01:15:50   9313      0
'''

inputFile = '../Data/Day 4 Input.txt'
inputFile = '../Data/Day 4 InputTEMP.txt'
inputFile = '../Data/Day 4 Input.txt'

L = list()

def parseInput():
    global L

    for line in open(inputFile, 'r') :
    #    L = line.strip('\n').split(' ')
        L.append(line.strip('\n'))

def cnt(testWord):
    if testWord == 'MAS':
        return 1
    else:
        return 0
    
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
            # up
            if row >= 3:
                testWord = L[row-1][col] + L[row-2][col] + L[row-3][col]
                pt1XmasCnt += cnt(testWord)
            # down
            if row <= len(L)-4:
                testWord = L[row+1][col] + L[row+2][col] + L[row+3][col]
                pt1XmasCnt += cnt(testWord)
            # right
            if col <= len(L[row])-4:
                testWord = L[row][col+1] + L[row][col+2] + L[row][col+3]
                pt1XmasCnt += cnt(testWord)
            # left
            if col >= 3:
                testWord = L[row][col-1] + L[row][col-2] + L[row][col-3]
                pt1XmasCnt += cnt(testWord)
            # up-left
            if row >= 3 and col >= 3:
                testWord = L[row-1][col-1] + L[row-2][col-2] + L[row-3][col-3]
                # if testWord == 'MAS':
                #     print(f'{row=}  {col=}')
                pt1XmasCnt += cnt(testWord)
            # up-right
            if row >= 3 and (col <= len(L[row])-4):
                testWord = L[row-1][col+1] + L[row-2][col+2] + L[row-3][col+3]
                pt1XmasCnt += cnt(testWord)
            # down-left
            if (row <= len(L)-4) and col >= 3:
                testWord = L[row+1][col-1] + L[row+2][col-2] + L[row+3][col-3]
                pt1XmasCnt += cnt(testWord)
            # down-right
            if (row <= len(L)-4) and (col <= len(L[row])-4):
                testWord = L[row+1][col+1] + L[row+2][col+2] + L[row+3][col+3]
                pt1XmasCnt += cnt(testWord)

    # part 2
    # look for 'A' check 4 MAS if any are found check the two cross items
    # e.g. if vert then check horiz
    #      if diag then check other diag
    pt2XmasCnt = 0
    for row in range(1,len(L)-1):
        for col in range(1,len(L[row])-1):
    # search for 'A'
            if L[row][col] != 'A':
                continue
            #vert
            # word1 = L[row-1][col] + L[row+1][col]
            # word2 = L[row][col-1] + L[row][col+1]
            # pt2XmasCnt += cntPt2(word1,word2)
            #diag
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
