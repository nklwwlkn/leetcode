/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    if (nums.length === k) return nums;
    
    const obj = {};
    const result = [];
    
    for (num of nums) {
        obj[num] = (obj[num] || 0) + 1
    }
    
    
    const sortedEntries = Object.entries(obj).sort(([, a], [, b]) => b - a);
    
    for (let i = 0; i < k; i++) {
        result.push(sortedEntries[i][0]);
    }
    
    return result
    
};