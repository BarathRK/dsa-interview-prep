class Solution {
    public List<Integer> majorityElement(int[] nums) {

        Integer candidate1 = null;
        Integer candidate2 = null;

        int count1 = 0;
        int count2 = 0;
        int n = nums.length;

        List<Integer> majorityElements = new ArrayList<>();

        // Finding the possible majority elements
        for (int element : nums) {
            if (candidate1 != null && candidate1 == element) {
                count1++;
            } else if (candidate2 != null && candidate2 == element) {
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
            if (candidate1 != null && candidate1 == element) {
                count1++;
            } else if (candidate2 != null && candidate2 == element) {
                count2++;
            }
        }

        if (count1 > n / 3) {
            majorityElements.add(candidate1);
        }
        if (count2 > n / 3) {
            majorityElements.add(candidate2);
        }

        return majorityElements;
    }
}