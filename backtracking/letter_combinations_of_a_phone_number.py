from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter
        combinations that the number could represent. Return the answer in any order.

        Constraints:
        - 0 <= digits.length <= 4
        - digits[i] is a digit in the range ['2', '9'].
        """
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    digits1 = "23"
    print(f"Test Case 1: digits = '{digits1}'")
    print(f"Output: {sol.letterCombinations(digits1)}")
    # Expected Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    # Test Case 2
    digits2 = ""
    print(f"\nTest Case 2: digits = '{digits2}'")
    print(f"Output: {sol.letterCombinations(digits2)}")
    # Expected Output: []
    
    # Test Case 3
    digits3 = "2"
    print(f"\nTest Case 3: digits = '{digits3}'")
    print(f"Output: {sol.letterCombinations(digits3)}")
    # Expected Output: ["a","b","c"]
