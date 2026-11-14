"""
Search Suggestions System (LeetCode #1268)
Difficulty: Medium

You are given an array of strings `products` and a string `searchWord`.

Design a system that suggests at most three product names from `products` after each 
character of `searchWord` is typed. Suggested products should have a common prefix with 
`searchWord`. If there are more than three products with a common prefix, return the 
three lexicographically minimum products.

Return a list of lists of the suggested products after each character of `searchWord` is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
  ["mobile","moneypot","monitor"],
  ["mobile","moneypot","monitor"],
  ["mouse","mousepad"],
  ["mouse","mousepad"],
  ["mouse","mousepad"]
]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [
  ["baggage","bags","banner"],
  ["baggage","bags","banner"],
  ["baggage","bags"],
  ["bags"]
]

Constraints:
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= searchWord.length <= 1000
- Total characters of products <= 2 * 10^4
- All strings of products contain lowercase English letters.
- searchWord contains lowercase English letters.
"""

from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # TODO: Implement solution
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    products1 = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord1 = "mouse"
    print("Test 1 Result:", solution.suggestedProducts(products1, searchWord1))

    # Test Case 2
    products2 = ["havana"]
    searchWord2 = "havana"
    print("Test 2 Result:", solution.suggestedProducts(products2, searchWord2))

    # Test Case 3
    products3 = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord3 = "bags"
    print("Test 3 Result:", solution.suggestedProducts(products3, searchWord3))
