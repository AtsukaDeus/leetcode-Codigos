class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        size = len(ransomNote)
        count = 0
        result = False
        
        if len(ransomNote) <= len(magazine):
            for i in range(size):  
                for j in range(len(magazine)):
                    if ransomNote[i] == magazine[j]:
                        magazine[j] = ""
                        ransomNote[i] = ""
                        count += 1
                        if size == count:
                            result = True
                        break
        return result
        


if __name__ == '__main__':
    
    
    s = Solution()
    r = "fihjjjjei"
    m = "hjibhhhhhhhhhhhajjfedjaeaebgi"
    print(s.canConstruct(r,m))
    
    
    pass