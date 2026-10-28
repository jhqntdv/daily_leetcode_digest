"""
Title: Merge k Sorted Lists (LeetCode 23)
Difficulty: Hard

Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        K-Way Merge using a Min-Heap.

        Approach:
        - We push the head of each non-empty linked list into a Min-Heap.
        - Important Python Trap: Since ListNode instances do not implement '<',
          if two nodes have equal values, comparing (node.val, node) raises a TypeError.
          We use a unique monotonic counter as a tie-breaker: (node.val, count, node).
        - Repeatedly pop the smallest node, append it to our merged list, and if
          that node has a next pointer, push node.next into the heap with an incremented counter.

        Complexity:
        - Time: O(N log k), where N is the total number of nodes and k is the number of lists.
          At any time, the heap holds at most k elements, so each push/pop takes O(log k).
        - Space: O(k) auxiliary space for the min-heap.
        """
        min_heap = []
        count = 0  # Tie-breaker to prevent comparison between ListNode instances

        # Initialize heap with head of each non-empty list
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, count, node))
                count += 1

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next


def build_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_array(node: Optional[ListNode]) -> List[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: [[1,4,5],[1,3,4],[2,6]]
    l1 = build_list([1, 4, 5])
    l2 = build_list([1, 3, 4])
    l3 = build_list([2, 6])
    merged1 = sol.mergeKLists([l1, l2, l3])
    print(f"Test 1: Got {list_to_array(merged1)}, Expected [1, 1, 2, 3, 4, 4, 5, 6]")

    # Test Case 2: []
    merged2 = sol.mergeKLists([])
    print(f"Test 2: Got {list_to_array(merged2)}, Expected []")

    # Test Case 3: [[]]
    merged3 = sol.mergeKLists([build_list([])])
    print(f"Test 3: Got {list_to_array(merged3)}, Expected []")

