"""
Title: Find Median from Data Stream (LeetCode 295)
Difficulty: Hard

Problem Statement:
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10^-5
  of the actual answer will be accepted.

Example 1:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
- If all integer numbers from the stream are between 0 and 100, how would you optimize it?
- If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

import heapq
from typing import List


class MedianFinder:
    """
    Two Heaps Pattern:
    - small_max: Max-Heap (stored with negative values) containing the lower half of numbers.
    - large_min: Min-Heap containing the upper half of numbers.

    Invariants maintained at all times:
    1. Balance: len(small_max) is either equal to len(large_min) or len(large_min) + 1.
    2. Ordering: Every element in small_max <= every element in large_min.

    Complexity:
    - addNum: O(log n) to push/pop from heaps.
    - findMedian: O(1) direct access to roots.
    - Space: O(n) to store all stream elements.
    """

    def __init__(self):
        self.small_max: List[int] = []  # stores negative values to simulate max-heap
        self.large_min: List[int] = []  # standard min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Push into small_max first
        heapq.heappush(self.small_max, -num)

        # Step 2: Ensure ordering invariant (-small_max[0] <= large_min[0])
        if self.small_max and self.large_min and (-self.small_max[0] > self.large_min[0]):
            val = -heapq.heappop(self.small_max)
            heapq.heappush(self.large_min, val)

        # Step 3: Ensure size invariant
        if len(self.small_max) > len(self.large_min) + 1:
            val = -heapq.heappop(self.small_max)
            heapq.heappush(self.large_min, val)
        elif len(self.large_min) > len(self.small_max):
            val = heapq.heappop(self.large_min)
            heapq.heappush(self.small_max, -val)

    def findMedian(self) -> float:
        if len(self.small_max) > len(self.large_min):
            return float(-self.small_max[0])
        return (-self.small_max[0] + self.large_min[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(f"Median after [1, 2]: Got {mf.findMedian()}, Expected 1.5")
    mf.addNum(3)
    print(f"Median after [1, 2, 3]: Got {mf.findMedian()}, Expected 2.0")
    mf.addNum(8)
    print(f"Median after [1, 2, 3, 8]: Got {mf.findMedian()}, Expected 2.5")
    mf.addNum(9)
    print(f"Median after [1, 2, 3, 8, 9]: Got {mf.findMedian()}, Expected 3.0")

