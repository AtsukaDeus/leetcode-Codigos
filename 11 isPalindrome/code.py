class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = ''
        for i in range(len(x)-1, -1, -1):
            y += x[i]
        
        return y == x
    



s = Solution()
print(s.isPalindrome(121))
    
