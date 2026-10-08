from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Invert Binary Tree
    Difficulty: Easy
    Category: Binary Tree

    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]

    Example 2:
        Input: root = [2,1,3]
        Output: [2,3,1]

    Example 3:
        Input: root = []
        Output: []

    Constraints:
        - The number of nodes in the tree is in the range [0, 100].
        - -100 <= Node.val <= 100
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # TODO: Implement your solution here
        pass

# --- Helper functions for testing ---
def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted1 = sol.invertTree(root1)
    print(f"Test Case 1 - Expected: [4, 7, 2, 9, 6, 3, 1], Got: {tree_to_list(inverted1)}")

    # Test Case 2
    root2 = build_tree([2, 1, 3])
    inverted2 = sol.invertTree(root2)
    print(f"Test Case 2 - Expected: [2, 3, 1], Got: {tree_to_list(inverted2)}")

    # Test Case 3
    root3 = build_tree([])
    inverted3 = sol.invertTree(root3)
    print(f"Test Case 3 - Expected: [], Got: {tree_to_list(inverted3)}")
