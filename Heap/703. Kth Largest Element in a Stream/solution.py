class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        # Initialize the heap
        heapq.heapify(self.minHeap)
        # While the length of the heap is greater than k, pop the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add value to the heap
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return the minimum value, which is the first value of min heap
        return self.minHeap[0]
