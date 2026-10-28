"""
Title: Last Stone Weight (LeetCode 1046)
Difficulty: Easy

Problem Statement:
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones
and smash them together. Suppose the heaviest two stones have weights x and y with x <= y.
The result of this smash is:
- If x == y, both stones are destroyed.
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Example 3:
Input: stones = [2,2]
Output: 0

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Simulates the stone smashing process using a Max-Heap.

        Approach:
        - In Python, heapq is a min-heap, so we invert values (-weight) to simulate a max-heap.
        - Heapify the negative weights in O(n) time.
        - While there are at least two stones in the heap:
            - Pop the two largest stones (first and second).
            - If they are unequal, push the difference back into the heap.
        - If one stone remains, return -heap[0]; otherwise return 0.

        Complexity:
        - Time: O(n log n), where n is the number of stones. Each smash pops 2 and pushes <= 1.
        - Space: O(n) for the heap representation.
        """
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)   # heaviest
            second = -heapq.heappop(max_heap)  # second heaviest

            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    stones1 = [2, 7, 4, 1, 8, 1]
    res1 = sol.lastStoneWeight(stones1)
    print(f"Test 1: Got {res1}, Expected 1")

    # Test Case 2
    stones2 = [1]
    res2 = sol.lastStoneWeight(stones2)
    print(f"Test 2: Got {res2}, Expected 1")

    # Test Case 3
    stones3 = [2, 2]
    res3 = sol.lastStoneWeight(stones3)
    print(f"Test 3: Got {res3}, Expected 0")

