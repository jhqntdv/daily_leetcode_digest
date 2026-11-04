from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, return True if they are the same tree, otherwise return False.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        Constraints:
        - The number of nodes in both trees is in the range [0, 100].
        - -10^4 <= Node.val <= 10^4
        """
        # TODO: Implement your solution here
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: p = [1,2,3], q = [1,2,3]
    #      1            1
    #     / \          / \
    #    2   3        2   3
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(f"Test Case 1: {solution.isSameTree(p1, q1)} (Expected: True)")

    # Test Case 2: p = [1,2], q = [1, None, 2]
    #      1            1
    #     /              \
    #    2                2
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(f"Test Case 2: {solution.isSameTree(p2, q2)} (Expected: False)")

    # Test Case 3: p = [1,2,1], q = [1,1,2]
    #      1            1
    #     / \          / \
    #    2   1        1   2
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    print(f"Test Case 3: {solution.isSameTree(p3, q3)} (Expected: False)")
