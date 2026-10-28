import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.

        Constraints:
        - 1 <= nums.length <= 10^5
        - -10^4 <= nums[i] <= 10^4
        - k is in the range [1, the number of unique elements in the array].
        - It is guaranteed that the answer is unique.

        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

        Approach (Min-Heap of size k):
        1. Count frequencies using collections.Counter in O(n) time.
        2. Maintain a min-heap of size k storing tuples of (freq, num).
           - Storing (freq, num) orders elements primarily by frequency.
           - When heap size exceeds k, pop the smallest frequency element.
        3. The heap retains the k most frequent elements.

        Complexity:
        - Time: O(n log k), where n is len(nums) and k is the number of top elements.
          (Alternatively, Bucket Sort achieves O(n) time and O(n) space).
        - Space: O(n + k) to store frequency map and heap of size k.
        """
        counts = Counter(nums)
        # Bounded min-heap of size k: (frequency, num)
        min_heap = []
        for num, freq in counts.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            elif freq > min_heap[0][0]:
                heapq.heapreplace(min_heap, (freq, num))

        return [num for _, num in min_heap]


if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Test Case 1: nums = {nums1}, k = {k1}")
    print(f"Output: {sol.topKFrequent(nums1, k1)} (Expected: [1, 2])\n")
    
    # Test Case 2
    nums2 = [1]
    k2 = 1
    print(f"Test Case 2: nums = {nums2}, k = {k2}")
    print(f"Output: {sol.topKFrequent(nums2, k2)} (Expected: [1])\n")
    
    # Test Case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3, -1, 2]
    k3 = 2
    print(f"Test Case 3: nums = {nums3}, k = {k3}")
    print(f"Output: {sol.topKFrequent(nums3, k3)} (Expected: [-1, 2] or [2, -1])\n")
