/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {   
    return arr.sort((a,b) => countBits(a) - countBits(b) || a - b);
};

let countBits = (num, counter = 0) => {
    for (let val of String((num).toString(2))) {
        if (val === '1') {
            counter++;
        }
    }
    return counter;
}