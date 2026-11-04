from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given the root of a binary search tree, and an integer k, 
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

        Constraints:
        - The number of nodes in the tree is n.
        - 1 <= k <= n <= 10^4
        - 0 <= Node.val <= 10^4
        - All the values in the tree are unique.
        """
        pass

if __name__ == '__main__':
    def build_tree(vals):
        if not vals:
            return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    sol = Solution()

    # Test Case 1
    root1 = build_tree([3, 1, 4, None, 2])
    print("Test 1 Result:", sol.kthSmallest(root1, 1), "| Expected: 1")

    # Test Case 2
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    print("Test 2 Result:", sol.kthSmallest(root2, 3), "| Expected: 3")

    # Test Case 3
    root3 = build_tree([2, 1, 3])
    print("Test 3 Result:", sol.kthSmallest(root3, 2), "| Expected: 2")
