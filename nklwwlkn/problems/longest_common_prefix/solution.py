class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minWord = min(strs, key=len)

        pref = ""
        counter = 0
        
        for i in range(len(minWord)):
            char = minWord[i]
            counter = 0
            for word in strs:
                if word[i] == char:
                    counter += 1
                else:
                    return pref
            if counter == len(strs):
                pref += char
           
        return pref


        