class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f'{len(s)}#{s}' for s in strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        left = 0
        
        while left < len(s):
            right = left

            while s[right] != '#':
                right += 1

            length = int(s[left : right])

            left = right + 1
            right = left + length

            res.append(s[left : right])

            left = right
            
        return res
        

            

                    



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))