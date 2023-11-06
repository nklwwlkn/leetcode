/**
 * @param {number[]} A
 * @return {number}
 */
var peakIndexInMountainArray = function(A) {
    let max = 0;

    for (let val of A) {
        if (val > max) {
            max = val;
        }
    }

    return A.indexOf(max);
};