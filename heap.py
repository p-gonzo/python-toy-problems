from math import floor, inf
from random import randrange
import time

class Heap:
    def __init__(self):
        self._heap = []
    
    def _compare(self, i, j):
        return i < j
    
    def getRoot(self):
        return self._heap[0]
    
    def insert(self, value):
        self._heap.append(value)

        def recursivelySwap(self, childIndex):
            if childIndex == 0:
                return
            
            parentIndex = floor((childIndex - 1) / 2)
            childValue = self._heap[childIndex]
            parentValue = self._heap[parentIndex]
            
            if self._compare(childValue, parentValue):
                self._heap[parentIndex] = childValue
                self._heap[childIndex] = parentValue
                recursivelySwap(self, parentIndex)

        recursivelySwap(self, len(self._heap) - 1)

    def removeRoot(self):
        # Swap last item with root
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        # Remove last item
        root = self._heap.pop()

        def recursivelySwap(self, parentIndex):
            
            if parentIndex >= len(self._heap):
                return
            
            parentValue = self._heap[parentIndex]
            child1Index = parentIndex * 2 + 1
            child2Index = parentIndex * 2 + 2

            child1Value = None if child1Index >= len(self._heap) else self._heap[child1Index]
            child2Value = None if child2Index >= len(self._heap) else self._heap[child2Index]
                
            if child1Value == None:
                return
            elif child2Value == None:
                smallestChildIndex = child1Index
            else:
                smallestChildIndex = child1Index if child1Value < child2Value else child2Index

            smallestChildValue = self._heap[smallestChildIndex]

            if self._compare(smallestChildValue, parentValue):
                self._heap[parentIndex] = smallestChildValue
                self._heap[smallestChildIndex] = parentValue
                recursivelySwap(self, smallestChildIndex)
        
        recursivelySwap(self, 0)
        return root


def heapSort(a_list):
    heap = Heap()
    result = []
    for item in a_list:
        heap.insert(item)
    while heap._heap:
        result.append(heap.removeRoot())
    return result

rand_list = [randrange(1, 10000) for x in range(10000)]

def bubble_sort(alist):
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0
        for i in range(len(alist) - 1):
            a = alist[i]
            b = alist[i + 1]
            if a > b:
                alist[i] = b
                alist[i + 1] = a
                num_swaps += 1
        if num_swaps == 0:
            is_sorted = True
    return alist
    
start0 = time.time()
sorted0 = bubble_sort(rand_list)
end0 = time.time()
print(end0 - start0)

start1 = time.time()
sorted1 = heapSort(rand_list)
end1 = time.time()
print(end1 - start1)

start2 = time.time()
sorted2 = rand_list.sort()
end2 = time.time()
print(end2 - start2)