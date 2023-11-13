from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums)
        n = len(nums)
        left_product = [1] * n  # Initialize left_product array with 1
        right_product = [1] * n  # Initialize right_product array with 1
        #print(left_product)
        #print(right_product)

        # Calculate the product of elements to the left of each element
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        #print("Left product: ", left_product)

        # Calculate the product of elements to the right of each element
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        #print("Right product: ", right_product)

        # Calculate the product of all elements except nums[i]
        result = [left_product[i] * right_product[i] for i in range(n)]
        return result

# Driver code
solution = Solution()

nums = [1, 2, 3, 4]
result = solution.productExceptSelf(nums)
print(result)
    