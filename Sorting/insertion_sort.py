# Insertion Sort

# Takes n^2/4 comparisions and n^2/8 swaps in average case and double amount in worst case

# Time complexity : O(n+d) where d is number of insertions
# worst case : O(n^2)

# Insert sort can sort the list online
# used when data is nearly sorted, small datasets and divide and conquer sorting algorithms like merge and quick sort 


def insertion_sort(A):
    for i in range(1, len(A)):
        v = A[i]
        j = i
        while(A[j-1]>v and j >= 1):
            A[j] = A[j-1]
            j -= 1
        A[j] = v


if __name__ == "__main__":
    A = [5,3,17,10,84,19,6,22,9]
    insertion_sort(A)
    print(A)