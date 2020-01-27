import random

sorted = []

unsorted = [random.randint(0,100) for i in range(10)]

minimum = unsorted[0]

while len(unsorted) > 0:
    minimum = unsorted[0]
    for number in unsorted:
        if number <= minimum:
            minimum = number
    unsorted.remove(minimum)
    sorted.append(minimum)


print(sorted)

#Complete
