class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        maxLucky = -1

        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key in hashmap:
            if key == hashmap.get(key, 0):
                maxLucky = max(maxLucky, key)

        return maxLucky