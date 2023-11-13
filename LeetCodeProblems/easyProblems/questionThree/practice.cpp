#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int maxProfit = 0;
        auto buyPriceIterator = std::max_element(prices.begin(), prices.end());
        int buyPrice = *buyPriceIterator;
        int buyIndex = 0;
        int sellPrice = 0;
        bool firstRun = true;

        // For buy Price 
        for (int i = 0; i < prices.size(); ++i) {
            if (firstRun) {
                if (i + 1 < prices.size() && prices[i] < prices[i + 1]) {
                    buyPrice = prices[i];
                    buyIndex = i;
                    firstRun = false;
                }
            }
            if (i + 1 < prices.size() && (prices[i] < prices[i + 1]) && (prices[i] < buyPrice)) {
                buyPrice = prices[i];
                sellPrice = prices[i];
                buyIndex = i;
            }
        }

        // For sell price
        for (int i = buyIndex; i < prices.size(); ++i) {
            if (prices[i] > sellPrice) {
                sellPrice = prices[i];
            }
        }
    
        maxProfit = sellPrice - buyPrice;
        std::cout << sellPrice << " - " << buyPrice << " = " << maxProfit << ", buy Index: " << buyIndex;
        return maxProfit;
    }
};

int main() {
    std::vector<int> priceVector = {3,2,6,5,0,3};
    int result;

    Solution solution;
    result = solution.maxProfit(priceVector);
    std::cout << result;
    
    return 0;
}