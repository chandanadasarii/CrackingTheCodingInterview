# Shell Sort

# Time complexity worst case : O(n(log^2)n), best case : O(n)
# Efficient for Medium size list

def shell_sort(A):
    n = len(A)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            v = A[i]
            j=i
            while(A[j-gap] > v and j >= gap):
                A[j] = A[j-gap]
                j -= gap
            A[j] = v
        gap //= 2


if __name__ == "__main__":
    A = [5,3,17,10,84,19,6,22,9]
    shell_sort(A)
    print(A)