class Solution {
    public int firstMissingPositive(int[] nums) {

        int i = 0;
        int n = nums.length;

        while (i < n) {
            int correctPosition = nums[i] - 1;

            if (nums[i] >= 1 && nums[i] <= n &&
                nums[i] != nums[correctPosition]) {

                int temp = nums[i];
                nums[i] = nums[correctPosition];
                nums[correctPosition] = temp;
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
}