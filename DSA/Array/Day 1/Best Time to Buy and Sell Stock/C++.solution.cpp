class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maximumProfit = -100000;
        int minimum = 1000000;

        for (int price : prices) {
            minimum = min(price, minimum);
            maximumProfit = max(maximumProfit, price - minimum);
        }

        return maximumProfit;
    }
};