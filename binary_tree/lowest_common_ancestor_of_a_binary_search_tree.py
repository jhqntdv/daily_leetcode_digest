"""
Lowest Common Ancestor of a Binary Search Tree (LeetCode #235)
Difficulty: Medium

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Examples:
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Iterative BST Split-Point Search.

        Approach:
        - Leverage the BST invariant (left < node < right):
            - If both p.val and q.val are strictly smaller than curr.val, the LCA must
              reside in the left subtree -> move to curr.left.
            - If both p.val and q.val are strictly greater than curr.val, the LCA must
              reside in the right subtree -> move to curr.right.
            - Otherwise, p and q split across curr (or one of them equals curr),
              making curr the Lowest Common Ancestor.

        Complexity:
        - Time: O(h), where h is the height of the BST (O(log n) balanced, O(n) skewed).
        - Space: O(1) using an iterative pointer.
        """
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        return root


def find_node(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    # BST: [6,2,8,0,4,7,9,null,null,3,5]
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)

    p1 = find_node(root1, 2)
    q1 = find_node(root1, 8)
    lca1 = solution.lowestCommonAncestor(root1, p1, q1)
    print(f"Test 1: LCA of 2 and 8 = {lca1.val if lca1 else None} (Expected: 6)")

    # Test Case 2
    p2 = find_node(root1, 2)
    q2 = find_node(root1, 4)
    lca2 = solution.lowestCommonAncestor(root1, p2, q2)
    print(f"Test 2: LCA of 2 and 4 = {lca2.val if lca2 else None} (Expected: 2)")

    # Test Case 3
    root3 = TreeNode(2)
    root3.left = TreeNode(1)
    p3 = find_node(root3, 2)
    q3 = find_node(root3, 1)
    lca3 = solution.lowestCommonAncestor(root3, p3, q3)
    print(f"Test 3: LCA of 2 and 1 = {lca3.val if lca3 else None} (Expected: 2)")
