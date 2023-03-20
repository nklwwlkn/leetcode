class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for i in range(len(word)):
            next_nodes = []
            w = word[i]
            for node in nodes:
                for v, child in node.children.items():
                    if v == w or w == ".":
                        next_nodes.append(child)
            nodes = next_nodes
            if i == len(word) - 1:
                for n in nodes:
                    if n.isEnd:
                        return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)