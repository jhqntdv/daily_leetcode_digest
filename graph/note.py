"""
# Algorithm Cheat Sheet: Graph Algorithms

## Core Concepts & Guarantees:
A graph G = (V, E) consists of a set of vertices (nodes) V and a set of edges E.
Graphs can be:
- **Directed (Digraph)**: Edges have direction (u -> v).
- **Undirected**: Edges are bidirectional (u <-> v).
- **Weighted vs. Unweighted**: Edges carry costs/lengths or uniform unit weights.
- **Cyclic vs. Acyclic**: Whether paths can loop back to a previously visited vertex (e.g., Directed Acyclic Graph / DAG).

### Graph Representations:
1. **Adjacency List (`List[List[int]]` or `collections.defaultdict(list)`)**:
   - Best for sparse graphs (E << V^2).
   - Space: O(V + E). Iterating neighbors of u takes O(deg(u)).
2. **Adjacency Matrix (`List[List[int]]`)**:
   - Best for dense graphs or when edge existence checks `(u, v) in E` need O(1) time.
   - Space: O(V^2).
3. **Implicit Grid Graph**:
   - Cells `(r, c)` are vertices; 4-directional or 8-directional neighbors within boundaries are edges.

---

## Core Patterns:

1. **Breadth-First Search (BFS) - Shortest Path in Unweighted Graph**:
   - Explores nodes level by level (by edge distance).
   - Guarantees the shortest path in unweighted graphs.
   - **Crucial Rule**: Mark nodes as visited immediately upon **enqueuing** (not upon dequeuing) to prevent exponential duplicate pushes.

2. **Multi-Source BFS (Simultaneous Expansion)**:
   - When multiple starting nodes expand simultaneously (e.g., spreading rot/fire, distance to nearest 0).
   - Enqueue all starting sources at `time = 0` before starting the BFS loop.

3. **Grid Traversal & Flood Fill**:
   - Explore connected components across adjacent cells.
   - Guard each move with boundary checks (`0 <= nr < R and 0 <= nc < C`) and condition checks (`grid[nr][nc] == target`).

4. **Directed Graph Cycle Detection (3-Color State DFS)**:
   - State 0 (White / Unvisited): node has not been explored.
   - State 1 (Gray / Visiting): node is currently in the active recursion call stack (ancestor).
     If an edge points to a State 1 node, a **directed cycle is detected**.
   - State 2 (Black / Visited): node and all its descendants have been fully processed.

5. **Topological Sorting (Kahn's Algorithm - In-degree BFS)**:
   - Linear ordering of vertices in a DAG such that for every directed edge u -> v, u comes before v.
   - Compute `in_degree` for each node.
   - Enqueue all nodes with `in_degree == 0`.
   - Pop node, append to topological order, and decrement neighbors' `in_degree`.
   - If `len(order) == V`, a valid topological order exists; otherwise, the graph has a cycle.

6. **Disjoint Set Union (DSU / Union-Find)**:
   - Efficiently maintains dynamic connected components and detects cycles in undirected graphs.
   - With **Path Compression** and **Union by Rank/Size**, operations run in nearly O(1) amortized time (inverse Ackermann function α(n)).

7. **Dijkstra's Algorithm (Shortest Path with Non-Negative Weights)**:
   - Uses a Min-Heap (`heapq` in Python) to greedily expand the closest unvisited node.
   - Time Complexity: O((V + E) log V).

---

## Common Pitfalls & Edge Cases:
- **Late Visited Marking in BFS**: Adding a node to `visited` on `popleft()` instead of `append()` causes the queue to explode exponentially on dense/grid graphs.
- **Python Recursion Limit**: Default recursion limit is 1000. Grid DFS on a 300x300 grid can exceed depth 90,000, causing `RecursionError`. Prefer iterative BFS or increase `sys.setrecursionlimit`.
- **Undirected Cycle Detection vs. Directed**:
  - Undirected: Cycle exists if we visit an already-visited neighbor that is NOT the immediate parent.
  - Directed: Checking visited alone is insufficient; you must verify if the visited node is an **ancestor in the current recursion stack** (3-color DFS or in-degree tracking).
- **Disconnected Graphs / Forests**: Always loop through all vertices `0` to `V - 1` to ensure disconnected components are processed.
- **In-place Grid Mutation vs. Visited Set**: Modifying `grid[r][c] = '0'` saves O(R * C) memory but mutates input data. Clarify if in-place mutation is permissible.
"""

from collections import deque
import heapq
from typing import List, Optional, Tuple


def template_bfs_shortest_path(num_nodes: int, adj: List[List[int]], start: int, target: int) -> int:
    """
    Pattern: Single-Source Shortest Path (Unweighted Graph).
    Returns the minimum number of edges to reach target from start, or -1 if unreachable.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start == target:
        return 0

    visited = [False] * num_nodes
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        curr, dist = queue.popleft()
        for neighbor in adj[curr]:
            if neighbor == target:
                return dist + 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

    return -1


def template_multi_source_bfs(grid: List[List[int]], sources: List[Tuple[int, int]]) -> List[List[int]]:
    """
    Pattern: Multi-Source BFS on a 2D Grid.
    Computes shortest distance from each cell to its nearest source.
    Time Complexity: O(R * C)
    Space Complexity: O(R * C)
    """
    if not grid or not grid[0]:
        return []

    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    for r, c in sources:
        dist[r][c] = 0
        queue.append((r, c))

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


def template_topological_sort_kahns(num_nodes: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    """
    Pattern: Kahn's Algorithm for Topological Sort & Cycle Detection in DAG.
    edges: list of directed pairs (u, v) indicating u -> v.
    Returns topological ordering, or None if a cycle is detected.
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    adj: List[List[int]] = [[] for _ in range(num_nodes)]
    in_degrees = [0] * num_nodes

    for u, v in edges:
        adj[u].append(v)
        in_degrees[v] += 1

    queue = deque([i for i in range(num_nodes) if in_degrees[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in adj[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_nodes else None


def template_directed_cycle_detection_dfs(num_nodes: int, adj: List[List[int]]) -> bool:
    """
    Pattern: Directed Graph Cycle Detection via 3-Color DFS.
    State 0: Unvisited, State 1: Visiting (in recursion stack), State 2: Fully visited.
    Returns True if a cycle exists, False otherwise.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    state = [0] * num_nodes

    def has_cycle(node: int) -> bool:
        state[node] = 1  # visiting
        for neighbor in adj[node]:
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0 and has_cycle(neighbor):
                return True
        state[node] = 2  # visited
        return False

    for i in range(num_nodes):
        if state[i] == 0:
            if has_cycle(i):
                return True

    return False


class UnionFind:
    """
    Pattern: Disjoint Set Union (DSU) with Path Compression and Union by Rank.
    Nearly O(1) amortized operations: find, union, connected.
    Space Complexity: O(n)
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # Already in same component (cycle in undirected graph)

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def template_dijkstra(num_nodes: int, adj: List[List[Tuple[int, int]]], start: int) -> List[float]:
    """
    Pattern: Dijkstra's Algorithm for Shortest Path with Non-Negative Edge Weights.
    adj: list of (neighbor, weight) for each node.
    Returns distance array from start node to all nodes (inf if unreachable).
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V + E)
    """
    dist = [float('inf')] * num_nodes
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > dist[u]:
            continue

        for v, weight in adj[u]:
            new_dist = curr_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist
