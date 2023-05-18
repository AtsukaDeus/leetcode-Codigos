

class Solution(object):
    def romanToInt(self, s):

        # XI = ["X","I"]
        s  = list(s)
        numList = []
        numInt = 0
        numAnt = 0
        count = 0
        
        
        romanDic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        for i in s: 
            for key in romanDic.keys():
                if i == key:
                    numList.append(romanDic[key])
                    
        #[1,5]
        # 0 1           
        for n in numList:
            if numAnt==1 and (n==5 or n==10):
                numList[count-1] = -numList[count-1]
                
            
            if numAnt==10 and (n==50 or n==100):
                numList[count-1] = -numList[count-1]
                

            if numAnt==100 and (n==500 or n==1000):
                numList[count-1] = -numList[count-1]
                
            
            count+=1
            numAnt=n
            
            
        
        for n in numList:
            numInt+=n    
                
        
        return numInt 
    
    
if __name__ == '__main__':
    
    
    s = Solution()
    solution = input(">> ").upper()
    print(s.romanToInt(solution))
    
    
    
    
