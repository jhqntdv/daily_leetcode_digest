"""
# Algorithm Cheat Sheet: Binary Tree & Binary Search Tree (BST)

## Core Concepts & Guarantees:
1. **Binary Tree Properties**:
   - A tree where each node has at most 2 children (`left` and `right`).
   - **Depth of a node**: Number of edges from the root to the node (root depth = 0).
   - **Height of a tree**: Number of nodes (or edges, depending on problem convention) along the longest path from root to a leaf.
   - **Balanced Tree**: Height is $O(\log n)$. **Skewed Tree** (linked-list-like): Height is $O(n)$.

2. **Binary Search Tree (BST) Global Invariant**:
   - For **every** node $u$:
     - **All** nodes in $u.\text{left}$ have values strictly $< u.\text{val}$.
     - **All** nodes in $u.\text{right}$ have values strictly $> u.\text{val}$.
   - **Crucial Property**: An **In-Order Traversal** (`Left -> Root -> Right`) of a valid BST visits values in **strictly increasing sorted order**.

---

## Four Canonical Traversals:

| Traversal | Order | Primary Use Cases |
| :--- | :---: | :--- |
| **Pre-Order DFS** | `Root -> Left -> Right` | Passing parent constraints top-down, tree cloning, serialization |
| **In-Order DFS** | `Left -> Root -> Right` | Extracting sorted order from BSTs, $k$-th smallest in BST |
| **Post-Order DFS** | `Left -> Right -> Root` | Bottom-up aggregation (heights, diameters, subtree sums, LCA) |
| **Level-Order BFS** | Depth-by-depth (`deque`) | Level grouping, right/left side views, minimum depth / shortest path |

---

## Core Algorithmic Patterns:

### Pattern 1: Bottom-Up Post-Order Aggregation (Height, Diameter, Max Path Sum)
- Each recursive call returns a single-branch metric (e.g., subtree height or max downward path sum) to its parent,
  while updating a global variable (`nonlocal best`) that combines both `left` and `right` subtrees (the "turning point").
- Example (Diameter):
  - Global update: `max_diameter = max(max_diameter, left_h + right_h)`
  - Return to parent: `1 + max(left_h, right_h)`

### Pattern 2: Top-Down Constraint / Range Propagation (Validate BST, Good Nodes)
- Pass accumulated ancestor state down the recursion parameters: `dfs(node, low, high)`.
- Moving left tightens the upper bound `(low, node.val)`; moving right tightens the lower bound `(node.val, high)`.

### Pattern 3: Level-Order BFS Snapshot (`len(queue)`)
- Use `collections.deque([root])`.
- At the start of each `while queue:` iteration, `level_size = len(queue)` freezes the exact count of nodes at the current depth.
- Loop `for i in range(level_size):` to process the entire level before advancing to the next depth.
  - `i == 0` is the leftmost node; `i == level_size - 1` is the rightmost node (Right Side View).

### Pattern 4: BST Split-Point / Binary Navigation (LCA in BST, BST Search)
- Because of the BST property, we do not need to search both subtrees if both targets lie on the same side:
  - Both $< \text{curr.val}$ $\to$ go left.
  - Both $> \text{curr.val}$ $\to$ go right.
  - Otherwise, `curr` is the split point (Lowest Common Ancestor). Runs in $O(h)$ time and $O(1)$ space!

### Pattern 5: General Binary Tree Lowest Common Ancestor (Post-Order Split)
- When the tree is NOT a BST:
  - Base case: `if not root or root == p or root == q: return root`
  - Recurse `left = lca(root.left, p, q)` and `right = lca(root.right, p, q)`.
  - If both `left` and `right` are non-null, `root` is the LCA; otherwise return whichever is non-null.

---

## Common Pitfalls & Edge Cases:
- **Local vs. Global BST Check Trap**:
  - Checking only `node.left.val < node.val < node.right.val` is **wrong**! A node deep inside the right subtree could still be smaller than an ancestor above its parent. Always pass `(low, high)` bounds or track `prev` in in-order traversal.
- **Edges vs. Nodes Count**:
  - Maximum Depth counts **nodes** on the longest path (empty tree = 0, single node = 1).
  - Diameter counts **edges** on the longest path (single node = 0). Always check problem definitions.
- **Using `list.pop(0)` instead of `deque.popleft()`**:
  - `list.pop(0)` is $O(n)$, degrading BFS from $O(n)$ to $O(n^2)$. Always use `collections.deque`.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================================
# Template 1: Bottom-Up Post-Order DFS (Height & Global Diameter/Path)
# ============================================================================
def template_bottom_up_diameter(root: Optional[TreeNode]) -> int:
    """
    Computes tree diameter (longest path in edges) via post-order traversal.
    Time: O(n), Space: O(h)
    """
    max_diameter = 0

    def dfs_height(node: Optional[TreeNode]) -> int:
        nonlocal max_diameter
        if not node:
            return 0
        left_h = dfs_height(node.left)
        right_h = dfs_height(node.right)

        max_diameter = max(max_diameter, left_h + right_h)
        return 1 + max(left_h, right_h)

    dfs_height(root)
    return max_diameter


# ============================================================================
# Template 2: Top-Down Range Propagation (Validate BST)
# ============================================================================
def template_validate_bst(root: Optional[TreeNode]) -> bool:
    """
    Validates strict BST property across all ancestors using (low, high) interval.
    Time: O(n), Space: O(h)
    """
    def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))


# ============================================================================
# Template 3: Level-Order BFS Snapshot
# ============================================================================
def template_level_order_bfs(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Traverses tree level by level using a FIFO deque.
    Time: O(n), Space: O(w) where w is max width of the tree.
    """
    if not root:
        return []

    levels: List[List[int]] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(current_level)

    return levels


# ============================================================================
# Template 4: General Binary Tree Lowest Common Ancestor (Post-Order)
# ============================================================================
def template_lca_general_tree(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Finds LCA of p and q in any binary tree (not necessarily a BST).
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = template_lca_general_tree(root.left, p, q)
    right = template_lca_general_tree(root.right, p, q)

    if left and right:
        return root
    return left if left else right

