class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
    
    
    
if __name__ == '__main__':
    
    obj = KthLargest(3,[4,5,8,2])
    param_1 = obj.add(3)
    print(param_1)