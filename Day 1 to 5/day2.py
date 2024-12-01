'''
Day 2: 

input is <>
Part 1: <> Answer is <> Test input answer is <>

Part 2 <>.  Answer is <> Test input answer is <>

personal stats
<>
'''

inputFile = '../Data/Day 1 Input.txt'
inputFile = '../Data/Day 1 InputTEMP.txt'

tempList = list()

def parseInput():
    global tempList

    for line in open(inputFile, 'r') :
        lineList = line.strip('\n').split(' ')
        tempList.append(lineList )

def doIt():


    print(f'Part 1: {42}')
    print(f'Part 2: {42}')


def main():
    parseInput()
    doIt()
    return

main()
