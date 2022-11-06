/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if (nums.length == 2) return [0,1];
    
    const hashMap = {};
    
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let lookup = target - num;
        
        if (hashMap[lookup] >= 0) {
             return [hashMap[lookup], i];
        } 
        
        hashMap[num] = i; 
    }
};