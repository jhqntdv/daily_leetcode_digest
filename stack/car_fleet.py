"""
Car Fleet

There are n cars at given miles away from the starting mile 0, traveling to a target mile.

You are given two integer arrays `position` and `speed`, both of length `n`, where position[i] 
is the starting position of the i-th car and speed[i] is the speed of the i-th car in miles per hour.

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper 
at the same speed. The faster car will slow down to match the slower car's speed. 

A car fleet is a non-empty set of cars driving at the same position and speed. 
Note that a single car is also considered a car fleet.

If a car catches up to a car fleet right at the destination mile, it is still considered 
to be part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until target.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence 1 fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then this fleet catches up to the car starting at 4 (speed 1) at position 6. The fleet moves at speed 1 until target.

Constraints:
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- All the values of position are unique.
- 0 < speed[i] <= 10^6
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    print(f"Test Case 1: {solution.carFleet(target1, position1, speed1)}")  # Expected: 3

    # Test Case 2
    target2 = 10
    position2 = [3]
    speed2 = [3]
    print(f"Test Case 2: {solution.carFleet(target2, position2, speed2)}")  # Expected: 1

    # Test Case 3
    target3 = 100
    position3 = [0, 2, 4]
    speed3 = [4, 2, 1]
    print(f"Test Case 3: {solution.carFleet(target3, position3, speed3)}")  # Expected: 1
