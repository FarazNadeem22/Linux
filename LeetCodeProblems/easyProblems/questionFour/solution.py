class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        loopOverThis = len(word1) + len(word2)
        counter = 0;
        mergedString = ""

        while (counter < loopOverThis):
            if(counter < len(word1)):
                try:
                    mergedString += word1[counter]
                except:
                    pass
            if(counter < len(word2)):
                try:
                    mergedString += word2[counter]
                except:
                    pass
            counter +=1
    
        return mergedString
    

# Driver code
if __name__ == "__main__":
    solution = Solution()

    word1 = "abc"
    word2 = "wxyz"
    merged = solution.mergeAlternately(word1, word2)
    print("Merged String:", merged)  # Output: Merged String: 