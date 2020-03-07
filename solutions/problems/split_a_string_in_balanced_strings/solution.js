/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let i = 0;
    let left = 0;
    let right = 0;
    let counter = 0;

    while (i !== s.length) {
         if (s[i] === 'R') {
            right++;
        } if (s[i] === 'L') {
            left++;
            }

        if ((right === left) && (right > 0 && left > 0)) {
            console.log(right, left, i)
            counter++;
            right = 0;
            left = 0;
        }

        i++;
    }

    return counter
};