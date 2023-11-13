#include <iostream>
#include <vector>
#include <algorithm>


class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int maxProfit = 0;
        int buyPrice = INT_MAX; // Initialize buyPrice with a high value
        int sellPrice = 0;
        for (int i = 0; i < prices.size(); ++i) {
            if (prices[i] < buyPrice) {
                buyPrice = prices[i];
            } else {
                int potentialProfit = prices[i] - buyPrice;
                if (potentialProfit > maxProfit) {
                    maxProfit = potentialProfit;
                    sellPrice = prices[i];
                }
            }
        }
        return maxProfit;
    }
};
int main() {
    std::vector<int> priceVector = {3, 2, 6, 5, 0, 3};
    int result;

    Solution solution;
    result = solution.maxProfit(priceVector);
    std::cout << result;

    return 0;
}