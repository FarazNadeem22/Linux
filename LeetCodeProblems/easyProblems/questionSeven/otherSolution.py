## Ok I did not understand the question correction I was interchanging the consecutive two vowels. 
# Now I understand that I have to reverse the complete string of vowels.
# I will keep this code for reference. 
class Solution:
    def reverseVowels(self, s: str) -> str:
        idxFirstVowel = None
        s = list(s)
        for i in range (0, len(s)):
            if s[i].upper() in ['A','E','I','O','U']:
                if idxFirstVowel is not None:
                    alpha = s[i]
                    beta = s[idxFirstVowel]
                    s[i] = beta
                    s[idxFirstVowel] = alpha
                    idxFirstVowel = i
                else:
                    idxFirstVowel = i
        return "".join(s)
        
# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    input_str = "hello"
    reversed_str = solution.reverseVowels(input_str)
    print("Reversed Vowels:", reversed_str)  # Output: Reversed Vowels: holle