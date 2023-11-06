class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        minn = min(a,b)
        if max(a,b) % minn == 0: 
            count +=1
        for i in range(1,(minn//2)+1): 
            if a % i == 0 and b % i ==0: 
                count +=1
        return count