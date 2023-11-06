/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function(A) {
    return A.map(el => Math.pow(el, 2)).sort((a,b) => a-b)
};