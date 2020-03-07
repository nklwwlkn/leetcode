/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    let obj = {};
    let result = 0;

    for (let val of S) {
        obj[val] = (obj[val] || 0) + 1;
    }

    for (let val of J) {
        if (obj[val]) {
            result += obj[val];
        }
    }
    return result;
};