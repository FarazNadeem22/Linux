public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        int idxOne = -1, idxTwo = -1;
        
        for (int i = 0; i < nums.length; i++) {
            int firstNumber = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                if (firstNumber + nums[j] == target) {
                    idxOne = i;
                    idxTwo = j;
                    break;
                }
            }
            if (idxOne != -1 && idxTwo != -1) {
                break;
            }
        }
        
        result[0] = idxOne;
        result[1] = idxTwo;
        return result;
    }
}