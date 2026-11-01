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
        """
        # Write your solution here
        pass

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
