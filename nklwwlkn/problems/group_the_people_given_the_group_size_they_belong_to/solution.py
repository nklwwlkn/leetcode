class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        res = []

        for idx, size in enumerate(groupSizes):
            group[size].append(idx)

            if len(group[size]) == size:
                res.append(group.pop(size))
        
        return res
        