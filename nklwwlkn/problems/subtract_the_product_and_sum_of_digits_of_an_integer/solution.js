/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let nums = String(n).split('').map(Number);

    return nums.reduce((a,b) => a * b) - nums.reduce((a,b) => a + b);
};