array = [1, 3, 2, 6, 8, 4]

# Not Complete

def mergSort(array):
    if len(array) > 1:
        leftSide = array[:len(array)//2]
        rightSide = array[len(array)//2]

    print(leftSide)
    print(rightSide)

    mergSort(leftSide)
    mergSort(rightSide)

mergSort(array)
