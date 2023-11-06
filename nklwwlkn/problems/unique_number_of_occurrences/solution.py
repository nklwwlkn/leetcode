class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numberOccurrences = Counter(arr).values()
        uniqueOccurrences = set(numberOccurrences)

        return len(numberOccurrences) == len(uniqueOccurrences)
