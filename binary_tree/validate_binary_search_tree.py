from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys strictly less than the node's key.
        - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.

        Example 1:
            Input: root = [2,1,3]
            Output: True

        Example 2:
            Input: root = [5,1,4,null,null,3,6]
            Output: False
            Explanation: The root node's value is 5 but its right child's value is 4.

        Example 3:
            Input: root = [5,4,6,null,null,3,7]
            Output: False
            Explanation: The root node's value is 5, but its right child has a left child with value 3 (which is <= 5).

        Constraints:
            - The number of nodes in the tree is in the range [1, 10^4].
            - -2^31 <= Node.val <= 2^31 - 1

        Approach (Top-Down Range Propagation DFS):
        - Every node in a BST must lie within a valid open interval `(low, high)` inherited from its ancestors:
            - The root starts with `(-inf, +inf)`.
            - Moving to `node.left` tightens the upper bound to `(low, node.val)`.
            - Moving to `node.right` tightens the lower bound to `(node.val, high)`.
        - If any node violates `low < node.val < high`, return False immediately.

        Complexity:
        - Time: O(n), visiting each node at most once.
        - Space: O(h) recursion stack, where h is the height of the tree.
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: [2, 1, 3]
    #     2
    #    / \
    #   1   3
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Test 1: {solution.isValidBST(t1)} (Expected: True)")

    # Test Case 2: [5, 1, 4, null, null, 3, 6]
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Test 2: {solution.isValidBST(t2)} (Expected: False)")

    # Test Case 3: [5, 4, 6, null, null, 3, 7]
    #     5
    #    / \
    #   4   6
    #      / \
    #     3   7
    t3 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    print(f"Test 3: {solution.isValidBST(t3)} (Expected: False)")
