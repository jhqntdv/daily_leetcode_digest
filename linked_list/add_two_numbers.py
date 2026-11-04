class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.

        Constraints:
        - The number of nodes in each linked list is in the range [1, 100].
        - 0 <= Node.val <= 9
        - It is guaranteed that the list represents a number that does not have leading zeros.

        Approach (Dummy Head + Carry Propagation):
        - Traverse both lists simultaneously while `l1`, `l2`, or `carry` is non-zero.
        - At each step:
            - Extract `v1 = l1.val if l1 else 0` and `v2 = l2.val if l2 else 0`.
            - Compute `carry, digit = divmod(v1 + v2 + carry, 10)`.
            - Append `ListNode(digit)` to the result list and advance pointers.

        Complexity:
        - Time: O(max(m, n)), where m and n are the lengths of l1 and l2.
        - Space: O(max(m, n)) for the newly created result linked list (O(1) auxiliary).
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, digit = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: [2,4,3] + [5,6,4] -> [7,0,8]
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    res1 = solution.addTwoNumbers(l1, l2)
    print("Test 1:", linked_list_to_list(res1))  # Expected: [7, 0, 8]

    # Test Case 2: [0] + [0] -> [0]
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    res2 = solution.addTwoNumbers(l1, l2)
    print("Test 2:", linked_list_to_list(res2))  # Expected: [0]

    # Test Case 3: [9,9,9,9,9,9,9] + [9,9,9,9] -> [8,9,9,9,0,0,0,1]
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    res3 = solution.addTwoNumbers(l1, l2)
    print("Test 3:", linked_list_to_list(res3))  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
