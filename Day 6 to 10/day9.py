'''
Day 9: Disk Fragmenter

input is long string of numbers which is  disk map
Part 1: compact the drive per write-up and calculate a check-sum
Answer is 6349606724455 Test input answer is 1928

Part 2 compact the drive using pt2 algoritm and cal check-sum.  
Answer is 6376648986651 Test input answer is 2858

Note:  Pt2 would be much more efficient if we kept an array of lists
of free space of each size (1 to 9 sectors).  Then files could be kept in 
a dict of filenum x location

'''

inputFile = '../Data/Day 9 InputTEMP.txt'
inputFile = '../Data/Day 9 Input.txt'


pt1DiskImageList = list()
pt2DiskImageList = list()
largestFileNum = 0

def parseInput():
    global pt1DiskImageList, pt2DiskImageList, largestFileNum

    fd = open(inputFile, 'r') 
    diskMapStr = fd.readline().strip('\n')

    fileFlag = True;     fileNum = 0
    for c in diskMapStr:
        if fileFlag:
            for i in range((int(c))):
                pt1DiskImageList.append(fileNum)
            fileFlag = False
            largestFileNum = fileNum
        else:
            for i in range((int(c))):
                pt1DiskImageList.append(-1)
            fileFlag = True
            fileNum += 1
    pt2DiskImageList.extend(pt1DiskImageList)
    

def findNextFree(index):
    global pt1DiskImageList

    tmp = index
    while pt1DiskImageList[tmp] != -1:
        tmp += 1
    return tmp


def findLastUsed(index):
    global pt1DiskImageList

    tmp=index
    while pt1DiskImageList[tmp] == -1:
        tmp -= 1
    return tmp


def doPt1():
    global pt1DiskImageList
    
    pt1Total = 0
    # pointers to first free slot and last used slot
    firstFreeSlot = findNextFree(0)
    lastUsedSlot = findLastUsed(len(pt1DiskImageList)-1)
    # finished when first >= last
    while firstFreeSlot <= lastUsedSlot:
    # move last into first
        pt1DiskImageList[firstFreeSlot] = pt1DiskImageList[lastUsedSlot]
        pt1DiskImageList[lastUsedSlot]  = -1
        firstFreeSlot = findNextFree(firstFreeSlot)
        lastUsedSlot  = findLastUsed(lastUsedSlot)
    # calc checksum
    i = 0
    # walk list pt1total += position*fileNum
    while pt1DiskImageList[i] != -1:
        pt1Total += pt1DiskImageList[i] * i
        i += 1
    return pt1Total


def findFile(fileNum, lastCheckedBlock):
    global pt2DiskImageList

    fileEnd=0; fileStart=0; fileCurrent = lastCheckedBlock

    while fileEnd == 0:
        # look for end of file:
        if pt2DiskImageList[fileCurrent] == fileNum:
            fileEnd = fileCurrent
        else:
            fileCurrent -= 1
    
    while fileStart == 0:
        # looking for start of file
        if pt2DiskImageList[fileCurrent] == fileNum:
            fileCurrent -= 1
        else:
            fileStart = fileCurrent+1

    return (fileStart,fileEnd-fileStart+1)


def findSpace(fileLen,endBlock,firstMinusOneBlock):
    global pt2DiskImageList

    doneFlag = False; inFreeSpaceFlag = False
    startBlock = firstMinusOneBlock

    while not doneFlag:
        if startBlock+fileLen > endBlock:
            return -1
        if not inFreeSpaceFlag:
            # find first -1
            if pt2DiskImageList[startBlock] == -1:
                inFreeSpaceFlag = True
            else:
                startBlock += 1
                if startBlock+fileLen > endBlock:
                    return -1
        else:
            # are there fileLen of them?
            if pt2DiskImageList[startBlock:startBlock+fileLen] == \
               [-1]*fileLen:
                doneFlag = True
            else:
                startBlock += 1
                inFreeSpaceFlag = False
    return startBlock


def doPt2():
    global pt2DiskImageList, largestFileNum

    firstMinusOneBlock = 0
    lastCheckedBlock = len(pt2DiskImageList)-1
    fileNum = largestFileNum
   
    # until done
    while fileNum > 0:
    # find last file (and size)
        (fileStart,fileLen) = findFile(fileNum,lastCheckedBlock)
        lastCheckedBlock = fileStart
    # find first open slot
        freeSpaceStart = findSpace(fileLen, lastCheckedBlock, \
                                   firstMinusOneBlock) 
    # is there space?
        if freeSpaceStart == -1:
            lastCheckedBlock = fileStart - 1
        else:
            # move file; free old file location
            for i in range(fileLen):
                pt2DiskImageList[freeSpaceStart+i] = fileNum
                pt2DiskImageList[fileStart+i] = -1
        fileNum -= 1
        while pt2DiskImageList[firstMinusOneBlock] != -1:
            firstMinusOneBlock += 1
    # calculate and return checksum
    pt2Total = 0
    # walk list pt2total += position*fileNum
    for i in range(len(pt2DiskImageList)):
        if pt2DiskImageList[i] != -1:
            pt2Total += pt2DiskImageList[i] * i
    return pt2Total


def doIt():
    print(f'Part 1: {doPt1()}')
    print(f'Part 2: {doPt2()}')
    return


def main():
    parseInput()
    doIt()
    return

main()
