/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const hs = new Set()

    for (let num of nums) {
        if (hs.has(num)) {
            return true
        }

        hs.add(num)
    }

    return false
};