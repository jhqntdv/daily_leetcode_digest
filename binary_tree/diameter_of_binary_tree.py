from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.

        Example 1:
        Input: root = [1,2,3,4,5]
        Output: 3
        Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

        Example 2:
        Input: root = [1,2]
        Output: 1

        Example 3:
        Input: root = [1]
        Output: 0

        Constraints:
        - The number of nodes in the tree is in the range [1, 10^4].
        - -100 <= Node.val <= 100

        Approach (Bottom-Up Post-Order DFS):
        - At every node, the longest path that uses this node as its highest "turning point"
          has length `left_height + right_height` (where height of an empty subtree is 0).
        - Use a post-order DFS helper that:
            1. Computes `left_height` and `right_height`.
            2. Updates `max_diameter = max(max_diameter, left_height + right_height)`.
            3. Returns `1 + max(left_height, right_height)` as the subtree height to its parent.

        Complexity:
        - Time: O(n), visiting each node exactly once.
        - Space: O(h) recursion stack, where h is the height of the tree (O(log n) balanced, O(n) skewed).
        """
        max_diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            # Longest path through current node as highest ancestor
            max_diameter = max(max_diameter, left_h + right_h)

            return 1 + max(left_h, right_h)

        height(root)
        return max_diameter


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1: root = [1,2,3,4,5]
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    t1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    res1 = sol.diameterOfBinaryTree(t1)
    print(f"Test Case 1: Result = {res1} (Expected: 3)")

    # Test Case 2: root = [1,2]
    #     1
    #    /
    #   2
    t2 = TreeNode(1, TreeNode(2))
    res2 = sol.diameterOfBinaryTree(t2)
    print(f"Test Case 2: Result = {res2} (Expected: 1)")

    # Test Case 3: root = [1]
    t3 = TreeNode(1)
    res3 = sol.diameterOfBinaryTree(t3)
    print(f"Test Case 3: Result = {res3} (Expected: 0)")
