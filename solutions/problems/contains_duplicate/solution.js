/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
   const m = new Map()
   
   for (let num of nums) {
       if (m.get(num)) return true
       
       m.set(num, true)
   }
    
    return false
};