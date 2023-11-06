class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hset = set()

        for email in emails:
            nick, domain = email.split('@')
            hset.add(self.transformNick(nick) + "@" + domain)
        
        return len(hset)
    
    def transformNick(self, nick: str) -> str:
        transformed = ""
        for char in nick:
            if char == ".":
                continue
            elif char == "+":
                break
            else:
                transformed += char
        
        return transformed

