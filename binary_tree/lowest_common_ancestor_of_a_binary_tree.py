"""
Lowest Common Ancestor of a Binary Tree (Medium)

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself)."

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Write your code here
        pass


if __name__ == '__main__':
    def find_node(node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None
        if node.val == val:
            return node
        return find_node(node.left, val) or find_node(node.right, val)

    sol = Solution()

    # Test Case 1: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    p1 = find_node(root1, 5)
    q1 = find_node(root1, 1)
    ans1 = sol.lowestCommonAncestor(root1, p1, q1)
    print(f"Test 1: {ans1.val if ans1 else None} (Expected: 3)")

    # Test Case 2: p = 5, q = 4
    p2 = find_node(root1, 5)
    q2 = find_node(root1, 4)
    ans2 = sol.lowestCommonAncestor(root1, p2, q2)
    print(f"Test 2: {ans2.val if ans2 else None} (Expected: 5)")

    # Test Case 3: root = [1,2], p = 1, q = 2
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    p3 = find_node(root3, 1)
    q3 = find_node(root3, 2)
    ans3 = sol.lowestCommonAncestor(root3, p3, q3)
    print(f"Test 3: {ans3.val if ans3 else None} (Expected: 1)")
