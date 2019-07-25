# Merge Sort

# Divide and Conqure
# Divides the list into two parts 

# Time complexity: O(nlogn)

# USed for sorting a linked list

def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    A = [5,3,17,10,84,19,6,22,9]
    merge_sort(A)
    print(A)