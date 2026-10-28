import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
        and an integer k, return the k closest points to the origin (0, 0).

        The distance between two points on the X-Y plane is the Euclidean distance:
            sqrt((x1 - x2)^2 + (y1 - y2)^2)

        You may return the answer in any order. The answer is guaranteed to be
        unique (except for the order that it is in).

        Examples:
            Example 1:
                Input: points = [[1, 3], [-2, 2]], k = 1
                Output: [[-2, 2]]

            Example 2:
                Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
                Output: [[3, 3], [-2, 4]]
                Explanation: [[-2, 4], [3, 3]] is also accepted.

            Example 3:
                Input: points = [[0, 1], [1, 0]], k = 2
                Output: [[0, 1], [1, 0]]

        Constraints:
            - 1 <= k <= points.length <= 10^4
            - -10^4 <= xi, yi <= 10^4

        Approach:
        - We maintain a Max-Heap of size k storing (-squared_distance, point).
        - Squared Euclidean distance (x^2 + y^2) is used directly to avoid costly and imprecise square roots.
        - Since Python's heapq is a min-heap, storing negative distances simulates a max-heap where the
          farthest point among our current k closest candidates is always at the root.
        - For each point:
            - If heap size is less than k: push (-dist, point).
            - Else if -dist > max_heap[0][0] (meaning current point is closer than the farthest in the heap):
              replace the root using heapq.heapreplace.
        - Finally, extract and return all points from the heap.

        Complexity:
        - Time: O(n log k), where n is the number of points.
        - Space: O(k) auxiliary space to store k elements in the heap.
        """
        # max_heap stores (-dist_sq, point)
        max_heap = []

        for point in points:
            dist_sq = point[0] ** 2 + point[1] ** 2
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist_sq, point))
            elif -dist_sq > max_heap[0][0]:
                heapq.heapreplace(max_heap, (-dist_sq, point))

        return [point for _, point in max_heap]


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    print(f"Test 1: {solution.kClosest(points1, k1)}")  # Expected: [[-2, 2]]

    # Test Case 2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    print(f"Test 2: {solution.kClosest(points2, k2)}")  # Expected: [[3, 3], [-2, 4]] or [[-2, 4], [3, 3]]

    # Test Case 3
    points3 = [[0, 1], [1, 0]]
    k3 = 2
    print(f"Test 3: {solution.kClosest(points3, k3)}")  # Expected: [[0, 1], [1, 0]] or [[1, 0], [0, 1]]
