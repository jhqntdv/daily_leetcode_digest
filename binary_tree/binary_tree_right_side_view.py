from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.

    Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

    Example 2:
    Input: root = [1,null,3]
    Output: [1,3]

    Example 3:
    Input: root = []
    Output: []

    Constraints:
    - The number of nodes in the tree is in the range [0, 100].
    - -100 <= Node.val <= 100
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS Level-Order Traversal capturing the last node of each level.

        Approach:
        - Traverse the tree level by level using a FIFO queue (deque).
        - At each level, record the number of nodes `level_length = len(queue)`.
        - Iterate through all nodes in the current level; the node at index
          `i == level_length - 1` is the rightmost visible node at that depth.
        - Push non-null left and right children into the queue for the next level.

        Complexity:
        - Time: O(n), where n is the number of nodes in the binary tree.
        - Space: O(w) <= O(n), where w is the maximum width of the tree.
        """
        if not root:
            return []

        result: List[int] = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1: [1, 2, 3, None, 5, None, 4]
    t1 = build_tree([1, 2, 3, None, 5, None, 4])
    res1 = sol.rightSideView(t1)
    print(f"Test Case 1 Output: {res1} | Expected: [1, 3, 4]")

    # Test Case 2: [1, None, 3]
    t2 = build_tree([1, None, 3])
    res2 = sol.rightSideView(t2)
    print(f"Test Case 2 Output: {res2} | Expected: [1, 3]")

    # Test Case 3: []
    t3 = build_tree([])
    res3 = sol.rightSideView(t3)
    print(f"Test Case 3 Output: {res3} | Expected: []")
