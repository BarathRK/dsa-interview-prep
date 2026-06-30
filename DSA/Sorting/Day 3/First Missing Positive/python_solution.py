class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while(i<n):
            correct_position = nums[i]-1
            if((nums[i]>=1 and nums[i]<=n) and (nums[i]!=nums[correct_position])):
                nums[i],nums[correct_position] = nums[correct_position],nums[i]
            else:
                i+=1
        for a in range(n):
            if nums[a]!=a+1:
                return a+1
        return n+1