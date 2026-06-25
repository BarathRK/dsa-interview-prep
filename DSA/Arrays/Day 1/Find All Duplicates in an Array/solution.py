class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []

        for element in nums:
            index = abs(element)-1
            
            if nums[index]<0:
                answer.append(abs(element))
            else:
                nums[index] = -nums[index]
        return answer