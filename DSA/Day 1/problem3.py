class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        n = len(nums)
        prefix_product = [0]*n
        suffix_product = [0]*n
        answer = [0]*n
        prefix_product[0] = nums[0]
        suffix_product[n-1] = nums[n-1]

        for index in range(1,n):
            prefix_product[index] = prefix_product[index-1]*nums[index]
         
        for index in range(n-2,-1,-1):
            suffix_product[index] = suffix_product[index+1]*nums[index]

        for index in range(n):
            if index == 0:
                answer[index] = suffix_product[index+1]
            elif index == n-1:
                answer[index] = prefix_product[index-1]
            else:
                answer[index] = prefix_product[index-1]*suffix_product[index+1]
        return answer