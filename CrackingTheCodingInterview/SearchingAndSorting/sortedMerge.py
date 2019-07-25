def sortedMerge(arr1, arr2):

    i = len(arr1)-1
    j = len(arr2)-1

    while i >= 0:
        if j >= 0:
            if arr1[i] < arr2[j]:
                