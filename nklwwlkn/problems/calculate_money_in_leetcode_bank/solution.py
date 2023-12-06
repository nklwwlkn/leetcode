class Solution:
    def totalMoney(self, n: int) -> int:
        currentDay = 0
        totalSavings = 0
        coeficient = currentDay // 7

        moneyToPut = 1
        while currentDay < n:
            totalSavings += moneyToPut
            moneyToPut += 1
            currentDay += 1

            if currentDay // 7 != coeficient:
                coeficient = currentDay // 7
                moneyToPut = 1 + coeficient

        return totalSavings
        