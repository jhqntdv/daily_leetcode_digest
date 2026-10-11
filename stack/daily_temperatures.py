from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given an array of integers temperatures represents the daily temperatures,
        return an array answer such that answer[i] is the number of days you have to wait
        after the ith day to get a warmer temperature. If there is no future day for which
        this is possible, keep answer[i] == 0 instead.

        Example 1:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]

        Example 2:
        Input: temperatures = [30,40,50,60]
        Output: [1,1,1,0]

        Example 3:
        Input: temperatures = [30,60,90]
        Output: [1,1,0]

        Constraints:
        - 1 <= temperatures.length <= 10^5
        - 30 <= temperatures[i] <= 100
        """
        pass

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    t1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Test 1: {sol.dailyTemperatures(t1)} (Expected: [1, 1, 4, 2, 1, 1, 0, 0])")

    # Test 2
    t2 = [30, 40, 50, 60]
    print(f"Test 2: {sol.dailyTemperatures(t2)} (Expected: [1, 1, 1, 0])")

    # Test 3
    t3 = [30, 60, 90]
    print(f"Test 3: {sol.dailyTemperatures(t3)} (Expected: [1, 1, 0])")
