# Quick Sort

# Divide and Conqure

# Time complexity: O(nlogn), worst case: O(n^2)

def partation(A, start, end):
    pivot = A[end]
    i = start-1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[end] = A[end], A[i]
    return i

def quick_sort(A, start=0, end=None):
    if end is None:
        end = len(A)-1

    if start < end:
        pi = partation(A, start, end)
        quick_sort(A, start, pi-1)
        quick_sort(A, pi+1, end)


if __name__ == "__main__":
    A = [5,3,17,10,84,19,6,22,9]
    quick_sort(A)
    print(A)