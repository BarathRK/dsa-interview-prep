class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {

        int i = 0;
        int n = nums.size();

        while (i < n) {
            int correctPosition = nums[i] - 1;

            if (nums[i] >= 1 && nums[i] <= n &&
                nums[i] != nums[correctPosition]) {

                swap(nums[i], nums[correctPosition]);
            } else {
                i++;
            }
        }

        for (int index = 0; index < n; index++) {
            if (nums[index] != index + 1) {
                return index + 1;
            }
        }

        return n + 1;
    }
};