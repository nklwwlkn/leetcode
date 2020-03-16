/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    let arr = [];
    let i = s.length - 1;

    while (i >= 0) {
        if (s[i] !== '#') {
            arr.unshift(String.fromCharCode(96 + Number(s[i])))
            i--
        } else if (s[i] === '#') {   
            arr.unshift(String.fromCharCode(96 + Number(s[i-2] + s[i - 1])))
            i-= 3;
        }
    }

    return arr.join('');
};