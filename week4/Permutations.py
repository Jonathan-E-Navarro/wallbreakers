class Solution:
    '''
    [1,2,3,4] -> [1,2,4,3]
    [1,2,3,4] -> [1,3,2,4]
    [1,2,3,4] -> [1,3,4,2]

    '''
    def __init__(self):
        self.nums = None
        self.ans = []
    def find_permutation(self,index):
        if index == len(self.nums):
            # print("index: ",index)
            self.ans.append(self.nums[:])
        for i in range(index,len(self.nums)):
            # print("index: ",index)
            # print("i: ",i)
            self.nums[index],self.nums[i] = self.nums[i],self.nums[index]
            # print(self.nums)
            self.find_permutation(index+1)
            self.nums[index],self.nums[i] = self.nums[i],self.nums[index]
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        # print(nums)
        self.nums = nums
        self.find_permutation(0)
        # print(self.ans)
        return self.ans
        