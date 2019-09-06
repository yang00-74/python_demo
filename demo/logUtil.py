# coding=utf-8
import re
import time


def logFilter():
    frt = open('log.txt')
    sample = frt.readlines()
    frs = open('log1.txt')
    test = frs.readlines()
    processQuence = set()
    timeQuence = []
    filterResult = []
    for tLine in test:
        tLinelist = tLine.strip().split(' ')
        for sLine in sample:
            sLinelist = sLine.strip().split(' ')
            if re.match(sLinelist[0], tLinelist[2]) and re.match(sLinelist[1], tLinelist[3]):
                tLinelist.append(sLinelist[-1])
                processQuence.add(sLinelist[-1])
                timeQuence.append(sLinelist[-1])
                filterResult.append(tLinelist)
    print("end:")
    processQuence = sorted(processQuence)
    print(processQuence)
    print(timeQuence)
    # for line in filterResult:
    #     print(line)
    index = []
    index0 = timeQuence.index(processQuence[0])
    index.append('0')
    time = timeQuence[index0:].copy()
    print(time)
    for i in processQuence[1:]:
       index.append(time.index(i))
    print(index)
    for i in range(len(index)-1):
        if int(index[i+1])-int(index[i]) != 1:
            print(False)



if __name__ == '__main__':
    logFilter()
