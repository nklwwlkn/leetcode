class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0

        for item in items:
            if self.isMatch(item, ruleKey, ruleValue):
                counter += 1
        
        return counter

    def isMatch(self, item: List[str], ruleKey: str, ruleValue: str) -> bool:
        value = None
        if ruleKey == "type":
            value = item[0]
        elif ruleKey == "color":
            value = item[1]
        else:
            value = item[2]

        return value == ruleValue
