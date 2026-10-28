"""
Title: Kth Largest Element in a Stream (LeetCode 703)
Difficulty: Easy

Problem Statement:
Design a class to find the kth largest element in a stream. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the
  stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element
  representing the kth largest element in the stream.

Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.
- It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

import heapq
from typing import List


class KthLargest:
    """
    Maintains a Min-Heap of size k.
    
    The min-heap holds the k largest numbers seen so far.
    The root (min_heap[0]) is always the smallest among these k elements,
    which corresponds exactly to the kth largest element overall.
    
    Complexity:
    - Init: O(n log k), where n is len(nums).
    - add(val): O(log k) to insert and maintain size k.
    - Space: O(k) auxiliary storage for the heap.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap: List[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]


if __name__ == "__main__":
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    print(f"add(3): Got {kth_largest.add(3)}, Expected 4")
    print(f"add(5): Got {kth_largest.add(5)}, Expected 5")
    print(f"add(10): Got {kth_largest.add(10)}, Expected 5")
    print(f"add(9): Got {kth_largest.add(9)}, Expected 8")
    print(f"add(4): Got {kth_largest.add(4)}, Expected 8")

