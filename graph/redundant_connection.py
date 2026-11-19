"""
Title: Redundant Connection
Difficulty: Medium
Tag: graph

Problem Statement:
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional
edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that
already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are
multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: edges = [[1, 2], [1, 3], [2, 3]]
Output: [2, 3]

Example 2:
Input: edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
Output: [1, 4]

Example 3:
Input: edges = [[1, 3], [3, 4], [1, 5], [3, 5], [2, 3]]
Output: [3, 5]

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    edges1 = [[1, 2], [1, 3], [2, 3]]
    output1 = solution.findRedundantConnection(edges1)
    print(f"Test Case 1: edges = {edges1}")
    print(f"Output: {output1} | Expected: [2, 3]\n")

    # Test Case 2
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    output2 = solution.findRedundantConnection(edges2)
    print(f"Test Case 2: edges = {edges2}")
    print(f"Output: {output2} | Expected: [1, 4]\n")

    # Test Case 3
    edges3 = [[1, 3], [3, 4], [1, 5], [3, 5], [2, 3]]
    output3 = solution.findRedundantConnection(edges3)
    print(f"Test Case 3: edges = {edges3}")
    print(f"Output: {output3} | Expected: [3, 5]\n")
