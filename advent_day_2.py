import numpy as np
FILENAME = "advent2"

def isSort(level):
    isSorted = 0
    if(np.array_equal(level, np.sort(level)) or np.array_equal(level, -np.sort(-level))):
        isSorted = 1
    return isSorted


def isGrad(level):
    isGradual = 1
    k = 0
    while k < (level.shape[0] - 1):
        value = np.abs(level[k] - level[k+1])
        if not ((value >=1) and (value <= 3)):
            isGradual = 0
        k += 1
    return isGradual

def tryDampener(level):
    for ele in np.arange(level.shape[0]):
        new_level = np.delete(level, [ele])
        if (isSort(new_level) and isGrad(new_level)):
            return 1
        else:
            continue
    return 0


def advent_day_2(f, dampener=0):
    count = 0
    for i, level in enumerate(f):

        level = np.array([int(ele) for ele in level.rstrip().split()])

        if (isSort(level)  and isGrad(level)):
            count+=1
        else:
            if (dampener == 1):
                count = count + tryDampener(level)
            else:
                pass
    return count



f = open(FILENAME)
count = advent_day_2(f, dampener=1)
f.close()


print(count)
