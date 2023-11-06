/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    let arr = ['z']
    let c = n;
    while (n !== 1 ) {
    if (c % 2 === 0) {
        arr.push('s')
    } else {
        arr.push('z');
    }
        n--;
    }

    return arr.join('');
};