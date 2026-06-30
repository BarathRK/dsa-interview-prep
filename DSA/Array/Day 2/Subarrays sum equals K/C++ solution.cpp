class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        unordered_map<int, int> mp;
        mp[0] = 1;

        int prefixSum = 0;
        int count = 0;

        for (int value : nums) {
            prefixSum += value;

            int previousPrefixSum = prefixSum - k;

            if (mp.find(previousPrefixSum) != mp.end()) {
                count += mp[previousPrefixSum];
            }

            mp[prefixSum]++;
        }

        return count;
    }
};