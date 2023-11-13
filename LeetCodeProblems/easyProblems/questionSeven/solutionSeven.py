class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowel = ['A','E','I','O','U']
        idxList = []
        vowelReplacement = []
        counter = 0
        s = list(s)
        for i in range (0, len(s)):
            if s[i].upper() in Vowel :
                idxList.append(i)
                vowelReplacement.append(s[i])
        idxList.reverse()
        for i in range(0, len(idxList)):
            s[idxList[i]] = vowelReplacement[i]    
        return "".join(s)
        
# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    input_str = "race car"
    reversed_str = solution.reverseVowels(input_str)
    print("Reversed Vowels:", reversed_str)  # Output: Reversed Vowels: holle