class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int n = nums.size();

        vector<int> prefixProduct(n);
        vector<int> suffixProduct(n);
        vector<int> answer(n);

        prefixProduct[0] = nums[0];
        suffixProduct[n - 1] = nums[n - 1];

        // Compute prefix products
        for (int i = 1; i < n; i++) {
            prefixProduct[i] = prefixProduct[i - 1] * nums[i];
        }

        // Compute suffix products
        for (int i = n - 2; i >= 0; i--) {
            suffixProduct[i] = suffixProduct[i + 1] * nums[i];
        }

        // Compute answer
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                answer[i] = suffixProduct[i + 1];
            } else if (i == n - 1) {
                answer[i] = prefixProduct[i - 1];
            } else {
                answer[i] = prefixProduct[i - 1] * suffixProduct[i + 1];
            }
        }

        return answer;
    }
};