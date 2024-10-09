def createListOfSequentialInts(loop: int):
    list = []
    for i in range(1, loop+1):
        list.append(i)
    return list

awfulList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
niceList = createListOfSequentialInts(39)

print(awfulList)
print(niceList)
print(niceList == awfulList)