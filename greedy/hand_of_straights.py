from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        LeetCode 846: Hand of Straights
        Difficulty: Medium

        Alice has some number of cards and she wants to rearrange the cards into groups
        so that each group is of size groupSize, and consists of groupSize consecutive cards.

        Given an integer array hand where hand[i] is the value written on the i-th card
        and an integer groupSize, return True if she can rearrange the cards, or False otherwise.

        Constraints:
        - 1 <= hand.length <= 10^4
        - 0 <= hand[i] <= 10^9
        - 1 <= groupSize <= hand.length
        """
        # TODO: Implement your solution here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Example 1
    hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize1 = 3
    print(f"Example 1 Output: {sol.isNStraightHand(hand1, groupSize1)} (Expected: True)")
    
    # Example 2
    hand2 = [1, 2, 3, 4, 5]
    groupSize2 = 4
    print(f"Example 2 Output: {sol.isNStraightHand(hand2, groupSize2)} (Expected: False)")
    
    # Example 3
    hand3 = [8, 10, 12]
    groupSize3 = 1
    print(f"Example 3 Output: {sol.isNStraightHand(hand3, groupSize3)} (Expected: True)")
