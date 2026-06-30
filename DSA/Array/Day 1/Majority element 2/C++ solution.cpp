class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {

        int candidate1 = 0;
        int candidate2 = 0;

        int count1 = 0;
        int count2 = 0;
        int n = nums.size();

        vector<int> majorityElements;

        // Finding the possible majority elements
        for (int element : nums) {
            if (candidate1 == element) {
                count1++;
            } else if (candidate2 == element) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = element;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = element;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Check whether the possible majority elements are actual majority elements
        count1 = 0;
        count2 = 0;

        for (int element : nums) {
            if (element == candidate1) {
                count1++;
            } else if (element == candidate2) {
                count2++;
            }
        }

        if (count1 > n / 3) {
            majorityElements.push_back(candidate1);
        }
        if (count2 > n / 3) {
            majorityElements.push_back(candidate2);
        }

        return majorityElements;
    }
};