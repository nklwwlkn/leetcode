/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let obj = {};
       
    for (let val of nums) {
        obj[val] = (obj[val] + 1) || 0;
    }


    let max = Math.max.apply(null, Object.values(obj));

    return Number(Object.keys(obj).find(key => obj[key] === max));
};