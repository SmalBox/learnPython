def findMinMax(L):
    if L == []:
        return (None, None)
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)
