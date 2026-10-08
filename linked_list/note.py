"""
# Algorithm Cheat Sheet: Linked List

## Core Patterns:
1. Reversal (In-Place Pointer Reversal):
   - Three pointers: `prev = None`, `curr = head`, `nxt = curr.next`.
   - Update `curr.next = prev`, shift `prev = curr`, `curr = nxt`.

2. Fast and Slow Pointers (Floyd's Cycle Detection):
   - Middle of list: `slow` moves 1 step, `fast` moves 2 steps.
   - Cycle detection: If `slow == fast`, cycle exists.
   - Cycle entry: Reset `slow = head`, move both 1 step until they meet.

3. Dummy Node:
   - When head might change (merge lists, remove node, add two numbers).
   - `dummy = ListNode(0); dummy.next = head`. Return `dummy.next`.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def template_reverse_list(head: ListNode) -> ListNode:
    """Iterative reversal in O(n) time, O(1) space."""
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def template_find_middle(head: ListNode) -> ListNode:
    """Find middle node using slow and fast pointers."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
