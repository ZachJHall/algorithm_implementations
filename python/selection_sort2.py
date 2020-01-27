import random

unsorted = [random.randint(0,100) for i in range(10)]

n = 0

print("The unsorted list was", unsorted)

for i in range(len(unsorted)):
    minimum = unsorted[n]
    for number in unsorted[n:]:
        if number <= minimum:
            minimum = number

    newMinIndex = unsorted.index(minimum)
    unsorted[n], unsorted[newMinIndex] = unsorted[newMinIndex], unsorted[n]
    n +=1


print("The sorted list is", unsorted)


#Very similiar to selection_sort.py but does not use multiple lists
#Complete
