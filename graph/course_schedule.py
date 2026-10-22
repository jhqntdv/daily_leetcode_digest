"""
Title: Course Schedule (LeetCode 207)
Difficulty: Medium

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that
you must take course b_i first if you want to take course a_i.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: True
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: False
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Example 3:
Input: numCourses = 3, prerequisites = [[0, 1], [0, 2], [1, 2]]
Output: True
Explanation: Course 2 has no prerequisites. Course 1 depends on 2. Course 0 depends on 1 and 2. A valid order is 2 -> 1 -> 0.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= a_i, b_i < numCourses
- All pairs prerequisites[i] are unique.
"""
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Topological Sort using Kahn's Algorithm (BFS with In-degrees).

        A prerequisite pair [a, b] indicates a directed edge from course b to course a (b -> a).
        A course can be taken if all its prerequisites have been completed (in-degree == 0).
        If we can process all `numCourses` courses, there is no directed cycle, so return True.
        Otherwise, a cycle exists, so return False.

        Time Complexity: O(V + E) where V = numCourses, E = len(prerequisites).
        Space Complexity: O(V + E) for the adjacency list and queue.
        """
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        in_degrees: List[int] = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1

        queue = deque([i for i in range(numCourses) if in_degrees[i] == 0])
        processed_courses = 0

        while queue:
            node = queue.popleft()
            processed_courses += 1

            for neighbor in adj[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return processed_courses == numCourses


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    numCourses1 = 2
    prereqs1 = [[1, 0]]
    result1 = solution.canFinish(numCourses1, prereqs1)
    print(f"Test Case 1: Expected=True, Got={result1}")

    # Test Case 2
    numCourses2 = 2
    prereqs2 = [[1, 0], [0, 1]]
    result2 = solution.canFinish(numCourses2, prereqs2)
    print(f"Test Case 2: Expected=False, Got={result2}")

    # Test Case 3
    numCourses3 = 3
    prereqs3 = [[0, 1], [0, 2], [1, 2]]
    result3 = solution.canFinish(numCourses3, prereqs3)
    print(f"Test Case 3: Expected=True, Got={result3}")
