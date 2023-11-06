/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
        let pointer = 0;
        let counter = 0;
    while (pointer <= nums.length && counter <= nums.length) {
         if(nums[pointer] === 0) { 
            nums.splice(pointer,1);
            nums.push(0)
         } else {
            pointer++; 
         }
          counter++; 
    }
    return nums
    
};