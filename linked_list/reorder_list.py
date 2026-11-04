"""
Title: Reorder List
Difficulty: Medium

Problem Statement:
You are given the head of a singly linked list. The list can be represented as:
L0 -> L1 -> ... -> Ln - 1 -> Ln

Reorder the list to be in the following form:
L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Examples:
Example 1:
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]

Example 2:
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]

Example 3:
Input: head = [1]
Output: [1]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        Three-Step In-Place Algorithm:
        1. Find the middle of the list using slow & fast pointers (`slow` stops at the end of the first half).
        2. Reverse the second half of the list (`slow.next` onward) in-place and sever the link (`slow.next = None`).
        3. Interleave (zip) the first half (`first = head`) and the reversed second half (`second = prev`).

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Split into two independent lists
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Interleave first half and reversed second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


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
    head1 = list_to_linked_list([1, 2, 3, 4])
    solution.reorderList(head1)
    res1 = linked_list_to_list(head1)
    print(f"Test Case 1: Expected [1, 4, 2, 3], Got {res1}")

    # Test Case 2
    head2 = list_to_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head2)
    res2 = linked_list_to_list(head2)
    print(f"Test Case 2: Expected [1, 5, 2, 4, 3], Got {res2}")

    # Test Case 3
    head3 = list_to_linked_list([1])
    solution.reorderList(head3)
    res3 = linked_list_to_list(head3)
    print(f"Test Case 3: Expected [1], Got {res3}")
