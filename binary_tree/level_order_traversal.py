from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]

    Example 2:
        Input: root = [1]
        Output: [[1]]

    Example 3:
        Input: root = []
        Output: []

    Constraints:
        - The number of nodes in the tree is in the range [0, 2000].
        - -1000 <= Node.val <= 1000
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    sol = Solution()

    # Helper function to construct tree from level-order list (with None for missing nodes)
    def build_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            curr = queue.popleft()
            if i < len(values) and values[i] is not None:
                curr.left = TreeNode(values[i])
                queue.append(curr.left)
            i += 1
            if i < len(values) and values[i] is not None:
                curr.right = TreeNode(values[i])
                queue.append(curr.right)
            i += 1
        return root

    # Test Case 1: root = [3,9,20,None,None,15,7]
    t1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test Case 1:", sol.levelOrder(t1))  # Expected: [[3], [9, 20], [15, 7]]

    # Test Case 2: root = [1]
    t2 = build_tree([1])
    print("Test Case 2:", sol.levelOrder(t2))  # Expected: [[1]]

    # Test Case 3: root = []
    t3 = build_tree([])
    print("Test Case 3:", sol.levelOrder(t3))  # Expected: []
