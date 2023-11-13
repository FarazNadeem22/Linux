from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # If n is 0, it's always possible to place 0 flowers
        if n == 0:
            return True

        # Add padding with zeros at the beginning and end of flowerbed
        flowerbed = [0] + flowerbed + [0]

        # Loop through flowerbed starting from index 1 and ending before the last element
        for i in range(1, len(flowerbed) - 1):
            # If there's already a flower, continue to the next position
            if flowerbed[i] == 1:
                continue
            
            # Check if the adjacent positions are also empty
            if flowerbed[i - 1] == flowerbed[i + 1] == 0:
                n -= 1  # Decrement n since a flower can be placed here
                flowerbed[i] = 1  # Mark the current position as planted

        # Return True if n is non-positive, meaning all flowers are planted
        return n <= 0

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"Can place {n} flowers? {result}")  # Output: Can place 1 flowers? True