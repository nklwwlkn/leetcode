/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    if (nums.length === k) return nums;
    
    const frequency = {}
    const bucket = new Array(nums.length + 1).fill()
        .map(() => []);
    const result = [];
    
    for (const num of nums) {
        frequency[num] = (frequency[num] || 0) + 1;
    }
        
    
    for (const key in frequency) {
        bucket[frequency[key]].push(Number(key))
    }
    
   
    let i = bucket.length - 1; 
    while (result.length !== k) {
        result.push(...bucket[i])
        i--;
    }
    
    return result
   
};