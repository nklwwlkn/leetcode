/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let reversed = String(x).split('').reverse().join('');

    return x == reversed ? true : false;


};