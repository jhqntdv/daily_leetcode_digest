"""
Title: Clone Graph (LeetCode 133)
Difficulty: Medium
Tag: graph

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Test Cases:
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Example 2:
Input: adjList = [[]]
Output: [[]]

Example 3:
Input: adjList = []
Output: []

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.
"""

from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # TODO: Implement your solution here
        pass

# Helper functions for testing
def build_graph(adjList: list[list[int]]) -> Optional[Node]:
    if not adjList:
        return None
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]

def graph_to_adj_list(node: Optional[Node]) -> list[list[int]]:
    if not node:
        return []
    visited = {}
    
    def dfs(curr: Node):
        visited[curr.val] = []
        for neighbor in curr.neighbors:
            visited[curr.val].append(neighbor.val)
            if neighbor.val not in visited:
                dfs(neighbor)
                
    dfs(node)
    max_val = max(visited.keys())
    adjList = []
    for i in range(1, max_val + 1):
        adjList.append(visited.get(i, []))
    return adjList

if __name__ == '__main__':
    solution = Solution()
    
    # Test Case 1
    adj1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = build_graph(adj1)
    cloned1 = solution.cloneGraph(graph1)
    print("Test Case 1:", graph_to_adj_list(cloned1) == adj1)
    
    # Test Case 2
    adj2 = [[]]
    graph2 = build_graph(adj2)
    cloned2 = solution.cloneGraph(graph2)
    print("Test Case 2:", graph_to_adj_list(cloned2) == adj2)
    
    # Test Case 3
    adj3 = []
    graph3 = build_graph(adj3)
    cloned3 = solution.cloneGraph(graph3)
    print("Test Case 3:", graph_to_adj_list(cloned3) == adj3)
