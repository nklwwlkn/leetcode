import hashlib

class Codec:
    def __init__(self):
        self.base = "https://tiny.com/"
        self.cache = {}

    def hash(self, s):
        return self.base + hashlib.md5(s.encode()).hexdigest()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        shortUrl = self.hash(longUrl)
        self.cache[shortUrl] = longUrl
        
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))