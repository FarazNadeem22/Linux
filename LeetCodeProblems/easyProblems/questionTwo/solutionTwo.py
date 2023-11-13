class Solution(object):

    def isPalindrome(self, x):
        # Check if the input number is negative, in which case it's not a palindrome
        if (x < 0):
            return False
        
        digit = x      # Store the original number for later comparison
        reversed = 0   # Initialize the reversed number
        
        # Reversing the digits of the number
        while(digit != 0):
            number = digit % 10          # Extract the last digit
            reversed = reversed * 10 + number  # Add the digit to the reversed number
            digit = digit // 10               # Remove the last digit from the original number
        
        # Compare the reversed number with the original number
        if (reversed == x):
            return True
        else:
            return False