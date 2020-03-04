/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    let obj1 = {};

    for (let val of s) {
        obj1[val] = (obj1[val] || 0) + 1;
    }

    for (let val of t) {
        if ((!obj1[val])) {
            return false;
        }
        obj1[val] = obj1[val] - 1;
    }
    
return true;
};