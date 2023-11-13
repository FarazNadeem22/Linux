class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        localMaxima = max(candies)
        resultLst = []
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= localMaxima:
                resultLst.append(True)
            else:
                resultLst.append(False)
        return resultLst
    