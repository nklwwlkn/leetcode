class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            maxWealth = max(sum(account), maxWealth)

        return maxWealth

    