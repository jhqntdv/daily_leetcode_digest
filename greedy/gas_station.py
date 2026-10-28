from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Gas Station (LeetCode #134)

        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
        to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas station's index if you can travel
        around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution,
        it is guaranteed to be unique.

        Example 1:
        Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3

        Example 2:
        Input: gas = [2,3,4], cost = [3,4,3]
        Output: -1

        Example 3:
        Input: gas = [5,1,2,3,4], cost = [4,4,1,5,1]
        Output: 4

        Constraints:
        - gas.length == n
        - cost.length == n
        - 1 <= n <= 10^5
        - 0 <= gas[i], cost[i] <= 10^4
        """
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    gas1, cost1 = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    print(f"Test 1: {sol.canCompleteCircuit(gas1, cost1)} (Expected: 3)")
    
    # Test Case 2
    gas2, cost2 = [2, 3, 4], [3, 4, 3]
    print(f"Test 2: {sol.canCompleteCircuit(gas2, cost2)} (Expected: -1)")
    
    # Test Case 3
    gas3, cost3 = [5, 1, 2, 3, 4], [4, 4, 1, 5, 1]
    print(f"Test 3: {sol.canCompleteCircuit(gas3, cost3)} (Expected: 4)")
