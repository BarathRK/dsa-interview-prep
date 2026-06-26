class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while(mid<n):
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
            else:
                mid+=1

    
        