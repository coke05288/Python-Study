def find_MAX_MIN(list1):
    max = list1[0]
    min = list1[0]
    for i in range(0, len(list1)):
        if max < list1[i]:
            max = list1[i]
        if min > list1[i]:
            min = list1[i]

    return max, min # return tuple
