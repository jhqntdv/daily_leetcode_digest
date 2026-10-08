class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
        and removing all non-alphanumeric characters, it reads the same forward and backward.
        Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.

        Example 1:
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.

        Example 2:
        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.

        Example 3:
        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.

        Constraints:
        - 1 <= s.length <= 2 * 10^5
        - s consists only of printable ASCII characters.
        """
        # Write your code here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Test Case 1: {sol.isPalindrome(s1)} (Expected: True)")
    
    # Test Case 2
    s2 = "race a car"
    print(f"Test Case 2: {sol.isPalindrome(s2)} (Expected: False)")
    
    # Test Case 3
    s3 = " "
    print(f"Test Case 3: {sol.isPalindrome(s3)} (Expected: True)")
