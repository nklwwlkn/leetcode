/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    let arr = [];

    nums.sort((a,b) => a - b);
    for (let i = 0; i + 1 < nums.length; i+=2) {
        arr.push(Math.min(nums[i], nums[i+1]));      
    }
    
    
    return arr.reduce((a,b) => a+b);
};