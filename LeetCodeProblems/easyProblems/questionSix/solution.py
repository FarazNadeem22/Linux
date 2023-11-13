from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0

        for i in range(0 ,len(flowerbed)):
            if (i == 0 and len(flowerbed) == 1):
                if (n == 0):
                    True
                else:
                    return not bool(flowerbed[i])
            elif (i == 0):
                try:
                    if (flowerbed[i] ==0 and flowerbed [i+1]==0 ):
                        flowerbed[i] = 1
                        counter +=1
                except:
                    continue               
            elif (i == len(flowerbed)-1):
                try:
                    if (flowerbed[i] ==0 and flowerbed [i-1]==0 ):
                        flowerbed[i] = 1
                        counter +=1
                except:
                    continue                 
            else: 
                if (flowerbed[i] ==0 and flowerbed [i-1]==0 and flowerbed[i+1] ==0):
                    flowerbed[i] = 1
                    counter +=1
        
        return (counter >= n)
    

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"Can place {n} flowers? {result}")  # Output: Can place 1 flowers? True