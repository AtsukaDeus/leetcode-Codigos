class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        flag = False
        for i in range(len(nums)):
            if flag:
                break
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    result.append(i)
                    result.append(j)
                    flag = True
                    break
        return result
    
    
if __name__ == "__main__":
    
    solution = Solution()
    nums = [3,2,4]
    target = 6
    print(solution.twoSum(nums,target))