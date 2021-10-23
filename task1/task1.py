from sys import argv


script_name, n, m = argv
n = int(n)
m = int(m)
roundList = list(map(lambda j: j + 1, [x for x in range(n)]))

length = n
route = []
routeMap = []
startIter = 0
while True:
    length += m
    q, r = divmod(length, len(roundList))
    roundL = roundList * 2 * q + roundList[:r]
    route.append(roundL[startIter])
    routeMap.append(roundL[startIter:startIter + m])
    startIter += (m - 1)
    if roundL[startIter + (m-1)] == roundList[0]:
        routeMap.append(roundL[startIter:startIter + m])
        route.append(roundL[startIter])
        break
resultStr = ''
for point in route:
    resultStr += str(point)
print(resultStr)
