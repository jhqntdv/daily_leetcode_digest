class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        There is a cycle in a linked list if there is some node in the list that can be reached 
        again by continuously following the next pointer. Internally, pos is used to denote the 
        index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.

        Constraints:
        - The number of nodes in the list is in the range [0, 10^4].
        - -10^5 <= Node.val <= 10^5
        - pos is -1 or a valid index in the linked-list.
        """
        # Write your solution here
        pass

if __name__ == '__main__':
    # Test Case 1: Cycle exists (3 -> 2 -> 0 -> -4 -> back to 2)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    # Test Case 2: Cycle exists (1 -> 2 -> back to 1)
    n5 = ListNode(1)
    n6 = ListNode(2)
    n5.next = n6
    n6.next = n5

    # Test Case 3: No cycle (1)
    n7 = ListNode(1)

    sol = Solution()
    print("Test Case 1 (Expected: True):", sol.hasCycle(n1))
    print("Test Case 2 (Expected: True):", sol.hasCycle(n5))
    print("Test Case 3 (Expected: False):", sol.hasCycle(n7))
