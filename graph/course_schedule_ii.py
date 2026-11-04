from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
        You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must
        take course b_i first if you want to take course a_i.

        Return the ordering of courses you should take to finish all courses.
        If there are many valid answers, return any of them.
        If it is impossible to finish all courses, return an empty array [].

        Constraints:
        - 1 <= numCourses <= 2000
        - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
        - prerequisites[i].length == 2
        - 0 <= a_i, b_i < numCourses
        - a_i != b_i
        - All pairs [a_i, b_i] are distinct.
        """
        # TODO: Implement solution
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"Test 1 Output: {solution.findOrder(numCourses1, prerequisites1)}")
    # Expected Output: [0, 1]

    # Test Case 2
    numCourses2 = 4
    prerequisites2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"Test 2 Output: {solution.findOrder(numCourses2, prerequisites2)}")
    # Expected Output: [0, 1, 2, 3] or [0, 2, 1, 3]

    # Test Case 3
    numCourses3 = 1
    prerequisites3 = []
    print(f"Test 3 Output: {solution.findOrder(numCourses3, prerequisites3)}")
    # Expected Output: [0]
