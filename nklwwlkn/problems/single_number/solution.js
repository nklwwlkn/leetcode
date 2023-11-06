/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
   let obj = {};
   let min;
    for (let val of nums) {
        obj[val] = (obj[val] || 0) + 1;
    }
    
    
    return Number(Object.keys(obj).find(key => obj[key] === 1));
};