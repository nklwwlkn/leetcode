/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
let arr = [];
    while (left <= right) {
        if (isSelf(left)) {
            arr.push(left);
        }
        left++;
    }

    return arr;
};

let isSelf = val => {
    let counter = 0;
    for (let num of String(val)) {
        if (val % num === 0) {
                    counter++;
                }
    }

    return counter === String(val).length
}