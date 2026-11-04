"""
# Algorithm Cheat Sheet: Linked List

## Core Patterns:
1. **In-Place Pointer Reversal**:
   - Three pointers: `prev = None`, `curr = head`, `nxt = curr.next`.
   - Update `curr.next = prev`, shift `prev = curr`, `curr = nxt`.
   - Time: $O(n)$, Space: $O(1)$.

2. **Fast and Slow Pointers (Floyd's Tortoise & Hare)**:
   - **Middle of list**: `slow` moves 1 step, `fast` moves 2 steps (`while fast and fast.next:`).
   - **Cycle detection**: If `slow is fast`, a cycle exists.
   - **Cycle entry point**: Reset `slow = head`, advance both 1 step at a time until `slow is fast`.

3. **Fixed-Gap Two Pointers (Nth Node from End)**:
   - Advance `fast` by `n + 1` steps from `dummy` first, then move `slow` and `fast` together until `fast` is `None`.
   - `slow.next` is the $n$-th node from the end: `slow.next = slow.next.next`.

4. **Dummy Sentinel Node**:
   - Use whenever the `head` node itself might change or be deleted (merging lists, removing $n$-th from end, adding numbers).
   - `dummy = ListNode(0, head)` $\to$ return `dummy.next`.

5. **Composite List Manipulation (Reorder List / Palindrome Linked List)**:
   - Step 1: Find middle (`slow`, `fast`).
   - Step 2: Reverse second half (`slow.next` onward) and sever `slow.next = None`.
   - Step 3: Interleave or compare the two halves in $O(1)$ space.

---

## Common Pitfalls & Edge Cases:
- **Dangling Cycle in Reorder / Split**: Always set `slow.next = None` when splitting a list into two halves; forgetting this leaves a cycle at the tail of the first half.
- **Deleting the Head Node**: Without a `dummy` node, removing the 1st node (`n == length`) requires special-case branching.
- **Final Carry in Digit Addition**: In `addTwoNumbers`, loop while `l1 or l2 or carry` so a trailing carry (e.g. `99 + 1 = 100`) is not dropped.
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


def template_interleave_lists(first: ListNode, second: ListNode) -> None:
    """In-place zipper merge of two lists (where len(first) >= len(second))."""
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
