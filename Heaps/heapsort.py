from Heap import Heap

# Time complexity : O(nlogn)
def heapsort(data):
    heap = Heap('maxheap')
    heap.build_heap(data)

    for i in range(len(data)-1, 0, -1):
        heap.data[i], heap.data[0] = heap.data[0], heap.data[i]
        heap.n -= 1
        heap.precolate_down(0)

    return heap.data

print(heapsort([5,3,17,10,84,19,6,22,9]))