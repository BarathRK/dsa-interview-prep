class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        target = k
        prefix_sum = 0
        count = 0
        for value in nums:
            prefix_sum+=value
            previous_prefix_sum = prefix_sum-target
            if previous_prefix_sum in hashmap:
                count+=hashmap.get(previous_prefix_sum)
            hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1
        return count