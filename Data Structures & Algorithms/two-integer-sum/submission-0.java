class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] indices = new int[2];

        for (int i = 0; i < nums.length; i++){
            for (int k = i + 1; k < nums.length; k++){
                if (nums[i] + nums[k] == target){
                    indices[0] = i;
                    indices[1] = k; 
                    break;
                }
            }
        }

        return indices;
    }
}
