/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function(A) {
  let set = new Set();

    for (let val of A) {
        if (set.has(val)) return val;
        set.add(val);
    }  

    return -1;
};