'''
Day 8: Resonant Collinearity

input is a grid with lines like
.......0....
an antinode occurs at any point that is in line with two antennas of the same frequency. 
when one of the antennas is twice as far away as the other.  This means, for any pair of antennas 
with the same frequency, there are two antinodes, one on either side of them.

Part 1: 
Antinodes exist only when one of the antennas is twice as far away as the other.  
This means, for any pair of antennas 
with the same frequency, there are two antinodes, one on either side of them.
How many unique locations within the bounds of the map contain an antinode?
 Answer is 336 Test input answer is 14

Part 2 
it turns out that an antinode occurs at any grid position exactly in line with at 
least two antennas of the same frequency, regardless of distance. 
This means that some of the new antinodes will occur at the position of each antenna 
(unless that antenna is the only one of its frequency).

Answer is 1131 Test input answer is 34

'''
from collections import defaultdict

inputFile = '../Data/Day 8 Input.txt'
inputFile = '../Data/Day 8 InputTEMP.txt'
inputFile = '../Data/Day 8 Input.txt'

antennaDict = defaultdict(list)
maxRow=-1; maxCol = -1

def parseInput():
    global antennaDict, maxRow, maxCol

    row = 0
    for line in open(inputFile, 'r') :
        line = line.strip('\n')
        for col in range(len(line)):
            # put all antennas in dict 
            if line[col] != '.':
                antennaDict[line[col]].append((row,col))
        row += 1
    maxRow = row; maxCol = len(line)



# inBounds checks that a node is on the grid
def inBounds (row, col):
    global maxRow, maxCol

    return (row >= 0 and row < maxRow and \
        col >= 0 and col < maxCol)
     

def doIt():
    global antennaDict, maxRow, maxCol

    pt1AntinodeSet = set(); pt2AntinodeSet =  set()
    # for each antenna symbol
    for locList in antennaDict.values():
    #  for each pair
        for first in range(len(locList)-1):
            for second in range(first+1,len(locList)):
    #    find vector between them
                firstRow, firstCol = locList[first]
                secondRow, secondCol = locList[second]
                deltaRow = firstRow - secondRow; deltaCol = firstCol - secondCol
    #    pt1 - find two antinodes - omit if out of bounds - place in set
                node1Row = firstRow + deltaRow;  node1Col = firstCol + deltaCol
                node2Row = secondRow - deltaRow; node2Col = secondCol - deltaCol
                if inBounds(node1Row, node1Col):
                    pt1AntinodeSet.add((node1Row,node1Col))
                if inBounds(node2Row, node2Col):
                    pt1AntinodeSet.add((node2Row,node2Col))
    #     pt2 - add the two nodes to pt2 set and
    #        add antinodes in each direction until you run off of the grid
                tmpRow = firstRow; tmpCol = firstCol
                while inBounds(tmpRow, tmpCol):
                    pt2AntinodeSet.add((tmpRow,tmpCol))
                    tmpRow += deltaRow; tmpCol += deltaCol
                tmpRow = secondRow; tmpCol = secondCol
                while inBounds(tmpRow, tmpCol):
                    pt2AntinodeSet.add((tmpRow,tmpCol))
                    tmpRow -= deltaRow; tmpCol -= deltaCol

    # pt1 answer  is size of pt1set
    print(f'Part 1: {len(pt1AntinodeSet)}')
    # pt2 answer  is size of pt2set    
    print(f'Part 2: {len(pt2AntinodeSet)}')


def main():
    parseInput()
    doIt()
    return

main()
