class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Example 1:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Example 2:
        Input: strs = ["dog","racecar","car"]
        Output: ""

        Example 3:
        Input: strs = ["apple", "apricot", "april"]
        Output: "ap"

        Constraints:
        1 <= strs.length <= 200
        0 <= strs[i].length <= 200
        strs[i] consists of only lowercase English letters.
        """
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    solver = Solution()

    # Test Case 1
    strs1 = ["flower", "flow", "flight"]
    result1 = solver.longestCommonPrefix(strs1)
    print(f"Input: {strs1}, Output: {result1}, Expected: 'fl'")
    assert result1 == "fl", f"Test Case 1 Failed: Expected 'fl', Got {result1}"

    # Test Case 2
    strs2 = ["dog", "racecar", "car"]
    result2 = solver.longestCommonPrefix(strs2)
    print(f"Input: {strs2}, Output: {result2}, Expected: ''")
    assert result2 == "", f"Test Case 2 Failed: Expected '', Got {result2}"

    # Test Case 3
    strs3 = ["apple", "apricot", "april"]
    result3 = solver.longestCommonPrefix(strs3)
    print(f"Input: {strs3}, Output: {result3}, Expected: 'ap'")
    assert result3 == "ap", f"Test Case 3 Failed: Expected 'ap', Got {result3}"

    print("All test cases passed!")
