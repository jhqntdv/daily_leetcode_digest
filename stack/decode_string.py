class Solution:
    def decodeString(self, s: str) -> str:
        """
        Given an encoded string, return its decoded string.

        The encoding rule is: k[encoded_string], where the encoded_string 
        inside the square brackets is being repeated exactly k times. 
        Note that k is guaranteed to be a positive integer.

        Constraints:
        - 1 <= s.length <= 30
        - s consists of lowercase English letters, digits, and square brackets '[]'.
        - s is guaranteed to be a valid input.
        - All the integers in s are in the range [1, 300].
        """
        # Write your code here
        pass

if __name__ == '__main__':
    solution = Solution()
    
    # Test Case 1
    s1 = "3[a]2[bc]"
    print(f"Input: s = '{s1}' | Output: '{solution.decodeString(s1)}' | Expected: 'aaabcbc'")
    
    # Test Case 2
    s2 = "3[a2[c]]"
    print(f"Input: s = '{s2}' | Output: '{solution.decodeString(s2)}' | Expected: 'accaccacc'")
    
    # Test Case 3
    s3 = "2[abc]3[cd]ef"
    print(f"Input: s = '{s3}' | Output: '{solution.decodeString(s3)}' | Expected: 'abcabccdcdcdef'")
