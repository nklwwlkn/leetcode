class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm = {}
        res = []

        for idx in range(len(names)):
            hm[heights[idx]] = names[idx]

        for height in sorted(heights, reverse=True):
            res.append(hm[height])

        return res
        