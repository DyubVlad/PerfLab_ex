from sys import argv


script_name, fArray = argv
with open(fArray, 'r') as f:
    inputList = f.read().split('\n')
inputList = [int(x) for x in inputList]


def get_median(sample):
    n = len(sample)
    index = n // 2
    if n % 2:
        return sorted(sample)[index]
    return sum(sorted(sample)[index - 1:index + 1]) / 2


listMedian = round(get_median(inputList))
iterCounter = 0

for index, item in enumerate(inputList):
    while inputList[index] != listMedian:
        if item > listMedian:
            inputList[index] -= 1
            iterCounter += 1
        elif item < listMedian:
            inputList[index] += 1
            iterCounter += 1
        elif item == listMedian:
            continue

print(iterCounter)
