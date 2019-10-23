unsorted = [13, 1, 50, 3, 2, 7]


iterationNumber = 0

isSorted = False

while isSorted == False:

    if iterationNumber >= (len(unsorted) - 1):
        break
    if unsorted[iterationNumber] > unsorted[iterationNumber + 1]:
        isSorted = False
        unsorted[iterationNumber], unsorted[iterationNumber + 1 ] = unsorted[iterationNumber + 1], unsorted[iterationNumber]

    iterationNumber += 1

print(unsorted)

#Currently the list does not sort lists completely, need to change the
#statement break and set it to a True or False condition
