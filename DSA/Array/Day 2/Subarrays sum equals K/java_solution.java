class Solution {
    public int subarraySum(int[] nums, int k) {

        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        int prefixSum = 0;
        int count = 0;

        for (int value : nums) {
            prefixSum += value;

            int previousPrefixSum = prefixSum - k;

            if (map.containsKey(previousPrefixSum)) {
                count += map.get(previousPrefixSum);
            }

            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }

        return count;
    }
}