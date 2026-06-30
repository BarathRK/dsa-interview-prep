class Solution {
    public int maxProfit(int[] prices) {
        int maximumProfit = -100000;
        int minimum = 1000000;

        for (int price : prices) {
            minimum = Math.min(price, minimum);
            maximumProfit = Math.max(maximumProfit, price - minimum);
        }

        return maximumProfit;
    }
}