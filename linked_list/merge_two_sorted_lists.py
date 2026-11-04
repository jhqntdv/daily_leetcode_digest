"""
Title: Merge Two Sorted Lists
Difficulty: Easy
Tag: linked_list

Problem Statement:
You are given the heads of two sorted linked lists, list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Examples:
Example 1:
  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4]

Example 2:
  Input: list1 = [], list2 = []
  Output: []

Example 3:
  Input: list1 = [], list2 = [0]
  Output: [0]

Constraints:
  - The number of nodes in both lists is in the range [0, 50].
  - -100 <= Node.val <= 100
  - Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative Two-Pointer Splice with Dummy Head.

        Approach:
        - Create a `dummy` sentinel node and a tail pointer `curr = dummy`.
        - While both `list1` and `list2` are non-empty:
            - Attach the node with the smaller value to `curr.next` and advance that list's pointer.
            - Advance `curr`.
        - Attach the remaining non-empty list (`list1 or list2`) directly to `curr.next`.
        - Return `dummy.next`.

        Complexity:
        - Time: O(m + n), where m and n are the lengths of the two lists.
        - Space: O(1) extra space (splices existing nodes in-place).
        """
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next


# Helper functions for testing
def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
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


if __name__ == '__main__':
    solution = Solution()
    
    # Test Case 1
    l1_1 = build_linked_list([1, 2, 4])
    l2_1 = build_linked_list([1, 3, 4])
    res1 = solution.mergeTwoLists(l1_1, l2_1)
    print(f"Test Case 1 Output: {linked_list_to_list(res1)} | Expected: [1, 1, 2, 3, 4]")
    
    # Test Case 2
    l1_2 = build_linked_list([])
    l2_2 = build_linked_list([])
    res2 = solution.mergeTwoLists(l1_2, l2_2)
    print(f"Test Case 2 Output: {linked_list_to_list(res2)} | Expected: []")
    
    # Test Case 3
    l1_3 = build_linked_list([])
    l2_3 = build_linked_list([0])
    res3 = solution.mergeTwoLists(l1_3, l2_3)
    print(f"Test Case 3 Output: {linked_list_to_list(res3)} | Expected: [0]")
