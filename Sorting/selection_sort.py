# Selection Sort
# works well for small files, elements with bigger values and smaller keys 

# Takes n^2/2 comparisions and n swaps.

# Time complexity O(n^2)

def selection_sort(A):
    for i in range(len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]

if __name__ == "__main__":
    A = [5,3,17,10,84,19,6,22,9]
    selection_sort(A)
    print(A)
