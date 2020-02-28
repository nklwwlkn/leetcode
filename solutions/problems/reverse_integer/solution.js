/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let reversedNum = String(Math.abs(x)).split('').reverse().join('');

    if (reversedNum > (Math.pow(2, 31) - 1)) {
        return 0;
    }

    return x < 0 ? -reversedNum : reversedNum;
};