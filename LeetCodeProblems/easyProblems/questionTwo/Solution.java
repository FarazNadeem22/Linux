class Solution {
    public boolean isPalindrome(int x) {
        // Check if the input number is negative, in which case it's not a palindrome
        if (x < 0) {
            return false;
        }
        
        // Store the original number for later comparison
        int original = x;
        int reversed = 0;  // Initialize the reversed number
        
        // Reversing the digits of the number
        while (x != 0) {
            int digit = x % 10;             // Extract the last digit
            reversed = reversed * 10 + digit;  // Add the digit to the reversed number
            x /= 10;                        // Remove the last digit from the original number
        }
        
        // Compare the reversed number with the original number
        return reversed == original;
    }
}