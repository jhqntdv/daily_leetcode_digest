class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously added string.

    Implement the WordDictionary class:
    - WordDictionary(): Initializes the object.
    - addWord(word: str) -> None: Adds word to the data structure, it can be matched later.
    - search(word: str) -> bool: Returns True if there is any string in the data structure that matches word or False otherwise.
      word may contain dots '.' where dots can be matched with any letter.
    """

    def __init__(self):
        # Initialize your data structure here.
        pass

    def addWord(self, word: str) -> None:
        """
        Adds a word to the data structure.
        """
        pass

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the data structure. A dot '.' can match any letter.
        """
        pass


if __name__ == '__main__':
    # Test Case 1
    wd1 = WordDictionary()
    wd1.addWord("bad")
    wd1.addWord("dad")
    wd1.addWord("mad")
    print(f"search('pad'): {wd1.search('pad')}")  # Expected: False
    print(f"search('bad'): {wd1.search('bad')}")  # Expected: True
    print(f"search('.ad'): {wd1.search('.ad')}")  # Expected: True
    print(f"search('b..'): {wd1.search('b..')}")  # Expected: True

    # Test Case 2
    wd2 = WordDictionary()
    wd2.addWord("a")
    wd2.addWord("a")
    print(f"search('.'): {wd2.search('.')}")    # Expected: True
    print(f"search('a.'): {wd2.search('a.')}")  # Expected: False

    # Test Case 3
    wd3 = WordDictionary()
    wd3.addWord("apple")
    print(f"search('app..'): {wd3.search('app..')}")  # Expected: True
    print(f"search('.pp..'): {wd3.search('.pp..')}")  # Expected: True
    print(f"search('a.p.e'): {wd3.search('a.p.e')}")  # Expected: True
    print(f"search('a.p.a'): {wd3.search('a.p.a')}")  # Expected: False
