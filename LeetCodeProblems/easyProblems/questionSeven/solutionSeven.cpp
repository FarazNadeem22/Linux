#include <iostream>


class Solution {
public:
    std::string reverseVowels(std::string s) {
        std::string phrase = s;
        std::string vowels = "aeiouAEIOU";
        char temp;
        int left = 0;
        int right = s.length() - 1;


        while (left < right){
            while(left<right && vowels.find(phrase[left]) == std::string::npos){
                left++;
            }
            while(left<right && vowels.find(phrase[right]) == std::string::npos){
                right--;
            }            
            
            temp = phrase[left];
            phrase[left] = phrase[right];
            phrase[right] = temp;

            left++;
            right--;    
        }
    }
};