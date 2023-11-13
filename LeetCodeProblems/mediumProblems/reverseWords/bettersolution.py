class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(list(s.split())))