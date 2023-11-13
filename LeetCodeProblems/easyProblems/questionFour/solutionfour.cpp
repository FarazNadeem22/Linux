#include <iostream>
#include <string>


class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        int lengthWordOne = word1.length();
        int lengthWordTwo = word2.length();
        int loopOverThis = lengthWordOne+lengthWordTwo;
        std::string  mergedString;
        int counter = 0;

        while(counter < loopOverThis){
            if (counter < lengthWordOne){
                try{
                    mergedString += word1[counter];
                }catch (...){
                    // Do nothing
                }
            }
            if (counter < lengthWordTwo){
                try{
                    mergedString += word2[counter];
                }catch (...){
                    // Do nothing
                }
            }
             counter++;
        }

        return mergedString;
    }

};

int main(){

    Solution sol;
    std::string result;
    result= sol.mergeAlternately("Anam","Wahid");
    std::cout<<result;

    return 0;
}