class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] indices = new int[2];
        HashMap<Integer, Integer> value = new HashMap<>(); //value -> index

        for (int i = 0; i < nums.length; i++){
            value.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if (value.containsKey(diff) && value.get(diff) != i){
                return new int[]{i, value.get(diff)};
            }
        }

        return indices;
    }
}
