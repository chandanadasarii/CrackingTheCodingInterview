import math

class Heap():

    def __init__(self, heap_type):
        self.heap_type = heap_type
        self.data = list()
        self.n = len(self.data)

    # Time complexity : O(1)
    def find_parent(self, i):
        if (i <= 0 or i >= self.n):
            return -1
        return int((i-1)/2)


    # Time complexity : O(1)
    def left_child_index(self, i):
        left = i*2 + 1
        if left >= self.n:
            return -1
        return left


    # Time complexity : O(1)
    def right_child_index(self, i):
        right = i*2 + 2
        if right >= self.n:
            return -1
        return right


    # Time complexity : O(1)
    def get_max_element(self):
        if self.n == 0:
            return -1
        return self.data[self.n-1]


    # Time complexity O(logn)
    def percolate_down(self, i):
        l = self.left_child_index(i)
        r = self.right_child_index(i)

        if l != -1 and self.data[l] > self.data[i]:
            maxi = l
        else:
            maxi = i

        if r != -1 and self.data[r] > self.data[maxi]:
            maxi = r

        if maxi != i:
            self.data[i], self.data[maxi] = self.data[maxi], self.data[i]
            self.percolate_down(maxi)


    # Time complexity O(logn)
    def delete_max(self):
        if self.n == 0:
            return -1
        maxelm = self.data[0]
        self.data[0] = self.data[self.n-1]
        del self.data[self.n-1]
        self.n = len(self.data)
        self.percolate_down(0)
        return maxelm


    # Time complexity O(logn)
    def insert_heap(self, elm):
        self.data.append(elm)
        self.n = len(self.data)
        i = self.n - 1
        p = self.find_parent(i)
        while(i >= 0 and self.data[i] > self.data[p]):
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p
            p = self.find_parent(i)


    # Time complexity O(nlogn)
    def build_heap(self, data):
        self.data = data
        self.n = len(data)
        for i in range(int(self.n/2), -1, -1):
            self.percolate_down(i)


    def heap_height(self):
        return math.ceil(math.log2(self.n+1))-1


    def print_heap(self):
        n=1
        print(self.data[0:1])
        for i in range(1, self.heap_height()+1):
            print(self.data[n:n+i*2])
            n = n+i*2


# heap = Heap('maxheap')
# heap.data = [17, 13, 6, 1, 4, 2, 5]
# print(heap.data)
# heap.insert_heap(10)
# print(heap.data)
# heap.delete_max()
# print(heap.data)
# heap.build_heap([1, 2, 4, 5, 6, 13, 17])
# heap.print_heap()