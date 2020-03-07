/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let counter = 0;

    nums.map(String).forEach(el => {
	if (el.length % 2 === 0) {
		counter++;
	}
})

    return counter
};