from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen
        numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times.
        Two combinations are unique if the frequency of at least one of the chosen
        numbers is different.

        Constraints:
        - 1 <= candidates.length <= 30
        - 2 <= candidates[i] <= 40
        - All elements of candidates are distinct.
        - 1 <= target <= 40
        """
        pass

if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    candidates1, target1 = [2, 3, 6, 7], 7
    print(f"Test 1 Output: {sol.combinationSum(candidates1, target1)}")
    print("Expected: [[2, 2, 3], [7]]\n")

    # Test Case 2
    candidates2, target2 = [2, 3, 5], 8
    print(f"Test 2 Output: {sol.combinationSum(candidates2, target2)}")
    print("Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]\n")

    # Test Case 3
    candidates3, target3 = [2], 1
    print(f"Test 3 Output: {sol.combinationSum(candidates3, target3)}")
    print("Expected: []\n")
