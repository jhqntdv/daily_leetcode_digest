"""
Title: Remove Nth Node From End of List
Difficulty: Medium
LeetCode Pattern: Fast & Slow Pointers / Two Pointers

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1, 2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow-up:
Could you do this in one pass?
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TODO: Implement your solution here
        pass


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    head1 = build_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    res1 = solution.removeNthFromEnd(head1, n1)
    print(f"Test Case 1: Expected [1, 2, 3, 5], Got {linked_list_to_list(res1)}")

    # Test Case 2
    head2 = build_linked_list([1])
    n2 = 1
    res2 = solution.removeNthFromEnd(head2, n2)
    print(f"Test Case 2: Expected [], Got {linked_list_to_list(res2)}")

    # Test Case 3
    head3 = build_linked_list([1, 2])
    n3 = 1
    res3 = solution.removeNthFromEnd(head3, n3)
    print(f"Test Case 3: Expected [1], Got {linked_list_to_list(res3)}")
