/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    let resultArr = [];
    
    let helper = arr => {
    if (arr.length <= 0) return arr;
    if (arr[0] === 1) {
        resultArr.push(arr[1]);
        return helper(arr.splice(2));
    }

    let i = 0;

    while (i < arr[0]) {
        resultArr.push(arr[1]);
        i++;
    }

    return helper(arr.splice(2));

    }

    helper(nums);

    return resultArr;
};
