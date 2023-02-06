class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_one_size = len(word1)
        word_two_size = len(word2)
        res = ""

        for i in range(word_one_size + word_two_size - 1):
            if i < word_one_size:
                res += word1[i]
            if i < word_two_size:
                res += word2[i]

        
        return res
                




        