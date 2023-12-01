class TrieNode:
    
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.isEnd = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
    
    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path == "/":
            return False

        curr = self.root
        parts  = path.split("/")[1:]

        for i, part in enumerate(parts):
            if part not in curr.children:
                if i < len(parts) - 1:
                    return False
                curr.children[part] = TrieNode()

            curr = curr.children[part]
        
        if curr.isEnd:
            return False
        
        curr.val = value
        curr.isEnd = True

        return curr.isEnd


    def get(self, path: str) -> int:
        if path == "" or path == "/":
            return False

        curr = self.root
        parts = path.split('/')[1:]

        for part in parts:
            if not part in curr.children:
                return -1
            
            curr = curr.children[part]
        
        return curr.val if curr.isEnd else -1



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)