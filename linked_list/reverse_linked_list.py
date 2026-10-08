class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.

        Constraints:
        - The number of nodes in the list is the range [0, 5000].
        - -5000 <= Node.val <= 5000

        Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    head1 = array_to_list([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    print(f"Test Case 1: Expected [5, 4, 3, 2, 1], Got {list_to_array(reversed1)}")

    # Test Case 2
    head2 = array_to_list([1, 2])
    reversed2 = solution.reverseList(head2)
    print(f"Test Case 2: Expected [2, 1], Got {list_to_array(reversed2)}")

    # Test Case 3
    head3 = array_to_list([])
    reversed3 = solution.reverseList(head3)
    print(f"Test Case 3: Expected [], Got {list_to_array(reversed3)}")
