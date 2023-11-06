/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let result = new Array(nums.length).fill(1);
    let product = 1
     
    for (let index = 0; index < nums.length; index++) {
        result[index] = product
        product *= nums[index]
    }

    product = 1;
    for (let index = nums.length - 1; index >= 0; index--) {
        result[index] *= product;
        product *= nums[index]
    }
    
    return result
};