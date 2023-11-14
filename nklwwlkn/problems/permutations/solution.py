class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        taken = set()
     
        def backtrack():
            if len(permutation) == len(nums): 
                res.append(permutation.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] not in taken:

                        permutation.append(nums[i])
                        taken.add(nums[i])

                        backtrack()

                        permutation.pop()
                        taken.remove(nums[i])

        backtrack()

        return res
        