from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees root and subRoot, return True if there is a subtree of root
        with the same structure and node values of subRoot and False otherwise.

        A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's
        descendants. The tree tree could also be considered as a subtree of itself.
        """
        pass

if __name__ == '__main__':
    def build_tree(nodes):
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

    sol = Solution()

    # Test Case 1: subRoot is an exact subtree
    # root = [3,4,5,1,2], subRoot = [4,1,2]
    root1 = build_tree([3, 4, 5, 1, 2])
    sub1 = build_tree([4, 1, 2])
    print(f"Test 1: {sol.isSubtree(root1, sub1)} (Expected: True)")

    # Test Case 2: subRoot matches partial structure but has extra descendants
    # root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub2 = build_tree([4, 1, 2])
    print(f"Test 2: {sol.isSubtree(root2, sub2)} (Expected: False)")

    # Test Case 3: Single node trees matching
    # root = [1], subRoot = [1]
    root3 = build_tree([1])
    sub3 = build_tree([1])
    print(f"Test 3: {sol.isSubtree(root3, sub3)} (Expected: True)")
