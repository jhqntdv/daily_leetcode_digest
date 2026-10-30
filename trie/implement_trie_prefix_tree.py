"""
LeetCode: Implement Trie (Prefix Tree)
Difficulty: Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie(): Initializes the trie object.
- void insert(String word): Inserts the string word into the trie.
- boolean search(String word): Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix): Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

Example 2:
Input:
["Trie", "insert", "search", "startsWith"]
[[], ["banana"], ["banana"], ["ban"]]
Output:
[null, null, true, true]

Example 3:
Input:
["Trie", "insert", "insert", "search", "search", "startsWith"]
[[], ["car"], ["card"], ["car"], ["cards"], ["card"]]
Output:
[null, null, null, true, false, true]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pass

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pass


if __name__ == "__main__":
    # Test Case 1: Standard insertions and searches
    trie1 = Trie()
    trie1.insert("apple")
    print("Test 1 - search('apple'):", trie1.search("apple"))      # Expected: True
    print("Test 1 - search('app'):", trie1.search("app"))          # Expected: False
    print("Test 1 - startsWith('app'):", trie1.startsWith("app"))  # Expected: True
    trie1.insert("app")
    print("Test 1 - search('app') after insert:", trie1.search("app")) # Expected: True

    # Test Case 2: Single word prefix and full word lookup
    trie2 = Trie()
    trie2.insert("banana")
    print("\nTest 2 - search('banana'):", trie2.search("banana"))  # Expected: True
    print("Test 2 - startsWith('ban'):", trie2.startsWith("ban"))  # Expected: True

    # Test Case 3: Multiple words with overlapping prefixes
    trie3 = Trie()
    trie3.insert("car")
    trie3.insert("card")
    print("\nTest 3 - search('car'):", trie3.search("car"))        # Expected: True
    print("Test 3 - search('cards'):", trie3.search("cards"))      # Expected: False
    print("Test 3 - startsWith('card'):", trie3.startsWith("card")) # Expected: True
