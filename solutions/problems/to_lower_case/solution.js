/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function(str) {
    for (let val of str) {
        if (isCapital(val)) {
           str = str.replace(val, String.fromCharCode(val.charCodeAt(0) + 32))
        }
    }

    return str
};

let isCapital = char => char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90;