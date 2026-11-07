from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        You are given a string s. We want to partition the string into as many 
        parts as possible so that each letter appears in at most one part.

        Note that the partition is done so that after concatenating all the parts in order, 
        the resultant string should be s.

        Return a list of integers representing the size of these parts.

        Example 1:
            Input: s = "ababcbacadefegdehijhklij"
            Output: [9, 7, 8]
            Explanation: The partition is "ababcbaca", "defegde", "hijhklij".

        Example 2:
            Input: s = "eccbbbbdec"
            Output: [10]

        Example 3:
            Input: s = "caedbdedda"
            Output: [1, 9]

        Constraints:
            - 1 <= s.length <= 500
            - s consists of lowercase English letters.
        """
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    s1 = "ababcbacadefegdehijhklij"
    res1 = sol.partitionLabels(s1)
    print(f"Test Case 1: {s1}")
    print(f"Output: {res1} | Expected: [9, 7, 8]\n")
    
    # Test Case 2
    s2 = "eccbbbbdec"
    res2 = sol.partitionLabels(s2)
    print(f"Test Case 2: {s2}")
    print(f"Output: {res2} | Expected: [10]\n")
    
    # Test Case 3
    s3 = "caedbdedda"
    res3 = sol.partitionLabels(s3)
    print(f"Test Case 3: {s3}")
    print(f"Output: {res3} | Expected: [1, 9]\n")
