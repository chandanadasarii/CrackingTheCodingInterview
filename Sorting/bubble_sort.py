# Bubble sort
# not a good sorting algorithm

# Takes n^2/2 comparisions and n^2/2 swaps in both average and worst case

# Time complexity : O(n^2)

def bubble_sort(A):
    for itr in range(len(A)-1, -1, -1):
        for i in range(itr):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]


# Best case time complexity : O(n)
def bubble_sort_improved(A):
    swapped = True
    for itr in range(len(A)-1, -1, -1):
        if not swapped:
            break
        swapped = False
        for i in range(itr):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True


if __name__ == "__main__":
    A1 = [5,3,17,10,84,19,6,22,9]
    A2 = [5,3,17,10,84,19,6,22,9]    
    bubble_sort(A1)
    bubble_sort_improved(A2)
    print(A1)
    print(A2)