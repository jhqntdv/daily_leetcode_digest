from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking with Pruning:
        1. Sort candidates in ascending order to enable early pruning.
        2. In each step, if remaining target == 0, record the current combination.
        3. If candidate > remain, break the loop immediately (pruning) because all
           subsequent candidates are greater or equal.
        4. Since an element can be chosen unlimited times, recurse starting at index `i`.

        Time Complexity: O(N^(T/M)) in the worst case, where N = len(candidates),
                         T = target, and M = min(candidates). Pruning significantly reduces the state space.
        Space Complexity: O(T/M) for the recursion call stack and current combination path.
        """
        candidates.sort()
        res: List[List[int]] = []
        path: List[int] = []

        def backtrack(start_index: int, remain: int) -> None:
            if remain == 0:
                res.append(list(path))
                return

            for i in range(start_index, len(candidates)):
                val = candidates[i]
                if val > remain:
                    break  # Pruning: all subsequent elements are >= val > remain

                path.append(val)
                backtrack(i, remain - val)  # Pass i because the same element can be reused
                path.pop()

        backtrack(0, target)
        return res

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
