from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    LeetCode: Maximum Depth of Binary Tree
    Difficulty: Easy

    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.

    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3

    Example 2:
        Input: root = [1,null,2]
        Output: 2

    Example 3:
        Input: root = []
        Output: 0

    Constraints:
        - The number of nodes in the tree is in the range [0, 10^4].
        - -100 <= Node.val <= 100
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Bottom-Up Post-Order DFS.

        Approach:
        - The maximum depth of an empty tree is 0.
        - For any non-empty node, its maximum depth is 1 + max(maxDepth(left), maxDepth(right)).

        Complexity:
        - Time: O(n), visiting every node once.
        - Space: O(h) recursion stack, where h is the height of the tree.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def build_tree(nodes: list) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"Test 1: {solution.maxDepth(tree1)} (Expected: 3)")

    # Test Case 2
    tree2 = build_tree([1, None, 2])
    print(f"Test 2: {solution.maxDepth(tree2)} (Expected: 2)")

    # Test Case 3
    tree3 = build_tree([])
    print(f"Test 3: {solution.maxDepth(tree3)} (Expected: 0)")
