class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None

        majorityelements = []
        count1 = 0
        count2 = 0
        n = len(nums)
        # Finding the possible majority elements
        for element in nums:
            if candidate1 == element:
                count1+=1
            elif candidate2 == element:
                count2+=1
            elif count1 == 0:
                candidate1 = element
                count1 =1
            elif count2 == 0:
                candidate2 = element
                count2 =1
            else:
                count1-=1
                count2-=1
        
        # Check the possible majority element is the final majority element
        count1 = 0
        count2 = 0
        for element in nums:
            if candidate1 == element:
                count1+=1
            elif candidate2 == element:
                count2+=1
        
        if count1>n//3:
            majorityelements.append(candidate1)
        if count2>n//3:
            majorityelements.append(candidate2)
        return majorityelements