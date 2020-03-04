/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    if (s === '') return true;
    let str = s.replace(/\W/g, '').toLowerCase();

    return str === str.split('').reverse().join('');
};