from typing import Optional

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Given the root of a binary tree and an integer targetSum, return True
        if the tree has a root-to-leaf path such that adding up all the values
        along the path equals targetSum.

        A leaf is a node with no children.

        Constraints:
        - The number of nodes in the tree is in the range [0, 5000].
        - -1000 <= Node.val <= 1000
        - -1000 <= targetSum <= 1000
        """
        # TODO: Implement your solution here
        pass

def build_tree(values):
    """Helper function to build a binary tree from level-order array representation."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

if __name__ == '__main__':
    sol = Solution()

    # Example 1:
    # Tree: [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    # Path: 5 -> 4 -> 11 -> 2 sums to 22
    # Target: 22
    # Output: True
    tree1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print(f"Example 1 Output: {sol.hasPathSum(tree1, 22)}")  # Expected: True

    # Example 2:
    # Tree: [1, 2, 3]
    # Target: 5
    # Output: False
    tree2 = build_tree([1, 2, 3])
    print(f"Example 2 Output: {sol.hasPathSum(tree2, 5)}")  # Expected: False

    # Example 3:
    # Tree: [] (Empty Tree)
    # Target: 0
    # Output: False
    tree3 = build_tree([])
    print(f"Example 3 Output: {sol.hasPathSum(tree3, 0)}")  # Expected: False
