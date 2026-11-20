from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

        Example 1:
            Input: head = [1, 2, 2, 1]
            Output: true

        Example 2:
            Input: head = [1, 2]
            Output: false

        Example 3:
            Input: head = [1, 2, 3, 2, 1]
            Output: true

        Constraints:
            - The number of nodes in the list is in the range [1, 10^5].
            - 0 <= Node.val <= 9
        """
        # Write your code here
        pass


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


if __name__ == '__main__':
    sol = Solution()

    # Example 1: [1, 2, 2, 1]
    head1 = create_linked_list([1, 2, 2, 1])
    print(f"Test 1: {sol.isPalindrome(head1)}")  # Expected: True

    # Example 2: [1, 2]
    head2 = create_linked_list([1, 2])
    print(f"Test 2: {sol.isPalindrome(head2)}")  # Expected: False

    # Example 3: [1, 2, 3, 2, 1]
    head3 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Test 3: {sol.isPalindrome(head3)}")  # Expected: True
