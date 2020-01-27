import random

unsorted = [random.randint(0,100) for i in range(10)]

l = len(unsorted)


#Go through all numbers
for i in range(l):
    #Ensures that it does not retest the last index
    for j in range(l - i - 1):
        #Tests the numbers against each other
        if unsorted[j] > unsorted[j + 1]:
            unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

print(unsorted)

#Not complete
