/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let obj = {};
    let occurrences = [];

    for (let val of arr) {
        obj[val] = (obj[val] || 0) + 1;
    }

    for (let val in obj) {
        occurrences.push(obj[val]);
    }

    return occurrences.length === occurrences.filter((v, i, a) => a.indexOf(v) === i).length; 

    
};