/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
let counter;
let resultArr = [];
  for (let i = 0; i < nums.length; i++) {
      counter = 0;
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] > nums[j]) {
                counter++;
            }
        }
        resultArr.push(counter);
  }
    return resultArr
};